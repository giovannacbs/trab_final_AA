# Necessário rodar apenas uma vez

import requests

token = "TELEGRAM_BOT_TOKEN"
url = "https://trab-final-aa.onrender.com/mensagem"
dados = {"url": url}
resposta = requests.post(f"https://api.telegram.org/bot{token}/setWebhook", data=dados)
print(resposta.json())

