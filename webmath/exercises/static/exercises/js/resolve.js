$(document).ready(function() {
    $("#submit-resolve").click(function() {
        if ($("#response").val()) {
            $("#resolve-form").submit(); // renvoie le formulaire si tous les champs sont remplis
        }
        else {
            $("#form-warning").modal("show"); // Affiche un message d'erreur si tous les champs ne sont pas rempli
            
        }
    });
});