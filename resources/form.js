function setup() {

   $(".formSpace").css('opacity', '1');
      setTimeout(bringInText, 0);
}

function bringInText() {
   $("form").css('opacity', '1');
}

$(document).ready(setup);
