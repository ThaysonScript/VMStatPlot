class MonitoringBase:
    """
    Classe base para monitoramento, define a estrutura padrão para os caminhos dos arquivos de log.
    """
    def __init__(self, name: str, base_log_path: str = './plotagem/registros de monitoramento dos testes de envelhecimento'):
        self.name = name
        self.base_log_path = f"{base_log_path}/{self.name}"
        
    def _path(self, filename: str) -> str:
        """Gera o caminho completo do arquivo de log."""
        return f"{self.base_log_path}/{filename}"

    @property
    def common_logs(self) -> dict:
        """Logs comuns a todas as classes de monitoramento."""
        return {
            'monitoring_cpu': self._path('machine_monitoring-cpu.csv'),
            'monitoring_disks': self._path('machine_monitoring-disk.csv'),
            'monitoring_zumbies': self._path('machine_monitoring-zombies.csv'),
            'monitoring_mem': self._path('machine_monitoring-mem.csv'),
            'machineHost_server_status': self._path('machineHost_server_status.csv'),
            'reset_times': self._path('reset_times.csv')
        }
