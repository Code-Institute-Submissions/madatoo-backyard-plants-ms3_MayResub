$(document).ready(function() {
	//sidenavbar inititialization
	$('.sidenav').sidenav({
		edge: "right"
	});
	//carousel
	$('#carousel-auto').carousel({
		fullWidth: true
	});
	setInterval(function() {
		$('#carousel-auto').carousel('next');
	}, 1800);
	//add plant form
	$('select').formSelect();
	$('.dropdown-trigger').dropdown({
		hover: true
	});
	$('input#plant_name, textarea#plant_description,textarea#plant_tips, texarea#plant_more_info, texarea#plant_notes').characterCounter();
	$('#plant_description').val('');
	M.textareaAutoResize($('#plant_description'));
    //https://web.dev/uses-passive-event-listeners/?utm_source=lighthouse&utm_medium=devtools to improve scrolling performance
    //document.addEventListener('touchstart', onTouchStart, {passive: true});
	// code taken from CI course material about Adding A Task - Writing to the Database Materialize Form Validation  (Tim Nelson)
	validateMaterializeSelect();

	function validateMaterializeSelect() {
		let classValid = {
			"border-bottom": "1px solid #4caf50",
			"box-shadow": "0 1px 0 0 #4caf50"
		};
		let classInvalid = {
			"border-bottom": "1px solid #f44336",
			"box-shadow": "0 1px 0 0 #f44336"
		};
		if ($("select.validate").prop("required")) {
			$("select.validate").css({
				"display": "block",
				"height": "0",
				"padding": "0",
				"width": "0",
				"position": "absolute"
			});
		}
		$(".select-wrapper input.select-dropdown").on("focusin", function() {
			$(this).parent(".select-wrapper").on("change", function() {
				if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function() {})) {
					$(this).children("input").css(classValid);
				}
			});
		}).on("click", function() {
			if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
				$(this).parent(".select-wrapper").children("input").css(classValid);
			} else {
				$(".select-wrapper input.select-dropdown").on("focusout", function() {
					if ($(this).parent(".select-wrapper").children("select").prop("required")) {
						if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
							$(this).parent(".select-wrapper").children("input").css(classInvalid);
						}
					}
				});
			}
		});
	}


});
