const searchButton = document.querySelector('#search-button');
const searchInput = document.querySelector('#search');

searchButton.addEventListener('click', () => {
  const searchText = searchInput.value;
  const books = document.querySelectorAll('.Book-name');
  books.forEach((book) => {
    if (book.textContent.toLowerCase().indexOf(searchText.toLowerCase()) > -1) {
      book.parentElement.parentElement.style.display = 'block';
    } else {
      book.parentElement.parentElement.style.display = 'none';
    }
  });
});