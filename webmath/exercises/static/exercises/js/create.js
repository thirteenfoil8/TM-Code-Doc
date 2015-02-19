$(document).ready(function() {
    $( ".corrigé" ).hide();
    $("#voir").click(function() {
        var $formule = $(".equation").val();
        // var $donnee= $("#donnee").val();
        $(".formule").text("$$" + $formule + "$$");
        // $("#donnee-apercu").text($donnee);
        // $("#apercu").css({display : "block"});
        $(".corrigé").show();
        MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    });
});
