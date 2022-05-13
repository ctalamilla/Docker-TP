docker build -t pythonitba .
docker-compose up -d
datapath=$(readlink -f data/datosDelitos.csv)
docker run -d --name itba -v $datapath:/datain/datosDelitos.csv pythonitba sleep 1000
docker network connect tpf-foundations-ctalamilla_default itba 
docker exec -it itba bash -c "cd /filltables;python3 filltables.py"     
