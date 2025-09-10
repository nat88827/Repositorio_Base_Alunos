from flask import Flask, render_template,request,jsonify
from datetime import datetime
import json
import resend
resend.api_key = "re_HsYrekDK_AewxV8UqwN5tzbZqDGqpYTqF"


app=Flask(__name__)

with open('dados.json','r',encoding='utf-8')as arquivo:
    dados=json.load(arquivo)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        nome=request.form['Nome']
        email=request.form['Email']
        mensagem=request.form['Mensagem']

        dados_mensagem={
            'nome':nome,
            'email':email,
            'mensagem':mensagem,
            'data':f'{datetime.today()}'
        }

        dados.append(dados_mensagem)

        with open('dados.json','w',encoding='utf-8')as arquivo:
            json.dump(dados,arquivo,indent=4,ensure_ascii=False)

        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "origanatasha5@gmail.com",
        "subject": f"Solicitação de adoção-{nome}",
         "html": f"<p>Email:{email}<br>{mensagem}</p>"
})

        return render_template('index.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)