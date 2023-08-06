'use strict';

const assitantID = document.getElementById('WACInputContainer__SendButton--homeScreenModern')
assitantID.addEventListener('click',function(){
    const user_input = document.getElementById('WACInputContainer-TextArea--homeScreenModern').value;
    console.log(user_input)
    appendMessage('You', user_input);

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `user_input=${user_input}`
        
    })
    .then(response => response.json())
    .then(data => {
        const reply = data.reply;
        appendMessage('Chatbot', reply);
    });

    document.getElementById('user-input').value = '';
})

