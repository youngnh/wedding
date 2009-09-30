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

var getDirections;

document.observe("dom:loaded", function() {
    // set the text for days until the wedding
    countdown();

    // setup the menu rollover/rollout underlining
    $$('#navigation a').each(function(a) { 
	a.observe("mouseover", menuRollover);
	a.observe("mouseout", menuRollout);
    });

    // populate the google maps
    if($('map_canvas')) {
	if(GBrowserIsCompatible()) {
	    var map = new GMap2($('map_canvas'));
	    var holyTrinityLatLng = new GLatLng(38.6040590, -89.9752430);
	    map.setCenter(holyTrinityLatLng, 13);
	    map.setUIToDefault();
	    var marker = new GMarker(holyTrinityLatLng);
	    map.addOverlay(marker);
	    GEvent.addListener(marker, "click", function() {
		var infoNode = $('directions_info_window');
		infoNode.remove();
		infoNode.show();
		marker.openInfoWindowHtml(infoNode);
	    });

	    getDirections = function() {
		var directions = new GDirections(map);
		directions.load("2035 Washington Ave, St. Louis, MO 63103 to 505 Fountains Pkwy, Fairview Heights, IL 62208");
	    };
	}
    }
});
