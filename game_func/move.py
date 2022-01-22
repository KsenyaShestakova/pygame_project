def move(player, movement, level_map, max_x, max_y):
    x, y = player.pos
    if movement == "up":
        if y > 0 and (level_map[y - 1][x] in ".@*+-|/"):
            player.move(x, y - 1)
    elif movement == "down":
        if y < max_y and (level_map[y + 1][x] in ".@*+-|/"):
            player.move(x, y + 1)
    elif movement == "left":
        if x > 0 and (level_map[y][x - 1] in ".@*+-|/"):
            player.move(x - 1, y)
    elif movement == "right":
        if x < max_x and (level_map[y][x + 1] in ".@*+-|/"):
            player.move(x + 1, y)