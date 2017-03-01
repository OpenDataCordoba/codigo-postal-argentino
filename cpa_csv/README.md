Varias normalizaciones se podrían hacer en esta cosa.


## Pares e impares

Aparentemente, la tabla de alturas tiene valores impares en `desde` y `hasta` para
indicar que solo refiere a valores de cierta paridad. Confirmado con
```
SELECT count(*)
FROM alturas
WHERE mod(desde,2)=1
  AND mod(hasta,2)=0;


SELECT count(*)
FROM alturas
WHERE mod(desde,2)=0
  AND mod(hasta,2)=1;

```
ambos con 0 resultados.