from flask import Flask, render_template, json, request
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

    return render_template("index.html", Title="Kira's Recipes")

@app.route("/input_recipe", methods=["POST", "GET"])
def input_recipe():

    return render_template("input_recipe.html", Title="Add a new Recipe")


@app.route("/recipes",methods=["GET"])
def recipes():
    user_input = request.args.get("search")
    cursor.execute("SELECT Title FROM Recipe WHERE Title LIKE %s", ('%' + user_input + '%'))
    results = cursor.fetchall()


    return render_template("recipe.html", Title="Kira's Recipes", results=results)

if __name__ == '__main__':


    app.run()
