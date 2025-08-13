// API notification

const button = document.querySelector('#button');
button.addEventListener('click', () => {
    Notification.requestPermission()
        .then(result => console.log(`The result is ${result}`));
});


if(Notification.permission === 'granted'){
    new Notification(`This is a notification`, {
        icon: 'img/css.png',
        body: 'Code with Migue, the best student'
    })
}