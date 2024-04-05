# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

## Primeira parte do trabalho

@app.route("/")
def index():
    return render_template("home.html")
    
@app.route("/portfolio")
def portifolio ():
    return render_template("portfolio.html")

@app.route("/curriculo")
def curriculo ():
    return render_template("curriculo.html")

## Parte da página dinâmica com raspagem do BBC PT

@app.route("/bbc")
def bbc ():
    return render_template("bbc.html")

@app.route("/reportagens.html", methods=["GET"])
def result():
    tema = request.args.get("tema")
    materias = exibir_top5(tema)
    return render_template("reportagens.html", tema=tema, materias=materias)

def exibir_top5(tema):
  url = 'https://www.bbc.com/portuguese/topics/' + tema

  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  h2 = soup.find_all('h2') # look for all titles 
  titulos = []
  for h in h2:
    titulo = h.get_text()
    titulos.append(titulo)

  titulos = titulos[:5] # select only first 5
  
  links = soup.find_all('a', {'class' : 'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})
  
  hrefs = []
  for href in links:
    hrefs.append(href.get('href'))

  hrefs = hrefs[:5]

  materias = list(zip(titulos, hrefs))

  return materias
