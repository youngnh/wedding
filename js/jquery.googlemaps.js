jQuery.fn.gmap2 = function(options) {
    return this.each(function() {
	var map = new GMap2(this);
	this.getMap = function() {
	    return map;
	};
	map.setCenter(options.center, options.zoom);
	map.setUIToDefault();
    });
};

jQuery.fn.addMarker = function(marker, options) {
    return this.each(function() {
	var map = this.getMap();
	map.addOverlay(marker);
	for(event in options) {
	    GEvent.addListener(marker, event, options[event]);
	}
    });
};

jQuery.fn.directions = function(from, to) {
    var map = getMap(this[0]);
    var show = this[1];
    var directions = new GDirections(map, show); // should probably do a call() or apply() here
    directions.load(from + " to " + to);
    return this;
};