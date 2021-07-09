function valid(form) {

    if (form.fname.value == "") {
        alert("Please enter first name");
        form.fname.focus();
        return false;
    }

    if (form.sname.value == "") {
        alert("Please enter last name");
        form.sname.focus();
        return false;
    }

    if (form.pass.value != "") {
        if (form.pass.value.length < 8) {
            alert("Error: Password must contain at least eight characters!");
            form.pass.focus();
            return false;
        }
        re = /[0-9]/;
        if (!re.test(form.pass.value)) {
            alert("Error: password must contain at least one number (0-9)!");
            form.pass.focus();
            return false;
        }
        be = /[a-z]/;
        if (!be.test(form.pass.value)) {
            alert("Error: password must contain at least one character (a-z)!");
            form.pass.focus();
            return false;
        }


    } else {
        alert("Error: Please enter a password");
        form.pass.focus();
        return false;
    }

    if (form.email.value != "") {
        if (form.email.value.length < 8) {
            alert("Error: Email must contain at least eight characters");
            form.email.focus();
            return false;
        }
        at = '@';
        dot = '.';
        if (!at.test(form.email.value) || !dot.test(form.email.value)) {
            alert("Error: enter a correct email ");
            form.email.focus();
            return false;
        }


    } else {
        alert("Error: Please enter an email");
        form.pass.focus();
        return false;
    }
    return true;
}