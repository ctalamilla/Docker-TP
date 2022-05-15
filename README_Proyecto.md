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

Para cumplir taxativamente con 

<img src="/img/ruta.png" alt="My cool logo"/>