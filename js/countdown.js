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
	    map.setCenter(new GLatLng(37, -122), 13);
	    map.setUIToDefault();
	}
    }
});
