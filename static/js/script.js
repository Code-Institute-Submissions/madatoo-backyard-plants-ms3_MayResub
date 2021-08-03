$(document).ready(function(){
    //sidenavbar inititialization
    $('.sidenav').sidenav({edge:"right"});
    //carousel
    $('#carousel-auto').carousel({fullWidth: true});
      setInterval(function() {
      $('#carousel-auto').carousel('next');
    }, 1800);

});
