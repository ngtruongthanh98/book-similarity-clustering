from flask import Flask, jsonify, request
import pandas as pd
import math
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# read all records from the CSV file and filter the columns
books = pd.read_csv('../database/books.csv', delimiter=';',
                    encoding='ISO-8859-1', on_bad_lines='skip')

ratings = pd.read_csv('../database/ratings.csv', delimiter=';',
                      encoding='ISO-8859-1')

users = pd.read_csv('../database/users.csv', delimiter=';',
                    encoding='ISO-8859-1')

louvain = pickle.load(
    open(f'../graph/louvain.pickle', 'rb'))

leiden = pickle.load(
    open(f'../graph/leiden.pickle', 'rb'))

girvan_newman = pickle.load(
    open(f'../graph/girvan_newman.pickle', 'rb'))

# define a function to convert snake case to camel case with hyphens
def snake_to_camel_with_hyphens(text):
    parts = text.split('-')
    return parts[0].lower() + ''.join(x for x in parts[1:])


# create a mapping of snake case column names to camel case with hyphens
mapping = {col: snake_to_camel_with_hyphens(col) for col in books.columns}


@app.route('/books/')
def index():
    # number of records per page
    PER_PAGE = 50
    # get the page number from the query string, default to 1
    page = int(request.args.get('page', 1))

    # calculate the offset and limit for the current page
    offset = (page - 1) * PER_PAGE
    limit = PER_PAGE

    # filter the records for the current page
    page_records = books.iloc[offset:offset +
                              limit].rename(columns=mapping).to_dict(orient='records')

    return jsonify(
        page_records,
    )

# define the route for getting a record by ID


@app.route('/book/<string:isbn>', methods=['GET'])
def get_book_by_id(isbn):
    # filter the DataFrame to find the record with the given ID
    record = books.loc[books['ISBN'] == isbn].rename(columns=mapping).to_dict(
        'records')

    # filter the ratings DataFrame to find the records with the given ISBN
    ratings_for_isbn = ratings.loc[ratings['ISBN'] == isbn]
    # calculate the average rating
    avg_rating = ratings_for_isbn['Book-Rating'].mean()
    # add the average rating to the book record

    # return the record as JSON if found, or a 404 error if not found
    if len(record) > 0:
        record[0]['avg_rating'] = math.ceil(avg_rating/2)
        return jsonify(record[0])
    else:
        return jsonify({'error': 'Record not found'}), 404


@app.route('/ratings/<string:isbn>', methods=['GET'])
def get_ratings_by_isbn(isbn):
    # filter the ratings DataFrame to find the records with the given ISBN
    filtered_ratings = ratings.loc[ratings['ISBN']
                                   == isbn]

    # join the ratings DataFrame with the users DataFrame on User-ID
    filtered_ratings = filtered_ratings.merge(users, on='User-ID')

    filtered_ratings['Book-Rating'] = filtered_ratings['Book-Rating'].apply(
        lambda x: math.ceil(x / 2))

    # return the ratings as JSON if found, or a 404 error if not found
    records = filtered_ratings.rename(
        columns={'Book-Rating': 'bookRating', 'Age': 'age', 'Location': 'location', 'User-ID': 'userId'}).rename(columns=mapping).to_dict('records')
    if len(records) > 0:
        return jsonify(records)
    else:
        return jsonify({'error': 'No ratings found for ISBN {}'.format(isbn)}), 404

@app.route('/<string:algorithm>/<string:isbn>')
def check_book(algorithm, isbn):
    if algorithm == 'louvain':
        for community in louvain:
            if isbn in community:
                records = books[books['ISBN'].isin(list(community))].rename(columns=mapping).to_dict('records')
                return jsonify(records)

    if algorithm == 'leiden':
        for community in leiden.communities:
            if isbn in community:
                records = books[books['ISBN'].isin(list(community))].rename(columns=mapping).to_dict('records')
                return jsonify(records)
            
    if algorithm == 'girvan_newman':
        for community in girvan_newman:
            if isbn in community:
                records = books[books['ISBN'].isin(list(community))].rename(columns=mapping).to_dict('records')
                return jsonify(records)

    else:
        return f"Invalid algorithm: {algorithm}."

if __name__ == '__main__':
    app.run(debug=True)
