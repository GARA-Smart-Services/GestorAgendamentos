function get_credentials(){  
    var front_user = document.getElementById("login__username").value  
    var front_password = document.getElementById("login__password").value
    eel.request_login_mongodb(front_user, front_password)
}