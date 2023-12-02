/**
 * Created by Juan U on 2023/11/s29
 * 
 * User.js
 * User related functions
 */


//Metodo para controlar el registro de usuarios en la base de datos
// user.js

function show() {
    var p = pwd
    p.setAttribute('type', 'text');
}

function hide() {
    var p = pwd
    p.setAttribute('type', 'password');
}

function init() {

    var pwShown = 0;

    eye.addEventListener("click", function () {
        if (pwShown == 0) {
            pwShown = 1;
            show();
        } else {
            pwShown = 0;
            hide();
        }
    }, false);
}



document.addEventListener("DOMContentLoaded", function () {
    init();
});
