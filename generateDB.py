import connection
import dbCommands

def main():
    database = r"database.db"

    sql_create_usuario_table = """ 
        CREATE TABLE IF NOT EXISTS usuario (
            id integer PRIMARY KEY,
            name text NOT NULL,
            login text NOT NULL,
            senha text NOT NULL   
        ); 
    """

    sql_create_cliente_table = """ 
        CREATE TABLE IF NOT EXISTS cliente (
            id integer PRIMARY KEY,
            documento text,
            nome text,
            endereco text,
            genero text
        );
    """
    sql_create_produto_table = """  
        CREATE TABLE IF NOT EXISTS produto (
            id integer PRIMARY KEY,
            nome text,
            descricao text,
            valor double
        );
    """
    sql_create_venda_table = """  
        CREATE TABLE IF NOT EXISTS venda (
            id integer PRIMARY KEY,
            id_produto integer NOT NULL,
            id_cliente integer NOT NULL,
            qtd_produto integer NOT NULL,
            valor_total double NOT NULL,
            data_venda text,
            FOREIGN KEY (id_produto) REFERENCES produto (id),
            FOREIGN KEY (id_cliente) REFERENCES cliente (id)
        );
    """

    # create a database connection
    conn = connection.create_connection(database)

    # create tables
    if conn is not None:
        # create tables
        dbCommands.executeComands(conn, sql_create_usuario_table)
        dbCommands.executeComands(conn, sql_create_cliente_table)
        dbCommands.executeComands(conn, sql_create_produto_table)
        dbCommands.executeComands(conn, sql_create_venda_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()