from classMonitoring.logs import MonitoringBase


class PodmanMonitoring(MonitoringBase):
    @property
    def logs(self) -> dict:
        return {
            **self.common_logs,
            'nginx': self._path('nginx.csv'),
            'postgres': self._path('postgres.csv'),
            'rabbitmq': self._path('rabbitmq.csv'),
            'redis': self._path('redis.csv'),
            'podman': self._path('podman.csv'),
            'conmon': self._path('conmon.csv'),
            'cron': self._path('cron.csv'),
            'crun': self._path('crun.csv'),
            'systemd': self._path('systemd.csv'),
            'java': self._path('java.csv'),
            'postgres_process': self._path('postgres_process.csv'),
            'mysqld': self._path('mysqld.csv'),
            'initdb': self._path('initdb.csv'),
            'beam.smp': self._path('beam.smp.csv')
        }