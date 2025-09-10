from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
   
    return render_template('ex_2-2.html')


@app.route('/sobre')
def sobre():
   
    return('Olá,sou a Natasha,estudante de Python')


@app.route('/saudacao/<nome>')
def saudacao(nome):
   
    return(f'Olá {nome}, tudo bem?')

@app.route('/dobro/<int:numero>')
def dobro(numero):
   
    return(f'O dobro de {numero} é {2*numero}')
 


 
if __name__=='__main__':
    app.run(debug=True)