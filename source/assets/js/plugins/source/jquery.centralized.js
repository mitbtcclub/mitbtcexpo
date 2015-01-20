/**
 *  centralized.js v0.2
 *  Centralize elements by width and height.
 *  Usage in combination with CSS class .centralized
 *
     $('.centralized').centralized({
        delay: 1500,
        fadeSpeed: 500
    });
    
 *  by Rewea: http://www.rewea.com
 *
 *  Copyright 2013 Rewea.com - Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0).
 *  http://creativecommons.org/licenses/by-sa/3.0/deed.en_US
 */
(function($){
    var $window = $(window);
    
    $.fn.centralized = function(options) {
        
        var defaults = {
            delay: 500,
            fadeSpeed : 300
        };
    
        var options =  $.extend(defaults, options);
        
        var obj = $(this);
        var o = options;
        
        function update(){
            obj.each(function(){
                var $this = $(this);
                
                setTimeout(function() {
                    $this.css("margin-top", "-" + Math.max(0, ($this.outerHeight() / 2)) + "px");
                    $this.css("margin-left", "-" + Math.max(0, ($this.outerWidth() / 2)) + "px");
                    $this.css('visibility','visible');
                    $this.fadeTo(o.fadeSpeed, 1);
                }, o.delay);
            });
        };
        
        
        $window.bind('resize', update);
        update();
    }
})(jQuery);