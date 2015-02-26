$("#search").click(function() {
    param = $("#"search_input).val();
    
    $.ajax({
        url: "exercises/...",
        type: "GET",
        dataType: "json",
        data : {
            // données
        },
        success:
        error:
    })
})