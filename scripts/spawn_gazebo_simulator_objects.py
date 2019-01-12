#!/usr/bin/env python
import rospy
import yaml
import os
import glob

from rospkg import RosPack
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

if __name__ == '__main__':
    # Initialize ROS node
    rospy.init_node('gazebo_simulator_object_spawner')

    # Wait until gazebo is ready to spawn sdf models
    rospy.wait_for_service('gazebo/spawn_sdf_model')
    spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)

    # Load yaml with list of objects that need to be loaded
    package_path = RosPack().get_path('fast_simulator_data')
    with open(package_path + '/sdf_test/objects_list_test2.yaml', 'r') as f:
        data = yaml.safe_load(f)

    # Get paths in $GAZEBO_MODEL_PATH
    model_paths = os.environ['GAZEBO_MODEL_PATH'].split(os.pathsep)

    # Iterate over objects and spawn
    for sod in data:
        # Define object pose
        object_pose = Pose()
        object_pose.position.x = sod['x']
        object_pose.position.y = sod['y']
        object_pose.position.z = sod['z']

        # Search for model folder in $GAZEBO_MODEL_PATH
        for path in model_paths:
            if os.path.isdir(path + '/' + sod['type']):
                model_path = path + '/' + sod['type']

        # Return error when folder could not be found
        try:
            model_path
        except NameError:
            print('Could not find model in GAZEBO_MODEL_PATH.')
            break

        # Search for sdf file
        if os.path.isfile(model_path + '/model.sdf'):
            sdf_model_path = model_path + '/model.sdf'
        else:
            # If is no model.sdf and there are multiple sdf files, return the last
            # alphabetically which is assumed to be for the highest sdf version.
            sdf_model_path = sorted(glob.glob(model_path + '/*.sdf'))[-1]

        # Return error when no sdf file could be found
        try:
            sdf_model_path
        except NameError:
            print('No sdf model found.')
            break

        with open(sdf_model_path, 'r') as f:
            sdf_file = f.read()

        # Spawn object
        spawn_model_prox(sod['id'], sdf_file, 'spawned_objects', object_pose, 'world'')
