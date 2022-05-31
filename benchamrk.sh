# usage: bash benchmark.sh redis

dstat -lcmdrsyTt --full --out $1/dtat-result-orginal.csv &
dstas_pid=$!
docker-compose -f $1/docker-compose.yml up --abort-on-container-exit
kill -9 $dstas_pid

sleep 5

dstat -lcmdrsyTt --full --out $1/dtat-result-slim.csv &
dstas_pid=$!
docker-compose -f $1/docker-compose.yml -f $1/docker-compose-slim.yml up --abort-on-container-exit
kill -9 $dstas_pid