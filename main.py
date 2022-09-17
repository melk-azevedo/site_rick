from flask import Flask, render_template

app = Flask(__name__)


# Route -> Diretório
# Função -> é o que será exibido na page
@app.route('/')
def homepage():
    return render_template('homepage.html')


# Colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)
