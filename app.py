from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
  return "<html>
    <title>Aceita pix</title>
    <body>
        <h1> Aqui vai o título da home.</h1>
    <p> Aqui começa um novo parágrafo.</p>
    </body>
</html>"
