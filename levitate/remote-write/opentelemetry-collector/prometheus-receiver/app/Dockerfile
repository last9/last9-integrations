FROM golang:1.18 as build
WORKDIR /app/
COPY . .
RUN CGO_ENABLED=0 go build -o main main.go
FROM alpine:3.15
COPY --from=build /app/main  /app/main
CMD ["/app/main"]
