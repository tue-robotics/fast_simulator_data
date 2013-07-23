#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    table1 = W.add_object("table-1", "table_120x80x76", 0.052, -1.403, 0)
    table2 = W.add_object("table-2", "table_120x80x76", 1.941, -1.403, 0)
    bed = W.add_object("bed-1", "hospital_bed", 5.0, -1.52, 0)

    coke1 = W.add_object("coke-1", "coke", 1.941, -1.403, 0.82)
