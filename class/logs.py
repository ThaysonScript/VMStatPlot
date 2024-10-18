NAME = 'logs'
PASTA_LOGS = f'./plotagem/registros de monitoramento dos testes de envelhecimento/qemu/{NAME}'
NAME_FORMAT = f'frag_{NAME.replace("/", "_")}'

# Arquivos comuns entre os ambientes
common_files = {
    'monitoring_cpu': 'machine_monitoring-cpu.csv',
    'monitoring_disks': 'machine_monitoring-disk.csv',
    'monitoring_zumbies': 'machine_monitoring-zombies.csv',
    'monitoring_mem': 'machine_monitoring-mem.csv',
    'machineHost_server_status': 'machineHost_server_status.csv',
    'reset_times': 'reset_times.csv',
    'server_response_time_monitoring': 'nginx_response.csv'
}

# Arquivos específicos por ambiente
env_specific_files = {
    'vbox': {
        'monitoring_VboxHeadless': 'vbox_monitoring-VBoxHeadless.csv',
        'monitoring_VboxSvc': 'vbox_monitoring-VBoxSVC.csv',
        'monitoring_VboxXPCOMIPCD': 'vbox_monitoring-VBoxXPCOMIPCD.csv',
    },
    'kvm': {
        'kvm_Headless': 'kvm_Headless_monitoring.csv',
        'kvm_libvirtd_service': 'kvm_libvirtd_service_monitoring.csv',
    },
    'xen': {
        'xen_monitoring_oxenstored': 'xen_monitoring-oxenstored.csv',
        'xen_monitoring_xen_balloon': 'xen_monitoring-xen-balloon.csv',
        'xen_monitoring_xenbus': 'xen_monitoring-xenbus.csv',
        'xen_monitoring_xenconsoled': 'xen_monitoring-xenconsoled.csv',
    }
}

# Função para construir dicionário completo de arquivos por ambiente
def build_env_files(env_name):
    return {key: f'{PASTA_LOGS}/{filename}' for key, filename in common_files.items()}

# Função para adicionar os arquivos específicos
def add_env_specific_files(env_name, env_dict):
    if env_name in env_specific_files:
        env_dict.update({key: f'{PASTA_LOGS}/{filename}' for key, filename in env_specific_files[env_name].items()})
    return env_dict

# Gerar os dicionários completos por ambiente
vbox = add_env_specific_files('vbox', build_env_files('vbox'))
kvm = add_env_specific_files('kvm', build_env_files('kvm'))
xen = add_env_specific_files('xen', build_env_files('xen'))

# Containers Docker e Podman
docker_base_files = {
    'runs': 'runs.csv',
    'cpu': 'cpu.csv',
    'memory': 'memory.csv',
    'disk': 'disk.csv',
    'process': 'process.csv',
    'nginx': 'nginx.csv',
    'postgres': 'postgres.csv',
    'rabbitmq': 'rabbitmq.csv',
    'redis': 'redis.csv',
}

docker_specific_files = {
    'docker': 'docker.csv',
    'dockerd': 'dockerd.csv',
    'containerd': 'containerd.csv',
    'containerd-shim': 'containerd-shim.csv',
    'docker-proxy': 'docker-proxy.csv',
    'runc': 'runc.csv',
    'java': 'java.csv',
    'beam.smp': 'beam.smp.csv',
    'initdb': 'initdb.csv',
    'mysqld': 'mysqld.csv',
    'postgres_process': 'postgres_process.csv',
}

def build_docker_files(docker_type):
    return {key: f'{PASTA_LOGS}/{filename}' for key, filename in {**docker_base_files, **docker_specific_files}.items()}

dock_antigo = build_docker_files('docker_antigo')
dock_novo = build_docker_files('docker_novo')

podman_specific_files = {
    'podman': 'podman.csv',
    'conmon': 'conmon.csv',
    'cron': 'cron.csv',
    'crun': 'crun.csv',
    'systemd': 'systemd.csv',
}

def build_pod_files():
    return {key: f'{PASTA_LOGS}/{filename}' for key, filename in {**docker_base_files, **podman_specific_files}.items()}

pod = build_pod_files()
