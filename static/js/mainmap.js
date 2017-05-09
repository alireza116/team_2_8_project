/**
 * Created by fablab on 4/9/2017.
 */
var map = L.map('mapid').setView([35.2271, -80.8431], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
    '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
    'Imagery © <a href="http://mapbox.com">Mapbox</a>',
    id: 'mapbox.streets'
}).addTo(map);

map._initPathRoot();

var svg = d3.select("#mapid").select("svg"),
    g= svg.append("g");

// var tip = d3.tip().attr("class", "d3-tip")
//     .offset([-10,0])
//     .html(function(d){
//         return "<strong>Shelter Name:</strong> <span style='color:red'>" + d.properties.providerName + "</span> <br>" +
//             "<strong>Shelter count:</strong> <span style='color:red'>" + d.properties.count + "</span> <br>";
//     });

// svg.call(tip);

var circles;

var selectedID;

var selectedName;

$.get("http://127.0.0.1:5000/place/counts", function(data){

    var collection = data;

    var shelterLatLong = {};

    var countBouds = d3.extent(collection, function(d){
        return d.count
    });

    var radiusScale = d3.scale.linear().range([10,25]).domain(countBouds);

    collection.forEach(function(d){
        console.log(d)
        d.latLng = new L.LatLng(d.Y,d.X)
    });

    console.log(collection);

    circles = g.selectAll("circle")
        .data(collection)
        .enter().append("circle")
        .style("stroke", "red")
        .style("opacity", 0.8)
        .style("fill", "red")
        .attr("r", function(d){
            return radiusScale(d.count)
        }).attr("class",function(d){
            return "place"+d.placeID;
        }).attr("title",function(d){
            return d.count;
        }).on("mouseover",function(d){
            d3.select(this).style("fill","darkorange");
            var id = d.placeID;
            console.log(id);
            d3.select(".table-responsive").select(".place"+id).selectAll("td").style("color","darkorange");
        }).on("mouseout", function(d){
            d3.select(this).style("fill", "red");
            var id = d.placeID;
            d3.select(".table-responsive").select(".place"+id).selectAll("td").style("color","black");
        });

    circles.on("click", function(d){
        var placeid = d.placeID;
        modal = 1;
        $.get("http://127.0.0.1:5000/bed?placeid="+placeid,function(newData){
            createTable.newTable(newData)
        })

    });

    $("#seeAll").click(function(){
        modal = 0;
        createTable.newTable(data)
    });
    // circles
    //     .on('mouseover', tip.show)
    //     .on('mouseout', tip.hide);

    map.on("viewreset", reset);
    reset();

    function reset(){
        circles.attr("transform",function(d){
            return "translate("+
                map.latLngToLayerPoint(d.latLng).x +","+
                map.latLngToLayerPoint(d.latLng).y +")";
        })
    }
});

// $.get("http://127.0.0.1:5000/place/counts", function(data) {
//     console.log(data);
//     var countBouds = d3.extent(data, function(d){
//         return d.count
//     });
//
//     var radiusScale = d3.scale.linear().range([50,200]).domain(countBouds);
//     data.forEach(function(d) {
//         d.X = +d.X;
//         d.Y = +d.Y;
//         console.log(d);
//         var radius = radiusScale(d.count);
//         L.circle([d.Y,d.X], radius, {
//             color: 'red',
//             fillColor: '#f03',
//             fillOpacity: 0.5
//         }).addTo(map);
//
//     });
//
//
// });
