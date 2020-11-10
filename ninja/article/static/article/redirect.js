let area = document.getElementById("area");
const submit = document.getElementById("submit");
const formm = document.getElementById("form");

sub = () => {
  console.log(area.value.length);
  if (area.value.length < 144) {
    alert("the article content must contain at least more than 50 words");
    return false;
  } else {
    return true;
  }
}
