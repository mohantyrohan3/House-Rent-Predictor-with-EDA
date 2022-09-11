function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
}
  
function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
}


function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var location = document.getElementById("uiLocations");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var estPrice = document.getElementById("uiEstimatedPrice");
    
    var url1 = "http://127.0.0.1:5000/"; //Use this if you are NOT using nginx which is first 7 tutorials
    if (location.value=='Ahmedabad'){
        url1 += "ahmedabad";
    }
    else{
        url1 += location.value;
    }
    
    url1 += '_model';
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url1, {
        bedroom: bhk,
        area: parseFloat(sqft.value), 
        bathroom: bathrooms,
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Thousand Rupees</h2>";
        console.log(status);
    });
}

function onPageLoad(){
    console.log("document loaded")
}




window.onload = onPageLoad;