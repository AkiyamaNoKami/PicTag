window.onload = () => {
    document.querySelectorAll('.search-group').forEach((element) => {
      const
        searchField = element.querySelector('input'),
        searchSuggestions = element.querySelector('ul');

      searchField.addEventListener('keyup', (event) => {
        if (event.key != 'Escape') {
          fetch(`/autocomplete/tags/?q=${event.target.value}`)
            .then((response) => { return response.json(); })
            .then((data) => {
              searchSuggestions.style.display = 'block';
              searchSuggestions.innerHTML = data.map((item) => { return `<li>${item.name}</li>` }).join('');
            });
        }
      });

      searchSuggestions.addEventListener('click', (event) => {
        searchField.value = event.target.textContent;
      });

      document.addEventListener('click', (event) => {
        if (event.target != searchField) {
          searchSuggestions.style.display = 'none';
        }
      });
    });
}
