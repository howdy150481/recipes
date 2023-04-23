from flask import Flask, render_template, request, redirect, url_for
from app.controller.recipes_controller import RecipesController

app = Flask(__name__)
rezept_controller = RecipesController()

@app.route('/')
def list():
    return rezept_controller.list()

@app.route('/recipe/<string:wochentag>', methods=['GET'])
def recipe(wochentag):
    return rezept_controller.recipe(wochentag)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
