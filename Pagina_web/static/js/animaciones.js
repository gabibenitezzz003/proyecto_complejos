// Agrega un evento de clic a los enlaces del menú para cambiar la sección visible y el fondo del body
var enlacesMenu = document.querySelectorAll("nav ul li a");
enlacesMenu.forEach(function (enlace) {
  enlace.addEventListener("click", function (event) {
    event.preventDefault();
    var seccionId = enlace.getAttribute("href").substr(1); // Obtiene el ID de la sección
    var colorFondo = enlace.getAttribute("data-color"); // Obtiene el color de fondo deseado desde el atributo data-color
    mostrarSeccion(seccionId, colorFondo);
  });
});
//Le da un color de fondo a la seccion
function mostrarSeccion(seccionId, colorFondo) {
  // Oculta todas las secciones
  var secciones = document.querySelectorAll("section");
  secciones.forEach(function (seccion) {
    seccion.style.display = "none";
  });

  // Muestra la sección seleccionada
  var seccionMostrada = document.getElementById(seccionId);
  seccionMostrada.style.display = "block";

  // Cambia el fondo del body
  document.body.style.backgroundColor = colorFondo;
}
// Cambia la imagen
document.addEventListener("DOMContentLoaded", function () {
  const images = ["imagenes/10.png", "imagenes/9.jpg"];
  let currentIndex = 0;
  const imageElement = document.getElementById("image");
  function changeImage() {
    imageElement.src = images[currentIndex];
    currentIndex = (currentIndex + 1) % images.length;
  }
  setInterval(changeImage, 4000);
});

// Obtén todas las imágenes de la cuadrícula
const images = document.querySelectorAll(".grid img");

// Agrega el evento mouseover para agrandar las imágenes al pasar el cursor
images.forEach((image) => {
  image.addEventListener("mouseover", () => {
    image.style.transform = "scale(1.1)";
  });

  image.addEventListener("mouseout", () => {
    image.style.transform = "scale(1)";
  });

  // Agrega el evento clic para mostrar la imagen en pantalla completa
  image.addEventListener("click", () => {
    const fullscreen = document.createElement("div");
    fullscreen.classList.add("fullscreen");
    const fullscreenImage = document.createElement("img");
    fullscreenImage.src = image.src;
    fullscreen.appendChild(fullscreenImage);
    document.body.appendChild(fullscreen);

    // Agrega el evento clic para cerrar la imagen en pantalla completa
    fullscreen.addEventListener("click", () => {
      fullscreen.remove();
    });
  });
});
document.addEventListener("DOMContentLoaded", function () {
  var fechaIngreso = document.getElementById("fecha_ingreso");
  var fechaSalida = document.getElementById("fecha_salida");

  fechaIngreso.addEventListener("input", function () {
    fechaSalida.min = sumarDias(fechaIngreso.value, 1);
    validarFechaSalida();
  });

  fechaSalida.addEventListener("input", function () {
    validarFechaSalida();
  });

  function sumarDias(fecha, dias) {
    var nuevaFecha = new Date(fecha);
    nuevaFecha.setDate(nuevaFecha.getDate() + dias);
    return nuevaFecha.toISOString().split("T")[0];
  }

  function validarFechaSalida() {
    if (fechaSalida.value && fechaSalida.value <= fechaIngreso.value) {
      alert(
        "La fecha de salida debe ser al menos un día después de la fecha de ingreso."
      );
      fechaSalida.value = "";
    }
  }

  // Establecer el valor mínimo inicial de fecha_salida
  fechaSalida.min = sumarDias(fechaIngreso.value, 1);
});
