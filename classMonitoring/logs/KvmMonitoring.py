from classMonitoring.logs import MonitoringBase


class KvmMonitoring(MonitoringBase):
    @property
    def logs(self) -> dict:
        return {
            **self.common_logs,
            'server_response_time_monitoring': self._path('nginx_response.csv'),
            'kvm_Headless': self._path('kvm_Headless_monitoring.csv'),
            'kvm_libvirtd_service': self._path('kvm_libvirtd_service_monitoring.csv')
        }
