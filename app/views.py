
from flask import Flask, render_template, request
from app import app
import sys
from static.python.memegenerator import make_meme
from jinja2 import Template


@app.route("/")
def index():
	return render_template("/index.html")

@app.route("/send", methods=['POST'])
def send():

	txtSup = request.form["txtSup"]
	txtInf = request.form["txtInf"]

		# se necesita la ruta completa de la imagen. Ver como mejorar en el futuro por motivos de seguridad
    	make_meme(txtSup, txtInf, "/Users/carlosprieto/desarrollo/generamemes/app/static/python/sap.jpg")
	
	return render_template('/meme.html')

