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
        success: function () {
            document.getElementById(id).remove();
        },
        error: function(){
            console.log("hi")
        }
    })
});