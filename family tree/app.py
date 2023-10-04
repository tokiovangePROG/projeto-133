# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "otávio" # escreva seu nome
    idade = "13" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")

# defina a rota para a página da mãe
@app.route("/mãe")

# defina a rota para a página do amigo
@app.route("/eu")

# adicione outras rotas, se você quiser
@app.route("/amigo")



# execute o arquivo
if __name__  ==  '__main__':    
    app.run(debug=True)
