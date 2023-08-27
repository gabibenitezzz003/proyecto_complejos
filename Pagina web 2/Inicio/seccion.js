// Función para cambiar la sección visible al hacer clic en un enlace del menú
function mostrarSeccion(seccionId) {
  // Oculta todas las secciones
  var secciones = document.querySelectorAll("section");
  secciones.forEach(function (seccion) {
    seccion.style.display = "none";
  });

  // Muestra la sección seleccionada
  var seccionMostrada = document.getElementById(seccionId);
  seccionMostrada.style.display = "block";
}

// Agrega un evento de clic a los enlaces del menú para cambiar la sección visible
var enlacesMenu = document.querySelectorAll("nav ul li a");
enlacesMenu.forEach(function (enlace) {
  enlace.addEventListener("click", function (event) {
    event.preventDefault();
    var seccionId = enlace.getAttribute("href").substr(1); // Obtiene el ID de la sección
    mostrarSeccion(seccionId);
  });
});
