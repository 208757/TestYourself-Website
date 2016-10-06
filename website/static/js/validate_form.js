function validateForm()
{
    var username = document.getElementById("id_username").value;
    var email = document.getElementById("id_email").value;
    var password = document.getElementById("id_password").value;
    var password2 = document.getElementById("id_password2").value;

    if(username != validateForm.previous_username || email != validateForm.previous_email || 
       password != validateForm.previous_password || password2 != validateForm.previous_password)
    {
        validateForm.previous_username = username;
        validateForm.previous_email = email;
        validateForm.previous_password = password;
        validateForm.previous_password2 = password2;

        if(username == "")
            username = "."

        var regex = new RegExp("[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)+$")
        if(email == "" || !regex.test(email))
            email = "."    
        query = "validate@username=" + username
        query += "@email=" + email
        $.getJSON(query, function(result){
            if(result["username"] && result["email"])
                document.getElementById("id_register").disabled=false;
            else
                document.getElementById("id_register").disabled=true;

            document.getElementById("errorUserAndEmail").innerHTML = "";
            if(!result["username"] && username != ".")
                document.getElementById("errorUserAndEmail").innerHTML += "Podana nazwa użytkownika nie jest dostępna<br>";
            if(!result["email"] && email != ".")
                document.getElementById("errorUserAndEmail").innerHTML += "Podany adres e-mail znajduje się w bazie danych<br>";
            checkPassword();
        })
    }
}

function checkPassword()
{
    var password = document.getElementById("id_password").value;
    var password2 = document.getElementById("id_password2").value;

    document.getElementById("errorPassword").innerHTML="";
    if(password != password2 && password2 != "")
    {
        document.getElementById("errorPassword").innerHTML = "Podane hasła różnią się";
        document.getElementById("id_register").disabled=true;
    }
    else if(password == "" || password2 == "")
        document.getElementById("id_register").disabled=true;
}
