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
    var bigDay = new Date($('big_day').textContent).getTime();

    var daysToGo = Math.ceil(((((bigDay - today) / 1000) / 60) / 60) / 24);

    $('days_to_go').update(daysToGo + " days to go!");
}

function wireUpMenu() {
    $$('#navigation a').each(function(a) { 
	a.observe("mouseover", menuRollover);
	a.observe("mouseout", menuRollout);
    });
}

function getDirectionsInfoWindow(map) {
    var deep = true;
    var infoNode = $('directions_info_window').cloneNode(deep);
    infoNode.id = "";
    infoNode.show();

    var inputs = infoNode.select('input');
    var textField = inputs[0];
    var button = inputs[1];
    button.observe('click', function(event) {
	var directions = new GDirections(map);
	directions.load(textField.value + " to 505 Fountains Pkwy, Fairview Heights, IL 62208");
    });

    return infoNode;
}

function populateMap() {
    if($('map_canvas')) {
	if(GBrowserIsCompatible()) {
	    var map = new GMap2($('map_canvas'));
	    var holyTrinityLatLng = new GLatLng(38.6040590, -89.9752430);
	    map.setCenter(holyTrinityLatLng, 13);
	    map.setUIToDefault();
	    var marker = new GMarker(holyTrinityLatLng);
	    map.addOverlay(marker);
	    GEvent.addListener(marker, "click", function() {
		var infoNode = getDirectionsInfoWindow(map);
		marker.openInfoWindowHtml(infoNode);
	    });
	}
    }
}

document.observe("dom:loaded", function(event) {
    // set the text for days until the wedding
    countdown();

    // setup the menu rollover/rollout underlining
    wireUpMenu();

    // populate the google maps
    populateMap();
});
