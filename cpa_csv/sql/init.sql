CREATE TABLE provincias (
	id INTEGER PRIMARY KEY,
	nombre TEXT
);


CREATE TABLE parajes (
	id INTEGER PRIMARY KEY,
	id_provincia INTEGER REFERENCES provincias (id) MATCH SIMPLE,
	nombre TEXT
	);


CREATE TABLE tipos_camino (
	id INTEGER PRIMARY KEY,
	nombre TEXT
	);


CREATE TABLE cpa (
	id INTEGER PRIMARY KEY,
	cpa TEXT
	);


CREATE TABLE cp_1974 (
	id INTEGER PRIMARY KEY,
	cod_postal INTEGER
	);


CREATE TABLE localidades (
	id INTEGER PRIMARY KEY,
	id_paraje INTEGER REFERENCES parajes (id) MATCH SIMPLE,
	nombre TEXT,
	id_cpa INTEGER REFERENCES cpa (id) MATCH SIMPLE,
	id_cp_1974 INTEGER REFERENCES cp_1974 (id) MATCH SIMPLE
	);


CREATE TABLE calles (
	id INTEGER PRIMARY KEY,
	id_localidad INTEGER REFERENCES localidades (id) MATCH SIMPLE,
	nombre_completo TEXT,
	apellido TEXT,
	nombre TEXT,
	titulo TEXT,
	nombre_abreviado TEXT,
	barrio TEXT,
	punto_cardinal TEXT,
	id_tipo_camino INTEGER REFERENCES tipos_camino (id) MATCH SIMPLE
	);


CREATE TABLE alturas (
	id INTEGER PRIMARY KEY,
	id_calle INTEGER REFERENCES calles (id) MATCH SIMPLE,
	desde INTEGER, hasta INTEGER,
	id_cpa INTEGER REFERENCES cpa (id) MATCH SIMPLE,
	id_cp_1974 INTEGER REFERENCES cp_1974 (id) MATCH SIMPLE
	);


CREATE INDEX localidades_nombre_idx ON localidades (nombre ASC);


CREATE INDEX parajes_nombre_idx ON parajes (nombre ASC);


CREATE INDEX provincias_nombre_idx ON provincias (nombre ASC);

