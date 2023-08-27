document.addEventListener("DOMContentLoaded", function () {
  // Obtén el contenedor de la imagen
  const imageContainer = document.getElementById("image-container");

  const images = ["imagenes/10.png", "imagenes/9.jpg"];
  let currentIndex = 0;
  const imageElement = document.getElementById("image");

  function changeImage() {
    imageElement.src = images[currentIndex];
    currentIndex = (currentIndex + 1) % images.length;
  }

  setInterval(changeImage, 4000);
});
