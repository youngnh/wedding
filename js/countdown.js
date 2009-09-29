function countdown() {
    var today = new Date().getTime();
    var bigDay = new Date($('big_day').textContent).getTime();

    var daysToGo = Math.ceil(((((bigDay - today) / 1000) / 60) / 60) / 24);

    $('days_to_go').update(daysToGo + " days to go!");
}

document.observe("dom:loaded", function() {
    countdown();
});
