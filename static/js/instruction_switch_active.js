$(".instruction-list li").on("click", function(){
   $(".instruction-list").find(".active").removeClass("active");
   $(this).addClass("active");
});