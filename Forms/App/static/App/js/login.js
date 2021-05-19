var label = document.getElementsByTagName('label');
var input = document.getElementsByTagName('input');




for (var i = 0; i <= input.length; i++) {


    input[i].addEventListener('click', function(e) {
        prevnt
        var placeholder = input[i].getAttribute('placeholder');
        label[0].innerHTML = placeholder;
        //label[i].setAttribute(placeholder, '');

        setTimeout(function() {
            label[i].style.transform = 'translateY(0 px)';
        }, 500);

    })





}