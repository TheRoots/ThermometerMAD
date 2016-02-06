$(document).ready(function () {
    //sidebar hide/show
    $('#menu').click(function () {
        var hidden = $('#slider');
        if (hidden.hasClass('visible')) {
            hidden.animate({"right": "-350px"}, "medium").removeClass('visible');

        } else {
            hidden.animate({"right": "0px"}, "medium").addClass('visible');
        }
    });
    
    // Hide Header on on scroll down
    var didScroll;
    var lastScrollTop = 0;
    var delta = 5;
    var navbarHeight = $('.header').outerHeight();

    $(window).scroll(function (event) {
        didScroll = true;
    });
    
    function hasScrolled() {
        var st = $(this).scrollTop();

        // Make sure they scroll more than delta
        if (Math.abs(lastScrollTop - st) <= delta) {
            return;
        }
        // If they scrolled down and are past the navbar, add class .nav-up.
        // This is necessary so you never see what is "behind" the navbar.
        if (st > lastScrollTop && st > navbarHeight) {
            var isopen = $('#slider').hasClass('visible');
            if (! isopen) {
                // Scroll Down
            $('.header').removeClass('header-down').addClass('header-up');
            }
        } else {
            // Scroll Up
            if (st + $(window).height() < $(document).height()) {
                $('.header').removeClass('header-up').addClass('header-down');
            }
        }

        lastScrollTop = st;
    }

    setInterval(function () {
        if (didScroll) {
            hasScrolled();
            didScroll = false;
        }
    }, 250);

    
});