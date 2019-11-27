$(document).ready(function(){
  $("#navigation").removeClass("down");
  $(window).on("scroll", function(event) {
    //refers to the distance of the scrollbar in pixels
    var fromTop = document.documentElement.scrollTop+$('#navigation').height()
    // var toSpeakers = $("#page-welcome").height()
    // $("#navigation.dropdown").toggleClass("down", (fromTop >= toSpeakers));
    console.log(fromTop);
    $("#navigation").toggleClass("down", (fromTop >= 75));
  });

  $('.pages').on('scrollSpy:enter', function() {
    console.log(' entering', this);
    $('a[href="#'+$(this).attr('id')+'"]').toggleClass("active", true)
  });

  $('.pages').on('scrollSpy:exit', function() {
    console.log(' leaving', $(this));
    $('a[href="#'+$(this).attr('id')+'"]').toggleClass("active", false)
  });

  $('.pages').scrollSpy();
})
$('.fullheight').css('height',$(window).height()+1)
$(window).resize(function() {
  $('.fullheight').css('height',$(window).height()+1)
});

//adjust anchors so they account for the static top bar
var betterAnchor = function(document, history, location) {
  var HISTORY_SUPPORT = !!(history && history.pushState);

  var anchorScrolls = {
    ANCHOR_REGEX: "#",
    ANCHOR_REGEX: /^#[^ ]+$/,

    /**
    * Establish events, and fix initial scroll position if a hash is provided.
    */
    init: function() {
      this.scrollIfAnchor(location.hash);
      $('body').on('click', 'a', $.proxy(this, 'delegateAnchors'));
    },

    /**
    * Return the offset amount to deduct from the normal scroll position.
    * Modify as appropriate to allow for dynamic calculations
    */
    getFixedOffset: function() {
      return $('#navigation').height()
    },

    /**
    * If the provided href is an anchor which resolves to an element on the
    * page, scroll to it.
    * @param  {String} href
    * @return {Boolean} - Was the href an anchor.
    */
    scrollIfAnchor: function(href, pushToHistory) {
      var match, anchorOffset;

      if(!this.ANCHOR_REGEX.test(href)) {
        return false;
      }

      match = $(href)
      if(match.length > 0) {
        console.log(this.getFixedOffset());
        var anchorOffset = match.offset().top - this.getFixedOffset()+2; //add one pixel to make sure it activates the nav highlighting for the right page
        window.scroll({
          top: anchorOffset,
          behavior: 'smooth'
        });


        // Add the state to history as-per normal anchor links
        try {
          if(HISTORY_SUPPORT && pushToHistory) {
            history.pushState({}, document.title, location.pathname + href);
          }
        } catch (e) {}
      }

      return !!match;
    },

    /**
    * If the click event's target was an anchor, fix the scroll position.
    */
    delegateAnchors: function(e) {
      var elem = e.target;
      if(this.scrollIfAnchor(elem.getAttribute('href'), true)) {
        e.preventDefault();
      }
    }
  };
  $(document).ready($.proxy(anchorScrolls, 'init'))
}
betterAnchor(window.document, window.history, window.location)
