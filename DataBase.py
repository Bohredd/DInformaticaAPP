import sqlite3
import PySimpleGUI as sg

conn = sqlite3.connect('Pedidos.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pedidos (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Cliente TEXT NOT NULL,
    Email TEXT NOT NULL,
    Telefone TEXT NOT NULL,
    Orçamento TEXT NOT NULL,
    Descrição TEXT NOT NULL,
    Status TEXT NOT NULL
);
""")

print('Conectado DataBase.DB!')