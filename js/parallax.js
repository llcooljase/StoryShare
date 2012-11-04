/*
Plugin: jQuery Parallax
Version 1.1
Author: Ian Lunn
Author URL: http://www.ianlunn.co.uk/
Plugin URL: http://www.ianlunn.co.uk/plugins/jquery-parallax/

Dual licensed under the MIT and GPL licenses:
http://www.opensource.org/licenses/mit-license.php
http://www.gnu.org/licenses/gpl.html
*/

//function that places the navigation in the center of the window

function hm(){

}

(function( $ ){
	$.fn.parallax = function() {
		
		$(window).bind('scroll', function(){ //when the user is scrolling...
			var scrollPos = $(window).scrollTop(); //position of the scrollbar
			$(this).css({'top': scrollPos});
//			inView(scrollPos, $(this));
		})
//if scrollPos is > 0 < windowHeight, 		
		//setup defaults if arguments aren't specified
	/*	var windowHeight = $(window).height();
		if(xpos == null){xpos = "50%"}
		if(adjuster == null){adjuster = 0}
		if(inertia == null){inertia = 0.1}
		if(outerHeight == null){outerHeight = true}
		
		height = $(this).height();
		$(this).css({'backgroundPosition': newPos(xpos, outerHeight, adjuster, inertia)}); 
		
		function newPos(xpos, windowHeight, scrollPos, adjuster, inertia){
			return xpos + " " + Math.round((-((windowHeight + scrollPos) - adjuster) * inertia)) + "px";
		}
		
		$window.bind('scroll', function(){ //when the user is scrolling...
			var scrollPos = $window.scrollTop(); //position of the scrollbar
			inView(scrollPos, $(this));
		})
	}
	
	function inView(scrollPos, element){
	
	element.each(function(){ //for each selector, determine whether it's inview and run the move() function
		var element = $(this);
		var top = element.offset().top;
		if(outerHeight == true){
			var height = element.outerHeight(true);
		}else{
			var height = element.height();
		}
		//above & in view
		if(top + height >= scrollPos && top + height - windowHeight < scrollPos){
			move(scrollPos, height);
		}		
		//full view
		if(top <= scrollPos && (top + height) >= scrollPos && (top - windowHeight) < scrollPos && top + height - windowHeight > scrollPos){
			move(scrollPos, height);
		}
		//below & in view
		if(top + height > scrollPos && top - windowHeight < scrollPos && top > scrollPos){
			move(scrollPos, height);
		}
	});
	
		//function to be called whenever the window is scrolled or resized
		function move(scrollPos, height){ 
				$(this).css({'backgroundPosition': scrollPos/*newPos(scrollPos, adjuster, inertia)}); 
		}
}		
*/}})( jQuery );