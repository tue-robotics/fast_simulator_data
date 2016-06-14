#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    W.add_object("block-1", "rokus_experiments/small_block", 0.875, -0.5, 0.0, 0.0, 0.0, 1.570796)
    W.add_object("block-2", "rokus_experiments/small_block", 0.225,  0.5, 0.0, 0.0, 0.0, 1.570796)
    W.add_object("block-3", "rokus_experiments/small_block", 0.625,  0.9, 0.0, 0.0, 0.0, 1.570796)
    W.add_object("block-4", "rokus_experiments/small_block", 2.175,  1.85, 0.0, 0.0, 0.0, 0.0)
    W.add_object("block-5", "rokus_experiments/small_block", 0.625,  2.7, 0.0, 0.0, 0.0, 1.570796)
    W.add_object("block-6", "rokus_experiments/small_block", 0.225,  0.5, 0.0, 0.0, 0.0, 1.570796)
    W.add_object("block-7", "rokus_experiments/small_block", -1.025,  1.85, 0.0, 0.0, 0.0, 0.0)
