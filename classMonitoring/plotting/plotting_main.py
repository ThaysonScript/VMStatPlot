import sys
from classMonitoring.plotting.virtualizers import KvmPlotting, XenPlotting
from classMonitoring.plotting.virtualizers.LxcPlotting import LxcPlotting
from directory_setup import DirectorySetup
from classMonitoring.plotting.virtualizers.VboxPlotting import VBoxPlotting
from plotagem.plot_fragmentacao import fragmentacao
from pathlib import Path
from plotagem.logs import vbox
from plotagem.logs import kvm
from plotagem.logs import xen
from constants import MINIMUM_PROCESS_OCCURRENCES


class PlottingMain:
    def __init__(self):
        self.dir_setup = DirectorySetup(
            Path("plotagem/plot_images"),
            Path("plotagem/registros de monitoramento dos testes de envelhecimento")
        )

    def setup_directories(self):
        self.dir_setup.check_and_create_dirs()

    def run_vbox_plots(self):
        fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        vbox_plotter = VBoxPlotting(vbox)
        
        vbox_plotter.plot_cpu()
        vbox_plotter.plot_disks()
        vbox_plotter.plot_zumbis()
        vbox_plotter.plot_memory()
        vbox_plotter.plot_vboxheadless()
        vbox_plotter.plot_vboxsvc()
        vbox_plotter.plot_vboxxcomipcd()
        vbox_plotter.plot_server_response_time()
        
    def run_kvm_plots(self):
        fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        kvm_plotter = KvmPlotting(kvm)
        
        kvm_plotter.plot_cpu()
        kvm_plotter.plot_disks()
        kvm_plotter.plot_zumbis()
        kvm_plotter.plot_memory()
        kvm_plotter.plot_kvm_headless()
        kvm_plotter.plot_kvm_libvirt_service()
        kvm_plotter.plot_server_response_time()

    def run_xen_plots(self):
        fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        xen_plotter = XenPlotting(xen)
        
        xen_plotter.plot_cpu()
        xen_plotter.plot_disks()
        xen_plotter.plot_zumbis()
        xen_plotter.plot_memory()
        xen_plotter.plot_xen_monitoring_oxenstored()
        xen_plotter.plot_xen_monitoring_xen_balloon()
        xen_plotter.plot_xen_monitoring_xenbus()
        xen_plotter.plot_xen_monitoring_xenconsoled()
        xen_plotter.plot_server_response_time()

    def run_lxc_plots(self):
        lxc_plotter = LxcPlotting()
        lxc_plotter.plot_lxc()


starter = PlottingMain()
starter.setup_directories()
starter.run_vbox_plots()
starter.run_kvm_plots()
starter.run_xen_plots()
starter.run_lxc_plots()
