import sqlite3
import json
from models.Document import DocumentResponse


def conectar_banco():
    conn = sqlite3.connect('documentos.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Document (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        tags TEXT,
        signer TEXT,
        summary TEXT,
        translation TEXT
    )
    ''')
    conn.commit()
    return conn, cursor


def inserir_documento(cursor, conn, document: DocumentResponse):
    tags_json = json.dumps(document.tags)
    cursor.execute('''
    INSERT INTO Document (title, tags, signer, summary, translation)
    VALUES (?, ?, ?, ?, ?)
    ''', (document.title, tags_json, document.signer, document.summary, document.translation))
    conn.commit()
    print("Documento inserido com sucesso!")
