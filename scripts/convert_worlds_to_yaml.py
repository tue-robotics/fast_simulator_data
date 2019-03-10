#!/usr/bin/python
import os
import string
import yaml


def parseStr(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return x


parentdir = "../worlds"

for subdir in sorted(os.listdir(parentdir)):
    dir_path = os.path.join(parentdir, subdir)
    if not os.path.isdir(dir_path):
        continue

    for file in sorted(os.listdir(dir_path)):
        file_path = os.path.join(dir_path, file)
        # Only read files
        if not os.path.isfile(file_path):
            continue
        # Don't read data summary files
        if not os.path.splitext(file_path)[1] == ".py":
            continue

        yaml_file = os.path.join(os.path.dirname(file_path), "objects.yaml")

        with open(file_path, "r") as f:
            lines = f.readlines()

        lines = [l.strip() for l in lines]
        object_lines = []
        for line in lines:
            if line.startswith("W.add_object"):
                line2 = map(parseStr, line.lstrip("W.add_object(").rstrip(")").split(","))
                object_lines.append([x.strip().strip('"') if isinstance(x, str) else x for x in line2])

        yaml_list = []
        yaml_keys = ["id", "type", "x", "y", "z", "rx", "ry", "rz"]
        for o in object_lines:
            yaml_list.append({yaml_keys[i]: o[i] for i in range(len(o))})

        output_list = ["- {}".format(yaml.safe_dump(item, default_flow_style=True, indent=4)) for item in yaml_list]
        with open(yaml_file, "w") as f:
            f.writelines(output_list)
