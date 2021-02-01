$(function(){

$('form').on('submit',function(event){



$.ajax({
data : {
message:$("#formtext").val()
},
type: "POST",
url:'/finalprocessing'
})


.done(function(data){
if (data.error){
("#chatresponse").append("<p>"+data.error+"</p>");
$("#formtext").val('');

//alert("yo there was an error");

}else if (data.input_user && data.result_search && data.suggestion_search){
$("#chatresponse").append("<p>"+ "ce que tu cherches est => " + data.input_user+"</p>");
$("#chatresponse").append("<p>"+data.result_search+"</p>");
$("#chatresponse").append("<p>" + "voici des suggestions qui pourront t'aider à trouver"+ " davantage d'informations sur ce que tu cherches : "+ " <br>"+data.suggestion_search+"</p>")
$("#formtext").val('');

//alert('yo i received something');

}else{
    $("#chatresponse").append("<p>"+ "ce que tu cherches est => " + data.input_user+ "<br>"+ "<br>"+" et malheuresement nous n'avons pas trouver d'informations sur ce que tu cherches " +"</p>" );
    $("#chatresponse").append("<p>" + "voici des suggestions qui pourront t'aider à trouver"+" ce que tu cherches : "+ " <br>"+ " <br>"+data.suggestion_search+"</p>")
    $("#formtext").val('');


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

