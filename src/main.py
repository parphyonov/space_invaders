import pygame as pg

pg.init()

# functions
def player_update():
    global player_x
    player_x += player_dx

def model_update():
    player_update()

def display_redraw():
    display.fill('black', (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    pg.display.update()

def event_player(event):
    pass

def event_close_application(event):
    close = False
    if event.type == pg.QUIT:
        close = True
    return close

def event_process():
    """Processes keyboard & mouse events, returns False if the app is to be closed"""
    for event in pg.event.get():
        event_player(event)
        if event_close_application(event):
            return False
    return True

# load images
icon_img = pg.image.load('src/img/ufo.png')
player_img = pg.image.load('src/img/player.png')

# window dimensions
display_width = 800
display_height = 600
display_size = (display_width, display_height)

# starting a window
display = pg.display.set_mode(display_size)
pg.display.set_caption('Space Invaders')
pg.display.set_icon(icon_img)

# player's pos
player_width = player_img.get_width()
player_height = player_img.get_height()
player_gap = 10
player_x = display_width // 2 - player_width // 2
player_y = display_height - player_height - player_gap
player_speed = 1
player_dx = player_speed

# running flag
running = True
while running:
    running = event_process()

    # objects movements
    player_x += player_dx

    # drawing inside the window
    display_redraw()
