import sqlite3
import pandas as pd
from sqlite_utils import Database


class DBstorage():
    def __init__(self):
        self.con = sqlite3.connect("links.db")
        self.setup_tables()
        

    #creating tables
    def setup_tables(self):
        cur = self.con.cursor()
        results_table = r"""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY,
                title TEXT,
                query TEXT,
                rank INTEGER,
                link TEXT,
                snippet TEXT,
                html TEXT, 
                created DATETIME,
                relevance INTEGER,
                UNIQUE(query, link)
            );
        """
        users_table = r"""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                email TEXT,
                UNIQUE(username)
            );
        """
        cur.execute(results_table)
        cur.execute(users_table)
        self.con.commit()
        #self.con.close()

    
    def query_results(self, query):
        df = pd.read_sql(f"select * from results where query='{query}'order by rank asc;", self.con)
        return df

    def find_user(self, username):
        cur = self.con.cursor()
        try:
            res = cur.execute("select * from users where username = :username limit 1;", {'username': username})
            return res.fetchone()
        except sqlite3.IntegrityError:
            pass
        user = cur.fetchone()
        cur.close()
        return user

    def insert_row(self, values):
        cur = self.con.cursor()
        try:
            cur.execute('INSERT INTO results (query, rank, link, title, snippet, html, created) VALUES(?,?,?,?,?,?,?)',values)
            self.con.commit()
        except sqlite3.IntegrityError:
            pass
        cur.close()

    #relevence score can manually indicate which results were relevant, store this data.
    #After enough searches use machine learning to filter our results
    def update_relevance(self, query, link, relevance):
        cur = self.con.cursor()
        cur.execute('UPDATE results SET relevance=? WHERE query=? AND link=?',[relevance, query, link])
        self.con.commit()
        cur.close()

    
    def register_user(self, username, password):
        try:
            cur = self.con.cursor()
            cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            self.con.commit()
        except sqlite3.IntegrityError:
            pass
        cur.close()
        
    
                        
    
        

    