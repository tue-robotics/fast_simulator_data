#!/usr/bin/env python

import os
import sys
import yaml

from rospkg import RosPack
import rospy
from fast_simulator import client

if __name__ == "__main__":
    my_args = rospy.myargv(argv=sys.argv)

    # Initialize ROS node
    rospy.init_node('fast_simulator_object_spawner')
    if len(my_args) < 2:
        rospy.logerr("Please provide objects yaml file")
        sys.exit(1)

    W = client.SimWorld()

    # Load yaml with list of objects that need to be loaded
    package_path = RosPack().get_path('fast_simulator_data')
    yaml_file = os.path.join(package_path, my_args[1])
    if not os.path.isfile(yaml_file):
        if os.path.isfile(yaml_file + ".yaml"):
            yaml_file = yaml_file + ".yaml"
        elif os.path.isfile(yaml_file + ".yml"):
            yaml_file = yaml_file + ".yml"
        else:
            rospy.logfatal("No objects file found for: {}".format(yaml_file))

    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    # Iterate over objects and spawn
    if isinstance(data, list):
        for sod in data:
            print(sod)
            W.add_object(**sod)
    elif isinstance(data, dict):
        W.add_object(**data)
