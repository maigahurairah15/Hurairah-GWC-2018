var lat;
var lng; //variables declared at the top

function sunriseTime () {
   lat = document.getElementById("lat").value; //gets user latitude value
   lng = document.getElementById("lng").value; //gets user longitude value
   var query = "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng;
   var request = new XMLHttpRequest();
   request.open('GET', query, false);
   request.send();
     var requestInformation = JSON.parse(request.responseText);
     var sunriseTime = requestInformation.results.sunrise;
     alert("The sunrise time is" + sunriseTime);
     var sunsetTime = requestInformation.results.sunset;
     alert("The sunset time is" + sunsetTime );
