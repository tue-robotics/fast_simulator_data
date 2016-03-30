#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    # W.add_object("coke-5", "sim-coke",  3.196, 4.652, 0.87)
    # W.add_object("person-1", "loy", 0.833, 0.780, 0.0)
