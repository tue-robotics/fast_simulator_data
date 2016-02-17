#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    W.add_object("coke-5", "sim-coke",  3.196, 4.652, 0.87)
    W.add_object("coke-6", "sim-coke",  3.214, 4.050, 0.87)
    W.add_object("coke-7", "sim-coke",  3.463, 4.353, 0.87)


    W.add_object("coke-1", "sim-coke",  1.056, 3.471, 0.8)
    W.add_object("coke-2", "sim-coke",  0.676, 3.559, 0.8)
    W.add_object("coke-3", "sim-coke",  0.303, 3.413, 0.8)
    W.add_object("coke-4", "sim-coke", 0.868, 1.955, 0.87)

    W.add_object("coke-under-table", "sim-coke", 0.4, 1.92, 0)

    W.add_object("person-1", "loy", 0.833, 0.780, 0.0)
