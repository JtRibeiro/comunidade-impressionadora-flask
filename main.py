from flask import  Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('contato.html')

@app.route("/contato")
def home():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html')


if __name__ == '__main__':
    app.run(debug=True)