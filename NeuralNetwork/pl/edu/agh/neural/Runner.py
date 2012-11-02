from pl.edu.agh.neural.Network import Network
from pl.edu.agh.neural.edges.Input import Input
from pl.edu.agh.neural.NeuronsLayer import NeuronsLayer
from pl.edu.agh.neural.psp.SumPotential import SumPotential
from pl.edu.agh.neural.activators.LinearActivator import LinearActivator
from pl.edu.agh.neural.Neuron import Neuron

def main():
    inputs = [Input(1), Input(1)]
    network = Network(inputs)
    layer = NeuronsLayer()
    layer.add_neuron(Neuron(SumPotential(), LinearActivator()))
    network.add_layer(layer)
    layer.set_edge_weight(0, 0, 0.5)
    layer.set_edge_weight(0, 1, 0.5)
    print network.calculate_network_response()

    print "Ciekawe czy to będzie konflikt..."

main()
