/**
 *  hashloader.js v0.1
 *  Load Ajax pages and elements using anchor/hash params.
 *  
 *   Params:
 *       Exmple: <a href="#pages/portfolio/readmore.html" data-destination="plugin-filter-elements" data-insert="appendTo" data-action="remove">
 *
 *       href should start with # and provide relative path to html file to be loaded
 *
 *       data-destination
 *           class for destination element. Where loaded file will be appended.
 *            
 *       data-insert
 *            Options: 
 *                    before
 *                    after
 *                    prependTo
 *                    appendTo
 *                    html
 *                    dafault: append
 *                        
 *       data-action / Not requred
 *            Options:
 *                    remove
 *                    hide
 *
 *  by Rewea: http://www.rewea.com
 *
 *  Copyright 2013 Rewea.com - Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0).
 *  http://creativecommons.org/licenses/by-sa/3.0/deed.en_US
 */
 
(function($){
    /* Dafault variables */
    hashDestination     = "";
    newHash             = "";
    
    /*
    *   If links with param data-destination is clicked (ajax call)
    *   We will trigger hashchange event.
    */
    $("data-destination").delegate("a", "click", function() {
        $(window).trigger('hashchange');
        return false;
    });
    
    
    $(window).bind('hashchange', function(){
        newHash = window.location.hash.substring(1);
        
        if (newHash) {
            hashDestination = $("a[href='#" + newHash +"']");
            
        
            /*
            *   Insert data
            *   Based on params data-insert
            */
            
            /* Check if new hash link esists on a page */
            if(hashDestination.data("destination")){
                $.get(newHash, function(data){
                    /*!
                    *   CUSTOM CONFIGURATION
                    */
                        /*  
                        *   Portfolio details
                        *   Slide down content and scroll to.
                        */
                        if($(".portfolio-item-details").length != 0 && hashDestination.data("destination") == 'portfolio-items') {
                            $(".portfolio-item-details").slideUp(500, function(){
                                $(this).remove();
                            });
                        }
                
                    /*  
                    *   Insert data
                    *   Using params "data-insert"
                    */
                    if(hashDestination.data("insert") == "before") {
                        $(data).insertBefore("." + hashDestination.data("destination"));
                    } else if(hashDestination.data("insert") == "after") {
                        $(data).insertAfter("." + hashDestination.data("destination"));
                    } else if(hashDestination.data("insert") == "prependTo") {
                        $(data).prependTo("." + hashDestination.data("destination"));
                    } else if(hashDestination.data("insert") == "appendTo") {
                        $(data).appendTo("." + hashDestination.data("destination"));
                    } else if(hashDestination.data("insert") == "html") {
                        $("." + hashDestination.data("destination")).html(data);
                    } else {
                        $(data).append("." + hashDestination.data("destination"));
                    }
                }).complete(function () {
                    /*!
                    *   CUSTOM CONFIGURATION
                    */
                        /*
                        *    Portfolio read more
                        *
                        *   If hasDestination block is used by some other plugin
                        *   Reload all elements after ajax load
                        */
                        if(hashDestination.data("destination") == 'plugin-filter-elements'){
                            setTimeout(function() {
                                $('.plugin-filter-elements').mixitup('remix','all');
                            }, 1000);
                        }
                        
                        /*  
                        *   Portfolio details
                        *   Slide down content and scroll to.
                        */
                        if(hashDestination.data("destination") == 'portfolio-items'){
                            $(".portfolio-item-details").slideDown();

                            $('html, body').animate({
                                scrollTop: $(".portfolio-item-details").offset().top - 70
                            }, 1000);
                        }
                    
                        /*  
                        *   Blog details
                        *   Slide down content and scroll to.
                        */
                        if(hashDestination.data("destination") == 'blog-details'){
                            $("article").slideDown();

                            $('html, body').animate({
                                scrollTop: $(".blog-details").offset().top - 70
                            }, 1000);
                        }
                    /*
                    *   Action on href element
                    */
                    if(hashDestination.data("action") == "remove") {
                        $(hashDestination).delay(500).slideUp(400, function(){
                            $(this).remove();
                        });
                    } else if(hashDestination.data("action") == "hide") {
                        $(hashDestination).delay(500).slideUp(400, function(){
                            $(this).remove();
                        });
                    }
                    
                });
            }
        };
    });
    
    
    /* Trigger hash change in canse that user is looking for ajax loaded page on load. */
    $(window).trigger('hashchange');
    
})(jQuery);