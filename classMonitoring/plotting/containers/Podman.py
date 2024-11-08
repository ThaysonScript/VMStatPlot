from plotagem.plot_graficos import plot


class Podman:
    def __init__(self, pod):
        self.pod = pod

    def plot_machine_resources(self):
        plot(
            title="CPU",
            filename=self.pod['cpu'],
            ylabel='(percentage)',
            dayfirst=True, includeColYlabel=True
        )

        plot(
            title="Memory",
            filename=self.pod['memory'],
            ylabel='(GB)',
            dayfirst=True,
            division=(1024**2), includeColYlabel=True
        )

        plot(
            title="Disk",
            filename=self.pod['disk'],
            ylabel='Disk usage (GB)',
            dayfirst=True, division=(1024**2)
        )

        plot(
            title="Zumbis",
            filename=self.pod['process'],
            ylabel='Zumbis processes(qtt)',
            dayfirst=True
        )

    def plot_container_process(self):
        plot(
            title="nginx",
            filename=self.pod['nginx'],
            ylabel='(seconds)',
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )

        plot(
            title="rabbitmq",
            filename=self.pod['rabbitmq'],
            ylabel='(seconds)',
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )

        plot(
            title="redis",
            filename=self.pod['redis'],
            ylabel='(seconds)',
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )

    def plot_podman_process(self):
        self.plot_process("podman", self.pod['podman'])
        self.plot_process("conmon", self.pod['conmon'])
        self.plot_process("crun", self.pod['crun'])
        self.plot_process("systemd", self.pod['systemd'])

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
