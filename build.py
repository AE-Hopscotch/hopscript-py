from builder import *
from pathlib import Path
from builder.stage import stage, HSStage
import importlib.util


def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_stage() -> dict:
    project_stage = stage
    project_json = {
        'scenes': [],
        'objects': [],
        'rules': [],
        'abilities': []
    }
    for scene in [path for path in Path('scenes').iterdir() if path.is_dir()]:
        scene_name = str(scene).replace('scenes/', '')
        scene_json = {'name': scene_name, 'filename': '', 'objects': []}
        for path in [path for path in scene.iterdir() if path.name.endswith('.py')]:
            module = module_from_file(path.name[:-3], path)
            stage_object: HSObject = getattr(module, 'Object')()  # hard-coded for now
            obj_json = stage_object.json()

            setattr(project_stage, path.name[:-3], stage_object)
            scene_json['objects'].append(obj_json['objectID'])
            project_json['objects'].append(obj_json)

        project_json['scenes'].append(scene_json)

    return project_json


# stage = build_stage()
# print(stage.object1())
# print(stage._objects)

