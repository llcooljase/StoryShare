// JavaScript Document

$(document).ready(function()
{$(".star").click(function()
{
var ID=$(this).attr('id');
var $a = $(this).children();
var b=$a.hasClass('disp');

if (b) {
$a.removeClass('disp');
$a.addClass('nodisp');
/*$.ajax({
type: "POST",
url: "table_edit_ajax.php",
data: dataString,
cache: false,
success: function(html)
});*/
}

else {
$a.removeClass('nodisp');
$a.addClass('disp');
/*$.ajax({
type: "POST",
url: "table_edit_ajax.php",
data: dataString,
cache: false,
success: function(html)
});*/
}	
});
});