#Ver na documentacao 
#https://www.sqlitetutorial.net/sqlite-python/creating-tables/

CREATE TABLE IF NOT EXISTS usuario {
    id integer PRIMARY KEY,
    name text NOT NULL,
    login text NOT NULL,
    senha text NOT NULL   
}

CREATE TABLE IF NOT EXISTS cliente {
    id integer PRIMARY KEY,
    documento text,
    nome text,
    endereco text,
    genero text
}

    CREATE TABLE IF NOT EXISTS produto {
        id integer PRIMARY KEY,
        nome text,
        descricao text,
        valor double,
    }

    CREATE TABLE IF NOT EXISTS venda {
        id integer PRIMARY KEY,
        id_produto integer NOT NULL,
        id_cliente integer NOT NULL,
        qtd_produto integer NOT NULL,
        valor_total double NOT NULL
        data_venda text,
        FOREIGN KEY (id_produto) REFERENCES produto (id),
        FOREIGN KEY (id_cliente) REFERENCES cliente (id),
    }