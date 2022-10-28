function goContrastScreen() {
	if ($('body').hasClass('contrast')) {
		$('body').removeClass('contrast');
	} else {
		$('body').addClass('contrast');
	}
	$(document).scrollTop(0);
}

/* Zoom */
var currentZoom = 100;
function setZoom() {
	$('body').css('zoom', ' ' + currentZoom + '%');
	// Firefox
	$('body').css('-moz-transform', 'scale(' + currentZoom/100 + ')');
	$('body').css('-moz-transform-origin', 'left top');
	adjustContentTop();
}
function increaseZoom() {
	currentZoom = currentZoom + 1;
	setZoom();
}
function decreaseZoom() {
	currentZoom = currentZoom - 1;
	setZoom();
}
function clearZoom() {
	currentZoom = 100;
	setZoom();
}

/* Full screen */
function isFullScreenCurrently() {
	var full_screen_element = document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement || null;
	
	// If no element is in full-screen
	if(full_screen_element === null)
		return false;
	else
		return true;
}

/* Full screen */
function goFullScreen() {
	if(isFullScreenCurrently()) {
		if(document.exitFullscreen)
			document.exitFullscreen();
		else if(document.mozCancelFullScreen)
			document.mozCancelFullScreen();
		else if(document.webkitExitFullscreen)
			document.webkitExitFullscreen();
		else if(document.msExitFullscreen)
			document.msExitFullscreen();
	} else {
		if(document.documentElement.requestFullscreen)
			document.documentElement.requestFullscreen();
		else if(document.documentElement.mozRequestFullScreen)
			document.documentElement.mozRequestFullScreen();
		else if(document.documentElement.webkitRequestFullscreen)
			document.documentElement.webkitRequestFullscreen();
		else if(document.documentElement.msRequestFullscreen)
			document.documentElement.msRequestFullscreen();
	}
}

// *****************************Modal **************************************

const openModal = document.querySelector('#btn_accesibilidad');
const modal = document.querySelector('.modal_accesibilidad');
const closeModal = document.querySelector('.modalAcc_close')

openModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.add('modalAcc--show');
});

closeModal.addEventListener('click', (e)=>{
   e.preventDefault();
   modal.classList.remove('modalAcc--show');
});