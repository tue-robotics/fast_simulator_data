#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    #Ballroom
    W.add_object("t1", "table_120x80x76", 10, 12, 0, 0, 0, 1.57)
    W.add_object("t2", "table_120x80x76", 10, 10.5, 0, 0, 0, 1.57)
    W.add_object("t3", "table_120x80x76", 10, 9, 0, 0, 0, 1.57)

    W.add_object("t4", "table_120x80x76", 12, 10.5, 0, 0, 0, 1.57)
    W.add_object("t5", "table_120x80x76", 12, 9, 0, 0, 0, 1.57)

    W.add_object("t6", "table_120x80x76", 14, 10.5, 0, 0, 0, 1.57)
    W.add_object("t7", "table_120x80x76", 14, 9, 0, 0, 0, 1.57)

    # Offices
    W.add_object("office_table1", "hanging-table", 14, 20.1, 0, 0, 0, 0)
    W.add_object("office_table2", "hanging-table", 15, 20.1, 0, 0, 0, 0)

    W.add_object("office_table3", "hanging-table", 8.5, 25.8, 0, 0, 0, 0)

    W.add_object("office_table4", "table", 8, 22, 0, 0, 0, 0)
    W.add_object("office_table5", "table", 8, 21, 0, 0, 0)
    W.add_object("office_table6", "table", 8, 20, 0, 0, 0)
    W.add_object("office_table7", "table", 8, 19, 0, 0, 0)
    W.add_object("office_table8", "table", 8, 18, 0, 0, 0)

    W.add_object("office_table9", "table", 11, 22, 0, 0, 0, 0)
    W.add_object("office_table10", "table", 11, 21, 0, 0, 0)
    W.add_object("office_table11", "table", 11, 20, 0, 0, 0)
    W.add_object("office_table12", "table", 11, 19, 0, 0, 0)
    W.add_object("office_table13", "table", 11, 18, 0, 0, 0)

    W.add_object("office_table15", "hanging-table", 5.9, 25, 0, 0, 0)
    W.add_object("bisc", "rwc2014.biscuits", 9.2,4.2, 0,0)
