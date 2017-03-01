SELECT calles.nombre_completo,
       alturas.desde,
       alturas.hasta,
       cpa.cpa,
       cp_1974.cod_postal
FROM alturas
JOIN cpa ON cpa.id=alturas.id_cpa
JOIN cp_1974 ON cp_1974.id=alturas.id_cp_1974
JOIN calles ON calles.id=alturas.id_calle
JOIN localidades ON localidades.id=calles.id_localidad
JOIN parajes ON parajes.id=localidades.id_paraje
JOIN provincias ON provincias.id=parajes.id_provincia
WHERE alturas.desde < 340
  AND alturas.hasta > 340
  AND mod(alturas.desde - 340, 2)=0
  AND calles.nombre_completo ILIKE '%BROWN%'
  AND localidades.nombre ILIKE '%CORDOBA%'
  AND parajes.nombre ILIKE '%CAPITAL%'
  AND provincias.nombre ILIKE '%CORDOBA%' LIMIT 10;

SELECT count(*)
FROM calles
JOIN localidades ON localidades.id=calles.id_localidad
JOIN parajes ON parajes.id=localidades.id_paraje
JOIN provincias ON provincias.id=parajes.id_provincia
WHERE calles.nombre_completo ILIKE '%BROWN%'
  AND localidades.nombre ILIKE '%CORDOBA%'
  AND parajes.nombre ILIKE '%CAPITAL%'
  AND provincias.nombre ILIKE '%CORDOBA%' LIMIT 10;

SELECT count(*)
FROM localidades
JOIN parajes ON parajes.id=localidades.id_paraje
JOIN provincias ON provincias.id=parajes.id_provincia
WHERE localidades.nombre ILIKE '%CORDOBA%'
  AND parajes.nombre ILIKE '%CAPITAL%'
  AND provincias.nombre ILIKE '%CORDOBA%' LIMIT 10;