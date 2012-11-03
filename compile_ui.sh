#!/bin/bash
pyuic4 NeuralNetwork/pl/edu/agh/neural/gui/MainWindowUi.ui -o NeuralNetwork/pl/edu/agh/neural/gui/MainWindowUi.py
pyuic4 NeuralNetwork/pl/edu/agh/neural/gui/creator/NetworkCreatorUi.ui -o NeuralNetwork/pl/edu/agh/neural/gui/creator/NetworkCreatorUi.py
pyuic4 NeuralNetwork/pl/edu/agh/neural/gui/launcher/SimulationLauncherUi.ui -o NeuralNetwork/pl/edu/agh/neural/gui/launcher/SimulationLauncherUi.py