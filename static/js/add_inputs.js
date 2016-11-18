var ingred_num = 0;
var instr_num = 0;

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
    newInstruction.name = "instruction" + toString(instr_num);
    console.log(toString(newInstruction.name));
    elem.appendChild(document.createElement('br'));
    elem.appendChild(newInstruction);

};