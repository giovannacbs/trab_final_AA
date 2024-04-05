# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import requests
import os
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

## Parte da página dinâmica com raspagem do BBC 

@app.route("/bbc")
def bbc ():
    return render_template("bbc.html")

@app.route("/reportagens.html", methods=["GET"])
def result():
    tema = request.args.get("tema")
    materias = exibir_top5(tema)
    return render_template("reportagens.html", tema=tema, materias=materias)

## Parte do Bot do Telegram

token = os.environ["TELEGRAM_BOT_TOKEN"]

# Conectando ao bot 
url = f"https://api.telegram.org/bot{token}/"

def enviar_mensagem(chat_id, texto):
    url_mensagem = url + "sendMessage"
    data = {"chat_id": chat_id, "text": texto}
    requests.post(url_mensagem, json=data)

@app.route('/mensagem', methods=['POST'])
def mensagem():
    mensagem = request.json
    chat_id = mensagem['message']['chat']['id']
    texto = mensagem['message']['text']
    
    if texto == '/start':
        resposta = "Escolha uma opção e responda com o número selecionado:\n1. Brasil\n2. Internacional\n3. Tecnologia\n4. Economia"
    elif texto == '1':
        resposta = brasil()
    elif texto == '2':
        resposta = internacional()
    elif texto == '3':
        resposta = tecnologia()
    elif texto == '4':
        resposta = economia()
    else:
        resposta = "Opção inválida. Por favor, escolha um dos quatro temas ou digite '/start' para voltar ao menu inicial."

    enviar_mensagem(chat_id, resposta)
    return "OK", 200


## Função da raspagem
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

## Funções para o retorno do bot 
def brasil():
    tema = 'cz74k717pw5t'  
    noticias = exibir_top5(tema)
    resposta = "Últimas 5 notícias sobre o Brasil disponíveis no site da BBC em português:\n\n"
    for titulo, link in noticias:
        resposta += f"{titulo}\n{link}\n\n"
    resposta += "Digite '/start' para voltar ao menu inicial."    
    return resposta

def internacional():
    tema = 'cmdm4ynm24kt'  
    noticias = exibir_top5(tema)
    resposta = "Últimas 5 notícias internacionais disponíveis no site da BBC em português:\n\n"
    for titulo, link in noticias:
        resposta += f"{titulo}\n{link}\n\n"
    resposta += "Digite '/start' para voltar ao menu inicial."    
    return resposta

def tecnologia():
    tema = 'c404v027pd4t'  
    noticias = exibir_top5(tema)
    resposta = "Últimas 5 notícias sobre tecnologia disponíveis no site da BBC em português:\n\n"
    for titulo, link in noticias:
        resposta += f"{titulo}\n{link}\n\n"
    resposta += "Digite '/start' para voltar ao menu inicial."    
    return resposta

def economia():
    tema = 'cmdm4ynm24kt'  
    noticias = exibir_top5(tema)
    resposta = "Últimas 5 notícias de economia disponíveis no site da BBC em português:\n\n"
    for titulo, link in noticias:
        resposta += f"{titulo}\n{link}\n\n"
    resposta += "Digite '/start' para voltar ao menu inicial."        
    return resposta

if __name__ == '__main__':
    app.run(threaded=True)
