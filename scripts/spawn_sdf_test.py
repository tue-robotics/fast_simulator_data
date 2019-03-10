#!/usr/bin/python
from ed_object_models import spawn_sdf_in_gazebo
from rospkg import RosPack


if __name__ == "__main__":
    # This spawns 7 coke cans, similar to fast_simulator_data/worlds/robotics_testlabs/robotics_testlabs.py
    package_path = RosPack().get_path('fast_simulator_data')
    spawn_sdf_in_gazebo.from_yaml(package_path + '/sdf_test/objects_list_test.yaml')
