from classMonitoring.plotting.plotting_base import PlottingBase
from plotagem.plot_graficos import plot

class XenPlotting(PlottingBase):
    def plot_xen_monitoring_oxenstored(self):
        plot(
            title="Process - xen_monitoring_oxenstored", 
            filename=self.logs['xen_monitoring_oxenstored'], 
            cols_to_divide=["rss","vsz","swap"],
            ylabel={
                'cpu': 'CPU usage (percentage)',
                "rss": "Physical memory usage(MB)",
                "vsz": "Virtual memory usage (MB)",
                "swap": "Swap used(MB)",
                'mem': 'Memory usage (percentage)',
                "thread": "Number of threads(qtt)"
            },
            division=1024, dayfirst=True
        )

    def plot_xen_monitoring_xen_balloon(self):
        plot(
            title="Process - xen_monitoring_xen_balloon", 
            filename=self.logs['xen_monitoring_xen_balloon'], 
            cols_to_divide=["rss","vsz","swap"],
            ylabel={
                'cpu': 'CPU usage (percentage)',
                "rss": "Physical memory usage(MB)",
                "vsz": "Virtual memory usage (MB)",
                "swap": "Swap used(MB)",
                'mem': 'Memory usage (percentage)'
            },
            division=1024, dayfirst=True
        )

    def plot_xen_monitoring_xenbus(self):
        plot(
            title="Process - xen_monitoring_xenbus", 
            filename=self.logs['xen_monitoring_xenbus'], 
            cols_to_divide=["rss","vsz","swap"],
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                "rss": "Physical memory usage(MB)",
                "vsz": "Virtual memory usage (MB)",
                "thread": "Number of threads(qtt)",
                "swap": "Swap used(MB)",
            },
            division=1024, dayfirst=True
        )

    def plot_xen_monitoring_xenconsoled(self):
        plot(
            title="Process - xen_monitoring_xenconsoled", 
            filename=self.logs['xen_monitoring_xenconsoled'], 
            cols_to_divide=["rss","vsz","swap"],
            ylabel={
                'cpu': 'CPU usage (percentage)',
                "rss": "Physical memory usage(MB)",
                "vsz": "Virtual memory usage (MB)",
                "swap": "Swap used(MB)",
                'mem': 'Memory usage (percentage)'
            },
            division=1024, dayfirst=True
        )

    def plot_server_response_time(self):
        plot(
            title="Server response time", 
            filename=self.logs['server_response_time_monitoring'], 
            ylabel='Response time (seconds)', 
            multiply=1000, dayfirst=True
        )
    
    def plot_cpu(self):
        plot(
            title="CPU",
            filename=self.logs['monitoring_cpu'], 
            ylabel='(percentage)', 
            dayfirst=True, includeColYlabel=True
        )

    def plot_disks(self):
        plot(
            title="Disk", 
            filename=self.logs['monitoring_disks'], 
            ylabel='Disk usage (GB)', 
            dayfirst=True, division=(1024**2)
        )

    def plot_zumbis(self):
        plot(
            title="Zumbis", 
            filename=self.logs['monitoring_zumbies'], 
            ylabel='Zumbies processes(qtt)', 
            dayfirst=True
        )

    def plot_memory(self):
        plot(
            title="Memory", 
            filename=self.logs['monitoring_mem'], 
            ylabel='(MB)', 
            dayfirst=True, 
            division=1024, includeColYlabel=True
        )
