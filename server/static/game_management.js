var delete_game = function(game_name) {
    var request = new XMLHttpRequest();
    request.open("DELETE", "/" + game_name + "/");
    request.send();
    document.location.reload();
}


var create_finished = function() {
    document.location = "/" + document.getElementById("newgamename").value + "/";
}


var new_game = function() {
    var request = new XMLHttpRequest();
    request.addEventListener("load", create_finished);
    request.open("PUT", "/" + document.getElementById("newgamename").value + "/");
    var free_space = document.getElementById("freespace").checked;
    var fake_form = new FormData();
    fake_form.append("free", free_space);
    request.send(fake_form);
}


var on_load = function() {
    var input = document.getElementById("newgamename");
    input.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            document.getElementById("submit").click();
        }
    });
}
