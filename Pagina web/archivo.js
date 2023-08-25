document.addEventListener("DOMContentLoaded", function () {
  // Obtén el contenedor de la imagen
  const imageContainer = document.getElementById("image-container");

  const images = ["imagenes/4.jpg", "imagenes/2.jpg", "imagenes/3.jpg"];
  let currentIndex = 0;
  const imageElement = document.getElementById("image");

  function changeImage() {
    imageElement.src = images[currentIndex];
    currentIndex = (currentIndex + 1) % images.length;
  }

  setInterval(changeImage, 4000);
});
