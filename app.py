from flask import Flask, redirect, url_for, request, render_template
import requests

app = Flask(__name__)
@app.route('/')
def index():
    return redirect(url_for('static',filename='index.html'))

@app.route('/numero')
def solicitado():
    argumentos = request.args.to_dict()
    numero = argumentos['numero']
    imagem = requests.get(f'http://127.0.0.1:8080/read_numero/{numero}')
    nome = imagem.json()
    nome = nome[0][3]
    imagem = requests.get(f'http://127.0.0.1:8000/{nome}')
    #return redirect('/')
    return redirect(url_for('static',filename='index.html'))


if __name__ == '__main__':
    app.run(app.run(port=8040, host='0.0.0.0', debug=True))