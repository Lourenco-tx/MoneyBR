import sqlite3
conn = sqlite3.connect('moneybr.db')
cursor = conn.cursor()
cursor.execute('''
    INSERT INTO transacoes (data, favorecido, categoria_id, subcategoria_id, descricao, tipo_cd, valor)
    VALUES ('2023-10-27', 'Teste de Sistema', 1, 1, 'Compra inicial', 0, 50.00)
''')
conn.commit()
conn.close()