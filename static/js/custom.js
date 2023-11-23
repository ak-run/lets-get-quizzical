document.addEventListener('DOMContentLoaded', function () {
    let button = document.querySelector('div.main-button');
    button.addEventListener('click', nextQuestion);

    let quizData = {
        response_code: 0,
        results: [
            {
                question: 'In Mulan (1998), who is the leader of the Huns?',
                correct_answer: 'Shan Yu',
                incorrect_answers: ['Chien-Po', 'Li Shang', 'Fa Zhou'],
            },
            {
                question: 'Which country do cities of Perth, Adelaide & Brisbane belong to?',
                correct_answer: 'Australia',
                incorrect_answers: ['Germany', 'Malta', 'France'],
            },
        ],
    };

    let currentQuestionIndex = 0;

    function loadQuestion() {
        let currentQuestion = quizData.results[currentQuestionIndex];
        document.getElementById('question-number').innerText =
            currentQuestionIndex + 1;
        document.getElementById('question-content').innerText =
            currentQuestion.question;
        let answersContainer = document.getElementById('answers-container');
        answersContainer.innerHTML = '';

        let allAnswers = [
            currentQuestion.correct_answer,
            ...currentQuestion.incorrect_answers,
        ];

        allAnswers.forEach(function (answer) {
            let answerDiv = document.createElement('div');
            answerDiv.classList.add('answer');
            answerDiv.innerHTML = `<input type="radio" name="answer" value="${answer}" class="main-button">
                                    <span>${answer}</span>`;
            answersContainer.appendChild(answerDiv);
        });
    }

    function nextQuestion() {
        currentQuestionIndex++;
        if (currentQuestionIndex < quizData.results.length) {
            loadQuestion();
        } else {
            alert('Quiz completed!');
        }
    }

    loadQuestion();
});
