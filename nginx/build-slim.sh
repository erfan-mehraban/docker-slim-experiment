docker-slim build \
    --target nginx:latest

cat slim.report.json | jq .artifact_location | xargs -I{} cp -r {} .
