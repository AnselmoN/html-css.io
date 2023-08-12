from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de membros para simular um banco de dados
membros = [
    {'nome': 'João', 'cargo': 'Farmacêutico'},
    {'nome': 'Maria', 'cargo': 'Enfermeira'},
    {'nome': 'Pedro', 'cargo': 'Médico'}
]

# Página inicial
@app.route('/')
def index():
    return render_template('index.html', membros=membros)

# Página do perfil de cada membro
@app.route('/perfil/<int:id>')
def perfil(id):
    membro = membros[id]
    return render_template('perfil.html', membro=membro)

if __name__ == '__main__':
    app.run(debug=True)


