$(document).ready(function(){
  $("#navigation").removeClass("down");
})
$('.fullheight').css('height',$(window).height())
$(window).resize(function() {
  $('.fullheight').css('height',$(window).height())
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
        anchorOffset = match.offset().top - this.getFixedOffset();
        anchorOffset=anchorOffset>0?"-="+String(anchorOffset):String(anchorOffset).replace('-','+=')
        console.log(anchorOffset);
        $('#main').mCustomScrollbar('scrollTo',anchorOffset)

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
