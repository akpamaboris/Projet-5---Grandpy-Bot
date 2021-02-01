$(function(){


$("#buttonsubmit").click(function(e){
let inputTextValue =$("#formtext").val();

$("#chatresponse").append("<p>"+inputTextValue+"</p>");
e.preventDefault(e);
$("#formtext").val('');
})

})

