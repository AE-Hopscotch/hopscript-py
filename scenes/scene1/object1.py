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

    @HSRule.game_starts
    def start_game(self):
        set_variable(original.letter, 1)
        set_variable(game.letter, 'A')
        set_variable(user.letter, 'B')
        set_variable(product.letter, 'C')
        set_variable(local.letter, 'D')
        set_variable(stage.object2.letter, 'E')
        save_input(self.letter, 'Enter a value (true) or zero (false)')
        show_popup(game.letter)
        show_popup(user.letter)
        show_popup(product.letter)
        show_popup(local.letter)
        show_popup(stage.object2.letter)

        set_variable(local.letter, 0)
        with repeat(5):
            change_variable(local.letter, 1)
            show_popup(local.letter)

        with repeat_forever():
            grow(1)
            with check_once_if(condition_greater_than(self.size, 800)):
                wait(10000)


    @HSRule.game_playing
    def rotate_forever(self):
        rotate(-5)
        with check_once_if(condition_equals(self.letter, 'A')):
            set_text('I can grow', 'HSB(100, 100, 100)')
        with ELSE():
            set_text('An "else" condition working??', 'HSB(0, 100, 100)')
            with check_once_if(1):
                set_color('#0088ff')

    # @HSRule.custom_rule('Name', 1, 2, 3)
    # def custom_rule(self): pass

    @HSRule.is_touching(stage.object2, stage.object2)
    def lose_collision(self):
        set_variable('self.game_over', 'TRUE')



# print(stage.TextObj2)
