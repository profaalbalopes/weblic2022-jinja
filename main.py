from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', texto='Hj é quarta')

@app.route('/cardapio', defaults={"porcentagem": "0"})
@app.route('/cardapio/<porcentagem>')
def cardapio(porcentagem):
  return render_template('cardapio.html', promocao=True, porcentagem=porcentagem)

@app.route('/avaliacoes')
def avaliacoes():
  clientes = [
    {'nome': 'Alba', 'nota': 5},
    {'nome': 'Werllan', 'nota': 2}, 
    {'nome': 'Marcos', 'nota': 3}, 
    {'nome': 'Kleyton', 'nota': 5}
  ]
  return render_template('avaliacoes.html', clientes=clientes)
  
app.run(host='0.0.0.0', port=81)