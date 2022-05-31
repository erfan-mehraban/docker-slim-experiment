docker-slim build \
    --continue-after signal \
    --show-clogs=true \
    --http-probe=false \
    --publish-port 11211 \
    memcached:1.6.15 &

pid=$!

sleep 10

docker run \
    --network=host \
    redislabs/memtier_benchmark \
    -P memcache_text \
    -p 11211

kill -SIGUSR1 $pid

sleep 30

cat slim.report.json | jq .artifact_location | xargs -I{} cp -r {} .