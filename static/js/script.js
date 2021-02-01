$(function(){

$('form').on('submit',function(event){



$.ajax({
data : {
message:$("#formtext").val()
},
type: "POST",
url:'/processing'
})


.done(function(data){
if (data.error){
("#chatresponse").append("<p>"+data.error+"</p>");
$("#formtext").val('');

//alert("yo there was an error");

}else {
$("#chatresponse").append("<p>"+data.message+"</p>");
$("#formtext").val('');

//alert('yo i received something');

}

});
event.preventDefault();


});

// Just below some experimentations i did with Javascript and Jquery
/*

$("#buttonsubmit").click(function(e){
let inputTextValue =$("#formtext").val();

$("#chatresponse").append("<p>"+inputTextValue+"</p>");
e.preventDefault(e);
$("#formtext").val('');
})
*/
});

