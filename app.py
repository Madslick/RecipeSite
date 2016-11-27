from flask import Flask, render_template, json, request, redirect
from flask import url_for
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Br0cade1'
app.config['MYSQL_DATABASE_DB'] = 'RecipeSite'
app.config['MYSQL_DATABASE_HOST'] = '192.168.1.142'


mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def main():

    cursor.execute("SELECT Title FROM Recipe LIMIT 10")
    results = cursor.fetchall()

    print len(results)

    return render_template("index.html", Title="Kira's Recipes", home=True, results=results)

@app.route("/insert_recipe", methods=["POST", "GET"])
def insert_recipe():
    title = request.form['title']
    ingredients = []

    ingredient_types = []
    instructions = []

    ing_count = 0
    instr_count = 0

    for key, value in request.form.items():

        if key.find('ingredient') >= 0:
            ing_count += 1
        if key.find('instruction') >= 0:
            instr_count += 1


    for i in range(0, ing_count):
        ingredients.append(request.form['ingredient' + str(i)])
        ingredient_types.append(request.form['ingr_type' + str(i)])
    for i in range(0, instr_count):
        instructions.append(request.form['instruction' + str(i)])

    for i in ingredients:
        print i
    for i in instructions:
        print i

    cursor.execute("INSERT INTO Recipe (Title) VALUES (%s)", (title))
    conn.commit()

    id = cursor.lastrowid

    ingredient_sql = "INSERT INTO Recipe_Ingredients (RecipeId, Name, IngredientTypeId)" \
                     " VALUES (%s, '%s', %s)" % (id, ingredients[0], ingredient_types[0])

    for i in range (1, len(ingredients)):
        ingredient_sql = ingredient_sql + ", (%s, '%s', %s)" % (id, ingredients[i], ingredient_types[i])
    print ingredient_sql
    cursor.execute(ingredient_sql)
    conn.commit()

    instruction_sql = "INSERT INTO Recipe_Instructions (RecipeId, Instruction, StepNumber) VALUES (%s, '%s', %s)" % (id, instructions[0], 1)

    for i in range (1, len(instructions)):
        instruction_sql = instruction_sql + ", (%s, '%s', %s)" % (id, instructions[i], i + 1)

    cursor.execute(instruction_sql)

    conn.commit()

    return redirect(url_for('main'))

@app.route("/read_recipe/<string:recipe_title>", methods=['GET'])
def read_recipe(recipe_title):
    ingredients = []
    ingredient_types = []
    instructions = []

    cursor.execute("SELECT Recipe_Ingredients.Name, Ingredient_Type.Name FROM Recipe_Ingredients "
                   "INNER JOIN Ingredient_Type ON Ingredient_Type.Id = Recipe_Ingredients.IngredientTypeId "
                   "INNER JOIN Recipe ON Recipe_Ingredients.RecipeId = Recipe.Id WHERE Recipe.Title = %s"
                   " ORDER BY Recipe_Ingredients.IngredientTypeId ASC", (recipe_title))
    results = cursor.fetchall()


    for row in results:
        ingredients.append(row[0])
        ingredient_types.append(row[1])

    cursor.execute("SELECT Instruction FROM Recipe_Instructions INNER JOIN Recipe ON Recipe_Instructions.RecipeId = Recipe.Id WHERE Recipe.Title = %s ORDER BY Recipe_Instructions.StepNumber ASC", (recipe_title))

    results = cursor.fetchall()

    for row in results:
        instructions.append(row[0])

    return render_template("read_recipe.html", Title=recipe_title, home=True, recipe_title=recipe_title, ingredients=ingredients, ingredient_types=ingredient_types, instructions=instructions)

@app.route("/input_recipe", methods=["POST", "GET"])
def input_recipe():

    return render_template("input_recipe.html", home=False, Title="Add a new Recipe")


@app.route("/recipes",methods=["GET"])
def recipes():
    user_input = request.args.get("search")
    cursor.execute("SELECT Title FROM Recipe WHERE Title LIKE %s", ('%' + user_input + '%'))
    results = cursor.fetchall()

    return render_template("recipe.html", Title="Kira's Recipes", home=True, query=user_input, results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
