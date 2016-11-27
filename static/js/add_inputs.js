var ingred_num = 1;
var ingr_dropdown_num = 1;
var instr_num = 1;

var next_row;

function add_ingredient(){
    var elem = document.getElementById("ingredients");

    var space2div = document.createElement("div");
    space2div.className = "col-sm-2";
    elem.appendChild(space2div);

    var space10div = document.createElement("div");
    space10div.className = "col-sm-10";

    var textSpan = document.createElement("span");
    textSpan.className = "input-group-btn";

    var newIngredient = document.createElement("input");
    newIngredient.className = "form-control";
    newIngredient.type = "text";
    newIngredient.name = "ingredient" + ingred_num;
    newIngredient.placeholder = "Tofu";
    ingred_num ++;

    space10div.appendChild(textSpan);
    textSpan.appendChild(newIngredient);
    elem.appendChild(space10div);

    var selectSpan = document.createElement("span");
    selectSpan.className = "input-group-btn";

    var ingr_dropdown = document.createElement("select");
    ingr_dropdown.id = "ingr_type" + ingr_dropdown_num;
    ingr_dropdown.name = "ingr_type" + ingr_dropdown_num;
    ingr_dropdown.className = "form-control";
    ingr_dropdown_num ++;

    space10div.appendChild(selectSpan);
    selectSpan.appendChild(ingr_dropdown);

    var protein_option = document.createElement("option");
    protein_option.value = "1";
    protein_option.textContent="Proteins";


    var grains_option = document.createElement("option");
    grains_option.value = "2";
    grains_option.textContent="Grains/Rice";

    var dry_ingredients_option = document.createElement("option");
    dry_ingredients_option.value = "3";
    dry_ingredients_option.textContent = "Dry Ingredients";

    var wet_ingredients_option = document.createElement("option");
    wet_ingredients_option.value = "4";
    wet_ingredients_option.textContent = "Wet Ingredients";

    var oils_option = document.createElement("option");
    oils_option.value = "5";
    oils_option.textContent = "Oils";

    var seasoning_option = document.createElement("option");
    seasoning_option.value = "6";
    seasoning_option.textContent = "Seasoning/Spices";

    ingr_dropdown.appendChild(protein_option);
    ingr_dropdown.appendChild(grains_option);
    ingr_dropdown.appendChild(dry_ingredients_option);
    ingr_dropdown.appendChild(wet_ingredients_option);
    ingr_dropdown.appendChild(oils_option);
    ingr_dropdown.appendChild(seasoning_option);

    next_row = newIngredient;

};

function setIngredientFocus(){
    next_row.focus();
}

function setInstructionFocus(){
    next_row.focus();
}

function add_instruction(){
    var elem = document.getElementById("instructions");

    var space2div = document.createElement("div");
    space2div.className = "col-sm-2";
    elem.appendChild(space2div);

    var space10div = document.createElement("div");
    space10div.className = "col-sm-10";
    elem.appendChild(space10div);

    var newInstruction = document.createElement('input');
    newInstruction.type = "text";
    newInstruction.className = "form-control";
    newInstruction.name = "instruction" + instr_num;
    instr_num ++;
    space10div.appendChild(newInstruction);

    next_row = newInstruction;

};