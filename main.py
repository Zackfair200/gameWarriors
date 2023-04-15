from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    nombre = 'Juan'
    return render_template('hola.html', nombre=nombre)

@app.route("/lucha")
def hello():
    return 'Hello, World'

@app.route('/vida/<int:vida>')
def barra_de_vida(vida):
    if vida >= 80:
        color = 'verde'
    elif vida >= 30:
        color = 'amarillo'
    else:
        color = 'rojo'
    return render_template('barraDeVida.html', vida=vida, color=color)

if __name__ == '__main__':
    app.run(debug=True)