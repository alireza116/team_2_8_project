/**
 * Created by fablab on 4/23/2017.
 */
$("#login-button").on("click",function(e){
    e.preventDefault();

    $("#login-modal").modal("toggle");
});


$("#login").on("click",function(e){
    e.preventDefault();
    var username  = $("#user-name").val();
    var password = $("#password").val();
    var logindata = {"username":username, "password":password};
    $.ajax({
        datatype: "json",
        url: "http://127.0.0.1:5000/login",
        data: logindata,
        success: function(data){
            console.log(data);
            if (data =="logged in"){
                $("#adminText").text("Admin Logged in");
                $("#login-modal").modal("toggle");
                d3.select("#login-button").style("pointer-events","none");
            }
            else {
                alert(data)
            }
        }

    })
});
