from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guerreros.db'
db = SQLAlchemy(app)

class Guerrero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    vida = db.Column(db.Integer, nullable=False)
    fuerza = db.Column(db.Integer, nullable=False)

@app.route('/guerreros')
def listar_guerreros():
    with app.app_context():
        guerreros = Guerrero.query.all()
        return render_template('listar_guerreros.html', guerreros=guerreros)

@app.route('/guerreros/crear', methods=['GET', 'POST'])
def crear_guerrero():
    if request.method == 'POST':
        with app.app_context():
            nombre = request.form['nombre']
            vida = request.form['vida']
            fuerza = request.form['fuerza']
            guerrero = Guerrero(nombre=nombre, vida=vida, fuerza=fuerza)
            db.session.add(guerrero)
            db.session.commit()
            return redirect(url_for('listar_guerreros'))
    else:
        return render_template('crear_guerrero.html')

@app.route('/guerreros/<int:id>/editar', methods=['GET', 'POST'])
def editar_guerrero(id):
    guerrero = Guerrero.query.get_or_404(id)
    if request.method == 'POST':
        with app.app_context():
            guerrero.nombre = request.form['nombre']
            guerrero.vida = request.form['vida']
            guerrero.fuerza = request.form['fuerza']
            db.session.commit()
            return redirect(url_for('listar_guerreros'))
    else:
        return render_template('editar_guerrero.html', guerrero=guerrero)

@app.route('/guerreros/<int:id>/eliminar', methods=['POST'])
def eliminar_guerrero(id):
    with app.app_context():
        guerrero = Guerrero.query.get_or_404(id)
        db.session.delete(guerrero)
        db.session.commit()
        return redirect(url_for('listar_guerreros'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
