from classMonitoring.plotting.constants import MINIMUM_PROCESS_OCCURRENCES
from plotagem.plot_graficos import plot


class DockerOld:
    def __init__(self, docker_old):
        self.docker_old = docker_old

    def fragmentacao(self, minimum_process_occurrences):
        pass
    
    def plotar_grafico(self, title, filename, ylabel, division=None, cols_to_divide=None, dayfirst=True, includeColYlabel=True):
        plot(
            title=title,
            filename=filename,
            ylabel=ylabel,
            division=division,
            cols_to_divide=cols_to_divide,
            dayfirst=dayfirst,
            includeColYlabel=includeColYlabel
        )
    
    def plotar_recursos_maquina(self):
        # --------------------- MACHINE RESOURCES
        self.plotar_grafico(
            title="CPU",
            filename=self.docker_old['cpu'],
            ylabel='(percentage)',
            dayfirst=True, includeColYlabel=True
        )

        self.plotar_grafico(
            title="Memory", 
            filename=self.docker_old['memory'], 
            ylabel='(MB)', 
            dayfirst=True, division=1024, includeColYlabel=True
        )

        self.plotar_grafico(
            title="Disk", 
            filename=self.docker_old['disk'], 
            ylabel='Disk usage (GB)', 
            dayfirst=True, division=(1024**2)
        )

        self.plotar_grafico(
            title="Zumbis", 
            filename=self.docker_old['process'], 
            ylabel='Zumbis processes(qtt)', 
            dayfirst=True
        )

    def plotar_container_process(self):
        # -------------------------- CONTAINER PROCESS
        self.plotar_grafico(
            title="nginx",
            filename=self.docker_old['nginx'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )

        self.plotar_grafico(
            title="rabbitmq",
            filename=self.docker_old['rabbitmq'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )

        self.plotar_grafico(
            title="redis",
            filename=self.docker_old['redis'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )

    def plotar_docker_process(self):
        # ----------------------------- DOCKER PROCESS
        process_titles = [
            ("docker_antigo - process", self.docker_old['docker']),
            ("dockerd_antigo - process", self.docker_old['dockerd']),
            ("containerd_antigo - process", self.docker_old['containerd']),
            ("containerd-shim_antigo - process", self.docker_old['containerd-shim']),
            ("docker-proxy_antigo - process", self.docker_old['docker-proxy']),
            ("runc_novo - process", self.docker_old['runc'])
        ]
        
        for title, filename in process_titles:
            self.plotar_grafico(
                title=title,
                filename=filename,
                ylabel={
                    'cpu': 'CPU usage (percentage)',
                    'mem': 'Memory usage (percentage)',
                    'rss': 'Physical memory usage(MB)',
                    'vsz': 'Virtual memory usage (MB)',
                    'threads': 'Number of threads(qtt)',
                    'swap': 'Swap used(MB)',
                },
                dayfirst=True, includeColYlabel=True,
                cols_to_divide=['rss', 'vsz', 'swap'],
                division=1024
            )

    def plotar_image_process(self):
        # -------------------------- IMAGE PROCESS
        image_titles = [
            ("java", self.docker_old['java']),
            ("beam.smp", self.docker_old['beam.smp']),
            ("mysqld", self.docker_old['mysqld'])
        ]
        
        for title, filename in image_titles:
            self.plotar_grafico(
                title=title,
                filename=filename,
                ylabel={
                    'cpu': 'CPU usage (percentage)',
                    'mem': 'Memory usage (percentage)',
                    'rss': 'Physical memory usage(MB)',
                    'vsz': 'Virtual memory usage (MB)',
                    'threads': 'Number of threads(qtt)',
                    'swap': 'Swap used(MB)',
                },
                dayfirst=True, includeColYlabel=True,
                cols_to_divide=['rss', 'vsz', 'swap'],
                division=1024
            )

    def executar(self):
        self.fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        self.plotar_recursos_maquina()
        self.plotar_container_process()
        self.plotar_docker_process()
        self.plotar_image_process()
