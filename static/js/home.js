

function reset() {
    document.getElementById("dateOption").value = '';
    document.getElementById("sourceOption").value = '';
    document.getElementById("destOption").value = '';
    document.getElementById("timeOption").value = '';
    document.getElementById("seatNbOption").value = '';
}

function filter(data) { 
    //var trips = document.getElementById("variable").value;
    //var trips = JSON.parse(data);
    console.log(data);
    var date = document.getElementById("dateOption").value;
    var source = document.getElementById("sourceOption").value;
    var dest = document.getElementById("destOption").value;
    var time = document.getElementById("timeOption").value;
    var seatNb = document.getElementById("seatNbOption").value;
    if(document.getElementById("dateOption").value != '')
        for(var trip in trips)
            console.log(trip.date);
}


    /*text = obj.options[obj.selectedIndex].value;

    document.getElementById("op1").style.display = 'none';
    document.getElementById("op2").style.display = 'none';
    document.getElementById("op3").style.display = 'none';
    document.getElementById("op4").style.display = 'none';
    document.getElementById("op5").style.display = 'none';

    if (text.match(op1)) {
        document.getElementById("op1").style.display = 'block';

    }
    if (text.match(op2)) {
        document.getElementById("op2").style.display = 'block';

    }

    if (text.match(op3)) {
        document.getElementById("op3").style.display = 'block';

    }

    if (text.match(op4)) {
        document.getElementById("op4").style.display = 'block';

    }

    if (text.match(op5)) {
        document.getElementById("op5").style.display = 'block';

    }*/

    /** 
    function date() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange =

            function() {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("da").innerHTML = this.responseText;
                }

            };
        xhttp.open("GET", "date.html", true);
        xhttp.send();
    }

    function time() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange =

            function() {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("ti").innerHTML = this.responseText;
                }

            };
        xhttp.open("GET", "time.html", true);
        xhttp.send();
    }**/