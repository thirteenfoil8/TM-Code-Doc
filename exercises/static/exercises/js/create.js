$(document).ready(function() {
    $("#voir").click(function() {
        var formule = $("#equation").val();
        var donnee= $("#donnee").val();
        $("#formule").text(formule);
        $("#donnee-apercu").text(donnee)
        $("#apercu").css({display : "block"})
    })
});
