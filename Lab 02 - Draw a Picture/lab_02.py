import arcade



arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# --- Draw the barn ---

arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BISQUE)
arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)
arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 260, 20, 30, arcade.color.BLACK)
arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)
arcade.draw_rectangle_filled(190, 220, 100, 100, arcade.color.BLACK_BEAN)
arcade.draw_rectangle_filled(190, 280, 180, 5, arcade.color.BLACK)

arcade.draw_polygon_filled([[20, 350],
                            [100, 470],
                            [280, 470],
                            [360, 340]],
                            arcade.color.BROWN)
arcade.draw_triangle_filled(100, 470, 280, 470, 190, 500, arcade.color.BROWN)
arcade.draw_rectangle_filled(130, 440, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(130, 440, 20, 30, arcade.color.BLACK)
arcade.draw_rectangle_filled(250, 440, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(250, 440, 20, 30, arcade.color.BLACK)
arcade.draw_rectangle_filled(175, 310, 30, 60, arcade.color.LIGHT_BROWN)
arcade.draw_rectangle_filled(205, 310, 30, 60, arcade.color.LIGHT_BROWN)
arcade.draw_rectangle_outline(175, 310, 30, 60, arcade.color.BLACK, 2)
arcade.draw_rectangle_outline(205, 310, 30, 60, arcade.color.BLACK, 2)


# --- Draw picket fence ---

def draw_picket_fence(x_start, y_start, fence_height, rail_width, rail_spacing, num_rails, num_pickets):
    """
    Draws a white picket fence with customizable parameters.

    :param x_start: X-coordinate to start drawing the fence
    :param y_start: Y-coordinate to start drawing the fence
    :param fence_height: Total height of the fence (affects picket height)
    :param rail_width: Thickness of each horizontal rail
    :param rail_spacing: Vertical spacing between rails
    :param num_rails: Number of horizontal rails (top to bottom)
    :param num_pickets: Number of vertical pickets
    """
    picket_width = 20
    spacing = 10  # horizontal space between pickets

    total_spacing = spacing * (num_pickets - 1)
    total_picket_width = picket_width * num_pickets
    fence_width = total_picket_width + total_spacing

    picket_height = fence_height - (rail_spacing * (num_rails - 1))

    # Draw rails
    for i in range(num_rails):
        rail_y = y_start + i * rail_spacing
        arcade.draw_lrtb_rectangle_filled(
            x_start, x_start + fence_width,
            rail_y + rail_width, rail_y,
            arcade.color.WHITE
        )

    # Draw pickets
    x_position = x_start
    top_y = y_start + rail_spacing * (num_rails - 1) + rail_width

    for _ in range(num_pickets):
        # Rectangle part
        arcade.draw_lrtb_rectangle_filled(
            x_position, x_position + picket_width,
            top_y, top_y - picket_height,
            arcade.color.WHITE
        )

        # Triangle top
        triangle = [
            [x_position, top_y],
            [x_position + picket_width, top_y],
            [x_position + picket_width / 2, top_y + 20]
        ]
        arcade.draw_polygon_filled(triangle, arcade.color.WHITE)

        x_position += picket_width + spacing

# --- Draw Fence ---
draw_picket_fence(
    x_start=0,
    y_start=120,
    fence_height=150,
    rail_width=10,
    rail_spacing=30,
    num_rails=3,
    num_pickets=27  # Customize this to control number of pickets
)

# --- Draw the tractor ---

arcade.draw_rectangle_filled(600, 120, 140, 70, arcade.color.GRAY)
arcade.draw_rectangle_filled(590, 105, 90, 40, arcade.color.BLACK)
arcade.draw_rectangle_filled(580, 175, 10, 40, arcade.color.BLACK)
arcade.draw_circle_filled(490, 100, 45, arcade.color.BLACK)
arcade.draw_circle_filled(490, 100, 40, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(490, 100, 35, arcade.color.OLD_LACE)
arcade.draw_circle_filled(490, 100, 10, arcade.color.RED)
arcade.draw_circle_filled(650, 85, 30, arcade.color.BLACK)
arcade.draw_circle_filled(650, 85, 25, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(650, 85, 18, arcade.color.OLD_LACE)
arcade.draw_circle_filled(650, 85, 5, arcade.color.RED)
arcade.draw_circle_filled(580, 220, 12, arcade.color.GRAY)
arcade.draw_circle_filled(570, 240, 10, (130, 130, 130))  # Custom Shade 1
arcade.draw_circle_filled(560, 260, 8, (150, 150, 150))  # Custom Shade 2
arcade.draw_circle_filled(550, 280, 6, (180, 180, 180))  # Custom Shade 3
arcade.draw_circle_filled(540, 300, 4, arcade.color.LIGHT_GRAY)
arcade.draw_rectangle_filled(525, 165, 35, 20, arcade.color.MAROON)
arcade.draw_rectangle_filled(510, 180, 10, 25, arcade.color.MAROON, -12)

# --- Finish drawing ---
arcade.finish_render()
arcade.run()