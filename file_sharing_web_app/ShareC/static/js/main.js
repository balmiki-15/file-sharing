const uploadBtn = document.getElementById("upload-btn");

uploadBtn.addEventListener("change", function () {
  const formData = new FormData();
  const fileField = document.querySelector('input[type="file"]');

//   formData.append("filename", this.files[0].name);
  formData.append("file", fileField.files[0]);
  const url = window.location.href;
  fetch(url+'send', {
    method: "POST",
    body: formData,
  })
    .then((response) => response.text())
    .then((result) => {
      console.log("Success:", result);
    })
    .catch((error) => {
      console.error("Error:", error);
    });

  //   fileChosen.textContent = this.files[0].name
});
