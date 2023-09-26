from flask import Flask, jsonify, request

app = Flask(__name__)

# json
materias = [
    {
      "id": 1,
      "nome": "Matemática",
      "material-didatico": [
        "Frações",
        "Divisibilidade",
        "Equações do 1º grau com uma variável",
        "Equações do 1º grau com duas variáveis",
        "Inequações do 1º grau",
        "Potenciação",
        "Radiciação",
        "Razões",
        "Proporções",
        "Algarismos romanos",
        "Grandezas proporcionais",
        "Regra de três",
        "Dízimas periódicas",
        "Porcentagem",
        "Geometria plana",
        "Medidas de superfície",
        "Medidas de volume",
        "Medidas de capacidade",
        "Medidas de massa",
        "Medidas de tempo",
        "Medidas de comprimento",
        "Equações do 2º grau",
        "Números decimais",
        "Médias",
        "Números racionais",
        "Tabelas",
        "Razões trigonométricas",
        "Semelhança de Polígonos",
        "Operações com números racionais decimais",
        "Quadriláteros",
        "Ângulos"
      ]
    },
    {
      "id": 2,
      "nome": "Português",
      "material-didatico": [
        "Frase, oração e período",
        "Termos da oração",
        "Termos essenciais da oração",
        "Termos integrantes da oração",
        "Termos acessórios da oração",
        "Verbos e Transitividade verbal",
        "Período composto por subordinação",
        "Período composto por coordenação",
        "Análise sintática",
        "Concordância verbal e nominal",
        "Regência verbal e nominal",
        "Partícula SE",
        "Estrutura e formação de palavras",
        "Substantivo",
        "Verbo",
        "Adjetivo",
        "Pronome",
        "Artigo",
        "Numeral",
        "Preposição",
        "Conjunção",
        "Interjeição",
        "Advérbio",
        "Pragmática",
        "Fonologia",
        "Ortogtafia",
        "Estilística"
      ]
    },
    {
      "id": 3,
      "nome": "Ciências",
      "material-didatico": [
        "Universo",
        "Sistema solar",
        "A lua",
        "O ar",
        "A Previsão do Tempo",
        "A Poluição do Ar",
        "A água",
        "O Planeta por Dentro e Por Fora",
        "Rochas, Minerais e Solo",
        "Terras para Agricultura",
        "Reciclagem",
        "Ecologia",
        "Cadeia alimentar",
        "Relações Ecológicas, Citologia",
        "Citoplasma",
        "O núcleo celular",
        "Química da vida",
        "Reprodução",
        "Embriologia",
        "Evolução",
        "Bioquímica",
        "Ecologia",
        "Morfologia vegetal",
        ""
      ]
    },
    {
      "id": 4,
      "nome": "Geografia",
      "material-didatico": [
        "Elementos do Universo",
        "Noções espaciais",
        "Cartografia e mapas",
        "Geologia",
        "Geomorfologia",
        "Solo",
        "Tempo e clima",
        "Vegetação",
        "Hidrografia",
        "Fenômenos naturais",
        "O Brasil",
        "Continentes",
        "A população e sua dinâmica espacial",
        "Processo de urbanização",
        "Atividades econômicas",
        "Extrativismo",
        "Geopolítica"
      ]
    },
    {
      "id": 5,
      "nome": "História",
      "material-didatico": [
        "Organizações populacionais",
        "Cidadania",
        "Organização dos três poderes",
        "Para que serve a história",
        "Tempo histórico",
        "Crenças, Cultos e religiões",
        "Os primeiros povos da América e os índios do Brasil",
        "Origens da humanidade",
        "História da humanidade",
        "Mundo",
        "Tipos de Guerras",
        "Formas de Governo",
        "As grandes civilizações",
        "Brasil",
        "Pre-História",
        "Idade Antiga",
        "Antiguidade oriental",
        "Idade Medieval",
        "A Transição do Feudalismo para o Capitalismo",
        "História do Capitalismo",
        "Idade moderna",
        "Idade contemporânea"
      ]
    },
]

tarefas = [
        {
            "id": 1,
            "matéria": "Matemática",
            "nome-tarefa": "Tarefa 1"
        },
        {
          "id": 2,
          "matéria": "Português",
          "nome-tarefa": "Tarefa 1"
        },
        {
          "id": 3,
          "matéria": "Ciências",
          "nome-tarefa": "Tarefa 1"
        },
        {
          "id": 4,
          "matéria": "Geografia",
          "nome-tarefa": "Tarefa 1"
        },
        {
          "id": 5,
          "matéria": "História",
          "nome-tarefa": "Tarefa 1"
        },
]

usuarios = [
        {
            "id": 1,
            "tipo": ["educador", "aluno"],
            "nome": "Bruno Paiva de Araújo",
            "email": "bruno_pa38@hotmail.com"
        },
      ]

# consultar (todos)
@app.route('/materias',methods=['GET'])
def obter_materias():
    return jsonify(materias)

@app.route('/tarefas',methods=['GET'])
def obter_tarefas():
    return jsonify(tarefas)

@app.route('/usuarios',methods=['GET'])
def obter_usuarios():
    return jsonify(usuarios)


# consultar (id)
@app.route('/materias/<int:id>',methods=['GET'])
def obter_materia_por_id(id):
    for materia in materias:
        if materia.get('id') == id:
            return jsonify(materia)
        
@app.route('/tarefas/<int:id>',methods=['GET'])
def obter_tarefa_por_id(id):
    for tarefa in tarefas:
        if tarefa.get('id') == id:
            return jsonify(tarefa)     
        
@app.route('/usuarios/<int:id>',methods=['GET'])
def obter_usuario_por_id(id):
    for usuario in usuarios:
        if usuario.get('id') == id:
            return jsonify(usuario)   

# criar (id)
@app.route('/materias',methods=['POST'])
def incluir_nova_materia():
    nova_materia = request.get_json()
    materias.append(nova_materia)
    return jsonify(materias)

@app.route('/tarefas',methods=['POST'])
def incluir_nova_tarefa():
    nova_tarefa = request.get_json()
    tarefas.append(nova_tarefa)
    return jsonify(tarefas)

@app.route('/usuarios',methods=['POST'])
def incluir_novo_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    return jsonify(usuarios)

# editar
@app.route('/materias/<int:id>',methods=['PUT'])
def editar_materias_por_id(id):
    materia_alterada = request.get_json()
    for indice,materia in enumerate(materias):
        if materia.get('id') == id:
            materias[indice].update(materia_alterada)
            return jsonify(materias[indice])
        
@app.route('/tarefas/<int:id>',methods=['PUT'])
def editar_tarefas_por_id(id):
    tarefa_alterada = request.get_json()
    for indice,tarefa in enumerate(tarefas):
        if tarefa.get('id') == id:
            tarefas[indice].update(tarefa_alterada)
            return jsonify(tarefas[indice])
        
@app.route('/usuarios/<int:id>',methods=['PUT'])
def editar_usuarios_por_id(id):
    usuario_alterado = request.get_json()
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            usuarios[indice].update(usuario_alterado)
            return jsonify(usuarios[indice])

# excluir
@app.route('/materias/<int:id>',methods=['DELETE'])
def excluir_materia(id):
    for indice, materia in enumerate(materias):
        if materia.get('id') == id:
            del materias[indice]
    return jsonify(materias)

@app.route('/tarefas/<int:id>',methods=['DELETE'])
def excluir_tarefa(id):
    for indice, tarefa in enumerate(tarefas):
        if tarefa.get('id') == id:
            del tarefas[indice]
    return jsonify(tarefas)

@app.route('/usuarios/<int:id>',methods=['DELETE'])
def excluir_usuario(id):
    for indice, usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            del usuarios[indice]
    return jsonify(usuarios)



app.run(port=5000,host='localhost',debug=True)


# Endpoint

    # materias
    # - localhost/materias (GET)
    # - localhost/materias/id (GET)
    # - localhost/materias/id (POST)
    # - localhost/materias/id (PUT)
    # - localhost/materias/id (DELETE)
    
    # tarefas
    # - localhost/tarefas (GET)
    # - localhost/tarefas/id (GET)
    # - localhost/tarefas/id (POST)
    # - localhost/tarefas/id (PUT)
    # - localhost/tarefas/id (DELETE)
    
    # usuarios
    # - localhost/usuarios (GET)
    # - localhost/usuarios/id (GET)
    # - localhost/usuarios/id (POST)
    # - localhost/usuarios/id (PUT)
    # - localhost/usuarios/id (DELETE)
    

# recursos

    # - materias
    # - tarefas
    # - usuarios