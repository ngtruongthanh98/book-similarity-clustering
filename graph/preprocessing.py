import json
import pandas as pd
import chardet
from collections import Counter


df = pd.read_csv('../database/ratings.csv', delimiter=';', names=[
                 'User-ID', 'ISBN', 'Book-Rating'], skiprows=1, encoding='ISO-8859-1')

f = 900000
t = -1
df = df.iloc[f:t, :]  # Select rows from 0 to 49999, and all columns

print(df)

# Filter out users who have only bought one book
user_counts = df.groupby('User-ID').size()
users = user_counts[user_counts > 1].index.tolist()
df = df[df['User-ID'].isin(users)]

# Exclude all books that have been bought only once by all users
book_counts = df.groupby('ISBN').size()
books = book_counts[book_counts > 1].index.tolist()
df = df[df['ISBN'].isin(books)]
# Count frequency of book pairs bought by the same user
pair_counts = Counter()
for user, group in df.groupby('User-ID'):
    books = group['ISBN'].tolist()
    for i in range(len(books)):
        for j in range(i + 1, len(books)):
            book1, book2 = books[i], books[j]
            book_pair = book1 + '-' + book2 if book1 + '-' + \
                book2 in pair_counts else book2 + '-' + book1
            if book_pair not in pair_counts:
                pair_counts[book_pair] = 0
            pair_counts[book_pair] += 1

# Write the results to a JSON file
with open(f'{f}to{t}.json', 'w') as f:
    json.dump(pair_counts, f)

print('Results written to book_pairs.json')


# # Create empty dictionary to represent adjacency list
# users = {}

# # Read CSV file and populate adjacency list
# with open('ratings.csv', newline='', encoding='ISO-8859-1') as csvfile:
#     reader = csv.reader(csvfile, delimiter=';', quotechar='"')
#     next(reader)  # skip header row
#     for row in reader:
#         user_id, isbn, rating = int(row[0]), row[1], int(row[2])
#         # Add the current book to the list of books the user has bought
#         if user_id not in users:
#             users[user_id] = []
#         users[user_id].append(isbn)

# # Remove users who have bought only one book
# users = {user_id: books for user_id, books in users.items() if len(books) > 1}

# # Create empty dictionary to keep track of book pairs and their counts
# book_pairs = {}

# # Loop through all pairs of books in the adjacency list
# for user_id, books in users.items():
#     books = list(set(books))
#     for i in range(len(books)):
#         for j in range(i + 1, len(books)):
#             book1, book2 = books[i], books[j]
#             book_pair = book1 + book2 if book1 + book2 in book_pairs else book2 + book1
#             if book_pair not in book_pairs:
#                 book_pairs[book_pair] = {'count': 0}
#             book_pairs[book_pair]['count'] += 1

# del users
# # Write adjacency list to a JSON file
# with open('book_pair.json', 'w') as jsonfile:
#     json.dump(book_pairs, jsonfile)
