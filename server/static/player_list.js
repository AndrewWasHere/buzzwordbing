var add_player = function(game_name) {
    var name = document.getElementById("newplayername").value;
    document.location = "/" + game_name + "/" + name + "/";
};


var on_load = function() {
    var input = document.getElementById("newplayername");
    input.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            document.getElementById("submit").click();
        }
    });
};


var delete_finished = function() {
    document.location = "/";
};


var delete_game = function(game_name) {
    var request = new XMLHttpRequest();
    request.addEventListener("load", delete_finished);
    request.open("DELETE", "/" + game_name + "/");
    request.send();
};
