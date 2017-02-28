COPY provincias FROM '/tmp/cpa_csv/provincias.csv' DELIMITER ',' HEADER CSV;
COPY parajes FROM '/tmp/cpa_csv/parajes.csv' DELIMITER ',' HEADER CSV;
COPY cpa FROM '/tmp/cpa_csv/cpa.csv' DELIMITER ',' HEADER CSV;
COPY cp_1974 FROM '/tmp/cpa_csv/cp_1974.csv' DELIMITER ',' HEADER CSV;
COPY localidades FROM '/tmp/cpa_csv/localidades.csv' DELIMITER ',' HEADER CSV;
COPY tipos_camino FROM '/tmp/cpa_csv/tipos_camino.csv' DELIMITER ',' HEADER CSV;
COPY calles FROM '/tmp/cpa_csv/calles.csv' DELIMITER ',' HEADER CSV;
COPY alturas FROM '/tmp/cpa_csv/alturas.csv' DELIMITER ',' HEADER CSV;
