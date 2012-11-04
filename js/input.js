// JavaScript Document

$(document).ready(function()
{
$(".edit_td").click(function()
{
var ID=$(this).attr('id');
$("#q1_"+ID).hide();
$("#q2_"+ID).hide();
$("#q3_"+ID).hide();
$("#q4_"+ID).hide();
$("#notes_"+ID).hide();
$("#q1_input_"+ID).show();
$("#q2_input_"+ID).show();
$("#q3_input_"+ID).show();
$("#q4_input_"+ID).show();
$("#notes_input_"+ID).show();
}).change(function()
{
var ID=$(this).attr('id');
var q1=$("#q1_input_"+ID).val();
var q2=$("#q2_input_"+ID).val();
var q3=$("#q3_input_"+ID).val();
var q4=$("#q4_input_"+ID).val();
var notes=$("#notes_input_"+ID).val();
var dataString = 'id='+ ID +'&q1='+q1+'&q2='+q2+'&q3='+q3+'&q4='+q4+'&notes='+notes;

if(q2.length>0&& q1.length>0 && q3.length>0 && q4>0)
{

/*$.ajax({
type: "POST",
url: "table_edit_ajax.php",
data: dataString,
cache: false,
success: function(html)
{*/
$("#q1_"+ID).html(q1);
$("#q2_"+ID).html(q2);
$("#q3_"+ID).html(q3);
$("#q4_"+ID).html(q4);
$("#notes_"+ID).html(notes);
/*}
});*/
}
else
{
alert('Please enter a value!');
}
});

// Edit input box click action
$(".editbox").mouseup(function() 
{
return false
});

// Outside click action
$(document).mouseup(function()
{
$(".editbox").hide();
$(".textinput").show();
});

});
