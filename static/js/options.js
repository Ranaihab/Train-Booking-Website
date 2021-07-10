function edit(obj, id1, id2, id3, id4, id5) {
    text = obj.options[obj.selectedIndex].value;

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

    }

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
}