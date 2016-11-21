var ingred_num = 1;
var ingr_dropdown_num = 1;
var instr_num = 1;
var amount_num = 1;

function add_ingredient(){
    var elem = document.getElementById("ingredients");
    elem.appendChild(document.createElement('br'));

    var amount = document.createElement('input');
    amount.type = "text";
    amount.name = "amount" + amount_num;
    amount.placeholder = "3 cups";
    amount_num ++;

    elem.appendChild(amount);

    var newIngredient = document.createElement('input');
    newIngredient.type = "text";
    newIngredient.name = "ingredient" + ingred_num;
    newIngredient.placeholder = "Tofu";
    ingred_num ++;

    elem.appendChild(newIngredient);

    var ingr_dropdown = document.createElement("select");
    ingr_dropdown.name = "ingr_type" + ingr_dropdown_num;
    ingr_dropdown_num ++;
    elem.appendChild(ingr_dropdown);

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


};

function add_instruction(){
    var elem = document.getElementById("instructions");

    var newInstruction = document.createElement('input');
    newInstruction.type = "text";
    newInstruction.name = "instruction" + instr_num;
    instr_num ++;
    elem.appendChild(document.createElement('br'));
    elem.appendChild(newInstruction);

};