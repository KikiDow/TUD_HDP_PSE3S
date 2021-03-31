/*global navigator*/
/*global $*/

function validateDate(inputText) {
    if( inputText.value == "" ) {
            alert( "No date entered !!" );
            //document.rosterSearchForm.q.focus() ;
            return false;
        }
        
    var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[\/](0?[1-9]|1[012])[\/]\d{4}$/;
    if(inputText.value.match(dateformat)) {
            var input_date = inputText.value.split('/');
            var dd = parseInt(input_date[0]);
            var mm  = parseInt(input_date[1]);
            var yy = parseInt(input_date[2]);
            var ListofDays = [31,28,31,30,31,30,31,31,30,31,30,31];
            
            if (mm==1 || mm>2) {
                if (dd>ListofDays[mm-1]) {
                    alert('Invalid date format!');
                    return false;
                }
            }
            if (mm==2) {
                var lyear = false;
                if ( (!(yy % 4) && yy % 100) || !(yy % 400)) {
                    lyear = true;
                }
                if ((lyear==false) && (dd>=29)) {
                    alert('Invalid date format!');
                    return false;
                }
                if ((lyear==true) && (dd>29)) {
                    alert('Invalid date format!');
                    return false;
                }
            }
    }
    else {
        alert("Invalid date format!");
        //document.rosterSearchForm.q.focus();
        return false;
    }
}

let options = {
      enableHighAccuracy: true,
      timeout: 10000,
      maximumAge: 300000
    }
    
function showLocationOnMap() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showCurrentLocationOnMap, handleErrors, options);
    } else {
        x.innerHTML("Gelocation is not supported by this browser.")
    }
}

function handleErrors(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
          alert("You must share your position if you wish to clock remotely.");
          break;
        case error.POSITION_UNAVAILABLE:
          alert("Unable to determine your current position.");
          break;
        case error.TIMEOUT:
          alert("The request for geolocation information timed out.");
          break;
        case error.UNKNOWN_ERROR:
          alert("An unknown error occurred. Unable to find your location at this time.");
          break;
    }
}

function showCurrentLocationOnMap(position) {
    //var crd = position.coords;
    //console.log("Here 1");
    var current_lat = position.coords.latitude;
    //console.log(current_lat)
    var current_lon = position.coords.longitude;
    var coords = current_lat + ', ' + current_lon;
    document.getElementById(id='google_map').setAttribute('src', 'https://maps.google.co.uk?q=' + coords + '&zoom=20&output=embed');
    alert("Your position is now on the map.")
}

function getLocationToClock() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(clockRemotely);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function clockRemotely(position) {
    var csrf = $("input[name=csrfmiddlewaretoken]").val()
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    $.ajax({
        url: "/clocking/get_user_coords/",
        type: "POST",
        dataType: "json",
        data : {
          'users_lat': latitude,
          'users_lon': longitude,
          csrfmiddlewaretoken: csrf
        },
        success : function(json) {
          //alert("Successfully sent the co-ordinates to Django");
          console.log("Success");
        },
        error : function(xhr,errmsg,err) {
          //alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText;
          console.log("Error " + xhr.status);
        }
     });
}