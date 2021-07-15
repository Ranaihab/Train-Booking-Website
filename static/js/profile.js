function valid() {
    if (document.getElementById("username").value == "") {
        alert("Please enter username");
        document.getElementById("username").focus();
        return false;
    }

    if (document.getElementById("fname").value == "") {
        alert("Please enter First name");
        document.getElementById("first").focus();
        return false;
    }

    if (document.getElementById("lname").value == "") {
        alert("Please enter last name");
        document.getElementById("last").focus();
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
    return true;
}



$('#submit').click(function(){
    if($('#submit').val() == 'update'){
        $('#submit').val('save');
        $('input').attr('readonly', false);
        return false;
    }

    if (!valid()){
        return false;
    }

    var userId = $(this).attr('user-id');
    var username = $("#username").val();
    var fname = $("#fname").val();
    var lname = $("#lname").val();
    var password = $("#password").val();
    var email = $("#email").val();
    var st = '&userId=' + userId + '&username=' + username +
                     '&password=' + password +'&fname=' + fname + '&lname=' + lname +'&email=' + email
    var submitData = {
        'userId': userId,
        'username': username,
        'fname': fname,
        'lname': lname,
        'email': email,
        'password': password
    };
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
        type: 'POST',
        url: '/updateProfile',
        data: JSON.stringify(submitData),
        dataType: 'json',
        contentType: 'application/json',
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function (response) {;
            if(response.msg == "Information Saved"){
                $('#submit').val('update');
                $('input').attr('readonly', true);
                document.getElementById("us").innerHTML = username;
            }
            document.getElementById("msg").innerHTML = response.msg;
            
        }
    })
});
