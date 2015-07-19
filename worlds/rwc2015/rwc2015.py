#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()
    
    # Put random stuff for the navigation challenge
    '''
    import random
    if bool(random.getrandbits(1)):
        rospy.logwarn("Adding door obstacle")
        W.add_object("door", "coke",  3.0, 3.5, 0.3)
    if bool(random.getrandbits(1)):
        rospy.logwarn("Adding obstacles between desk and dinner table")
        W.add_object("a1a", "coke",  4.0, 5.0, 0.3)
        W.add_object("a1b", "coke",  4.0, 5.5, 0.3)
    if bool(random.getrandbits(1)):
        rospy.logwarn("Adding obstacle between dinner table and wall")
        W.add_object("a2a", "coke",  4.0, 7.5, 0.3)
        W.add_object("a2b", "coke",  4.0, 8.0, 0.3)
    if bool(random.getrandbits(1)):
        rospy.logwarn("Adding obstacle next to thrashbin")
        W.add_object("a3a", "coke",  6.0, 1.0, 0.3)
        W.add_object("a3b", "coke",  6.0, 1.5, 0.3)
    '''
    
    '''
    # Put stuff on the grasp shelf (manipulation challenge)
    W.add_object("coke11", "coke", 0.765, 6.63, 0.40)
    W.add_object("coke21", "coke", 0.765, 6.83, 0.40)
    
    W.add_object("coke11", "coke", 0.765, 6.63, 0.75)
    W.add_object("coke31", "coke", 0.765, 7.03, 0.75)
    
    W.add_object("coke21", "coke", 0.765, 6.83, 1.11)
    W.add_object("coke31", "coke", 0.765, 7.03, 1.11)
    '''
    
    # Put stuff on the dinner table
    #W.add_object("coke_d1", "coke",     7.500, 0.4, 0.9)
    #W.add_object("coke_d2", "tea_pack", 7.400, 0.6, 0.9)
    #W.add_object("coke_d3", "marmalade",    7.350, 0.8, 0.9)
    #W.add_object("coke_d4", "cif",      7.400, 1.0, 0.9)

    # ## Put stuff (open challenge)
    # # Right_bookcase
    # W.add_object("coke11", "sim-coke", 0.765, 6.83, 0.40)
    # W.add_object("coke12", "sim-coke", 0.765, 6.63, 0.75)
    # W.add_object("coke13", "sim-coke", 0.765, 7.03, 0.75)
    
    # # Dinnertable
    # W.add_object("coke21", "sim-coke", 3.3, 6.7, 0.75)
    # W.add_object("coke22", "sim-coke", 3.7, 6.7, 0.75)
    
    # # Counter
    # W.add_object("coke31", "sim-coke", 2.05, 4.2, 0.75)
    # W.add_object("coke32", "sim-coke", 2.05, 4.6, 0.75)
    
    

