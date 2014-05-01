#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    W.add_object("dinner_table", "table_120x80x76", 3.174, -0.523, 0, 0, 0, 1.57)
    W.add_object("workbench", "table_120x80x76", 2.120, -3.010, 0, 0, 0, 1.57)
    W.add_object("supply_table", "table_120x80x76", 2.16, -4.16, 0)
    W.add_object("desk", "table_120x80x76", 1.150, -2.752, 0, 0, 0, 1.57)
    W.add_object("desk-2", "table_120x80x76", 1.150, -3.958, 0, 0, 0, 1.57)

    #bed = W.add_object("bed-1", "hospital_bed", 5.0, -1.52, 0)

    #coke1 = W.add_object("coke-1", "coke", 1.941, -1.403, 0.82)
    #qr_code1 = W.add_object("qr-code-1", "qr_code", 0.37, -0.41, 1.0)
