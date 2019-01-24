#!/usr/bin/python
from ed_object_models import spawn_sdf_in_gazebo

if __name__ == "__main__":
    # This spawns 7 coke cans, similar to fast_simulator_data/worlds/robotics_testlabs/robotics_testlabs.py
    spawn_sdf_in_gazebo.from_yaml('/sdf_test/objects_list_test.yaml')
