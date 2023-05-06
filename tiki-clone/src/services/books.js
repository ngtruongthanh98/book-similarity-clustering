import axios from "axios";

export const getBookByPage = (pageNumber) => {
  const url = `http://127.0.0.1:5000/books/?page=${pageNumber}`;
  return axios.get(url);
};

export const getBookDetails = (bookId) => {
  const url = `http://127.0.0.1:5000/book/${bookId}`
  return axios.get(url);
}
