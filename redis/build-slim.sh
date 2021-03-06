docker-slim build \
    --show-clogs=true \
    --http-probe=false \
    --target redis:7.0.0 \
    --exec redis-benchmark

cat slim.report.json | jq .artifact_location | xargs -I{} cp -r {} .
