$(document).ready(function(){
    /**
    *   PAGE | Twitter 
    *
    *   Pull latest tweets from user.
    *   Configuration: /plugins/twitter/index.php
    */
    $('.twitterfeed').tweet({
        modpath: '../../plugins/twitter/',
        username: 'MITBitcoinClub',
        count: 5
    });
    
    /* Make embeded videos responsive. */
    $.fn.responsivevideos();
});
