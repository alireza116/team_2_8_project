/**
 * Created by fablab on 4/9/2017.
 */

var createTable = function(){

    $.get("http://127.0.0.1:5000/place", function(data) {
        // create the table header
        d3.select("tr").remove();
        d3.select("th").remove();
        var thead = d3.select("thead").selectAll("th")
            .data(d3.keys(data[0]))
            .enter().append("th").text(function(d){return d});
        // fill the table
        // create rows
        var tr = d3.select("tbody").selectAll("tr")
            .data(data).enter().append("tr").attr("class", function(d){
                return d.placeID});

        tr.on("click",function(d){
            var placeid = d.placeID;
            $.get("http://127.0.0.1:5000/bed?placeid="+placeid,function(newData){
                createTable.newTable(newData)
            })
        });
        // cells
        var td = tr.selectAll("td")
            .data(function(i){return d3.values(i)})
            .enter().append("td")
            .text(function(i) {return i})
    });


    this.newTable = function(data){
        d3.selectAll("tr").remove();
        d3.selectAll("th").remove();
        var thead = d3.select("thead").selectAll("th")
            .data(d3.keys(data[0]))
            .enter().append("th").text(function(d){return d});
        // fill the table
        // create rows
        var tr = d3.select("tbody").selectAll("tr")
            .data(data).enter().append("tr").attr("class", function(d){
                console.log(d);
                return d.placeID});
        // cells
        var td = tr.selectAll("td")
            .data(function(i){return d3.values(i)})
            .enter().append("td")
            .text(function(i) {return i})

        tr.on("click",function(d){
            console.log("kir");
            $('#login-modal').modal('toggle');
        })
    }

};