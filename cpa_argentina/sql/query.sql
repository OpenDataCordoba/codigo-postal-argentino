SELECT *
FROM provincias
WHERE provincia ILIKE '%CORDOBA%';


SELECT *
FROM provincias
JOIN partidos ON partidos.provincia=provincias.codprov
WHERE provincias.provincia ILIKE '%CORDOBA%';


SELECT *
FROM provincias
JOIN partidos ON partidos.provincia=provincias.codprov
WHERE provincias.provincia ILIKE '%CORDOBA%'
  AND partidos.partido ILIKE '%CAPITAL%';


SELECT *
FROM provincias
JOIN partidos ON partidos.provincia=provincias.codprov
JOIN localidad ON localidad.codpart=partidos.codpart
WHERE provincias.provincia ILIKE '%CORDOBA%'
  AND partidos.partido ILIKE '%CAPITAL%'
  AND localidad.localidad ILIKE '%CORDOBA%';


SELECT calles.*
FROM provincias
JOIN partidos ON partidos.provincia=provincias.codprov
JOIN localidad ON localidad.codpart=partidos.codpart
JOIN calles ON calles.codloc=localidad.codloc
WHERE provincias.provincia ILIKE '%CORDOBA%'
  AND partidos.partido ILIKE '%CAPITAL%'
  AND localidad.localidad ILIKE '%CORDOBA%';


SELECT calles.*
FROM provincias
JOIN partidos ON partidos.provincia=provincias.codprov
JOIN localidad ON localidad.codpart=partidos.codpart
JOIN calles ON calles.codloc=localidad.codloc
WHERE provincias.provincia ILIKE '%CORDOBA%'
  AND partidos.partido ILIKE '%CAPITAL%'
  AND localidad.localidad ILIKE '%CORDOBA%'
  AND calles.nombrealt ILIKE '%BROWN%';


SELECT alturas.*
FROM provincias
JOIN partidos ON partidos.provincia=provincias.codprov
JOIN localidad ON localidad.codpart=partidos.codpart
JOIN calles ON calles.codloc=localidad.codloc
JOIN alturas ON alturas.codcalle=calles.codcalle
WHERE provincias.provincia ILIKE '%CORDOBA%'
  AND partidos.partido ILIKE '%CAPITAL%'
  AND localidad.localidad ILIKE '%CORDOBA%'
  AND calles.nombrealt ILIKE '%BROWN%';


SELECT count(*)
FROM provincias
JOIN partidos ON partidos.provincia=provincias.codprov
JOIN localidad ON localidad.codpart=partidos.codpart
JOIN calles ON calles.codloc=localidad.codloc
JOIN alturas ON alturas.codcalle=calles.codcalle
WHERE substring(alturas.codpostal,1,1) != provincias.codprov;

