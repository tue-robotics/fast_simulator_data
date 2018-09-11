#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    # cupboard
    W.add_object("coke-1", "sim-coke",  -2.75, 6.2, 0.36)
    W.add_object("coke-2", "sim-coke",  -2.75, 6.7, 0.36)
    W.add_object("coke-3", "sim-coke",  -2.75, 6.2, 0.71)
    W.add_object("coke-4", "sim-coke",  -2.75, 6.7, 0.71)
    W.add_object("coke-5", "sim-coke",  -2.75, 6.2, 1.125)
    W.add_object("coke-6", "sim-coke",  -2.75, 6.7, 1.125)
    W.add_object("coke-7", "sim-coke", -2.75, 6.2, 1.47)
    W.add_object("coke-8", "sim-coke", -2.75, 6.7, 1.47)

    # storage_table
    W.add_object("coke-9", "sim-coke",  -3.0, 5.9, 0.52)
    W.add_object("coke-10", "sim-coke",  -3.0, 5.6, 0.52)

    # counter
    W.add_object("coke-11", "sim-coke", -5.2, 4.5, 1.04)
    W.add_object("coke-12", "sim-coke", -5.7, 4.5, 1.04)
    W.add_object("coke-13", "sim-coke", -6.2, 4.5, 1.04)

    # dining_table
    W.add_object("coke-14", "sim-coke", -4.0, 1.9, 0.805)
    W.add_object("coke-15", "sim-coke", -4.0, 2.33, 0.805)
    W.add_object("coke-16", "sim-coke", -4.5, 2.33, 0.805)

    #cabinet
    W.add_object("coke-17", "sim-coke", -1.25, 0.3, 0.46)
    W.add_object("coke-18", "sim-coke", -1.45, 0.3, 0.46)
    W.add_object("coke-19", "sim-coke", -1.65, 0.3, 0.46)
    W.add_object("coke-20", "sim-coke", -1.25, 0.3, 0.76)
    W.add_object("coke-21", "sim-coke", -1.45, 0.3, 0.76)
    W.add_object("coke-22", "sim-coke", -1.65, 0.3, 0.76)
    W.add_object("coke-23", "sim-coke", -1.25, 0.3, 1.00)
    W.add_object("coke-24", "sim-coke", -1.45, 0.3, 1.00)
    W.add_object("coke-25", "sim-coke", -1.65, 0.3, 1.00)


    # # balcony_table
    # W.add_object("coke-7", "sim-coke",  0.00, -7.45, 0.71)
    # W.add_object("coke-8", "sim-coke", 0.1725, -7.525, 0.71)
    #
    # # left_rack
    # W.add_object("coke-9", "sim-coke", -2.35, -0.3, 0.91)
    #
    # # right_rack
    # W.add_object("coke-10", "sim-coke", -0.85, -0.3, 0.91)
    #
    # # kitchen_counter
    # W.add_object("coke-11", "sim-coke", 5.82, -3.7, 0.86)
    #
    # # sideboard
    # W.add_object("coke-12", "sim-coke", 2.64, -0.44, 0.50)
    # W.add_object("coke-13", "sim-coke", 2.64, -0.44, 0.91)
    #
    # # kitchen_shelf
    # W.add_object("coke-14", "sim-coke", 2.47, -4.15, 0.42)
    #
    # # kitchen_rack
    # W.add_object("coke-15", "sim-coke", 2.43, -3.15, 0.56)
    #
    # W.add_object("person-1", "loy", -1.0, -9.0, 0.0)
    #
    # W.add_object("food-1", "sim-coke", 6.014, -3.8, 0.9)
    # W.add_object("food-2", "sim-coke", 6.014, -3.6, 0.9)
    # W.add_object("food-3", "sim-coke", 2.382, -3.081, 0.7)
