/*
USE sigest;
*/

/* CREACION TABLA ARTICULOS */

DROP TABLE IF EXISTS articulos CASCADE;

CREATE TABLE articulos
(
    id varchar(13),
    descripcion varchar(13),
    alto float,
    ancho float,
    largo float,
    texto varchar(200),
    CONSTRAINT articulo_key PRIMARY KEY(id)
);

/* CREACION TABLA DEPOSITOS */

DROP TABLE IF EXISTS depositos CASCADE;

CREATE TABLE depositos
(
    id varchar(13),
    descripcion varchar(60),
    texto varchar(200),
    CONSTRAINT deposito_key PRIMARY KEY(id)
);

/* CREACION TABLA STOCK */

DROP TABLE IF EXISTS stock CASCADE;

CREATE TABLE stock
(
    idArt varchar(13),
    idDep varchar(13),
    stock float,
    CONSTRAINT stock_key PRIMARY KEY(idArt, idDep),
    FOREIGN KEY (idArt) REFERENCES articulos(id),
    FOREIGN KEY (idDep) REFERENCES depositos(id)
);
