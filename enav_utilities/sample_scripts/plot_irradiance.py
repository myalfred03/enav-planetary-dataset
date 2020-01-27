#!/usr/bin/env python

""" plot_irradiance.py

    Plot solar irradiance data of the enav dataset

    Author: Olivier Lamarre <olivier.lamarre@robotics.utias.utoronto.ca>

    Affl.:  Space and Terrestrial Autonomous Robotic Systems Laboratory
            University of Toronto
    
    Date:   February 10, 2019
    """

import sys
import argparse
import matplotlib.pyplot as plt

sys.path.append("..")
from rosbag_data_load import FetchEnergyDataset


# Parse bag file name
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--bag_file", help="path to rosbag file")
args = parser.parse_args()


if __name__ == "__main__":

    # Fetch data
    bag_obj = FetchEnergyDataset(args.bag_file)
    irradiance_data = bag_obj.load_irradiance_data(rel_time=True)

    # Plot data
    plt.figure()
    plt.plot(irradiance_data[:,0], irradiance_data[:,1])
    plt.xlabel('Time [s]')
    plt.ylabel('Irradiance [W/m^2]')
    plt.title("Solar irradiance received by the rover's top plane vs time")
    plt.show()
