ARG base_image

FROM $base_image

COPY entrypoint.sh /entrypoint.sh
RUN chmod 777 /entrypoint.sh
ENTRYPOINT /entrypoint.sh
