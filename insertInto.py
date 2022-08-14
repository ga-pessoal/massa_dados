import connection

data = [
    (1, 'teste1', 'teste1', '12345'),
    (2, 'teste2', 'teste2', '12345'),
    (3, 'teste3', 'teste3', '12345'),
]

def main():
    database = r"database.db"
    # create a database connection
    con = connection.create_connection(database)
    cur = con.cursor()

    if con is not None:
        # Insert data
        cur.executemany('INSERT INTO usuario VALUES(?, ?, ?, ?)', data)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()