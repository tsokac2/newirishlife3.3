var validateName = function(inputValue) {
    var valid;
    var inputName = inputValue;
    
    if(inputName === ""){
        valid = false;
    } else if (inputName.length < 2){
        valid = false;
    } else {
        valid = true;
    }

    return valid;
};

var validateEmail = function(inputValue) {
    var valid;
    var testEmail;
    var inputEmail = inputValue;
    if(inputEmail === "") {
        valid = false;
    } else if (!testEmail(inputEmail)){
        valid = false;
    } else {
        valid = true;
    }

    return valid;
};

var send = function(e) {
    e.preventDefault();
    e.stopPropagation();

    var checkName = validateName();
    var checkEmail = validateEmail();

    if(checkName === true && checkEmail === true) {
        sendEmail();
        reset();
        TnxForSupport("WOOHOO! Thank you for your support! You will receive a confirmation email soon. ");

    } else {
        validateName();
        validateEmail();
    }
};

var reset = function (){
    document.getElementById("newsForm").reset();
};

function TnxForSupport(tnxMessage) {
    var tnx = document.getElementById("tnx");
    tnx.style.visibility = "visible";
    tnx.innerText = tnxMessage;
}

function sendEmail() {
    var tempInputs = {
        "from_name": document.getElementById("newsName").value,
        "from_email": document.getElementById("newsEmail").value
    };

    emailjs.send("service_yf3pn0p", "newIrishLife", tempInputs)
        .then(function (response) {
                console.log("SUCCESS", response);
            },
            function (error) {
                console.log("FAILED", error);
            });
            return false;
   }


