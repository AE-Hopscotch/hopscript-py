import json

from builder import *
from build import build_stage
from web_frame import show_web_view
from builder.base import HSVariable, ability_manager

from pathlib import Path


def patch_json_encoder():
    def _default(_, obj):
        return getattr(obj.__class__, "json", _default.default)(obj)

    _default.default = json.JSONEncoder().default
    json.JSONEncoder.default = _default


if __name__ == "__main__":
    # move_forward(500)
    # change_x(200)
    intermediate_json = build_stage()
    intermediate_json['version'] = 34
    intermediate_json['playerVersion'] = '2.2.0'
    for obj in intermediate_json['objects']:
        for rule in obj['rules']:
            rule_json = rule.json(object_id = obj['objectID'], obj = obj['object'])
            intermediate_json['rules'].append(rule_json)
            index = obj['rules'].index(rule)
            obj['rules'][index] = rule_json['id']
            # Move the ability to the project abilities array
            # intermediate_json['abilities'].append(rule_json['ability'])
            del rule_json['ability']
        del obj['object']

    for ability in ability_manager.abilities.values():
        intermediate_json['abilities'].append(ability)

    # These instances are different from the ones that appear within blocks
    for info, var_id in HSVariable.instances.items():
        var_type, name = info
        var_data = {'objectIdString': var_id, 'name': name, 'type': var_type}
        intermediate_json['variables'].append(var_data)

    # for key, value in intermediate_json.items():
    #     print(key, value)

    # obj2 = stage.object2
    # obj1 = stage.object1.resolve()
    o1 = stage.get_objects()[0]
    print(o1.json())
    print(intermediate_json)
    # print('Rules', [value for key, value in obj1.__dict__.items() if not key.startswith('__')])

    patch_json_encoder()
    json_string = json.dumps(intermediate_json)
    Path('output.json').write_text(json_string)
    print('Project written to output.json')

    show_web_view(json_string)
