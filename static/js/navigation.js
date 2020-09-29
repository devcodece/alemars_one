function openNav(){
    document.getElementById("navContent").style.transitionDelay = ".2s";
    document.getElementById("navigationNav").style.width = "100vw";
    document.getElementById("navContent").style.width = "80vw";
    console.log("hey, im here");
};

function closeNav(){
    document.getElementById("navigationNav").style.transitionDelay = ".3s";
    document.getElementById("navigationNav").style.width = "0";    
    document.getElementById("navContent").style.width = "0";
};

window.onclick=function(e){
    var menu = document.getElementById("navigationNav");
    if(e.target == menu){
        closeNav();        
    }
};

