var ingred_num = 1;
var ingr_dropdown_num = 1;
var instr_num = 1;
var next_row;

//This function adds a row of inputs for the user to add an ingredient
function add_ingredient(){
    //Get the ingredients div
    var elem = document.getElementById("ingredients");

    //Add a 2 column divider to keep inputs inline
    var space2div = document.createElement("div");
    space2div.className = "col-sm-2";

    //We'll be putting the row in a 10 column div
    var space10div = document.createElement("div");
    space10div.className = "col-sm-10";

    //Ingredient span with the input-group-btn class to keep the input element inline
    var textSpan = document.createElement("span");
    textSpan.className = "input-group-btn";

    //Create and configure the input element
    var newIngredient = document.createElement("input");
    newIngredient.className = "form-control";
    newIngredient.type = "text";
    newIngredient.name = "ingredient" + ingred_num;
    newIngredient.placeholder = "Tofu";
    newIngredient.maxLength = "180";

    //Create the span for the select element
    var selectSpan = document.createElement("span");
    selectSpan.className = "input-group-btn";

    //Create the Select element
    var ingr_dropdown = document.createElement("select");
    ingr_dropdown.id = "ingr_type" + ingr_dropdown_num;
    ingr_dropdown.name = "ingr_type" + ingr_dropdown_num;
    ingr_dropdown.className = "form-control";

    //Create the protein option element for the Select element
    var protein_option = document.createElement("option");
    protein_option.value = "1";
    protein_option.textContent="Proteins";

    //Create the grains/rice option element for the Select element
    var grains_option = document.createElement("option");
    grains_option.value = "2";
    grains_option.textContent="Grains/Rice";

    //Create the dry_ingredients option element for the Select element
    var dry_ingredients_option = document.createElement("option");
    dry_ingredients_option.value = "3";
    dry_ingredients_option.textContent = "Dry Ingredients";

    //Create the wet_ingredients option element for the Select element
    var wet_ingredients_option = document.createElement("option");
    wet_ingredients_option.value = "4";
    wet_ingredients_option.textContent = "Wet Ingredients";

    //Create the Oils option element for the Select element
    var oils_option = document.createElement("option");
    oils_option.value = "5";
    oils_option.textContent = "Oils";

    //Create the seasoning option element for the Select element
    var seasoning_option = document.createElement("option");
    seasoning_option.value = "6";
    seasoning_option.textContent = "Seasoning/Spices";

    //Append the elements as children to the appropriate parent
    elem.appendChild(space2div); // Add the 2 column div to the ingredients div
    elem.appendChild(space10div); //Add the 10 column div to the ingredients div

    space10div.appendChild(textSpan); //Add the span element as child to the 10 column div
    textSpan.appendChild(newIngredient);//Add the input element as child to the span

    space10div.appendChild(selectSpan); //Add the select span to the 10 column div
    selectSpan.appendChild(ingr_dropdown); //Add the select element to the span

    ingr_dropdown.appendChild(protein_option); //Add the protein option to the select element
    ingr_dropdown.appendChild(grains_option); //Add the grains/rice option to the select element
    ingr_dropdown.appendChild(dry_ingredients_option); //Add the dry_ingredients option to the select element
    ingr_dropdown.appendChild(wet_ingredients_option); //Add the wet_ingredients option to the select element
    ingr_dropdown.appendChild(oils_option); //Add the oils option to the select element
    ingr_dropdown.appendChild(seasoning_option); //Add the seasoning option to the select element

    //Modify the variables for the next time
    next_row = newIngredient;
    ingred_num ++;
    ingr_dropdown_num ++;
};

//Sets the focus to the newly created ingredient text input
function setIngredientFocus(){
    next_row.focus();
}

//Sets the focus to the newly created instruction text input
function setInstructionFocus(){
    next_row.focus();
}

//Add a row for a new instruction
function add_instruction(){
    //Get the instructions div
    var elem = document.getElementById("instructions");

    //Create the 2 column div to stay inline
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
    newInstruction.maxLength = "400";
    instr_num ++;
    space10div.appendChild(newInstruction);

    next_row = newInstruction;

};