from plotagem.plot_graficos import plot

class PlottingBase:
    def __init__(self, logs: dict):
        self.logs = logs

    def plot_cpu(self):
        plot(
            title="CPU",
            filename=self.logs['monitoring_cpu'],
            ylabel='(percentage)',
            dayfirst=True,
            includeColYlabel=True
        )

    def plot_disks(self):
        plot(
            title="Disk",
            filename=self.logs['monitoring_disks'],
            ylabel='Disk usage (GB)',
            dayfirst=True,
            division=(1024**2)
        )

    def plot_zumbis(self):
        plot(
            title="Zumbis",
            filename=self.logs['monitoring_zumbies'],
            ylabel='Zumbis processes(qtt)',
            dayfirst=True
        )

    def plot_memory(self):
        plot(
            title="Memory",
            filename=self.logs['monitoring_mem'],
            ylabel='(MB)',
            dayfirst=True,
            division=1024,
            includeColYlabel=True
        )
