document.addEventListener("DOMContentLoaded", function () {
  const reservationForm = document.getElementById("reservation-form");

  reservationForm.addEventListener("submit", (e) => {
    e.preventDefault(); // Evita el envío del formulario por defecto

    // Obtén los datos del formulario
    const formData = new FormData(reservationForm);

    // Realiza una petición POST al servidor Flask
    fetch("/submit", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          return response.text(); // Retorna el mensaje de éxito desde el servidor
        }
        throw new Error("Error al enviar la reserva");
      })
      .then((message) => {
        alert(message); // Muestra el mensaje de éxito al usuario
      })
      .catch((error) => {
        console.error("Error:", error);
        // Podrías mostrar un mensaje de error al usuario si algo sale mal
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
