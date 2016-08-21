import MySQLdb

from testcontainers import config
from testcontainers.generic import DockerContainer
from testcontainers.waiting_utils import wait_container_is_ready


class MySqlDockerContainer(DockerContainer):
    def __init__(self, image='mysql:latest'):
        DockerContainer.__init__(self)
        self.image = image
        self.connection = None

    def start(self):
        """
        Start my sql container and wait to be ready
        :return:
        """
        self._docker.run(self.image, **config.my_sql_container)
        self.connection = self._get_connection()
        return self

    @wait_container_is_ready()
    def _get_connection(self):
        return MySQLdb.connect(**config.mysql_db)
