from pl.edu.agh.neural.learning.kohonen.topology.LinearTopology import LinearTopology
from pl.edu.agh.neural.learning.kohonen.topology.RectangularTopology import RectangularTopology

class TopologyUtil(object):
    LINEAR_TOPOLOGY = LinearTopology.NAME
    RECTANGULAR_TOPOLOGY = RectangularTopology.NAME

    REGISTERED_TOPOLOGIES = {
        LINEAR_TOPOLOGY: LinearTopology,
        RECTANGULAR_TOPOLOGY: RectangularTopology
    }

    @staticmethod
    def registered_topologies():
        return TopologyUtil.REGISTERED_TOPOLOGIES.keys()

    @staticmethod
    def get_topology(name, *args):
        return TopologyUtil.REGISTERED_TOPOLOGIES[name].create(*args)

    @staticmethod
    def default_topology():
        return TopologyUtil.LINEAR_TOPOLOGY
