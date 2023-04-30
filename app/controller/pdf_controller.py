from flask import render_template, Response
from weasyprint import HTML
import xml.etree.ElementTree as ET


class PdfController:
    def __init__(self):
        pass

    def pdf(self, wochentag):
        tree = ET.parse('recipes.xml')
        recipes = tree.getroot()
        for searchRecipe in recipes.findall("rezept"):
            if searchRecipe.get("wochentag") == wochentag:
                recipe = searchRecipe

        rendered_html = render_template(
            'reeciepes/pdf.html',
            recipe=recipe
        )

        pdf_data = HTML(string=rendered_html).write_pdf()
        return Response(
            pdf_data,
            mimetype="application/pdf",
            headers={"Content-Disposition": "attachment;filename=rezept.pdf"}
        )
