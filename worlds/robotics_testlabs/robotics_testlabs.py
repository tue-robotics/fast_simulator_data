#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    W.add_object("coke-1", "coke",  1.056, 3.471, 0.8)
    W.add_object("coke-2", "coke",  0.676, 3.559, 0.8)
    W.add_object("coke-3", "coke",  0.303, 3.413, 0.8)
    W.add_object("coke-4", "coke",  0.676, 1.906, 0.9)

