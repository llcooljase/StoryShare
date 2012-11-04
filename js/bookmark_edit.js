function bookmark_edit() {
	var item = $(this).parent();
	var url = item.find(".title").attr("href");
	item.load(
		"/save/?ajax&url=" + encodeURIComponent(url),
		null,
		function() {
			$("#save-form").submit(bookmark_save);
		}
	);
	return false;
}

$(document).ready(function() {
	$("ul.bookmarks .edit").click(bookmark_edit);
});

function bookmark_save() {
	var current = $(this);
	var item = $(this).parent();
	var info = {
		url: item.find("#id_url").val(),
		title: item.find("#id_title").val(),
		tags: item.find("#id_tags").val()
	};
	$.post("/save/?ajax", info, function(result) {
		if (result != "failure") {
			$current.hide();
			// PUT IN SCRIPT TO MAKE THIS WORK BETTERER
			$("ul.bookmarks .edit").click(bookmark_edit);
		}
		else {
			alert("Failed to validate bookmark before saving.");
		}
	});
	return false;
}