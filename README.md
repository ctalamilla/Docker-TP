# Trabajo Práctico Final Foundations
## ITBA - Cloud Data Engineering

### Dataset Elegido. 

El set de datos elegido fue el de delitos de la ciudad de buenos aires. 

Source: https://data.buenosaires.gob.ar/dataset/delitos

datasets:
2016: https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-justicia-y-seguridad/delitos/delitos_2016.csv

2017: https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-justicia-y-seguridad/delitos/delitos_2017.csv

2018: https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-justicia-y-seguridad/delitos/delitos_2018.csv

2019: https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-justicia-y-seguridad/delitos/delitos_2019.csv

2020: https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-justicia-y-seguridad/delitos/delitos_2020.csv

2021: https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-justicia-y-seguridad/delitos/delitos_2021.csv

### Preguntas a responder.
1. Cual es el Barrio con mayor incidencia de delitos. Indicador promedio de delitos mensual. 
2. Durante la pandemia el numero de delitos semanales disminuyo? En que magnitud? Analisis en el Top 5 de barrios inseguros de la pregunta 1.
3. Todos los dias de la semana tienen el mayor riesgo en cuando a la incidencia de delitos?
4. Cuales son las horas del dia con mayor numero de delitos?

### Resolución 
Para la ejecución de este repositorio es necesario tener instalado y ejecutandose Docker Desktop.

Ejecutar el siguiente comando para la iniciar la aplicación. 
~~~
bash init.sh
~~~

El contenido del iniciador se detalla a continuación:
~~~
docker build -t pythonitba .
docker-compose up -d
datapath=$(readlink -f data/datosDelitos.csv)
reportpath=$(readlink -f report)
docker run -d --name itba \
             -v $datapath:/datain/datosDelitos.csv \
             --network=network_app \
             -v $reportpath:/report \
             pythonitba sleep 1000
docker exec -it itba bash -c "cd /filltables;python3 filltables.py"
docker exec -it itba bash -c "cd /filltables;python3 report.py > /report/report.txt"
cat report/report.txt   
bash end.sh
~~~

Para cumplir taxativamente con las consignas se procedio a lo siguiente:
1. Crear un ```docker-compose.yml``` con la imagen de Postgres SQL versión 12.7. En el servicio ejecutado por instrucciones del compose se procedió a:
    - Nombrar al contenedor.
    - Configurar los puertos de comunicación
    - Crear un volumen para insertar un sql file para la creación de tablas.
    - Crear un segundo volumen para pasar al contenedor un ```script bash``` que ejecute dentro del contenedor el sql file nombrado en el punto anterior.

2. Crear un archivo ```Dockerfile``` para la generación de una imagen de un contenedor con Python 3 y las dependencias y librerias necesarias para:
    - Leer un archivo ```.csv``` que contiene los datos a insertar en la base de datos postgres. El mismo se encuentra alojado en la carpeta ```data```.
    - Generar la conexión hacia el contenedor con psql.
    - Contener un ```script Python```para que una vez generada la conexión pueble la base de datos en el contenedor con psql.
    - Contener un ```script Python```para realizar consultas a la base de datos y generar un reporte en formato texto.

3. La generación del reporte se hizo dentro del contenedor con python pero se realizo un montaje de volumenes para que una vez realizado el reporte el mismo tambien se ubique en la carpeta ```report``` de la carpeta de trabajo.
4. Finalmente se hizo uso de un ultimo ```script bash```para cerrar y terminar los contenedores.


### Rutas y archivos de la carpeta de trabajo
<img src="/img/ruta.png" alt="ruta de trabajo" width="500"/>