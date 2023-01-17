from flask import Flask, redirect, url_for, request, render_template
import requests


imagem = f'http://127.0.0.1:8000/'
app = Flask(__name__)
@app.route('/')
def index():
    print(imagem)
    return render_template('index.html', imagem=imagem) 



@app.route('/numero')
def solicitado():
    global imagem
    argumentos = request.args.to_dict()
    numero = argumentos['numero']
    imagem = requests.get(f'http://127.0.0.1:8080/read_numero/{numero}')
    nome = imagem.json()
    nome = nome[0][3]
    imagem = f'http://127.0.0.1:8000/{nome}'
    return redirect('/')
    #return render_template('index.html', imagem=imagem) 


if __name__ == '__main__':
    app.run(app.run(port=8040, host='0.0.0.0', debug=True))