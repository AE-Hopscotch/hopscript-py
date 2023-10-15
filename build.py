from builder import *
from builder.util import BadObjectDataError
from pathlib import Path
from builder.stage import stage
import importlib.util


def print_format(fmt, text: str):
    print(f'\x1b[{fmt}m{text}\x1b[0m')

def load_object_from_module(module, filename: str) -> HSObject | None:
    if not hasattr(module, 'Object'):
        print_format(33, f"[WARNING] Skipping '{filename}' because it did not define 'Object'")
        return None  # allow skipping files, but just warn the user

    obj_name = f"from '{filename}'"
    constructor = getattr(module, 'Object')  # hard-coded for now
    if not isinstance(constructor, type):
        raise BadObjectDataError(f'Object {obj_name} must be a class')

    stage_object: HSObject = constructor()
    if isinstance(stage_object, HSObject):
        return stage_object

    specified_name = constructor.__dict__.get('name', None)
    obj_name = f"'{specified_name}'" if specified_name else obj_name
    raise BadObjectDataError(f'Object {obj_name} must inherit the class HSObject')


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
        'abilities': [],
        'variables': [],
        'stageSize': {'width': stage.width, 'height': stage.height}
    }
    for scene in [path for path in Path('scenes').iterdir() if path.is_dir()]:
        scene_name = str(scene).replace('scenes/', '')
        scene_json = {'name': scene_name, 'filename': '', 'objects': []}
        for path in [path for path in scene.iterdir() if path.name.endswith('.py')]:
            module = module_from_file(path.name[:-3], path)
            stage_object: HSObject = load_object_from_module(module, path.name)
            if not stage_object: continue  # skip it
            obj_json = stage_object.json()

            setattr(project_stage, path.name[:-3], stage_object)
            scene_json['objects'].append(obj_json['objectID'])
            project_json['objects'].append(obj_json)

        project_json['scenes'].append(scene_json)

    project_stage.set_loaded()
    return project_json


# stage = build_stage()
# print(stage.object1())
# print(stage._objects)

