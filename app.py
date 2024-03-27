from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
      <title>Ana Carolina Andrade</title>
    <body>
      <div><style>
        body {
          font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif; 
          margin: 10px; 
          background-color: #f8f8f8; 
        }
        h1, h2, h3 {
          color: #8B0000; 
          margin-bottom: 10px; 
        }
        p {
          color: #232324; 
          margin-bottom: 10px; 
        }
        p {margin-bottom: 1px}</style>

    <h1>Sobre mim</h1>
    <style>.imagens {position: absolute; top: 40px; right: 30px;}         
    </style>
    <img class="imagens" src="https://raw.githubusercontent.com/elsavillon/site_automacao_grupo_5/main/static/fotoperfil.png" alt="Foto de Ana Carolina, uma mulher branca, de cabelos castanhos na altura do ombro e óculos de grau">

        <h2>Sou jornalista e produzo conteúdo para mídias digitais</h2>
        <text>Possuo graduação em <b>Jornalismo</b> pela <b>PUC-SP</b>, <b>pós-graduação</b>
            em Gestão da Comunicação em <br> <b>Mídias Digitais</b> pelo <b>Senac SP</b>,
            especialização em <b>Gênero e Sexualidade</b> pela <b>UERJ</b> e atualmente <br> 
            curso um <b>Master em Jornalismo de Dados, Automação e Data Storytelling</b> no <b>Insper</b>.</text>
        
        <h2>Tenho experiência com gestão, produção de reportagens e <br> criação de conteúdo para redes sociais</h2>
        <text>Já trabalhei na <b>Câmara Municipal de São Paulo</b>, na <b>Prefeitura Municipal de São Paulo</b>, <br> com <b>jornalismo sindical</b>, 
            cobertura sobre <b>direitos das mulheres</b> e no <b>BandNews TV</b>. <br> Hoje sou freelancer.</text>

        <p><button><a href="/curriculo">Currículo</a></button> <button><a href="/portfolio">Portfólio</a></button> </p>

    </div>
  </body>
</html>
"""
    
@app.route("/portfolio")
def portifolio ():
    return """
    <html>
    <html>
    <title> Portfólio</title>
          <div>        
            <style>
        body {
          font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif; 
          margin: 10px; 
          background-color: #f8f8f8; 
        }
        h1, h2, h3 {
          color: #8B0000; 
          margin-bottom: 10px; 
        }
        p {
          color: #232324; 
          margin-bottom: 10px; 
        }
        p {margin-bottom: 1px}

        .button-54 {
        font-family: "Open Sans", sans-serif;
        font-size: 16px;
        letter-spacing: 2px;
        text-decoration: none;
        text-transform: uppercase;
        color: #000;
        cursor: pointer;
        border: 3px solid;
        padding: 0.25em 0.5em;
        box-shadow: 1px 1px 0px 0px, 2px 2px 0px 0px, 3px 3px 0px 0px, 4px 4px 0px 0px, 5px 5px 0px 0px;
        position: relative;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
      }

      .button-54:active {
        box-shadow: 0px 0px 0px 0px;
        top: 5px;
        left: 5px;
      }

      @media (min-width: 768px) {
        .button-54 {
          padding: 0.25em 0.75em;
        }
      }
        </style>

    <body> 
    <h1>Portfólio</h1>
        <h2>Trabalhos recentes</h2>
            <img src="https://raw.githubusercontent.com/elsavillon/site_automacao_grupo_5/main/static//logos.jpg" alt="Régua de logotipos com os logos Bandnews, Fenametro Federação Nacional dos Metroviários, Mulheres do PSOL, Salonline, Sechat e Chicas Poderosas" width="440" height="180"><p>
        <h3>Conheça alguns projetos em que trabalhei e veja exemplos de materiais produzidos: </h3>
        <p>
        <h2>BandNews TV</h2> 
        <text>Desenvolvi o trabalho de Social Media com redação de textos, edição de imagens e vídeos para o canal. <br>
          Participei da cobertura das Eleições de 2022, e construí estratégias de cobertura para os debates eleitorais promovidos pelo Grupo Bandeirantes.</text>
        <title>bandnews</title>
        <p>
            <img src="https://raw.githubusercontent.com/elsavillon/site_automacao_grupo_5/main/static//bandnews1.png" alt="Print de publicação no facebook com cena do debate presidenciável de 2022 com os candidatos Lula à esquerda e Bolsonaro à direita. No rodapé direito, há janela com o intérprete de libras" width="400" height="250">
        </p>    
            <h2>Fenametro</h2> 
        <text>Produzo conteúdo para as redes sociais da entidade e reportagens sobre lutas sindicais. Desenvolvo estratégia, conteúdo, texto, edição de imagens e vídeos.</text>
        <p>
          <img src="https://raw.githubusercontent.com/elsavillon/site_automacao_grupo_5/main/static//fenametro.png" alt="Print do portal da Fenametro com manchete Greve do Metrô de MG exige revogação de leilão e garantia do trabalho dos metroviários">
        </p>
        <h3>Veja mais exemplos de reportagens:</h3>
        <text>  
        <a href="https://www.fenametro.org.br/noticias/encontro-internacional-de-metroviarios-amplia-unidade-da-luta-da-categoria.html">Encontro Internacional de metroviários amplia unidade da luta da categoria</a><br>
        <a href="https://www.fenametro.org.br/noticias/congresso-da-fenametro-organiza-categoria-para-combater-privatizacoes-bolsonaro-e-elege-nova-diretoria.html">Congresso da Fenametro organiza categoria para combater privatizações, Bolsonaro e elege nova diretoria</a>
        </text>  
          <h2>Mulheres do PSOL</h2> 
        <text>Produzo conteúdo para as redes sociais das Mulheres do PSOL nas temáticas de gênero, feminismo e direitos humanos. Desenvolvo estratégia, conteúdo, texto e orientação de design para produção de materiais gráficos.</text>
        <p>
          <img src="https://raw.githubusercontent.com/elsavillon/site_automacao_grupo_5/main/static//mulheresdopsol1.png" alt="Print de publicação no Instagram sobre os 91 anos da conquista do voto feminino no Brasil com foto de época com homens e mulheres em preto e branco">
        </p>   
        <h2>Chicas Poderosas</h2> 
        <text>Participei da equipe que coordenou o Laboratório de Histórias Poderosas Brasil, um projeto da Chicas Poderosas com o apoio da Open Society Foundations em 2021. Atuei na gestão de projetos e logística. O projeto teve como foco a produção de reportagens para abordar a crise do cuidado no Brasil enfrentada por milhões de mulheres durante a pandemia.</text>
        <a href="https://www.chicaspoderosas.org/noticias/historiasbrasil/">Conheça o projeto.</a>
        <p>
          <img src="https://raw.githubusercontent.com/elsavillon/site_automacao_grupo_5/main/static//chicas.png" alt="Print de matéria com o título Histórias sobre como as mulheres enfrentaram a crise do cuidado no Brasil".>
        </p>
        <br>
       </div>
       <p><button><a href="/">Voltar para a página inicial</a></button> <button><a href="/curriculo">Currículo</a></button> </p>
  </body>
</html>
"""

@app.route("/curriculo")
def curriculo ():
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
              color: #8B0000; 
              margin-bottom: 10px; 
            }
            p {
              color: #232324; 
              margin-bottom: 10px; 
            }
            p {margin-bottom: 1px}</style>
  <body><div class="linha-vertical"></div>
        <h3>Meu currículo e contatos</h3>
        <h1>ANA CAROLINA ANDRADE</h1>
        <h4>&nbsp;&nbsp;&nbsp;Jornalista e produtora de conteúdo para mídias digitais</h4>
        <div class="linha-vertical2"><h3 style="color: #8B0000;">&nbsp;&nbsp;&nbsp;FORMAÇÃO ACADÊMICA</h3></div>
        <p>2023 Master em Jornalismo de Dados, Automação e Data Storytelling - Insper (conclusão em 2024)<br>
            2020 Especialização em Gênero e Sexualidade - Universidade do Estado do Rio de Janeiro<br>
            2018 Pós-graduação em Gestão da Comunicação em Mídias Digitais - Senac São Paulo<br>
            2011 Graduação em Comunicação Social, habilitação Jornalismo - Pontifícia Universidade Católica de São Paulo <br>
            (PUC-SP)</p>

        <div class="linha-vertical2"><h3 style="color: #8B0000;">&nbsp;&nbsp;&nbsp;EXPERIÊNCIA PROFISSIONAL</h3></div>
        
        <p><h4>&nbsp;&nbsp;FREELANCER</h4><b>Jornalista e produtora de conteúdo para mídias digitais | Jan 2019 - atualmente</b><br>
            Produção de reportagens; redação e produção de materiais para sites e redes sociais como Instagram, Facebook e <br>
            X (Twitter);<br>
            Monitoramento e análise de redes; Cobertura de eventos nacionais e internacionais.<p>

        <p><h4>&nbsp;&nbsp;BANDNEWS TV</h4><b>Social Media | Jul 2022 - Jan 2023</b><br>
            Produção de conteúdo para as redes sociais do BandNews TV, do Grupo Bandeirantes de Comunicação.<p>

        <p><h4>&nbsp;&nbsp;FENAMETRO (FEDERAÇÃO NACIONAL DOS METROVIÁRIOS)</h4><b>Jornalista | Jul 2015 - Dez 2019</b><br>
            Produção de reportagens, edição do site da entidade; Redação e diagramação de<br>
            boletins impressos e digitais; Produção de conteúdo e gestão das redes sociais;<br>
            Cobertura de eventos nacionais e internacionais; Assessoria de imprensa<p>        

        <div class="linha-vertical2"><h3 style="color: #8B0000;">&nbsp;&nbsp;&nbsp;FORMAÇÃO COMPLEMENTAR</h3></div>

        <p>2020 Workshop Ferramentas Avançadas de Busca para Comunicadoras - Chicas Poderosas<br>
           2018 Curso de extensão “Fronteiras do Feminismo: pós-colonialismo, teorias e práticas PUC-SP. <br>
           2015 Curso de extensão “Fronteiras do Feminismo: pós-colonialismo, teorias e práticas latino-americanas” <br> PUC-SP.<p> 


            <title>contatos</title>
            <style>.imagens {position: absolute; top: 40px; right: 50px;}         
            </style>
            <img class="imagens" src="https://raw.githubusercontent.com/elsavillon/site_automacao_grupo_5/main/static/contatos_carol.jpg" alt="e-mail carol00andrade@gmail.com, telefone (11) 998655052, linkedin https://www.linkedin.com/in/carol00andrade, endereço Sumarezinho, São Paulo - SP">

            <title>contatos</title>
            <style>.imagens2 {position: absolute; top: 390px; right: 50px;}         
            </style>
            <img class="imagens2" src="https://raw.githubusercontent.com/elsavillon/site_automacao_grupo_5/main/static/qualificacoes_carol.jpg" alt="Imagem com as qualificações por tipo. Inglês (IELTS): fluente, espanhol (SIELE): fluente, francês: básico. Canva: avançado. Photoshop: intermediário. Indesign: avançado. Premiere: básico. Word: especialista. Excel: intermediário. Power Point: avançado. Wordpress: avançado.">
            
                        <p><button><a href="/">HOME</a></button> <button><a href="/portfolio">PORTIFOLIO</a></button> </p>

   </body>
</html>
"""






