#!/usr/bin/env python
import rospy

from rospkg import RosPack
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner',log_level=rospy.INFO)

    initial_pose = Pose()
    initial_pose.position.x = 1
    initial_pose.position.y = 1
    initial_pose.position.z = 1

    model_path = RosPack().get_path('ed_object_models')
    model_name = '/models/test_sdf/heightmap_walls'

    with open(model_path + model_name + '/model.sdf', 'r') as f:
        sdff = f.read()

    rospy.wait_for_service('gazebo/spawn_sdf_model')
    spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
    spawn_model_prox("some_object_name", sdff, "spawned_objects", initial_pose, "world")
