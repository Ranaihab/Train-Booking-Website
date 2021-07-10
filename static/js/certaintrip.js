function check(form) {


    if (form.textfield2.value.length > 30) {
        alert("Error : Too Long! ");
        form.textfield2.focus();
        return false;

    }
    if (form.textfield.value.length > 30) {
        alert("Error : Too Long! ");
        form.textfield2.focus();
        return false;

    }
    if (form.textfield3.value.length > 30) {
        alert("Error : Too Long! ");
        form.textfield2.focus();
        return false;

    }
    if (form.textfield4.value.length > 30) {
        alert("Error : Too Long! ");
        form.textfield2.focus();
        return false;

    }
    if (form.textfield5.value.length > 30) {
        alert("Error : Too Long! ");
        form.textfield2.focus();
        return false;

    }
}

function displayNumber() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange =

        function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById("num").innerHTML = this.responseText;
            }

        };
    xhttp.open("GET", "num.html", true);
    xhttp.send();
}