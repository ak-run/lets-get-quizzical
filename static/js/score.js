document.getElementById('saveScoreButton').addEventListener('click', function(event) {
    event.preventDefault();
    const submitUrl = this.getAttribute('data-submit-url');
    const redirectUrl = this.getAttribute('data-redirect-url');

    fetch(submitUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'nickname': '{{ session.get('nickname') }}',
            'score': '{{ session.get('user_score') }}'
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.href = redirectUrl;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
