docker build -t pythonitba .
docker-compose up -d
docker run -d --name itba  pythonitba sleep 1000
docker network connect tpf-foundations-ctalamilla_default itba 
docker exec -it itba bash -c "cd /filltables;python3 filltables.py"     
