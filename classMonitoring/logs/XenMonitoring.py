from classMonitoring.logs import MonitoringBase


class XenMonitoring(MonitoringBase):
    @property
    def logs(self) -> dict:
        return {
            **self.common_logs,
            'server_response_time_monitoring': self._path('response_times.csv'),
            'xen_monitoring_oxenstored': self._path('xen_monitoring-oxenstored.csv'),
            'xen_monitoring_xen_balloon': self._path('xen_monitoring-xen-balloon.csv'),
            'xen_monitoring_xenbus': self._path('xen_monitoring-xenbus.csv'),
            'xen_monitoring_xenconsoled': self._path('xen_monitoring-xenconsoled.csv')
        }
