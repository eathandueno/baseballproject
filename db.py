import sqlite3

DATABASE = 'baseball_team_manager.db'

def connect():
    return sqlite3.connect(DATABASE)

def read_all_players():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Player ORDER BY batOrder")
    players = cursor.fetchall()
    conn.close()
    return players

def add_player(batOrder, firstName, lastName, position, atBats, hits):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits) VALUES (?, ?, ?, ?, ?, ?)",
                   (batOrder, firstName, lastName, position, atBats, hits))
    conn.commit()
    conn.close()

def delete_player(playerID):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Player WHERE playerID = ?", (playerID,))
    conn.commit()
    conn.close()

def update_player(playerID, position, atBats, hits):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE Player SET position = ?, atBats = ?, hits = ? WHERE playerID = ?",
                   (position, atBats, hits, playerID))
    conn.commit()
    conn.close()

def update_bat_order(playerID, batOrder):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE Player SET batOrder = ? WHERE playerID = ?", (batOrder, playerID))
    conn.commit()
    conn.close()
