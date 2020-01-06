from pyglet import resource
from pyglet.image import ImageGrid, Animation, load


class Image:
    resource.path.append("../res/image")
    resource.reindex()

    try:
        background = resource.image("background.png")
        menu = resource.image("menu.png")
        mario = resource.image("mario.png")
        sprite_set = resource.image("sprite_set.png")
    except resource.ResourceNotFoundException:
        raise SystemExit("cannot find images!")

    sprite_set_small = ImageGrid(sprite_set, 20, 20)
    sprite_set_big = ImageGrid(sprite_set, 10, 20)

    # mario
    mario_walk_right_small = [sprite_set_small[(18, 0)], sprite_set_small[(18, 1)], sprite_set_small[(18, 2)]]
    mario_walk_left_small = [image.get_transform(flip_x=True) for image in mario_walk_right_small]

    mario_walk_right_big = [sprite_set_big[(8, 0)], sprite_set_big[(8, 1)], sprite_set_big[(8, 2)]]
    mario_walk_left_big = [image.get_transform(flip_x=True) for image in mario_walk_right_big]

    mario_walk_right_fire = [sprite_set_big[(7, 0)], sprite_set_big[(7, 1)], sprite_set_big[(7, 2)]]
    mario_walk_left_fire = [image.get_transform(flip_x=True) for image in mario_walk_right_fire]

    mario_walk = [[mario_walk_right_small, mario_walk_left_small],
                  [mario_walk_right_big, mario_walk_left_big],
                  [mario_walk_right_fire, mario_walk_left_fire]]

    mario_jump_right_small = sprite_set_small[(18, 4)]
    mario_jump_left_small = mario_jump_right_small.get_transform(flip_x=True)

    mario_jump_right_big = sprite_set_big[(8, 4)]
    mario_jump_left_big = mario_jump_right_big.get_transform(flip_x=True)

    mario_jump_right_fire = sprite_set_big[(7, 4)]
    mario_jump_left_fire = mario_jump_right_fire.get_transform(flip_x=True)

    mario_jump = [[mario_jump_right_small, mario_jump_left_small],
                  [mario_jump_right_big, mario_jump_left_big],
                  [mario_jump_right_fire, mario_jump_left_fire]]

    mario_stand_right_small = sprite_set_small[(18, 6)]
    mario_stand_left_small = mario_stand_right_small.get_transform(flip_x=True)

    mario_stand_right_big = sprite_set_big[(8, 6)]
    mario_stand_left_big = mario_stand_right_big.get_transform(flip_x=True)

    mario_stand_right_fire = sprite_set_big[(7, 6)]
    mario_stand_left_fire = mario_stand_right_fire.get_transform(flip_x=True)

    mario_stand = [[mario_stand_right_small, mario_stand_left_small],
                   [mario_stand_right_big, mario_stand_left_big],
                   [mario_stand_right_fire, mario_stand_left_fire]]

    mario_die = sprite_set_small[(18, 5)]

    mario_walk_to_castle = [Animation.from_image_sequence(mario_walk_right_small, 0.1),
                            Animation.from_image_sequence(mario_walk_right_big, 0.1),
                            Animation.from_image_sequence(mario_walk_right_fire, 0.1)]

    mario_lower_flag_small = [sprite_set_small[(18, 7)], sprite_set_small[(18, 8)]]
    mario_lower_flag_big = [sprite_set_big[(8, 7)], sprite_set_big[(8, 8)]]
    mario_lower_flag_fire = [sprite_set_big[(7, 7)], sprite_set_big[(7, 8)]]

    mario_lower_flag = [Animation.from_image_sequence(mario_lower_flag_small, 0.2),
                        Animation.from_image_sequence(mario_lower_flag_big, 0.2),
                        Animation.from_image_sequence(mario_lower_flag_fire, 0.2)]

    mario_lower_flag_turn_around = [sprite_set_small[(18, 8)].get_transform(flip_x=True),
                                    sprite_set_big[(8, 8)].get_transform(flip_x=True),
                                    sprite_set_big[(7, 8)].get_transform(flip_x=True)]

    # prop
    normal_mushroom = sprite_set_small[(7, 0)]
    life_mushroom = sprite_set_small[(7, 1)]

    frames = [sprite_set_small[(5, 0)], sprite_set_small[(5, 1)]]
    fire_flower_blink = Animation.from_image_sequence(frames, 0.3)

    # enemy
    frames = [sprite_set_small[(10, 7)], sprite_set_small[(10, 8)]]
    goomba_move = Animation.from_image_sequence(frames, 0.3)
    goomba_die = sprite_set_small[(10, 9)]

    frames = [sprite_set_big[(5, 0)], sprite_set_big[(5, 1)]]
    koopa_move = Animation.from_image_sequence(frames, 0.3)
    koopa_die = sprite_set_small[(10, 4)]

    # others
    # cliff is a total transparent image
    cliff = sprite_set_small[(2, 2)]

    coin = sprite_set_big[(3, 4)]

    flag = sprite_set_small[(0, 0)]
    castle_flag = sprite_set_small[(2, 0)]

    normal_brick = sprite_set_small[(0, 3)]
    unknown_brick = sprite_set_small[(0, 6)]

    try:
        normal_brick2 = load("../res/image/brick.png")
    except Exception as e:
        raise SystemExit(e)
