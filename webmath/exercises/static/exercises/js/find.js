$(document).ready(function() {
    $("#search").click(function() {
        var search = $("#search_input").val();
        
        $.ajax({
            url: "/exercises/search/",
            type: "GET",
            dataType: "json",
            data : {
                search : search,
            },
            success : function(response) {
            },
            error : function() {
            }
        });
    });
});