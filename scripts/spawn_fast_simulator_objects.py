#!/usr/bin/python
import yaml
import rospy

from os import getenv
from rospkg import RosPack
from fast_simulator import client

if __name__ == "__main__":
    # Initialize ROS node
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    # Load yaml with list of objects that need to be loaded
    package_path = RosPack().get_path('fast_simulator_data')
    with open(package_path + "/worlds/robotics_testlabs/robotics_testlabs", 'r') as f:
        data = yaml.safe_load(f)

    # Iterate over objects and spawn
    for sod in data:
        W.add_object(sod["id"], sod["type"], sod["x"], sod["y"], sod["z"])
