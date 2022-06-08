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
  clientes = ['Alba', 'Werllan', 'Marcos', 'Kleyton']
  return render_template('avaliacoes.html', clientes=clientes)
  
app.run(host='0.0.0.0', port=81)