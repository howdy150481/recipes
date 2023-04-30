from flask import render_template, redirect, url_for
import xml.etree.ElementTree as ET


class RecipesController:
    def __init__(self):
        tree = ET.parse('recipes.xml')
        self.recipes = tree.getroot()

    def list(self):
        return render_template(
            'reeciepes/list.html',
            recipes=self.recipes,
            route='list'
        )

    def recipe(self, wochentag):
        for searchRecipe in self.recipes.findall("rezept"):
            if searchRecipe.get("wochentag") == wochentag:
                recipe = searchRecipe

        return render_template(
            'reeciepes/recipe.html',
            recipes=self.recipes,
            recipe=recipe,
            route=wochentag
        )
