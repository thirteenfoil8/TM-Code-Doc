$(document).ready(function() {
    $('#false').hide(); // Cache les divs #false et #true
    $('#true').hide();
    $("#search").click(function() {
        $("#lien").empty(); // Supprime l'éventuelle ancienne valeur
        var $search = $("#search_input").val(); // enregistre la valeur de la recherche
        $('#false').hide();
        $('#true').hide();
        
        $.ajax({
            url: "/exercises/search/",
            type: "GET",
            dataType: "json",
            data : {
                search : $search, //récupère les données de la recherche par rapport à l'exercice recherché ( $search )
            },
            success : function(response) { // Ajoute le lien de l'exercice si il existe et l'affiche à l'utilisateur dans la div #true
                var $url= response["url"];
                $('#true').show();
                $("<a>", {
                "href": $url,
                }).text("Voici le lien").appendTo("#lien");
            },
            error : function() { // Affiche le message d'erreur si l'exercice n'existe pas 
                $("#false").show();
            }
        });
    });
});

