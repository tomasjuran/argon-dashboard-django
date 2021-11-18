$(document).ready(function() {
    $(".radio-group .radio").click(function() {
        $('.radio').removeClass("selected");
        $(this).addClass("selected");
    });

    $(".eliminar-plan").click(function() {
        // TODO Eliminar plan
        console.log("TODO Eliminar plan");
    });

    $(".guardar-cambios").click(function () {
        // TODO Guardar cambios
        console.log("TODO Guardar cambios");
    });
});
