$(function(){
//j'initialise la variable nécessaire pour l'incrémentation
var rowNum = 0;

// Je sélectionne l'élément form et j'attends qu'il soit en event submit
$('form').on('submit',function(event){

//j'envoye ma requête ajax au root / url finalprocessing
$.ajax({
data : {
message:$("#formtext").val()
},
type: "POST",
url:'/finalprocessing'
})

// Une fois que ça a été fais je regarde la réponse du serveur
.done(function(data){

// si le serveur me renvoye une erreur
if (data.error){
("#chatresponse").append("<p>"+data.error+"</p>");
$("#formtext").val('');

// Si le serveur me renvoye les éléments , input_user, result_search , suggestion_search
//latitude , longitude et datacarte :

}else if (data.input_user && data.result_search && data.suggestion_search && data.latitude && data.longitude && data.datacarte)
{
$("#chatresponse").append("<p>"+ "ce que tu cherches est => " + data.input_user+"</p>");
$("#chatresponse").append("<p>"+data.result_search+"</p>");


//1 - je commence ma fonctionnalité d'incrémentation
// elle fonctionne car je l'ai testé avec un alert
rowNum++;

//2- je crée un nouvel élément avec la fonctionnalité d'incrémentation
var row = $("<div id='newmap-"+rowNum+"' class='address' />");

//3- je crée la variable sous forme de string
//ça fonctionne j'ai vérifié
var variablemap = '#newmap-'+rowNum;

//4 je vérifie qu'elle fonctionne avec un console.log
//ça fonctionne j'ai vérifié

console.log(variablemap);

//5 je vérifie qu'elle fonctionne avec un alert
//ça fonctionne j'ai vérifié

alert(variablemap);




// je rajoute cet élément à l'id Chat response
//ça fonctionne j'ai vérifié
$("#chatresponse").append(row);
$(variabemap).html(data.datacarte)

// J' affiche la carte entre ces deux commentaires
//je teste si la variable que je viens de créer
// => variablemap fonctionne dynamiquement
/*
new GMaps({
  div: variablemap,
  lat: -12.043333,
  lng: -77.028333
});
*/
/*
map = new google.maps.Map(document.getElementById('dispnlaycard'), {
  center: {lat:data.latitude, lng: data.longitude},
  zoom: 8
});*/

// affichage de la carte finit



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

