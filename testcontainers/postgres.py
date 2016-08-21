import psycopg2

from testcontainers import config
from testcontainers.generic import DockerContainer
from testcontainers.waiting_utils import wait_container_is_ready


class PostgresContainer(DockerContainer):
    def start(self):
        self._docker.run(**config.postgres_container)
        self.connection = self._get_connection
        return self

    @wait_container_is_ready()
    def _get_connection(self):
        return psycopg2.connect(**config.postgres_db)

    def __init__(self, image="postgres:latest"):
        DockerContainer.__init__(self)
        config.postgres_container["image"] = image
        self.connection = None
