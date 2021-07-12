$(".cancel").click(function () {
    var id = $(this).attr('data-id')
    $.ajax({
        type: 'GET',
        url: '/cancelBook',
        data: {
            'bookId': id
        },
        success: function () {
            document.getElementById(bookId).remove();
        }
    })
});