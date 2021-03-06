function menuRollover(event) {
    var img = this.firstDescendant();
    img.src = img.src.replace(".png", "_u.png");
}

function menuRollout(event) {
    var img = this.firstDescendant();
    img.src = img.src.replace("_u.png", ".png");
}

function countdown() {
    var today = new Date().getTime();
    var bigDay = new Date($('#big_day').text()).getTime();

    var daysToGo = Math.ceil(((((bigDay - today) / 1000) / 60) / 60) / 24);

    if(daysToGo < 0) {
      $('#days_to_go').replaceWith(daysToGo + " days to go!");
    } else if(daysToGo == 0) {
      $('#days_to_go').replaceWith("It's the big day!");
    } else {
      $('#days_to_go').replaceWith("Happily married for " + (daysToGo * -1) + " days!");
    }
}

function wireUpMenu() {
    $$('#navigation a').each(function(a) { 
	a.observe("mouseover", menuRollover);
	a.observe("mouseout", menuRollout);
    });
}

function populateMap(lat, lng, zoom, dest) {
    $('#directions_button').click(function(event) {
	var from = $(event.target).prev().val();
	$('#map_canvas, #directions_show').directions(from, dest);
    });						      
    
    var holyTrinityLatLng = new GLatLng(lat, lng);    
    $('#map_canvas').gmap2({center: holyTrinityLatLng,
			    zoom: zoom});
    $('#map_canvas').addMarker(new GMarker(holyTrinityLatLng), 
			       { click: function() {
				   var deep = true;
				   $('#directions_info_window').clone(deep).show().openAsInfoWindow(this);
			       }});
}
