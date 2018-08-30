$(document).ready( function () {
    $("#btnTrans").click(function() {
        $.post("/get_trans", {"method": 'tofill', "text": $("#input").val()}, function(response) {
            $("#afterTrans").val(response)
        })
    })
})

