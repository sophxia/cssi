function setup() {

   $(".button").css('opacity', '1');
      setTimeout(bringInMenu, 0);
      setTimeout(bringInYam, 0);
}


function bringInMenu() {
   $(".logo").css('opacity', '1');
   $("ul").css('opacity', '1');
   $("li a").css('opacity', '1');
   $(".menu").css('opacity', '1');
}

function bringInYam() {
   $("#yamLove").css('opacity', '1');
}
















$(document).ready(setup);
