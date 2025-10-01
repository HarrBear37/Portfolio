var originalBackground;
function toggleHighlight() {
    var pos = this.getAttribute('value');
    var color;
    switch (pos) {
        case 'bear':
        color='green';
        break;
        case 'cat':
        color='red';
        break;
        case 'dog':
        color='red';
        break;
        case 'elephant':
        color='red';
        break;
        case 'frog':
        color='red';
        break;
    }
    var status = this.checked;
    var spans = document.getElementsByClassName(pos);
    for (var i=0; i < spans.length; i++) {
            if (status == true) {
                spans[i].styles.backgroundColor = color;
            } else {
                spans[i].styles.backgroundColor = originalBackground;
            }
    }
}

function init() {
    originalBackground = document.body.style.backgroundColor;
    var checkboxes = document.getElementsByTagName('input');
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].addEventListener('click', toggleHighlight, false);
    }
}

window.addEventListener('DOMContentLoaded',init,false);