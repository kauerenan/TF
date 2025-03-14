from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="alunosdb",
        user="postgres",
        password="password"
    )
    return conn

@app.route('/alunos', methods=['GET'])
def get_alunos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()
    conn.close()
    return jsonify({'alunos': alunos})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
