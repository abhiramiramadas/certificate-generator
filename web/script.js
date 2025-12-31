function generate() {
  const name = document.getElementById("nameInput").value;
  document.getElementById("name").innerText = name || "Your Name";
}
