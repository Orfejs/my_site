//console.log('tetris');
//
//function myFunction() {
//console.log(response.seconds);
//

$(document).ready(function(){
    var csrf = $("input[name=csrfmiddlewaretoken]").val();

$(".fav").click(function(){
//console.log('tetris')
    $.ajax({
        url: '',
        type: 'get',
        data: {
            test: 'someValue'
        },
        success: function(response) {
          $("#mypic").attr("src", response.question);

    }}
    )

});


$(".add").click(function(){
    $.ajax({
        url: '',
        type: 'post',
        data: {
            test2: $("#mypic").attr("src"),
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
             console.log(response.good)
             alert("Picture saved")

    }}
    )
});

$(".act").click(function(){
    $.ajax({
        url: '',
        type: 'post',
        data: {
            test3: 'someval',
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
            console.log(response.well)
        }
    })
}
)
})