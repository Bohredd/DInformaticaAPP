import sqlite3
import PySimpleGUI as sg

conn = sqlite3.connect('Servicos.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Servicos (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Código TEXT NOT NULL,
    Nome TEXT NOT NULL,
    Preço TEXT NOT NULL
);
""")

print('Conectado Servicos.DB!')