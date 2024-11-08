from plotagem.plot_graficos import plot


class NewDocker:
    def __init__(self, new_docker):
        self.new_docker = new_docker

    def plot_machine_resources(self):
        plot(
            title="CPU",
            filename=self.new_docker['cpu'],
            ylabel='(percentage)',
            dayfirst=True, includeColYlabel=True
        )

        plot(
            title="Memory",
            filename=self.new_docker['memory'],
            ylabel='(MB)',
            dayfirst=True,
            division=1024, includeColYlabel=True
        )

        plot(
            title="Disk",
            filename=self.new_docker['disk'],
            ylabel='Disk usage (GB)',
            dayfirst=True, division=(1024**2)
        )

        plot(
            title="Zumbis",
            filename=self.new_docker['process'],
            ylabel='Zumbis processes(qtt)',
            dayfirst=True
        )

    def plot_container_process(self):
        plot(
            title="nginx",
            filename=self.new_docker['nginx'],
            ylabel='(seconds)',
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )

        plot(
            title="rabbitmq",
            filename=self.new_docker['rabbitmq'],
            ylabel='(seconds)',
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )

        plot(
            title="redis",
            filename=self.new_docker['redis'],
            ylabel='(seconds)',
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )

    def plot_docker_process(self):
        self.plot_process("docker_novo - process", self.new_docker['docker'])
        self.plot_process("dockerd_novo - process", self.new_docker['dockerd'])
        self.plot_process("containerd_novo - process", self.new_docker['containerd'])
        self.plot_process("containerd-shim_novo - process", self.new_docker['containerd-shim'])
        self.plot_process("docker-proxy_novo - process", self.new_docker['docker-proxy'])
        self.plot_process("runc_novo - process", self.new_docker['runc'])

    def plot_image_process(self):
        self.plot_process("java", self.new_docker['java'])
        self.plot_process("beam.smp", self.new_docker['beam.smp'])
        self.plot_process("mysqld", self.new_docker['mysqld'])

    def plot_process(self, title, filename):
        plot(
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