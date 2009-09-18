function countdown() {
    var today = new Date().getTime();
    var bigDay = new Date($('_ctl1__ctl0_lblWeddingDate').textContent).getTime();

    var daysToGo = Math.ceil(((((bigDay - today) / 1000) / 60) / 60) / 24);

    $('_ctl1__ctl0_lblCountdown').update(daysToGo + " days to go!");
}

document.observe("dom:loaded", function() {
    countdown();
});
