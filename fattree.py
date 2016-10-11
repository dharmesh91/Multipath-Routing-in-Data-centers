#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, Intf, TCLink
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
import logging
import os 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger( __name__ )

class HugeTopo(Topo):
    logger.debug("Class HugeTopo")
    CoreSwitchList = []
    AggSwitchList = []
    EdgeSwitchList = []
    HostList = []
    iNUMBER = 0
    def __init__(self):
        logger.debug("Class HugeTopo init")
        iNUMBER = 2
        
        self.iNUMBER = iNUMBER
        self.iCoreLayerSwitch = iNUMBER
        self.iAggLayerSwitch = iNUMBER * 3
        self.iEdgeLayerSwitch = iNUMBER * 3
        self.iHost = self.iEdgeLayerSwitch * 2 
    
    
        #Init Topo
        Topo.__init__(self)

    def createTopo(self):    
        logger.debug("Start create Core Layer Swich")
        self.createCoreLayerSwitch(self.iCoreLayerSwitch)
        logger.debug("Start create Agg Layer Swich ")
        self.createAggLayerSwitch(self.iAggLayerSwitch)
        logger.debug("Start create Edge Layer Swich ")
        self.createEdgeLayerSwitch(self.iEdgeLayerSwitch)
        logger.debug("Start create Host")
        self.createHost(self.iHost)

    """
    Create Switch and Host
    """

    def createCoreLayerSwitch(self, NUMBER):
        logger.debug("Create Core Layer")
        for x in range(1, NUMBER+1):
            PREFIX = "100"
            if x >= int(10):
                PREFIX = "10"
            self.CoreSwitchList.append(self.addSwitch(PREFIX + str(x)))

    def createAggLayerSwitch(self, NUMBER):
        logger.debug( "Create Agg Layer")
        for x in range(1, NUMBER+1):
            PREFIX = "200"
            if x >= int(10):
                PREFIX = "20"
            self.AggSwitchList.append(self.addSwitch(PREFIX + str(x)))

    def createEdgeLayerSwitch(self, NUMBER):
        logger.debug("Create Edge Layer")
        for x in range(1, NUMBER+1):
            PREFIX = "300"
            if x >= int(10):
                PREFIX = "30"
            self.EdgeSwitchList.append(self.addSwitch(PREFIX + str(x)))
    
    def createHost(self, NUMBER):
        logger.debug("Create Host")
        for x in range(1, NUMBER+1):
            PREFIX = "400"
            if x >= int(10):
                PREFIX = "40"
            self.HostList.append(self.addHost(PREFIX + str(x))) 

    
    def createLink(self):
            logger.debug("Create Core to Agg")
        
            self.addLink(self.CoreSwitchList[0], self.AggSwitchList[0], bw=100)
            self.addLink(self.CoreSwitchList[0], self.AggSwitchList[1], bw=100)
            self.addLink(self.CoreSwitchList[0], self.AggSwitchList[2], bw=100)
            self.addLink(self.CoreSwitchList[0], self.AggSwitchList[3], bw=100)
            self.addLink(self.CoreSwitchList[0], self.AggSwitchList[4], bw=100)
            self.addLink(self.CoreSwitchList[0], self.AggSwitchList[5], bw=100)  

            self.addLink(self.CoreSwitchList[1], self.AggSwitchList[0], bw=100)
            self.addLink(self.CoreSwitchList[1], self.AggSwitchList[1], bw=100)
            self.addLink(self.CoreSwitchList[1], self.AggSwitchList[2], bw=100)
            self.addLink(self.CoreSwitchList[1], self.AggSwitchList[3], bw=100)
            self.addLink(self.CoreSwitchList[1], self.AggSwitchList[4], bw=100)
            self.addLink(self.CoreSwitchList[1], self.AggSwitchList[5], bw=100)     
      
            logger.debug("Create Agg to Edge")
     
            self.addLink(self.AggSwitchList[0], self.EdgeSwitchList[0], bw=100)
            self.addLink(self.AggSwitchList[0], self.EdgeSwitchList[1], bw=100)
            self.addLink(self.AggSwitchList[1], self.EdgeSwitchList[0], bw=100)
            self.addLink(self.AggSwitchList[1], self.EdgeSwitchList[1], bw=100)
            
            self.addLink(self.AggSwitchList[2], self.EdgeSwitchList[2], bw=100)
            self.addLink(self.AggSwitchList[2], self.EdgeSwitchList[3], bw=100)
            self.addLink(self.AggSwitchList[3], self.EdgeSwitchList[2], bw=100)
            self.addLink(self.AggSwitchList[3], self.EdgeSwitchList[3], bw=100)

            self.addLink(self.AggSwitchList[4], self.EdgeSwitchList[4], bw=100)
            self.addLink(self.AggSwitchList[4], self.EdgeSwitchList[5], bw=100)
            self.addLink(self.AggSwitchList[5], self.EdgeSwitchList[4], bw=100)
            self.addLink(self.AggSwitchList[5], self.EdgeSwitchList[5], bw=100)
  
            
            logger.debug("Create Edge to Host")
        
           
            self.addLink(self.EdgeSwitchList[0], self.HostList[0])
            self.addLink(self.EdgeSwitchList[0], self.HostList[1])
            self.addLink(self.EdgeSwitchList[1], self.HostList[2])
            self.addLink(self.EdgeSwitchList[1], self.HostList[3])
            self.addLink(self.EdgeSwitchList[2], self.HostList[4])
            self.addLink(self.EdgeSwitchList[2], self.HostList[5])
            self.addLink(self.EdgeSwitchList[3], self.HostList[6])
            self.addLink(self.EdgeSwitchList[3], self.HostList[7])
            self.addLink(self.EdgeSwitchList[4], self.HostList[8])
            self.addLink(self.EdgeSwitchList[4], self.HostList[9])
            self.addLink(self.EdgeSwitchList[5], self.HostList[10])
            self.addLink(self.EdgeSwitchList[5], self.HostList[11]) 

def createTopo():
    logging.debug("LV1 Create HugeTopo")
    topo = HugeTopo()
    topo.createTopo() 
    topo.createLink() 
  
    logging.debug("LV1 Start Mininet")
    
    net = Mininet(topo=topo, link=TCLink, controller=None)

    net.start()


    CLI(net)


if __name__ == '__main__':
    setLogLevel('info')
    if os.getuid() != 0:
        logger.debug("You are NOT root")
    elif os.getuid() == 0:
        createTopo()
