let box = document.getElementsByClassName('brand-image');
let box2 = document.getElementsByClassName('login-logo');
let footer = document.getElementsByClassName('main-footer')

try{
    box[0].setAttribute('src', '/static/img/logo.png');
    box[0].removeAttribute("style");
}
catch(e){}

try{
    let img = box2[0].children[0].children[0];
    img.setAttribute('width', '80%')
}
catch(e){}

try{
    console.log(footer[0].children[0].children[0]);
    footer[0].children[0].innerHTML = '<b>+996 558 120 012  ITADIS</b>';
}
catch(e){}
