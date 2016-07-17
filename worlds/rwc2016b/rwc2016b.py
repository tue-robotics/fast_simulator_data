#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    W.add_object("coke-1", "sim-coke",  11.834, 5.093, 0.83)
    W.add_object("coke-2", "sim-coke",  12.187, 5.094, 0.83)

# W.add_object("person-1", "loy", 1.770, 0.194, 0.0, 0, 0, 1)
