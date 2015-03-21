$(document).ready(function() {
    $("#submit-resolve").click(function() {
        if ($("#response").val()) {
            $("#resolve-form").submit();
        }
        else {
            $("#form-warning").modal("show");
            
        }
    });
});