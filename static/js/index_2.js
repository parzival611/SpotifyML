$(document).ready(function(){
    var text;
    $('a').click(function(){
        var cur = $(this).html();
        console.log(cur);
        var pre = $(this).parent().attr('id');
        text = pre +" "+cur;
        $("#text").append(text);
        $("#text").append('<br>');
    })
});