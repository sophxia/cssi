function setup() {

   $(".formSpace").css('opacity', '1');
      setTimeout(bringInText, 800);
      setTimeout(bringInYam, 1500);
}

function bringInText() {
   $("form").css('opacity', '1');
}

function bringInYam() {
   $("#yamLove").css('opacity', '1');
}








$(document).ready(setup);
