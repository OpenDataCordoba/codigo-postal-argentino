COPY provincias FROM '/tmp/cpa_argentina/provincias.CSV' DELIMITER ';' HEADER CSV;
COPY partidos FROM '/tmp/cpa_argentina/partidos.CSV' DELIMITER ';' HEADER CSV;
COPY localidad FROM '/tmp/cpa_argentina/localidad.CSV' DELIMITER ';' HEADER CSV;
COPY calles FROM '/tmp/cpa_argentina/calles.CSV' DELIMITER ';' HEADER CSV;
COPY alturas FROM '/tmp/cpa_argentina/alturas.CSV' DELIMITER ';' HEADER CSV;