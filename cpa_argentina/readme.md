Limpie alturas.CSV quitando las ultimas filas nulas con
```
grep -v "\"\";" alturas_old.CSV > alturas.CSV
```

Limpiar localidades
```
awk '!v[$1]++' /tmp/cpa_argentina/localidad.CSV > /tmp/cpa_argentina/localidad_uniq.CSV
```

## Pares e impares

Aparentemente, la tabla de alturas tiene valores impares en `desde` y `hasta` para
indicar que solo refiere a valores de cierta paridad. Confirmado con
```
SELECT count(*)
FROM alturas
WHERE mod(desde,2)=1
  AND mod(hasta,2)=0;
```
Tiene 31698 resultados que corresponden todos a filas en las que desde=1 y hasta=2

```
SELECT count(*)
FROM alturas
WHERE mod(desde,2)=0
  AND mod(hasta,2)=1;

```
da 0 resultados.


# Redundancia

La tabla de alturas tiene una columna de codigo postal. Este string comienza con el codigo de la provincia y
es redundante ya que no hay filas para las que no pueda deducirse
```
SELECT count(*)
FROM provincias
JOIN partidos ON partidos.provincia=provincias.codprov
JOIN localidad ON localidad.codpart=partidos.codpart
JOIN calles ON calles.codloc=localidad.codloc
JOIN alturas ON alturas.codcalle=calles.codcalle
WHERE substring(alturas.codpostal,1,1) != provincias.codprov;
```
resulta en 0.


# Codigos postales

Todas las filas de alturas tienen length(codpostal) = 8

Todos son distintos ya que `select count(distinct(codpostal)) from alturas;` da igual a la cantidad de filas.

Solo hay 2764 valores distintos para el codigo de area postal (los 4 digitos).
```
select count(distinct(substring(codpostal,2,4))) from alturas;
```

# Buscar

```
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

```