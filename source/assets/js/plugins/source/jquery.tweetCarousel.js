/**
 *  tweetCarousel.js v0.1
 *  Genereate markup for Tweet list
 *  Markup is used with Twitter Bootstrap Carousel plugin.
 *
 *  by Rewea: http://www.rewea.com
 *
 *  Copyright 2013 Rewea.com - Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0).
 *  http://creativecommons.org/licenses/by-sa/3.0/deed.en_US
 */
(function($){
    $.fn.tweetCarousel = function(options) {
        
        var defaults = {
            interval: 7000,
            pause: "hover"
        };
    
        var options =  $.extend(defaults, options);
        
        var obj = $(this);
        var o = options;
        
        function update(){
            obj.each(function(){
                var $this = $(this);
                var $thisId = $this.attr("id");
                
                $this.find('.tweet_list').addClass("carousel-inner");
                $this.find('.tweet_list li').addClass('item').first().addClass("active");
                    
                $this.append("<ol class='carousel-indicators'></ol>");
                
                var indicators =  $this.find(".carousel-indicators"); 
                $this.find(".carousel-inner").children(".item").each(function(index) {
                    if(index === 0) {
                        indicators.append("<li data-target='#" + $thisId + "' data-slide-to='"+index+"' class='active'></li>");
                    } else {
                        indicators.append("<li data-target='#" + $thisId + "' data-slide-to='"+index+"'></li>");
                    }
                });
                
               $($thisId).carousel({
                    interval: o.interval,
                    pause: o.pause
                });
            });
        };

        update();
    }
})(jQuery);