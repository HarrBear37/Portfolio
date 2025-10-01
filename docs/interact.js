window.addEventListener('DOMContentLoaded',init,false);

function init() {
    alert('The page loaded!');
    var buttons = document.getElementsByTagName("button")
    buttons[0].addEventListener('click', changeColor,false)
    buttons[1].addEventListener('click', noClick, false)
}

function changeColor() {
var colorMe1 = document.getElementById("colorToggle") 
{colorMe1.style.backgroundColor = "skyblue";
}
}/* here, style is a *property*: the CSS styling of an element: you can add a CSS property after invoking style. */

function noClick() {
    alert('I said do NOT click me!');
    var element = document.getElementByTagName("p");
    for (var i = 0, length = element.length; i < length; i++){
    {element[i].style.backgroundColor = "red";}
    }
}