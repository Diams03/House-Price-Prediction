function getBathValue(){
    var uiBathrooms=document.getElementsByName("uiBathrooms")
    for(var i in uiBathrooms){
        if(uiBathrooms[i].checked){
            return parseInt(i)+1;
        } 
    }
    return -1;
}

function getBhkValue(){
    var uiBHK=document.getElementsByName("uiBHK")
    for(var i in uiBHK){
        if(uiBHK[i].checked){
            return parseInt(i)+1;
        } 
    }
    return -1;
}

function  onClickedEstimatePrice(){
    var bath=getBathValue();
    var bhk=getBhkValue;
    var total_sqft=document.getElementById("uiSqft");
    var locations=document.getElementById("uiLocations");
    var estim_price=document.getElementById("uiEstimatedPrice");
    var url="/api/predict_home_price";

    $.post(url,{
        total_sqft: parseFloat(total_sqft.value),
        location: locations.value,
        bhk: bhk,
        bath: bath
    },function(data,status){
        estim_price.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
    });
}

function onPageLoad(){
    var url="/api/get_locations_name";
    $.get(url,function(data,status){
        if(data){
            var location=data.location;
            var uiLocations=document.getElementById("uiLocations")
            $('uiLocations').empty();
            for(var i in location){
                var opt=new Option(location[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}






















window.onload = onPageLoad;