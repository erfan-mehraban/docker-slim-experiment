docker build mongo-perf -t mongo-perf

docker-slim build \
    --continue-after signal \
    --show-clogs=true \
    --http-probe=false \
    --publish-port 27017 \
    mongo:5.0.8 &

pid=$!

sleep 5

docker run \
    --network=host \
    mongo-perf \
    --host mongo \
    -f /workdir/testcases/query_unique_idx.js \
    -t '2' \
    --trialTime '1'

kill -SIGUSR1 $pid

sleep 20

cat slim.report.json | jq .artifact_location | xargs -I{} cp -r {} .
