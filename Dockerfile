FROM minio/minio

EXPOSE 9000 9001

CMD ["minio", "server", "/data", "--address", ":9000", "--console-address", ":9001"]
