
function add_ingredient(){
    var elem = document.getElementById("ingredients");


    var newIngredient = document.createElement('input');
    newIngredient.type = "text";
    elem.appendChild(document.createElement('br'));
    elem.appendChild(newIngredient);

};

function add_instruction(){

    var elem = document.getElementById("instructions");


    var newInstruction = document.createElement('input');
    newInstruction.type = "text";
    elem.appendChild(document.createElement('br'));
    elem.appendChild(newInstruction);

};