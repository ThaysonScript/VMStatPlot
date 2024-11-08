from classMonitoring.logs import MonitoringBase


class VboxMonitoring(MonitoringBase):
    @property
    def logs(self) -> dict:
        return {
            **self.common_logs,
            'server_response_time_monitoring': self._path('nginx_response.csv'),
            'monitoring_VboxHeadless': self._path('vbox_monitoring-VBoxHeadless.csv'),
            'monitoring_VboxSvc': self._path('vbox_monitoring-VBoxSVC.csv'),
            'monitoring_VboxXPCOMIPCD': self._path('vbox_monitoring-VBoxXPCOMIPCD.csv')
        }
