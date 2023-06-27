console.log('hii')

var number = 10;
var string = 'Square';
var israd = true;

document.getElementById('sq').innerHTML = string;

var stuff = ['Ay', 'Broo', 'Yo'];

function liststuff(){
    for(var i=0; i < stuff.length; i++){
        console.log(stuff[i]);
    }
}
liststuff();

document.getElementById('cr').addEventListener('click', function(){
    alert('Thats a Circle');
});

