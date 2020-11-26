function validateDate(inputText) {
    if( inputText.value == "" ) {
            alert( "No date entered !!" );
            document.rosterSearchForm.q.focus() ;
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
        document.rosterSearchForm.q.focus();
        return false;
    }
}