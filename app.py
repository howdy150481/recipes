from flask import Flask
from app.controller.recipes_controller import RecipesController
from app.controller.pdf_controller import PdfController

app = Flask(__name__)
recipes_controller = RecipesController()
pdf_controller = PdfController()


@app.route('/')
def list():
    return recipes_controller.list()


@app.route('/recipe/<string:wochentag>', methods=['GET'])
def recipe(wochentag):
    return recipes_controller.recipe(wochentag)


@app.route('/pdf/<string:wochentag>', methods=['GET'])
def pdf(wochentag):
    return pdf_controller.pdf(wochentag)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
