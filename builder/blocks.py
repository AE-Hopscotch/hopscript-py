from builder.base import generate_block

def wait_til_timestamp(value):
    return generate_block(19, 'Wait Til Timestamp', [value])


def none(value):
    return generate_block(22, 'None', [value])


def move_forward(amount):
    return generate_block(23, 'Move', [amount])


def rotate(degrees):
    return generate_block(24, 'Rotate', [degrees])


# Turn this into a context manager (with leave_a_trail)
def leave_a_trail(value):
    return generate_block(26, 'Leave A Trail', [value])


def change_x(amount):
    return generate_block(27, 'Change X', [amount])


def change_y(amount):
    return generate_block(28, 'Change Y', [amount])


def scale(percent):
    return generate_block(29, 'Scale', [percent])


def clear():
    return generate_block(30, 'Clear')


def set_trail_width(width):
    return generate_block(31, 'Set Trail Width', [width])


def set_trail_color(color):
    return generate_block(32, 'Set Trail Color', [color])


def change_pose():
    return generate_block(33, 'Change Pose')


def set_speed(speed):
    return generate_block(34, 'Set Speed', [speed])


def wait(milliseconds):
    return generate_block(35, 'Wait', [milliseconds])


def set_opacity(percent):
    return generate_block(36, 'Set Opacity', [percent])


def pen_down():
    return generate_block(37, 'Pen Down')


def pen_up():
    return generate_block(38, 'Pen Up')


def set_angle(degrees):
    return generate_block(39, 'Set Angle', [degrees])


def set_text(text, color):
    return generate_block(40, 'Set Text', [text, color])


def set_position(x, y):
    return generate_block(41, 'Set Position', [x, y])


def send_to_back():
    return generate_block(42, 'Send To Back')


def bring_to_front():
    return generate_block(43, 'Bring To Front')


def change_variable(var, value):
    return generate_block(44, 'Change Variable', [var, value])


def set_variable(var, value):
    return generate_block(45, 'Set Variable', [var, value])


def move_with_trail(distance):
    return generate_block(46, 'Move With Trail', [distance])


def set_invisibility(percent):
    return generate_block(47, 'Set Invisibility', [percent])


def grow(percent):
    return generate_block(48, 'Grow', [percent])


def shrink(percent):
    return generate_block(49, 'Shrink', [percent])


def flip():
    return generate_block(50, 'Flip')


def set_size(percent):
    return generate_block(51, 'Set Size', [percent])


def play_sound(sound, wait_ms):
    return generate_block(52, 'Play Sound', [sound, wait_ms])


def make_a_clone(times):
    return generate_block(53, 'Make A Clone', [times])


def set_color(color):
    return generate_block(54, 'Set Color', [color])


def destroy():
    return generate_block(55, 'Destroy')


def set_image(image):
    return generate_block(56, 'Set Image', [image])


def set_width_and_height(width, height):
    return generate_block(57, 'Set Width And Height', [width, height])


def set_z_index(index):
    return generate_block(58, 'Set Z Index', [index])


def set_origin(x, y):
    return generate_block(59, 'Set Origin', [x, y])


def set_center(x, y):
    return generate_block(60, 'Set Center', [x, y])


def wait_seconds(seconds):
    return generate_block(61, 'Wait Seconds', [seconds])


def play_sound_seconds(sound, wait_sec):
    return generate_block(62, 'Play Sound', [sound, wait_sec])


def save_input(var, prompt):
    return generate_block(63, 'Save Input', [var, prompt])


def set_text_to_input(color, prompt):
    return generate_block(64, 'Set Text To Input', [color, prompt])


def play_note(note, rhythm):
    return generate_block(65, 'Play Note', [note, rhythm])


def set_tempo(tempo):
    return generate_block(66, 'Set Tempo', [tempo])


def set_instrument(instrument):
    return generate_block(67, 'Set Instrument', [instrument])


def open_project(uuid):
    return generate_block(68, 'Open Project', [uuid])


def comment(text):
    return generate_block(69, 'Comment', [text])


def set_background(color):
    return generate_block(70, 'Set Background', [color])


def set_trail_cap(cap):
    return generate_block(71, 'Set Trail Cap', [cap])


def show_popup(text):
    return generate_block(72, 'Show Popup', [text])


def set_trail_opacity(percent):
    return generate_block(73, 'Set Trail Opacity', [percent])


def repeat(times):
    return generate_block(120, 'Repeat', [times])


def repeat_forever():
    return generate_block(121, 'Repeat Forever')


def check_once_if(condition):
    return generate_block(122, 'Check Once If', [condition])


def ability(*args):
    return generate_block(123, 'Ability', [*args])


def check_if_else(condition):
    return generate_block(124, 'Check If Else', [condition])


def change_scene(scene):
    return generate_block(125, 'Change Scene', [scene])


def broadcast_message(message):
    return generate_block(126, 'Broadcast Message', [message])


def request_seeds(amount, product):
    return generate_block(127, 'Request Seeds', [amount, product])

