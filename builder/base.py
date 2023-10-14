from builder.util import generate_uuid, Parameter, Operator, generate_operator
from builder.variable import HSVariable, ObjectVariableContainer, HSTrait


class HSAbilityManager:
    def __init__(self):
        self.current_id = None
        self._current_time = 1
        self.abilities = {}

    def create(self, name: str = "", *, activate: bool = False):
        """Creates a new ability"""
        ability_id = generate_uuid()
        ability = {
            'abilityID': ability_id,
            'blocks': [],
            'createdAt': self._current_time
        }
        if name: ability['name'] = name
        self.abilities[ability_id] = ability
        self._current_time += 1
        if activate: self.current_id = ability_id

    @property
    def active_ability(self):
        return self.abilities[self.current_id]

    def activate(self, ability_id: str):
        if ability_id not in self.abilities:
            raise AttributeError('Ability ID does not exist')

        self.current_id = ability_id


ability_manager = HSAbilityManager()


class HSObjectRef(ObjectVariableContainer):
    def __init__(self, objs, item):
        self._stage = objs
        self._item = item
        super().__init__(HSVariable.OBJECT)

    @property
    def _obj_id(self) -> str:
        return self.resolve().json()['objectID']

    def __getattr__(self, item) -> HSVariable:
        return HSVariable(HSVariable.OBJECT, item, object_id = self._obj_id)

    def resolve(self):
        """Returns the HSObject that this object is referring to"""
        obj = self._stage.get(self._item)
        if not obj:
            raise ReferenceError(f"No object was defined in '{self._item}.py'")

        return obj


def generate_block(block_id: int, name: str, parameters: list[any] = None):
    block = {
        "block_class": "method",
        "type": block_id,
        "description": name
    }
    if parameters:
        block['parameters'] = [Parameter.from_raw(raw).json() for raw in parameters]
    # print(json.dumps(block))
    ability_manager.active_ability['blocks'].append(block)
    return block


def generate_ability(generation_fn: callable, name: str = None, obj = None):
    # No nested ability support yet
    ability_manager.create(name, activate = True)
    # with contextlib.redirect_stdout(io.StringIO()) as output:
    generation_fn(obj)

    # blocks = json.loads('[' + output.getvalue().replace('\n{', ',{') + ']')
    # print(blocks)
    # print('ALSO BLOCKS:')
    # print('   ', ability_manager.active_ability['blocks'])
    # ability = {'abilityID': generate_uuid(), 'blocks': blocks, 'createdAt': 0}
    # if name: ability['name'] = name
    ability = ability_manager.active_ability
    return ability
