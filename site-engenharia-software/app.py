from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faculdades')
def faculdades():
    return render_template('faculdades.html')

@app.route('/jornada')
def jornada():
    return render_template('jornada.html')

@app.route('/idiomas')
def idiomas():
    return render_template('idiomas.html')

@app.route('/cargos')
def cargos():
    return render_template('cargos.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

if __name__ == '__main__':
    app.run(debug=True)
