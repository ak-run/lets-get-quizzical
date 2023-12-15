// Selecting elements from the DOM
let button = document.querySelector('.next-button');
let timeDisplay = document.getElementById('time');
let intervalId;
let radioButtons = document.querySelectorAll('input[name="user_answer"]');

// Checking if timeDisplay exists before running the stopwatch
if (timeDisplay) {
    // Only run the stopwatch if timeDisplay exists
    stopWatch();
}

function stopWatch() {
	let number = 21;
	intervalId = setInterval(function () {
		number--;
		let formattedTime = `00:${String(number).padStart(2, '0')}`;
		timeDisplay.textContent = formattedTime;

		if (number === 0) {
			clearInterval(intervalId);
			currentQuestionIndex++;
			//            loadQuestion();
			timeDisplay.textContent = 'Time is up!';
			number = 20;
			stopWatch();
		}
	}, 1000);
}

 radioButtons.forEach(function(radioButton) {
     radioButton.addEventListener("click", function(event) {

        button.disabled = false;

     });
 });

 // script to auto submit the question once the timer is up (after 21 seconds to account for slight delay)
var timerDuration = 21000;
// Start the timer
var timer = setTimeout(function () {
    // Enable the submit button and trigger form submission
    document.getElementById("submit-btn").removeAttribute("disabled");
    document.getElementById("question_form").submit();
}, timerDuration);