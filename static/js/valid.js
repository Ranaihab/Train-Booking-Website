function valid() {
    console.log("hiiiiiiii");
    if (document.getElementById("username").value == "") {
        alert("Please enter username");
        document.getElementById("username").focus();
        return false;
    }

    if (document.getElementById("first").value == "") {
        alert("Please enter First name");
        document.getElementById("first").focus();
        return false;
    }

    if (document.getElementById("last").value == "") {
        alert("Please enter last name");
        document.getElementById("last").focus();
        return false;
    }

    if (document.getElementById("password").value != "") {
        if (document.getElementById("password").value.length < 8) {
            alert("Error: Password must contain at least eight characters!");
            document.getElementById("password").focus();
            return false;
        }
        re = /[0-9]/;
        if (!re.test(document.getElementById("password").value)) {
            alert("Error: password must contain at least one number (0-9)!");
            document.getElementById("password").focus();
            return false;
        }
        be = /[a-z]/;
        if (!be.test(document.getElementById("password").value)) {
            alert("Error: password must contain at least one character (a-z)!");
            document.getElementById("password").focus();
            return false;
        }


    } else {
        alert("Error: Please enter a password");
        document.getElementById("password").focus();
        return false;
    }

    if (document.getElementById("password").value != document.getElementById("confirmPass").value) {
        alert("Confirm Password should be the same as password");
        document.getElementById("password").focus();
        return false;
    }

    if (document.getElementById("email").value != "") {
        if (document.getElementById("email").value.length < 8) {
            alert("Error: Email must contain at least eight characters");
            document.getElementById("email").focus();
            return false;
        }
        at = '@';
        dot = '.';
        if (!document.getElementById("email").value.includes(at) || !document.getElementById("email").value.includes(dot)) {
            alert("Error: enter a correct email ");
            document.getElementById("email").focus();
            return false;
        }


    } else {
        alert("Error: Please enter an email");
        document.getElementById("email").focus();
        return false;
    }

    if(!document.getElementById("admin").checked && !document.getElementById("customer").checked){
        alert("Error: Please choose User Type");
        return false;
    }
    return true;
}