$(document).ready(function () {

    $('#assignment_type').change(function () {
        var name = $('#assignment_type').val();
        $(".details").hide();
        $("." + name).show();
        console.log(name);
    })

    console.log("test");

});