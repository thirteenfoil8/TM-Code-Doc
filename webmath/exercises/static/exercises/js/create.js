$(document).ready(function() {
    $( ".corrigé" ).hide(); // cache la div du corrigé qui sera affiché plus tard
    $("#voir").click(function() {
        var $formule = $(".equation").val(); // Récupère la valeur de l'équation
        $(".formule").text("$$" + $formule + "$$"); // La formate en Latex grâce à MathJax
        $(".corrigé").show();
        MathJax.Hub.Queue(["Typeset", MathJax.Hub]); // permet d'afficher l'équation en Latex sans avoir à recharger la page
    });
    $("#submit-resolve").click(function() { 
        if ($("#correction").val()&& $("#equation").val()) {
                $("#create-form").submit(); // renvoie le formulaire si les tous les champs sont remplis
            }
        else {
            $("#form-warning").modal("show"); // Affiche un message d'erreur si tous les champs ne sont pas rempli
            
        }
    });
});
