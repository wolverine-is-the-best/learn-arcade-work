import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y, variant=1):
    """ Draw a snow person. Variant changes pose and proportions. """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Body sizes differ slightly by variant
    if variant == 1:
        size1, size2, size3 = 60, 50, 40  # Base to head
    else:
        size1, size2, size3 = 55, 50, 36  # Slightly smaller

    # Body
    arcade.draw_circle_filled(x, 60 + y, size1, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, size2, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, size3, arcade.color.WHITE)

    # Eyes
    eye_offset = 15 if variant == 1 else 10
    arcade.draw_circle_filled(x - eye_offset, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + eye_offset, 210 + y, 5, arcade.color.BLACK)

    # Nose
    arcade.draw_triangle_filled(x - 5, 205 + y, x + 5, 205 + y, x + 15, 185 + y, arcade.color.ORANGE)

    # Mouth shape varies
    if variant == 1:
        arcade.draw_arc_filled(x, 185 + y, 20, 20, arcade.color.BLACK, 0, 180)
    else:
        arcade.draw_arc_filled(x, 185 + y, 20, 20, arcade.color.BLACK, 180, 360)  # Frown

    arm_y = 140 + y

    if variant == 1:
        # Left Arm
        arcade.draw_line(x - 40, arm_y, x - 70, arm_y + 30, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x - 70, arm_y + 30, x - 95, arm_y + 50, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x - 95, arm_y + 50, x - 105, arm_y + 64, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x - 95, arm_y + 50, x - 109, arm_y + 52, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x - 95, arm_y + 50, x - 104, arm_y + 42, arcade.color.DARK_BROWN, 2)

        # Right Arm
        arcade.draw_line(x + 40, arm_y, x + 60, arm_y + 5, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x + 60, arm_y + 5, x + 85, arm_y + 15, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x + 85, arm_y + 15, x + 95, arm_y + 23, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x + 85, arm_y + 15, x + 97, arm_y + 14, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x + 85, arm_y + 15, x + 94, arm_y + 5, arcade.color.DARK_BROWN, 2)

    else:
        # Variant 2: Waving with right arm up
        # Left Arm
        arcade.draw_line(x - 40, arm_y, x - 70, arm_y - 10, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x - 70, arm_y - 10, x - 95, arm_y - 15, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x - 95, arm_y - 15, x - 105, arm_y - 2, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x - 95, arm_y - 15, x - 108, arm_y - 10, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x - 95, arm_y - 15, x - 100, arm_y - 24, arcade.color.DARK_BROWN, 2)

        # Right Arm (upward wave)
        arcade.draw_line(x + 40, arm_y + 20, x + 60, arm_y + 60, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x + 60, arm_y + 60, x + 80, arm_y + 85, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x + 80, arm_y + 85, x + 90, arm_y + 92, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x + 80, arm_y + 85, x + 92, arm_y + 80, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x + 80, arm_y + 85, x + 88, arm_y + 73, arcade.color.DARK_BROWN, 2)


def on_draw(delta_time):
    arcade.start_render()
    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140, variant=1)
    draw_snow_person(450, 180, variant=2)
    on_draw.snow_person1_x += 1


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()