document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById("avatarModal");
    const btn = document.getElementById("avatarModalBtn");
    const span = document.getElementsByClassName("close")[0];

    btn.onclick = function() {
        modal.style.display = "block";
    };

    span.onclick = function() {
        modal.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };

    document.querySelectorAll('#avatarChoices img').forEach(function(img) {
        img.addEventListener('click', function() {
            let avatarValue = img.getAttribute('src');
            document.getElementById('selectedAvatar').value = avatarValue.split('/').pop();
            document.getElementById('avatarPreview').src = avatarValue;
            modal.style.display = "none";
        });
    });

    // Get the nickname input and start button elements
    const nicknameInput = document.getElementById('nickname');
    const startButton = document.getElementById('startGame');

    // Add an event listener to the nickname input
    nicknameInput.addEventListener('input', function() {
        // Enable the start button if the nickname is not empty
        const isNicknameEntered = nicknameInput.value.trim() !== '';
        startButton.disabled = !isNicknameEntered;

        // Add or remove the active button class based on the nickname input
        if (isNicknameEntered) {
            startButton.classList.add('button-active');
        } else {
            startButton.classList.remove('button-active');
        }
    });
});


