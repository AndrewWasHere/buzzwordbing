var req_seq = 1;
var bingoed = false;

var PlayByPlay = function() {
    this.next_idx = 0;
    this.plays = [];
    this.handle = function(response) {
        //console.log("Live updates passed to handle()!")
        var lines = response.split('\n');
        p.next_idx = parseInt(lines[0]);
        if (isNaN(p.next_idx)) {
            p.next_idx = 0 ;
            //throw "The data was formatted incorrectly. Is the server running flask/jinja2?";
            console.log("Something went wrong...")
        }
        while (!lines[lines.length-1]) {
            // Purge ALL the newlines!
            lines.pop();
            break;
        }

        if (lines.length == 0) {
            console.log("I guess that connection failed...")
            document.getElementById("connection_problems").className = "";
        } else {
            document.getElementById("connection_problems").className = "hidden";
        }
        lines.shift();
        p.plays = p.plays.concat(lines);
        //console.log(lines.length + " lines received:" + lines)
    }
    this.fetch = function () {
        var r = new XMLHttpRequest();
        var onFinish = function(){p.handle(r.response)};
        r.addEventListener("loadend", onFinish);
        r.open('POST', '/'+game_id+'/play-by-play/');
        var fake_form = new FormData();
        fake_form.append("idx", p.next_idx);
        r.send(fake_form);
    };
    this.get = function(n) {
        if (n === undefined) {
            n = 5;
        }
        return this.plays.slice(-n)
    }
};

p = new PlayByPlay();

var upd_PBP = function() {
    //console.log("--------------------- request_seq = " + req_seq + " ---------------------");
    p.fetch();
    var display = p.get(20);
    var el = document.getElementById("play_by_play");
    //console.log(display.length + " items")
    el.innerText = ""
    for (var x = 0; x < display.length; x ++) {
        el.innerText = el.innerText + display[x] + "\n";
    }
    req_seq ++;
};
setInterval(upd_PBP, 500);


var sendMove = function(text) {
    var r = new XMLHttpRequest();
    r.open("POST", "/" + game_id + "/" + player_id + "/");
    var fake_form2 = new FormData();
    fake_form2.append("move", text);
    r.send(fake_form2);
};


var didWeWin = function() {
    var words = document.getElementsByClassName('word');
    console.debug("left and right");
    for (var x = 0; x < 25; x += 5) {
        console.debug(x);
        var elsToCheck = [words[x].className == "word selected", words[x+1].className == "word selected", words[x+2].className == "word selected", words[x+3].className == "word selected", words[x+4].className == "word selected"];
        console.debug(elsToCheck);
        if (elsToCheck[0] && elsToCheck[1] && elsToCheck[2] && elsToCheck[3] && elsToCheck[4] && true) {
            console.log("- " + elsToCheck);
            return true;
        }
    }
    console.debug("up and down");
    for (var x = 0; x < 5; x += 1) {
        console.debug(x);
        var elsToCheck = [words[x].className == "word selected", words[x+5].className == "word selected", words[x+10].className == "word selected", words[x+15].className == "word selected", words[x+20].className == "word selected"];
        console.debug(elsToCheck);
        if (elsToCheck[0] && elsToCheck[1] && elsToCheck[2] && elsToCheck[3] && elsToCheck[4] && true) {
            console.log("| " + elsToCheck);
            return true;
        }
    }
    console.log("diagonals")
    var elsToCheck2 = [words[0].className == "word selected", words[6].className == "word selected", words[12].className == "word selected", words[18].className == "word selected", words[24].className == "word selected"]
    console.debug(elsToCheck2);
    if (elsToCheck2[0] && elsToCheck2[1] && elsToCheck2[2] && elsToCheck2[3] && elsToCheck2[4] && true) {
        console.log("\\ " + elsToCheck2);
        return true;
    }
    var elsToCheck2 = [words[4].className == "word selected", words[8].className == "word selected", words[12].className == "word selected", words[16].className == "word selected", words[20].className == "word selected"]
    console.debug(elsToCheck2);
    if (elsToCheck2[0] && elsToCheck2[1] && elsToCheck2[2] && elsToCheck2[3] && elsToCheck2[4] && true) {
        console.log("/" + elsToCheck2);
        return true;
    }
    return false;
}


var toggleType = function(event) {
    if (!bingoed) {
        var element = event.target;
        //console.log("click " + event.target + element.className)
        if (element.className === "word selected") {
            //console.log("removing SELECTED")
            sendMove("unmarked \"" + element.innerText + "\".");
            element.className = "word";
        } else if (element.className === "word") {
            //console.log("making SELECTED")
            sendMove("marked \"" + element.innerText + "\"!");
            element.className = "word selected";
        }
        if (didWeWin()) {
            document.getElementById("newboard").className = "selectedstyledbutton";
            document.getElementById("newboard").innerText = "Play Again";
            document.getElementById("bingo").className = "";
            bingoed = true;
            sendMove("got a BINGO!");
        }
    }
    event.preventDefault();
}


var on_load = function() {
    var words = document.getElementsByClassName('word');
    for (var x = 0; x < words.length; x ++) {
        var el = words[x];
        el.addEventListener("click", toggleType);
        console.log("add event listener on click")
    }
}
