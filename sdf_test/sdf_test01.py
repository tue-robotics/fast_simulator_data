#!/usr/bin/env python
import rospy

from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner',log_level=rospy.INFO)

    initial_pose = Pose()
    initial_pose.position.x = 1
    initial_pose.position.y = 1
    initial_pose.position.z = 1

    f = open('/home/kwinvdv/ros/kinetic/system/src/ed_object_models/models/test_sdf/heightmap_walls/model.sdf', 'r')
    sdff = f.read()
    f.close()

    rospy.wait_for_service('gazebo/spawn_sdf_model')
    spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
    spawn_model_prox("some_object_name", sdff, "spawned_objects", initial_pose, "world")