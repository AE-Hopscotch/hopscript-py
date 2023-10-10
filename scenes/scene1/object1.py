from builder import *

class Object(HSObject):
    x = 512
    y = 384
    name = "Text Object Ha"
    type = 1
    text = "Not text"
    width = 75
    height = 75
    resize_scale = 1
    # filename = 'text-object.png' should be inferred

    @HSRule.game_playing
    def rotate_forever(self):
        set_variable('self.letter', 'A')
        rotate(-5)

    # @HSRule.custom_rule('Name', 1, 2, 3)
    # def custom_rule(self): pass

    @HSRule.is_touching(stage.object2, stage.object2)
    def lose_collision(self):
        set_variable('self.game_over', 'TRUE')



# print(stage.TextObj2)
