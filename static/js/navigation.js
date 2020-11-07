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

//Display/hide form container

function openSearchForm(){
    document.getElementById("searchForm").style.transitionDelay = ".2s";
    document.getElementById("searchFormWrapper").style.height = "100%";
    document.getElementById("searchForm").style.height = "80vh";
    console.log("hey, im from open search form function");
};

function closeSearchForm(){
    document.getElementById("searchFormWrapper").style.transitionDelay = ".3s";
    document.getElementById("searchFormWrapper").style.height = "0";    
    
};


document.addEventListener('mouseup', function(e) {
    var searchForm = document.getElementById("searchForm");
    if (!searchForm.contains(e.target)) {
        closeSearchForm(); 
    }
  });


document.onclick=function(e){
    var menu = document.getElementById("navigationNav");
    if(e.target == menu){
        closeNav();        
    }
};


addToCart = document.querySelector('#addCartAmount');
addToCart.addEventListener('click', function(){
    var counterDOM = document.querySelector('#counterAmount')
    var counter = parseInt(counterDOM.textContent);
    counter += 1;
    counterDOM.textContent = counter;
    console.log(counter);
    
});



