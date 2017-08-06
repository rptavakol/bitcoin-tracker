$(document).ready(function () {

    function ajax_call() {
        $.ajax({
        type: "GET",
        url: "../../run",
        dataType: "json",
        success: inject_DOM
        });
    }

    function inject_DOM(data) {
        $("#ask").text(data["last"]);
        $("#high").text(data["high"]);
        $("#low").text(data["low"]);
        console.log("New Price: " + data["last"])
    }

    setInterval(ajax_call,3000)

});