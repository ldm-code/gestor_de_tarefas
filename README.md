# Gestor de Tarefas

Este é um projeto básico em Flask, criado para praticar:
- Framework **Flask** para desenvolvimento web em Python;
- Persistência de dados em **JSON** (sem uso de banco de dados relacional);
- Estruturação de **templates HTML** (com **Jinja2**);
- **Hash de senhas** com `werkzeug.security`.

---

##  Estrutura do Projeto

- gestor_de_tarefas/
- ├── dados/
- │ ├── tarefas.json
- │ └── login.json
- ├── static/
- ├ └── css/
- │ ├── login.css
- │ ├── tarefa.css
- │└── add.css
- ├── templates/
- │ ├── login.html
- │ ├── tarefa.html
- │ └── add.html
- ├── manage.py
- └── README.md

- **dados/**  
  Contém os arquivos JSON onde os dados de login e tarefas são armazenados.

- **templates/**  
  Armazena os arquivos HTML que o Flask renderiza nas diferentes rotas. 

- **manage.py**  
  Arquivo principal que executa o servidor Flask e define as rotas da aplicação.

---

##  Funcionalidades

1. **Login / Registro de usuário**  
   Quando um usuário faz login, o sistema:
   - Cria um hash da senha com `generate_password_hash`.
   - Salva os dados do usuário em `dados/login.json`.
   *(Observação: atualmente ele **sempre cria um novo registro na hora do login**, mesmo que já exista, o que pode ser ajustado.)*

2. **Visualização de tarefas**  
   A rota `/t` carrega as tarefas salvas em `dados/tarefas.json` e as exibe por meio do template `add.html`.

3. **Adição de tarefas**  
   Ao acessar `/add` via POST, a aplicação:
   - Recebe os dados da tarefa (título e descrição) via formulário;
   - Salva a tarefa no arquivo JSON (`dados/tarefas.json`);
   - Renderiza novamente a página com a lista atualizada.

---


