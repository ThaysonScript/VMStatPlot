from classMonitoring.logs import MonitoringBase


class DockerMonitoring(MonitoringBase):
    @property
    def logs(self) -> dict:
        return {
            **self.common_logs,
            'nginx': self._path('nginx.csv'),
            'postgres': self._path('postgres.csv'),
            'rabbitmq': self._path('rabbitmq.csv'),
            'redis': self._path('redis.csv'),
            'docker': self._path('docker.csv'),
            'dockerd': self._path('dockerd.csv'),
            'containerd': self._path('containerd.csv'),
            'containerd-shim': self._path('containerd-shim.csv'),
            'docker-proxy': self._path('docker-proxy.csv'),
            'runc': self._path('runc.csv'),
            'java': self._path('java.csv'),
            'beam.smp': self._path('beam.smp.csv'),
            'initdb': self._path('initdb.csv'),
            'mysqld': self._path('mysqld.csv'),
            'postgres_process': self._path('postgres_process.csv')
        }