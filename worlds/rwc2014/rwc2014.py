#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()
    
    W.add_object("milk", "coke", 8.0, 5.0, 0.82)
    W.add_object("pringles", "garlic_sauce", 8.0, 5.5, 0.82)
    W.add_object("noodles", "rwc2014.noodles", 8.0, 6.0, 0.82)
    W.add_object("biscuits", "seven_up", 8.0, 6.5, 0.82)


