from flask import Flask, request, render_template
from werkzeug.security import generate_password_hash,check_password_hash
import json
import os
app=Flask(__name__)
def carregar_tarefas():
    if os.path.exists('dados/tarefas.json'):
        with open('dados/tarefas.json', 'r', encoding='utf-8') as arq:
            return json.load(arq)
    else:
        return []
def salvar_tarefa(tarefas):
    with open("dados/tarefas.json","w",encoding="utf-8") as arq:
        json.dump(tarefas,arq,indent=4,ensure_ascii=False)
@app.route("/")
def inicio():
    return render_template ('login.html')
@app.route('/log',methods=['POST'])
def login():
    nome=request.form.get('nome')
    senha=request.form.get('senha')
    senha_cripto=generate_password_hash(senha)
    check_password_hash(senha_cripto,senha)
    dados={"usuario":nome,
           "senha":senha_cripto}
    try:
        with open ("dados/login.json","r") as arq:
           dados_login= json.load(arq)
    except FileNotFoundError:
        dados_login=[]
    dados_login.append(dados)
    with open('dados/login.json',"w") as arq:
        json.dump(dados_login,arq,indent=4)
    return render_template('tarefa.html')
@app.route('/t',methods=['GET'])
def logado():
    tarefas=carregar_tarefas()
    return render_template('add.html',tarefas=tarefas)
@app.route('/add',methods=['POST'])
def add_tarefa():
    tarefa=request.form.get('tarefa')
    descricao=request.form.get('descricao')
    tarefa_criada={'tarefa':tarefa,
                   'descricao':descricao}
    nova_tarefa=carregar_tarefas()
    
    nova_tarefa.append(tarefa_criada)
    salvar_tarefa(nova_tarefa)
    return render_template('tarefa.html',tarefas=nova_tarefa)
if __name__=="__main__":
    app.run(debug=True)