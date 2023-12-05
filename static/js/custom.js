let button = document.querySelector('.next-button');
let timeDisplay = document.getElementById('time');
let intervalId



let currentQuestionIndex = 0;




// function loadQuestion()


function stopWatch() {
    let number = 21;
    intervalId = setInterval(function () {
        number--;
        let formattedTime = `00:${String(number).padStart(2, '0')}`;
        timeDisplay.textContent = formattedTime;

        if (number === 0) {
            clearInterval(intervalId);
            currentQuestionIndex++;
            loadQuestion();
            timeDisplay.textContent = 'Time is up!';
            number = 20;
            stopWatch();
        }
    }, 1000);
}

//function nextQuestion() {
//    currentQuestionIndex++;
//    if (currentQuestionIndex < quizData.results.length) {
//        clearInterval(intervalId);
//        // loadQuestion();
//        stopWatch();
//    } else {
//        alert('Quiz completed!');
//    }
//}

// loadQuestion()
stopWatch();
