from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>

@app.route("/curriculo")
def index():
    return """
    <html>
      <title>Currículo</title>
      <div>   
        <style>
            body {
              font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif; 
              margin: 10px; 
              background-color: #f8f8f8; 
            }
            h1, h2, h3 {
              color: #fc0317; 
              margin-bottom: 10px; 
            }
            p {
              color: #232324; 
              margin-bottom: 10px; 
            }
            p {margin-bottom: 1px}</style>
        <body>
          <div class="linha-vertical"></div>
          <h3>Meu curriculo e contatos</h3>
          <h1>ANA CAROLINA ANDRADE</h1>
          <h4>&nbsp;&nbsp;&nbsp;Jornalista e produtora de conteúdo para mídias digitais</h4>
          <div class="linha-vertical2"><h3 style="color: red;">&nbsp;&nbsp;&nbsp;FORMAÇÃO ACADÊMICA</h3></div>
          <p>2023 Master em Jornalismo de Dados, Automação e Data Storytelling - Insper (conclusão em 2024)<br>
              2020 Especialização em Gênero e Sexualidade - Universidade do Estado do Rio de Janeiro<br>
              2018 Pós-graduação em Gestão da Comunicação em Mídias Digitais - Senac São Paulo<br>
              2011 Graduação em Comunicação Social, habilitação Jornalismo - Pontifícia Universidade Católica de São Paulo (PUC-SP)</p>

          <div class="linha-vertical2"><h3 style="color: red;">&nbsp;&nbsp;&nbsp;EXPERIÊNCIA PROFISSIONAL</h3></div>
          
          <p><h4>&nbsp;&nbsp;FREELANCER</h4><b>Jornalista e produtora de conteúdo para mídias digitais | Jan 2019 - atualmente</b><br>
              Produção de reportagens; redação e produção de materiais para sites e redes sociais como Instagram, Facebook e X (Twitter);<br>
              Monitoramento e análise de redes; Cobertura de eventos nacionais e internacionais.<p>

          <p><h4>&nbsp;&nbsp;BANDNEWS TV</h4><b>Social Media | Jul 2022 - Jan 2023</b><br>
              Produção de conteúdo para as redes sociais do BandNews TV, do Grupo Bandeirantes de Comunicação.<p>

          <p><h4>&nbsp;&nbsp;FENAMETRO (FEDERAÇÃO NACIONAL DOS METROVIÁRIOS)</h4><b>Jornalista | Jul 2015 - Dez 2019</b><br>
              Produção de reportagens, edição do site da entidade; Redação e diagramação de<br>
              boletins impressos e digitais; Produção de conteúdo e gestão das redes sociais;<br>
              Cobertura de eventos nacionais e internacionais; Assessoria de imprensa<p>        

          <div class="linha-vertical2"><h3 style="color: red;">&nbsp;&nbsp;&nbsp;FORMAÇÃO COMPLEMENTAR</h3></div>

          <p>2020 Workshop Ferramentas Avançadas de Busca para Comunicadoras - Chicas Poderosas<br>
             2018 Curso de extensão “Fronteiras do Feminismo: pós-colonialismo, teorias e práticas PUC-SP. <br>
             2015 Curso de extensão “Fronteiras do Feminismo: pós-colonialismo, teorias e práticas latino-americanas” PUC-SP.<p> 


          <title>contatos</title>
          <style>.imagens {position: absolute; top: 40px; right: 150px;}         
          </style>
          <img class="imagens" src="C:\\Users\\Valmerson\\Downloads\\contatos.jpg" alt="contatos_Ana_Carolina">

          <title>contatos</title>
          <style>.imagens2 {position: absolute; top: 390px; right: 150px;}         
          </style>
          <img class="imagens2" src="C:\\Users\\Valmerson\\Downloads\\qualificações.jpg" alt="skills">

          <button><a href="/">Voltar para página inicial</a></button>

       </body>
    </html>
    """






