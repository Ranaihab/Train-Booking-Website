$('.cancel').click(function () {
    var id = $(this).attr('data-id');
    var userId = $(this).attr('data-user');
    $.ajax({
        type: 'GET',
        url: '/cancelBook',
        data: {
            'bookId': id, 
            'userId': userId
        },
        success: function (response) {
            if (response.msg == "Book is canceled") {
                document.getElementById(id).remove();
                var rows = document.getElementById("tripsTable").children;
                var table = document.getElementById("tripsTable");
                if (table.rows.length == 1) {
                    var row = table.insertRow(1);
                    var cell = row.insertCell(0);
                    cell.innerHTML = "No Books";
                    cell.colSpan = "10";

                }
            }
            document.getElementById("msg").innerHTML = response.msg
        }
    })
});