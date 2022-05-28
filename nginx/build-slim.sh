docker-slim build \
    --target nginx:1.22.0

cat slim.report.json | jq .artifact_location | xargs -I{} cp -r {} .
