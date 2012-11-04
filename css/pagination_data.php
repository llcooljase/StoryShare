<!-- FULU GETTER MACHINE v1.0 by Jason Adleberg! -->


<!-- Load JQuery -->
<script type="text/javascript" src="http://cdn.jquerytools.org/1.2.6/full/jquery.tools.min.js"></script>

<!-- Some Functions to make it look purty + ratings -->
<script type="text/javascript">
$(document).ready(function()
{
			$(".like").click(function()
			{var id=$(this).attr("id");			
			var name=$(this).attr("name");
			var dataString = 'id='+ id + '&name='+ name;
			
			$("#votebox"+id).slideDown("slow");
			$("#flash"+id).fadeIn("slow");
			$.ajax ({
			id:$(this).attr("id"),
			type: "POST",
			url: "rating.php",		
			data: dataString,
			cache: false,
			success: function(html)
			{
			$("#flash"+id).fadeOut("slow");
			$("#content"+id).html(html);			
			} 
			
			});
			});
});			
</script>

<!-- The fun part -->
<?php
error_reporting(0);

// Connect to Database
include('config.php');

// Define variables
$per_page = 8; // 8 fulus/page, subject to change.

// How to get the page
if($_GET)
{$page=$_GET['page'];}

// Let's figure out which fulus to get
$forcount = "select * from fulus";
$count = mysql_num_rows($forcount);
$pages = ceil($count/$per_page);

// (Trust me this does it)
$start = $count - (($pages- $page+1)*$per_page);

if ($start < 0) {
	$plus = $per_page + $start;
	$start = 0;
}

else {$plus = $per_page;}
$sql = "select * from fulus limit $start,$plus";
$query = mysql_query($sql);

// Get Youtube ID from URL
function getYouTubeIdFromURL($url)
{
  $url_string = parse_url($url, PHP_URL_QUERY);
  parse_str($url_string, $args);
  return isset($args['v']) ? $args['v'] : false;
}
?>



		
<?php

// get data
while($data= mysql_fetch_array($query))
{

// sniffs out if it's a link
$content=$data['content'];
	preg_match('/[a-zA-Z]+:\/\/[0-9a-zA-Z;.\/?:@=_#&%~,+$]+/', $content, $matches);

// Figure out if Fu or Lu and assign red or blue
if ($data['fu']) {
	$redorblue = "red";
}

else {
	$redorblue = "blue";
}

// Return only first name
$name = $data['name'];
$pos = strpos($data['name'], ' ');
if ($pos) {
$name = substr($data['name'], 0, $pos);
}

//spill out message
$message = $data['message'];

// if youtube video
	if($matches[0])
	{
		$youtube_id = getYouTubeIdFromURL($data['content']);
					
		$matter='http://youtube.com/embed/'.$youtube_id;
		$content='<div class="iframe"><iframe src="'.$matter.'" width="131" height="131" autoplay="false"></iframe></div>';
		$youtube = true;
	} 
	
// if not youtube video	
	else {
			$youtube = false;	
			$string="";
			$fileCount=0;
			$filePath='images/preview/'; 
			$dir = opendir($filePath); 
			while ($file = readdir($dir)) { 
			  if (eregi($content,$file)) { # Look at only files with a .php extension
				$string = "$file";
				$fileCount++;
			  }
			}

			if ($fileCount > 0) {
				$content='<div class="content"><img src="'.$filePath.$string.'" width="131" height="131"></div>';
			}
			
			else {
			$content='<div class="content"><img class="stock" src="images/fulu.png" width="131" height="131"></div>';
			}

}
?>


<div class="thumbs <?php echo $redorblue;?>" id="demo">
<?php echo $content;?>
<div class="message"><p class="message_text"><?php echo $message;?></p></div>

<div class="bottom_fulu">
<p class="fuluname">FuLu to <?php echo $name;?></p>
<p class="ld">
<a href="javascript: void(0);" class="like up" id="<?php echo $data['id']?>" name="up">Like   </a>
<a href="javascript: void(0);" class="like down" style="color:#A00;" id="<?php echo $data['id']?>" name="down">Dislike</a></p>

<div class="tofb"><a name="fb_share" share_url="www.fulumail.com/fulu.php?id=<?php echo $data['id']?>"></a> </div>
</div>

<!--None of this really shows up-->
<div id="votebox<?php echo $data['id'];?>" class="votebox">
	<span id='close<?php echo $data['id'];?>'><a href="#" class="close" title="Close This">X</a></span>
	<div style="height:13px">
	<div id="flash<?php echo $data['id'];?>" class="flash">Loading........</div>
	</div>
	<div id="content<?php echo $data['id'];?>">
</div>
</div>
</div>	

                    <?php
}	
						?>

		
	
<script>
jQuery.noConflict();
jQuery("#demo img[title]").tooltip();
jQuery("#demo iframe[title]").tooltip();

</script>

<script src="http://static.ak.fbcdn.net/connect.php/js/FB.Share" type="text/javascript">
</script>