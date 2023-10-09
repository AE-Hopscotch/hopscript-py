from builder import *
from build import build_stage
from web_frame import show_web_view


if __name__ == "__main__":
    move_forward(500)
    change_x(200)
    intermediate_json = build_stage()
    for obj in intermediate_json['objects']:
        obj['rules'] = [] # temp

    print(intermediate_json)
    obj2 = stage.object2
    obj1 = stage.object1.resolve()
    o1 = stage.get_objects()[0]
    print(o1.json())
    # print('Rules', [value for key, value in obj1.__dict__.items() if not key.startswith('__')])
    show_web_view(intermediate_json)
