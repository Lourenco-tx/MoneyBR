from flask import Flask, render_template
app = Flask(__name__)

lista_usuarios = ['Lourenço', 'Flávio', 'Alam', 'Victor']

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)

@app.route('/sobreMoneyBr')
def sobreMoneyBr():
    return render_template("sobreMoneyBr.html")

if __name__ == '__main__':
    app.run(debug=True)


