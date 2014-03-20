$(document).ready(function() {
    $(".btn-setlang").click(function(e) {
        var form = $(".set_language");
        form.find("input[name='language']").val(
            $(this).attr("data-language")
        );
        form.submit();
    });
});
