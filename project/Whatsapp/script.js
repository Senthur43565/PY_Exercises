document.getElementById("run-python").addEventListener("click", function () {
  fetch("/run-python")
    .then(response => response.text())
    .then(result => {
      document.querySelector(".contain").style.display = "block";
      document.querySelector(".contain").textContent = result;
    });
});
