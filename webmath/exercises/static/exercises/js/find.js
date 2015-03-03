$(document).ready(function() {
    $('#false').hide();
    $('#true').hide();
    $("#search").click(function() {
        $("#lien").empty();
        var search = $("#search_input").val();
        $('#false').hide();
        $('#true').hide();
        
        $.ajax({
            url: "/exercises/search/",
            type: "GET",
            dataType: "json",
            data : {
                search : search,
            },
            success : function(response) {
                var $url= response["url"];
                $('#true').show();
                $("<a>", {
                "href": $url,
                }).text("Voici le lien").appendTo("#lien");
            },
            error : function() {
                $("#false").show();
            }
        });
    });
});

