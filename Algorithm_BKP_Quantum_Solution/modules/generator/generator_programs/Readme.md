algoritmos para generar instancias de prueba

fuente:
http://hjemmesider.diku.dk/~pisinger/codes.html

comando para compilar cada programa:
>> cc -O0 program_name.c -lm [-o out_program_name]
[] opcionales 

FLAGS

cc -> indica el compilador

-o name -> nombre archivo de salida, si o se esecifica se tomara el nombre a.out, b.out, ..., zz.out ascendentemente en orden alfabetico.

-lm -> agrega la biblioteca indicada a la lista de bibliotecas que se vincularán. Por ejemplo, si está usando funciones de la biblioteca matemática de C.

-O0 -> Crea un ejecutable optimizado. El compilador analizará su código y, si conoce algún truco inteligente para acelerar el rendimiento, lo implementará en el código de bytes.



