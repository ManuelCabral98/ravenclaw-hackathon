from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


class Funcionarios(db.Model):
    rowid = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(200), nullable=False)
    birthdate = db.Column(db.Integer)
    dni = db.Column(db.Integer)
    email = db.Column(db.Text)

    def __init__(self, name, birthdate, dni, email):
        self.name = name
        self.birthdate = birthdate
        self.dni = dni
        self.email = email

@app.route("/form", methods= ["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        birthdate = request.form["birthdate"]
        dni = request.form["dni"]
        email = request.form["email"]

        funcionario = Funcionarios(name, birthdate, dni, email)
        db.session.add(funcionario)
        db.session.commit()
        return "Se envio el formulario"
    return render_template('formulario.html')

with app.app_context():
    db.create_all(bind_key='__all__')

if __name__ =="__main__":
    app.run(debug=True)