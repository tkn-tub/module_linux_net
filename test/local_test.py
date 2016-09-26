import logging
import datetime
import time
import random
import wishful_upis as upis
from wishful_agent.core import wishful_module
from wishful_agent.timer import TimerEventSender

__author__ = "Anatolij Zubow"
__copyright__ = "Copyright (c) 2016, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "{zubow}@tkn.tu-berlin.de"

'''
Local test of net linux component.
'''

@wishful_module.build_module
class NetLinuxController(wishful_module.ControllerModule):
    def __init__(self):
        super(NetLinuxController, self).__init__()
        self.log = logging.getLogger('NetLinuxController')

    @wishful_module.on_start()
    def my_start_function(self):
        self.log.info("start net linux test")

        node = self.localNode
        iface_lst = node.net.get_ifaces()
        self.log.info('Discovered ifaces %s' % str(iface_lst))

        for iface in iface_lst:
            try:
                if_hw_addr = node.net.get_iface_hw_addr(iface)
                if_ip_addr = node.net.get_iface_ip_addr(iface)
                self.log.info('Iface %s, hw_addr %s, ip_addr %s' % (iface, if_hw_addr, if_ip_addr))
            except Exception as e:
                self.log.error("{} Failed with iface: {}, err_msg: {}".format(datetime.datetime.now(), iface, e))


        self.log.info('... done')

    @wishful_module.on_exit()
    def my_stop_function(self):
        self.log.info("stop net linux test")