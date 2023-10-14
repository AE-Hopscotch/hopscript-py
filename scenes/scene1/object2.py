from builder import *


class Object(HSObject):
    type = 2
    x = 200
    y = 100
    name = "Octopus"

    @HSRule.game_starts
    def game_start(self):
        rotate(360)
        set_text('this works?', 'HSB(50,100,100)')
        with leave_a_trail('#000', 20):
            move_forward(200)
        # set_variable(self.letter, 'A')

        create_a_clone()

        with repeat_forever():
            set_position(stage.last_touch_x, stage.last_touch_y)

    # @HSRule.custom_rule('Name', 1, 2, 3)
    # def custom_rule(self): pass

    @HSRule.object_cloned
    def clone_rule(self):
        with repeat_forever():
            with leave_a_trail('#f008', 40):
                set_position(original.x_position, original.y_position)
                set_color(Color.random())

    @HSRule.shake
    def lose_collision(self):
        set_variable('self.game_over', 'TRUE')


# print(stage.TextObj)
