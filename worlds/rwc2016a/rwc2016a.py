#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    W.add_object("coke-1", "sim-coke",  10.069, 3.745, 0.8)
    W.add_object("coke-2", "sim-coke",  14.351, 5.626, 0.8)
    W.add_object("coke-3", "sim-coke",  15.609, 3.310, 0.8)
    W.add_object("coke-4", "sim-coke",  12.971, 0.785, 0.5)
    W.add_object("coke-5", "sim-coke",  4.396, -1.169, 0.8)
    W.add_object("coke-6", "sim-coke",  0.253, 4.592, 0.8)

# W.add_object("person-1", "loy", 1.770, 0.194, 0.0, 0, 0, 1)
