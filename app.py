from flask import Flask, render_template, json, request, redirect
from flask import url_for
from flaskext.mysql import MySQL

#Initialize the app
app = Flask(__name__)

#Configure the app with the info to connect to the database
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Br0cade1'
app.config['MYSQL_DATABASE_DB'] = 'RecipeSite'
app.config['MYSQL_DATABASE_HOST'] = '192.168.1.142'

#Connect to the database and create a cursor object
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

def connect():
    conn = mysql.connect()
    cursor = conn.cursor()
def query(sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Exception:
        connect()
        cursor = conn.cursor()
        cursor.execute(sql)
    return cursor

#Home Page
@app.route("/")
def main():
    #Get 10 Recipe's render them on home page
    results = query("SELECT Title FROM Recipe LIMIT 10").fetchall()
    return render_template("index.html", Title="Kira's Recipes", home=True, results=results)

#Add a Recipe Page
@app.route("/input_recipe", methods=["POST", "GET"])
def input_recipe():
    return render_template("input_recipe.html", home=False, Title="Add a new Recipe")

#Input Recipe calls this method to insert the new recipe
@app.route("/insert_recipe", methods=["POST", "GET"])
def insert_recipe():
    #Get the Title of the recipe
    title = request.form['title']

    #Initialize the arrays for the users ingredients and instructions
    ingredients = []
    ingredient_types = []
    instructions = []

    #Counters for ingredients and instructions
    ing_count = 0
    instr_count = 0

    #Get the number of ingredient indices and number of instruction indices
    for key, value in request.form.items():
        #If the key value has the string ingredient, increment
        if key.find('ingredient') >= 0:
            ing_count += 1
        #If the key value has the string instruction, increment
        if key.find('instruction') >= 0:
            instr_count += 1

    #For the number of ingredients we found, store in the ingredient and ingreidnt_types array
    for i in range(0, ing_count):
        #Ingredients along with their corresponding ingredient type
        ingredients.append(request.form['ingredient' + str(i)])
        ingredient_types.append(request.form['ingr_type' + str(i)])

    #For the number of instructions, put them in the instructions array
    for i in range(0, instr_count):
        instructions.append(request.form['instruction' + str(i)])

    #Start the insertion of the title to the database
    cursor.execute("INSERT INTO Recipe (Title) VALUES (%s)", (title))
    conn.commit()

    #Get the Primary key of the Recipe table row to link the ingredient and instruction rows
    id = cursor.lastrowid
    #The initial insert MySQL command for the Recipe_Ingredients data
    ingredient_sql = "INSERT INTO Recipe_Ingredients (RecipeId, Name, IngredientTypeId)" \
                     " VALUES (%s, '%s', %s)" % (id, ingredients[0], ingredient_types[0])
    #A recursive approach to insert the rest of the ingredients
    for i in range (1, len(ingredients)):
        ingredient_sql = ingredient_sql + ", (%s, '%s', %s)" % (id, ingredients[i], ingredient_types[i])
    #Execute, Captain
    query(ingredient_sql)
    conn.commit()

    #The initial insert for the Recipe_Instructions data
    instruction_sql = "INSERT INTO Recipe_Instructions (RecipeId, Instruction, StepNumber) VALUES (%s, '%s', %s)" % (id, instructions[0], 1)
    #The recursive approach to add the rest of the instructions in one MySQL insert
    for i in range (1, len(instructions)):
        instruction_sql = instruction_sql + ", (%s, '%s', %s)" % (id, instructions[i], i + 1)
    #Execute, Captain
    query(instruction_sql)
    conn.commit()

    #Take the user back to the home page
    return redirect(url_for('read_recipe', recipe_title=title))

#Page for the individual recipes
@app.route("/read_recipe/<string:recipe_title>", methods=['GET'])
def read_recipe(recipe_title):
    #Instantiate the arrays used to display the recipe
    ingredients = []
    ingredient_types = []
    instructions = []

    #MySQL SELECT statement fo the Ingredients
    results = query("SELECT Recipe_Ingredients.Name, Ingredient_Type.Name FROM Recipe_Ingredients "
                   "INNER JOIN Ingredient_Type ON Ingredient_Type.Id = Recipe_Ingredients.IngredientTypeId "
                   "INNER JOIN Recipe ON Recipe_Ingredients.RecipeId = Recipe.Id WHERE Recipe.Title = %s "
                   "ORDER BY Recipe_Ingredients.IngredientTypeId ASC", (recipe_title)).fetchall()


    #Store the ingredients and ingredient types in their respective arrays
    for row in results:
        ingredients.append(row[0])
        ingredient_types.append(row[1])

    #MySQL SELECT statement for the instructions
    cursor.execute("SELECT Instruction FROM Recipe_Instructions "
                   "INNER JOIN Recipe ON Recipe_Instructions.RecipeId = Recipe.Id "
                   "WHERE Recipe.Title = %s ORDER BY Recipe_Instructions.StepNumber ASC", (recipe_title))
    results = cursor.fetchall()

    #Put the instructions into the instructions array
    for row in results:
        instructions.append(row[0])

    #Render the page with all the data about the recipe
    return render_template("read_recipe.html", Title=recipe_title, home=True, recipe_title=recipe_title, ingredients=ingredients, ingredient_types=ingredient_types, instructions=instructions)

#Search results for user's recipe query
@app.route("/recipes",methods=["GET"])
def recipes():
    #Get the user input
    user_input = request.args.get("search")

    #Get recipe titles that contain the query
    results = query("SELECT Title FROM Recipe WHERE Title LIKE %s", ('%' + user_input + '%')).fetchall()


    #Render the list of results
    return render_template("recipe.html", Title="Kira's Recipes", home=True, query=user_input, results=results)

#run the application
if __name__ == '__main__':
    app.run()
