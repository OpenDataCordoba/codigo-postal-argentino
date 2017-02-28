CREATE TABLE provincias (
	codprov TEXT PRIMARY KEY,
	provincia TEXT
);

CREATE TABLE partidos (
	codpart INTEGER PRIMARY KEY,
	partido TEXT,
	provincia TEXT REFERENCES provincias (codprov)
);

CREATE TABLE localidad (
	codloc INTEGER,
	localidad TEXT,
	codpostal TEXT,
	partido TEXT,
	provincia TEXT REFERENCES provincias (codprov),
	codpart INTEGER REFERENCES partidos (codpart)
);

CREATE TABLE calles (
	codcalle INTEGER,
	tipocalle TEXT,
	nombrecalle TEXT,
	barrio TEXT,
	referencia TEXT,
	nombrealt TEXT,
	codloc INTEGER
);

CREATE TABLE alturas (
	codcalle INTEGER,
	desde INTEGER,
	hasta INTEGER,
	codpostal TEXT
);