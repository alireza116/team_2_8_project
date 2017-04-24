/**
 * Created by fablab on 4/23/2017.
 */
$("#login-button").on("click",function(e){
    e.preventDefault();

    $("#login-modal").modal("toggle");
});