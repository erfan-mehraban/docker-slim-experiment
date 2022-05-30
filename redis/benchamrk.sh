dstat -lcmdrsyTt --full --out dtat-result-orginal.csv &
dstas_pid=$!
docker-compose -f docker-compose-original.yml up --abort-on-container-exit
kill -9 $dstas_pid

dstat -lcmdrsyTt --full --out dtat-result-slim.csv &
dstas_pid=$!
docker-compose -f docker-compose-slim.yml up --abort-on-container-exit
kill -9 $dstas_pid