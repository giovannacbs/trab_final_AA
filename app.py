from flask import Flask, render_template

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
def curriculo ():
    return render_template("bbc.html")

@app.route('/reportagens.html', methods=['GET'])
def result():
    tema = request.args.get('tema')
    materias = exibir_top5(tema)
    return render_template('reportagens.html', tema=tema, materias=materias)


