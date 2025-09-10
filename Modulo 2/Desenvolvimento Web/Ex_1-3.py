from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
   
    return('Olá Mundo')


@app.route('/sobre')
def sobre():
   
    return('Olá,sou a Natasha,estudante de Python')
 

@app.route('/saudacao/<nome>')
def saudacao(nome):
   
    return(f'Olá {nome}, tudo bem?')
 


if __name__=='__main__':
    app.run(debug=True)