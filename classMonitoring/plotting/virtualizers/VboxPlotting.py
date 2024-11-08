from plotting_base import PlottingBase
from plotagem.plot_graficos import plot

class VboxPlotting(PlottingBase):
    def plot_vboxheadless(self):
        plot(
            title="Process - VBoxHeadless",
            filename=self.logs['monitoring_VboxHeadless'],
            cols_to_divide=["vmrss", "vsz", "swap"],
            ylabel={
                'cpu': 'CPU usage (percentage)',
                "vmrss": "Physical memory usage(MB)",
                "vsz": "Virtual memory usage (MB)",
                "swap": "Swap used(MB)",
                'mem': 'Memory usage (percentage)',
                "thread": "Number of threads(qtt)"
            },
            division=1024,
            dayfirst=True
        )

    def plot_vboxsvc(self):
        plot(
            title="Process - VBoxSVC",
            filename=self.logs['monitoring_VboxSvc'],
            cols_to_divide=["vmrss", "vsz", "swap"],
            ylabel={
                'cpu': 'CPU usage (percentage)',
                "vmrss": "Physical memory usage(MB)",
                "vsz": "Virtual memory usage (MB)",
                "swap": "Swap used(MB)",
                'mem': 'Memory usage (percentage)'
            },
            division=1024,
            dayfirst=True
        )

    def plot_vboxxcomipcd(self):
        plot(
            title="Process - VBoxXPCOMIPCD",
            filename=self.logs['monitoring_VboxXPCOMIPCD'],
            cols_to_divide=["vmrss", "vsz", "swap"],
            ylabel={
                'cpu': 'CPU usage (percentage)',
                "vmrss": "Physical memory usage(MB)",
                "vsz": "Virtual memory usage (MB)",
                "swap": "Swap used(MB)",
                'mem': 'Memory usage (percentage)'
            },
            division=1024,
            dayfirst=True
        )

    def plot_server_response_time(self):
        plot(
            title="Server response time",
            filename=self.logs['server_response_time_monitoring'],
            ylabel='Response time(s)',
            multiply=1000,
            dayfirst=True
        )
