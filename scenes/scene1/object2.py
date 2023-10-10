from builder import *

class Object(HSObject):
    type = 2
    x = 200
    y = 100

    @HSRule.game_starts
    def game_start(self):
        rotate(360)
        set_text('this works?', 'HSB(50,100,100)')
        # set_variable(self.letter, 'A')

    # @HSRule.custom_rule('Name', 1, 2, 3)
    # def custom_rule(self): pass

    @HSRule.shake
    def lose_collision(self):
        set_variable('self.game_over', 'TRUE')


# print(stage.TextObj)
