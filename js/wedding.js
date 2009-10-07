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

    $('#days_to_go').replaceWith(daysToGo + " days to go!");
}

function wireUpMenu() {
    $$('#navigation a').each(function(a) { 
	a.observe("mouseover", menuRollover);
	a.observe("mouseout", menuRollout);
    });
}

function getDirectionsInfoWindow(map, dest) {
    var deep = true;
    var infoNode = $('directions_info_window').cloneNode(deep);
    infoNode.id = "";
    infoNode.show();

    var inputs = infoNode.select('input');
    var textField = inputs[0];
    var button = inputs[1];
    button.observe('click', function(event) {
	var directionsDiv = $('directions_text');
	var directions = new GDirections(map, directionsDiv);
	directions.load(textField.value + " to " + dest);
    });

    return infoNode;
}

function populateMap(lat, lng, zoom, dest) {
    var holyTrinityLatLng = new GLatLng(lat, lng);    
    $('#map_canvas').gmap2({center: holyTrinityLatLng,
			    zoom: zoom});
    var marker = new GMarker(holyTrinityLatLng);
    $('#map_canvas').addOverlay(marker);
    marker.click(function() {
	var infoNode = getDirectionsInfoWindow(map, dest);
	marker.openInfoWindowHtml(infoNode);
    });
}
