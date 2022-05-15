docker build -t pythonitba .
docker-compose up -d
datapath=$(readlink -f data/datosDelitos.csv)
reportpath=$(readlink -f report)
docker run -d --name itba \
             -v $datapath:/datain/datosDelitos.csv \
             --network=network_app \
             -v $reportpath:/report \
             pythonitba sleep 1000
#docker network connect network_app itba 
docker exec -it itba bash -c "cd /filltables;python3 filltables.py"
docker exec -it itba bash -c "cd /filltables;python3 report.py > /report/report.txt"
cat report/report.txt   
bash end.sh