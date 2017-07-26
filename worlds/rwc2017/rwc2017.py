#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    # kitchen_table
    W.add_object("coke-1", "sim-coke",  3.85, -2.12, 0.81)
    W.add_object("coke-2", "sim-coke",  3.85, -2.32, 0.81)
    W.add_object("coke-3", "sim-coke",  4.05, -2.12, 0.81)
    W.add_object("coke-4", "sim-coke",  3.85, -3.60, 0.81)

    # desk
    W.add_object("coke-5", "sim-coke",  -1.93, -2.1, 0.71)
    W.add_object("coke-6", "sim-coke",  -1.93, -3.0, 0.71)

    # balcony_table
    W.add_object("coke-7", "sim-coke",  0.00, -7.45, 0.71)
    W.add_object("coke-8", "sim-coke", 0.1725, -7.525, 0.71)

    W.add_object("person-1", "loy", -1.0, -9.0, 0.0)
