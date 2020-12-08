let correlativo = 0;
let btnAddColor = document.querySelector('#addProdColor');
let btnNext = document.querySelector('#btnSaveInfo');

function deleteColor(correlativo){
    document.querySelector('#rows'+correlativo).remove();
}

btnAddColor.addEventListener('click', function(){
    correlativo++;
    let productColor = document.querySelector('#colors').value;
    let myLabel = document.querySelector('#myLabel');
    document.querySelector('#productColorTable').innerHTML+="<tr id='rows"+correlativo+"'><td> <input type='hidden' name='arrayProductColor[row"+correlativo+"][product]' value="+productColor+"/> <p>"+productColor+"</p></td><td><button  onClick='deleteColor("+correlativo+")'>Eliminar</button></td></tr>";
});

btnNext.addEventListener('click', function(){
    document.querySelector('.form__sec-product--color').style.gridRow = '2 / 3';
    document.querySelector('.form__sec-product--color').style.display = 'block';  
    document.querySelector('.form__sec-product--sku').style.display = 'block';    
});

/*function miFuncion(){
    correlativo++;
    var username = $('#username').val();
    var myLabel = $('#miLabel');
    $('#tableUsuario').append("<tr id='fila"+correlativo+"'><td> <input type='hidden' name='arrayUsername[row"+correlativo+"][usuario]' value="+username+"/> <p>"+username+"</p></td><td><button  onClick='eliminar("+correlativo+")'>Eliminar</button></td></tr>");
}*/