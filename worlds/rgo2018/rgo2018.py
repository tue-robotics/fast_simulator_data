#!/usr/bin/python
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    # dinnertable
    W.add_object("coke-1",  "sim-coke",   1.65, 0.90, 0.8)
    W.add_object("coke-2",  "sim-coke",   1.85, 0.90, 0.8)
    W.add_object("coke-3",  "sim-coke",   1.65, 1.40, 0.8)
    W.add_object("coke-4",  "sim-coke",   1.65, 1.15, 0.8)
    W.add_object("coke-1b", "sim-coke",   3.08, 0.90, 0.8)
    W.add_object("coke-2b", "sim-coke",   3.28, 0.90, 0.8)
    W.add_object("coke-3b", "sim-coke",   3.28, 1.40, 0.8)
    W.add_object("coke-4b", "sim-coke",   3.28, 1.15, 0.8)

    # kitchencounter
    W.add_object("coke-5", "sim-coke",  3.00, 4.15, 1.04)
    W.add_object("coke-6", "sim-coke",  3.45, 4.15, 1.04)
    W.add_object("coke-7", "sim-coke",  3.90, 4.15, 1.04)

    # cabinet
    W.add_object("coke-8", "sim-coke",  0.20, 3.1, 0.8)
    W.add_object("coke-9", "sim-coke",  0.20, 3.5, 0.8)
    W.add_object("coke-10", "sim-coke",  0.20, 3.1, 0.5)
    W.add_object("coke-11", "sim-coke",  0.20, 3.5, 0.5)
    W.add_object("coke-12", "sim-coke",  0.20, 3.1, 1.1)
    W.add_object("coke-13", "sim-coke",  0.20, 3.5, 1.1)

    W.add_object("person-1", "loy", 6.00, 7.00, 0.0)
