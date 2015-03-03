$(document).ready(function() {
    $("#submit-resolve").click(function() {
        if ($("#student").val() && $("#response").val()) {
            $("#resolve-form").submit();
        }
        else {
            $("#form-warning").modal("show");
            
        }
    });
});