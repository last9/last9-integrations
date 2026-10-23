FROM golang:1.18 as build
WORKDIR /app/
COPY . .
RUN CGO_ENABLED=0 go build -o main main.go
FROM alpine:3.22
# The base image ships CA bundle 20260909; 20261020+ distrusts the compromised eMudhra intermediates.
RUN apk add --no-cache --upgrade ca-certificates ca-certificates-bundle
COPY --from=build /app/main  /app/main
CMD ["/app/main"]
