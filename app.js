function getNumbers() {
  const main = document.getElementById("main");

  fetch("http://localhost:8080/get_numbers")
    .then((r) => r.text())
    .then((txt) => (main.innerHTML = txt));
}

(() => {
  const button = document.getElementById("button");
  button.addEventListener("click", getNumbers);
})();
