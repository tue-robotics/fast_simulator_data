#!/usr/bin/env python
import rospy
import yaml

from os import getenv
from rospkg import RosPack
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

if __name__ == "__main__":
    # Initialize ROS node
    rospy.init_node('gazebo_simulator_object_spawner')

    # Wait until gazebo is ready to spawn sdf models
    rospy.wait_for_service('gazebo/spawn_sdf_model')
    spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)

    # Load yaml with list of objects that need to be loaded
    package_path = RosPack().get_path('fast_simulator_data')
    with open(package_path + "/sdf_test/objects_list_test.yaml", 'r') as f:
        data = yaml.safe_load(f)

    # Get path to ed_object_models/models
    model_path = getenv("ED_MODEL_PATH")

    # Iterate over objects and spawn
    for sod in data:
        # Define object pose
        object_pose = Pose()
        object_pose.position.x = sod["x"]
        object_pose.position.y = sod["y"]
        object_pose.position.z = sod["z"]

        # Load object sdf model
        with open(model_path + sod["type"] + '/model.sdf', 'r') as f:
            sdf_file = f.read()

        # Spawn object
        spawn_model_prox(sod["id"], sdf_file, "spawned_objects", object_pose, "world")
