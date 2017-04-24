/**
 * Created by fablab on 4/23/2017.
 */

var reserveBed = function() {

$("#reserve-bed").on("click",function(e){
    e.preventDefault();

    var guestID = $("#guest-id").val();
    var bed_id = createTable.bed_id;
    var guestData = {
        guest_id: guestID,
        bed_id : bed_id
    };
    console.log(JSON.stringify(guestData));
    if (bed_id != null && guestID != ""){
        console.log(bed_id);

    //     $.post("http://127.0.0.1:5000/bed/reserve",data).done(
    //         console.log("Success")
    // )

        $.ajax({
            url: 'http://127.0.0.1:5000/bed/reserve',
            dataType: 'json',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify(guestData),
            success: function(d){
                alert("success!")
            }
            ,
            error: function( jqXhr, textStatus, errorThrown ){
                console.log( errorThrown );
            }
        });
    } else {
        alert('please enter guest id!')
    }
});

    $("#checkout-bed").on("click",function(e){
        e.preventDefault();

        // var guestID = $("#guest-id").val();
        var checkoutSure = $("#checkout-sure").val();
        console.log(checkoutSure);
        var bed_id = createTable.bed_id;
        var guestData = {
            bed_id : bed_id
        };
        console.log(JSON.stringify(guestData));
        if (bed_id != null && document.getElementById('checkout-sure').checked){
            console.log(bed_id);

            //     $.post("http://127.0.0.1:5000/bed/reserve",data).done(
            //         console.log("Success")
            // )

            $.ajax({
                url: 'http://127.0.0.1:5000/bed/checkout',
                dataType: 'json',
                type: 'post',
                contentType: 'application/json',
                data: JSON.stringify(guestData),
                success: function(d){
                    alert("success!")
                }
                ,
                error: function( jqXhr, textStatus, errorThrown ){
                    console.log( errorThrown );
                }
            });
        } else {
            alert('please click on checkbox if you want to check out!')
        }
    })

};