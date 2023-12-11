let button = document.querySelector('.next-button');
let timeDisplay = document.getElementById('time');
let intervalId;
let radioButtons = document.querySelectorAll('input[name="user_answer"]');
// console.log(radioButtons);
// let isAnswered = 0
// let noAnswerError = document.getElementsByClassName('no-answer-error')
// console.log(noAnswerError);



let currentQuestionIndex = 0;

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

