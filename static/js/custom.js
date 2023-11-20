let checkChecks;
let selectedAnswer = null;

const main = () => {
	prepareDOMelements();
	prepareDOMevents();
};

const prepareDOMelements = () => {
	checkChecks = document.querySelectorAll('.check');
};

const prepareDOMevents = () => {
	checkChecks.forEach((check) => {
		check.addEventListener('click', changeColour);
	});
};

const changeColour = (event) => {
	const clickedCheck = event.currentTarget;

	checkChecks.forEach((check) => {
		check.style.backgroundColor = '';
	});

	if (clickedCheck !== selectedAnswer) {
		clickedCheck.style.backgroundColor = 'rgba(255, 255, 255, 0.67)';
		selectedAnswer = clickedCheck;
	} else {
		selectedAnswer = null;
	}
};

document.addEventListener('DOMContentLoaded', main);
