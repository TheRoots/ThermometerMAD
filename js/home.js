$(document).ready(function(){
    //fade in/out down icon
    var didScroll = false;
    var icon = $("#godown");
    var header = $("#header");
    var $window = $(window);

    $(window).scroll(function(){
      didScroll = true;
    });

    window.setInterval(function () {
    if (didScroll) {
      if (1-$window.scrollTop()/200 > -10) {
          icon.css({opacity: 1-$window.scrollTop()/200});
      }
      didScroll = false;
    }
    }, 50);
    
    
    //smooth scroll contact
    $("#btn_contact").click(function() {
        $('html,body').animate({
            scrollTop: $("#join").offset().top},
        'slow');
    });

    
    
});