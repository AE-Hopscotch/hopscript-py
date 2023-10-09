from builder.traits import *
from builder.rules import *
from builder.base import HSObjectRef, generate_uuid, Parameter


class HSRule:
    def __init__(self, callback, operator):
        self._callback = callback
        self._operator = operator
        self._id = generate_uuid()
        self._ability = generate_uuid()

    def __call__(self, *args, **kwargs):
        print('called??')

    def json(self, *, object_id: str) -> dict:
        return {
            "id": self._id,
            "objectID": object_id,
            "abilityID": self._ability,
            "parameters": [Parameter.from_operator(self._operator)],
            "ruleBlockType": 6000
        }

    @classmethod
    def game_starts(cls, fn): return cls(fn, event_start())
    @classmethod
    def is_tapped(cls, ref): return lambda fn: cls(fn, event_tap(ref))
    @classmethod
    def is_touching(cls, ref1, ref2): return lambda fn: cls(fn, event_is_touching(ref1, ref2))
    @classmethod
    def is_pressed(cls, ref): return lambda fn: cls(fn, event_hold(ref))
    @classmethod
    def tilt_right(cls, fn): return cls(fn, event_tilt_right())
    @classmethod
    def tilt_left(cls, fn): return cls(fn, event_tilt_left())
    @classmethod
    def tilt_up(cls, fn): return cls(fn, event_tilt_up())
    @classmethod
    def tilt_down(cls, fn): return cls(fn, event_tilt_down())
    @classmethod
    def loud_noise(cls, fn): return cls(fn, event_loud_noise())
    @classmethod
    def shake(cls, fn): return cls(fn, event_shake())
    @classmethod
    def bump(cls, ref1, ref2): return lambda fn: cls(fn, event_bump(ref1, ref2))
    @classmethod
    def swipe_right(cls, ref): return lambda fn: cls(fn, event_swipe_right(ref))
    @classmethod
    def swipe_left(cls, ref): return lambda fn: cls(fn, event_swipe_left(ref))
    @classmethod
    def swipe_up(cls, ref): return lambda fn: cls(fn, event_swipe_up(ref))
    @classmethod
    def swipe_down(cls, ref): return lambda fn: cls(fn, event_swipe_down(ref))
    @classmethod
    def enter_the_world(cls, fn): return cls(fn, event_enter_the_world())
    @classmethod
    def tilt_right_editor(cls, fn): return cls(fn, event_tilt_right_editor())
    @classmethod
    def tilt_left_editor(cls, fn): return cls(fn, event_tilt_left_editor())
    @classmethod
    def tilt_up_editor(cls, fn): return cls(fn, event_tilt_up_editor())
    @classmethod
    def tilt_down_editor(cls, fn): return cls(fn, event_tilt_down_editor())
    @classmethod
    def not_pressed(cls, ref): return lambda fn: cls(fn, event_not_pressed(ref))
    @classmethod
    def game_playing(cls, fn): return cls(fn, event_game_playing())
    @classmethod
    def touch_ends(cls, fn): return cls(fn, event_touch_ends())
    @classmethod
    def hear_message(cls, msg): return lambda fn: cls(fn, event_hear_message(msg))
    @classmethod
    def message_matches(cls, msg): return lambda fn: cls(fn, event_message_matches(msg))
    @classmethod
    def is_not_touching(cls, ref1, ref2):
        return lambda fn: cls(fn, event_is_not_touching(ref1, ref2))


class HSVariable:
    pass


OBJECT_FILENAMES = {
    "0": "monkey", "1": "text-object", "2": "octopus", "3": "gorilla", "4": "cupcake", "5": "bear",
    "6": "dino", "7": "frog", "8": "greenman", "9": "mustache", "10": "spacepod",
    "11": "zombieBear", "12": "ghoulopus", "13": "bats", "14": "frankenrilla", "15": "jodyWitch",
    "16": "cauldron", "17": "pumpkin", "18": "broom", "19": "lantern", "20": "parrotFlying",
    "21": "mandrill", "22": "mosquito", "23": "missChief", "24": "venus", "25": "jeepers",
    "26": "banyan", "27": "stargirl", "28": "astro", "29": "chillanna", "30": "robo",
    "31": "raccoon", "32": "bird", "33": "HS_END_OF_CHARACTERS", "34": "square", "35": "circle",
    "36": "hexagon", "37": "triangle", "38": "rightTriangle", "39": "rectangle", "40": "heart",
    "41": "star", "42": "arch", "43": "parallelogram", "44": "squiggle", "45": "donut",
    "46": "tetrisZ", "47": "tetrisT", "48": "tetrisL", "49": "corner", "50": "flower",
    "51": "threeProngedBoomerang", "52": "squishedBox", "53": "bead", "54": "chevron",
    "55": "xShape", "56": "tetrisLine", "57": "HS_END_OF_SHAPES", "58": "toucan", "59": "anteater",
    "60": "crocodile", "61": "sloth", "62": "iguana", "63": "hut", "64": "penguin",
    "65": "winterQueen", "66": "shyYeti", "67": "deer", "68": "elf", "69": "snowGlobe",
    "70": "polarbear", "71": "sleigh", "72": "mistletoe", "73": "snowMan", "74": "snowflake",
    "100": "fullSizeRoundedSquare", "101": "fullSizeSquare", "102": "fullSizeCircle",
    "103": "fullSizeHexagon", "104": "fullSizeTriangle", "105": "fullSizeRightTriangle",
    "106": "fullSizeRectangle", "107": "fullSizeHeart", "108": "fullSizeStar",
    "109": "fullSizeArch", "110": "fullSizeParallelogramTall", "111": "fullSizeSquiggle",
    "112": "fullSizeDonut", "113": "fullSizeTetrisZ", "114": "fullSizeTetrisT",
    "115": "fullSizeTetrisL", "116": "fullSizeCorner", "117": "fullSizeFlower",
    "118": "fullSizeFanblade", "119": "fullSizeSquishedBox", "120": "fullSizeRoundedRightTriangle",
    "121": "fullSizeArrowRounded", "122": "fullSizeBead", "123": "fullSizeParallelogramWide",
    "124": "fullSizeChevron", "125": "fullSizeZ", "126": "fullSizeTetrisLine", "150": "hexagonV3",
    "151": "triangleV3", "152": "rectangleV3", "153": "heartV3", "154": "starV3", "155": "archV3",
    "156": "squiggleV3", "157": "tetrisZV3", "158": "tetrisTV3", "159": "tetrisLV3",
    "160": "fanbladeV3", "161": "arrowRoundedV3", "162": "beadV3", "163": "parallelogramWideV3",
    "164": "chevronV3", "165": "HS_END_OF_FULL_SIZE_SHAPES", "166": "HS_NUMBER_OF_OBJECTS",
    "3001": "crocodileJaws", "3002": "fullSize_lantern", "3003": "HS_END_OF_CHARACTERS2",
    "2e3": "image", "3e3": "HS_START_OF_CHARACTERS2", "1e4": "nil", "3e4": "edgeOfScreen"
}


class HSObject:
    x = 512
    y = 384
    name = "Text Object Ha"
    type = 1
    text = "Not text"
    width = 75
    height = 75
    resize_scale = 1
    # filename = 'text-object.png' should be inferred
    def __init__(self):
        self._id = generate_uuid()

    def __getattr__(self, item) -> HSVariable:
        return HSVariable()

    def json_parse_rule(self, rule: HSRule) -> dict:
        return rule.json(object_id = self._id)

    def json(self) -> dict:
        rules = [value for key, value in type(self).__dict__.items() if
                 type(value) == HSRule and not key.startswith('__')]  # Methods belong to class
        data = {'xPosition': self.x, 'yPosition': self.y, 'name': self.name, 'type': self.type,
                'text': self.text, 'width': str(self.width), 'height': str(self.height),
                'resizeScale': self.resize_scale, 'rules': rules, 'objectID': self._id,
                'filename': OBJECT_FILENAMES[str(self.type)] + '.png'}
        return data


class HSStage:
    _objects = None
    def __init__(self, *, width: int = 1024, height: int = 768):
        self._width = width
        self._height = height
        self._objects = {}

    def __setattr__(self, key, value):
        if self._objects is not None:
            self._objects[key] = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item) -> HSObjectRef:
        if self._objects is not None:
            return HSObjectRef(self._objects, item)
        else:
            return self.__dict__[item]

    def get_objects(self) -> list[HSObject]:
        return [obj for obj in self._objects.values()]

    @property
    def width(self): return self._width  # Never changes throughout project
    @property
    def height(self): return self._height  # Never changes throughout project
    @property
    def tilt_up(self): return stage_trait_tilt_up()
    @property
    def tilt_down(self): return stage_trait_tilt_down()
    @property
    def tilt_left(self): return stage_trait_tilt_left()
    @property
    def tilt_right(self): return stage_trait_tilt_right()
    @property
    def last_touch_x(self): return stage_trait_last_touch_x()
    @property
    def last_touch_y(self): return stage_trait_last_touch_y()
    @property
    def total_objects(self): return stage_trait_total_objects()


print('hmm')
stage = HSStage()
