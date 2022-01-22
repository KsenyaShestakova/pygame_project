from py_files.file_with_sprite_groups import levels_sprites


def end_lvl(camera, player):
    camera.dx = 0
    camera.dy = 0
    player.kill()
    for el in levels_sprites:
        el.kill()
