function check() {
    var count = $("#op :selected").length;

    if (count == 0) {
        alert("You should select at least on seat");
        return false;
    }
    if (!document.getElementById("credit").checked && !document.getElementById("cash").checked) {
        alert("You should select payement method");
        return false;
    }
    if (document.getElementById("credit").checked) {
        if (document.getElementById("creditNum").value.length != 16 || isNaN(document.getElementById("creditNum").value)) {
            alert("Credit Number should be 16 digits");
            return false;
        }
        if (document.getElementById("ccv").value.length != 3 || isNaN(document.getElementById("ccv").value)) {
            alert("CCV should be 3 digits");
            return false;
        }
    }
    return true;

}

$('#op').change(function () {
    var count = $("#op :selected").length;
    var price = $(this).attr('data');
    var tPrice = count * price;
    $("#price").val(tPrice);
});



function displayCredit() {
    var x = document.getElementById('textBox');
    if (x.style.visibility === 'hidden') {
        x.style.visibility = 'visible';
    }
}

function hideCredit() {
    var x = document.getElementById('textBox');
    if (x.style.visibility === 'visible') {
        x.style.visibility = 'hidden';
    }
}