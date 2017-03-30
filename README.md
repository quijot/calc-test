# calc-test

Pruebas de exactitud para las correcciones de la [calculadora](http://www.fceia.unr.edu.ar/gps/calc/).

## Uso

0. Clonar este repositorio

        $ git clone https://github.com/quijot/calc-test.git

1. Completar en el archivo `coord.xyz` con las [coordenadas cartesianas geocéntricas POSGAR07 oficiales publicadas por IGN de cada Estación Permanente](http://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Mapa) que se quiera incluir en el procesamiento.

2. Ejecutar el script:

        $ python graph.py

3. Buscar las gráficas en el directorio `plot`
