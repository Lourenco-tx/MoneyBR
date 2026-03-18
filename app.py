from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)


def conectar():
    # Certifique-se de que o caminho do banco está correto
    conn = sqlite3.connect('moneybr.db')
    conn.row_factory = sqlite3.Row  # ESSENCIAL: transforma a linha em um "dicionário"
    return conn

@app.route('/')
def index():
    # O Flask vai procurar esse arquivo dentro da pasta /templates
    return render_template('homepage.html')


@app.route('/api/transacoes', methods=['GET'])
# CORREÇÃO DA FUNÇÃO:
def listar_transacoes():
    # 1. Chamamos a função para criar a conexão 'conn' aqui dentro
    conexao = conectar()

    # 2. Agora sim podemos criar o cursor
    cursor = conexao.cursor()

    # 3. Fazemos a consulta (exemplo para o MoneyBr)
    cursor.execute("SELECT * FROM transacoes")
    resultados = cursor.fetchall()

    # 4. Fechamos a conexão para não travar o banco
    conexao.close()

    return [dict(row) for row in resultados]


# Exemplo da rota de inserção para os novos campos
@app.route('/api/transacoes/inserir', methods=['POST'])
def inserir():
    dados = request.json
    conn = conectar()
    cursor = conn.cursor()

    sql = '''INSERT INTO transacoes (data, favorecido, categoria_id, subcategoria_id, descricao, tipo_cd, valor)
             VALUES (?, ?, ?, ?, ?, ?, ?)'''

    cursor.execute(sql, (
        dados['data'], dados['favorecido'], dados['categoria_id'],
        dados['subcategoria_id'], dados['descricao'], dados['tipo_cd'], dados['valor']
    ))

    conn.commit()
    conn.close()
    return jsonify({"status": "sucesso"}), 201


@app.route('/api/transacoes/atualizar', methods=['POST'])
def atualizar():
    dados = request.json
    id_registro = dados.get('id')

    if not id_registro:
        return jsonify({"erro": "ID não fornecido"}), 400

    conn = sqlite3.connect('moneybr.db')
    cursor = conn.cursor()

    # O SQL para atualizar os dados baseados no ID
    sql = '''
          UPDATE transacoes
          SET data            = ?, \
              favorecido      = ?, \
              categoria_id    = ?,
              subcategoria_id = ?, \
              descricao       = ?, \
              tipo_cd         = ?, \
              valor           = ?
          WHERE id = ? \
          '''

    valores = (
        dados['data'],
        dados['favorecido'],
        dados['categoria_id'],
        dados['subcategoria_id'],
        dados['descricao'],
        dados['tipo_cd'],
        dados['valor'],
        id_registro  # O ID vai no WHERE
    )

    cursor.execute(sql, valores)
    conn.commit()
    conn.close()

    return jsonify({"status": "sucesso"}), 200


if __name__ == '__main__':
    app.run(debug=True)

