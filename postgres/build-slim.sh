docker-slim build \
    --target postgres:14.3-alpine \
    --env POSTGRES_HOST_AUTH_METHOD=trust \
    --show-clogs=true \
    --http-probe=false \
    --exec "pgbench -i -U postgres -s 10 postgres && pgbench -U postgres -c 10 -t 2000 postgres"

cat slim.report.json | jq .artifact_location | xargs -I{} cp -r {} .