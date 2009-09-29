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
    countdown();
    $$('#navigation a').each(function(a) { 
	a.observe("mouseover", menuRollover);
	a.observe("mouseout", menuRollout);
    });
});
