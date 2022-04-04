import pygame

pygame.init()


kLTC_COLOR = (192, 192, 192)
kBLACK = (0, 0, 0)
kFPS = 30
kBTC_COLOR = (255, 215, 0)
kCOIN_PLACE = (360, 450)
kWHITE = (255, 255, 255)
kRED = (255, 0, 0)
kW = 800
kH = 600
kCELL_W = 100
kCELL_H = 20

screen = pygame.display.set_mode((kW, kH), pygame.SCALED)
pygame.display.set_caption("Miner")
bg_surf = pygame.image.load("images/mine_wallpaper.png").convert()
btc_surf = pygame.image.load("images/btc_button.png").convert_alpha()
btc_button = btc_surf.get_rect(centerx=kCOIN_PLACE[0]+50, centery=kCOIN_PLACE[1] + 50)
ltc_surf = pygame.image.load("images/litecoin_button.png").convert_alpha()
btc_surf_revers = pygame.image.load("images/btc_button_revers.png").convert_alpha()
ltc_surf_revers = pygame.image.load("images/litecoin-revers_new.png").convert_alpha()
icon = pygame.image.load("images/pick.png").convert_alpha()
pygame.display.set_icon(icon)
font_switch_coin = pygame.font.SysFont('arial', 20)
text_switch_coin = font_switch_coin.render("press TAB to switch the coin", True, kWHITE, None)
improve_button_surf = pygame.Surface((kCELL_W, kCELL_H))
improve_button_surf.fill(kRED)
improve_btc_autoclick = improve_button_surf.get_rect(x=kCELL_W // 2 + 4 * kCELL_W, y=kCELL_H)
text_improve_btc_auto_click = pygame.font.SysFont('arial', 15).render('improve autoclick', False, kWHITE, None)

btc_line = pygame.draw.line(screen, kWHITE, (kCELL_W // 2, kCELL_H), (9 * (kCELL_W // 2) - 3, kCELL_H), 1)
ltc_line = pygame.draw.line(screen, kWHITE, (kCELL_W // 2, 2 * kCELL_H), (9 * (kCELL_W // 2) - 3, 2 * kCELL_H - 1), 1)
last_line = pygame.draw.line(screen, kWHITE, (kCELL_W // 2, 3 * kCELL_H), (9 * (kCELL_W // 2) - 3, 3 * kCELL_H - 1), 1)
first_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2, kCELL_H * 0), (kCELL_W // 2, 3 * kCELL_H - 2), 1)
second_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2 + kCELL_W, kCELL_H * 0), (kCELL_W // 2 + kCELL_W, 3 * kCELL_H - 2), 1)
third_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2 + 2 * kCELL_W, kCELL_H * 0), (kCELL_W // 2 + 2 * kCELL_W, 3 * kCELL_H - 2), 1)
fourth_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2 + 3 * kCELL_W, kCELL_H * 0), (kCELL_W // 2 + 3 * kCELL_W, 3 * kCELL_H - 2), 1)
last_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2 + 4 * kCELL_W, kCELL_H * 0), (kCELL_W // 2 + 4 * kCELL_W, 3 * kCELL_H - 2), 1)

#btc_cell
cell_btc = pygame.draw.rect(bg_surf, kWHITE, (kCELL_W * 0, kCELL_H, kCELL_W // 2, kCELL_H), 1)
font_cell_btc = pygame.font.SysFont('arial', 15)
text_cell_btc = font_cell_btc.render("BTC", True, kBTC_COLOR, None)
#ltc_cell
cell_ltc = pygame.draw.rect(bg_surf, kWHITE, (kCELL_W * 0, kCELL_H * 2 - 1, kCELL_W // 2, kCELL_H), 1)
font_cell_ltc = pygame.font.SysFont('arial', 15)
text_cell_ltc = font_cell_btc.render("LTC", True, kLTC_COLOR, None)

c_click_column = pygame.draw.rect(screen, kBLACK, (kCELL_W // 2 - 1, kCELL_H, kCELL_W, kCELL_H * 2 - 1))
c_second_column = pygame.draw.rect(screen, kBLACK, (3 * (kCELL_W // 2) - 2, kCELL_H, kCELL_W, kCELL_H * 2 - 1))
autoclick_column = pygame.draw.rect(screen, kBLACK, (5 * (kCELL_W // 2) - 2, kCELL_H, kCELL_W, kCELL_H * 2 - 1))
amount_column = pygame.draw.rect(screen, kBLACK, (7 * (kCELL_W // 2) - 2, kCELL_H, kCELL_W, kCELL_H * 2 - 1))


font_c_click = pygame.font.SysFont('arial', 15)
text_c_click = font_c_click.render("coins / click", True, kWHITE, None)


font_c_second = pygame.font.SysFont('arial', 15)
text_c_second = font_c_second.render("coins / second", True, kWHITE, None)


font_autoclick = pygame.font.SysFont('arial', 15)
text_autoclick = font_c_second.render("autoclick", True, kWHITE, None)



font_amount = pygame.font.SysFont('arial', 15)
text_amount = font_c_second.render("amount", True, kWHITE, None)



screen.blit(bg_surf, [0, 0])
screen.blit(btc_surf, kCOIN_PLACE)
screen.blit(improve_button_surf, (kCELL_W // 2 + 4 * kCELL_W, kCELL_H))
screen.blit(text_improve_btc_auto_click, (kCELL_W // 2 + 4 * kCELL_W, kCELL_H))
screen.blit(text_switch_coin, (kCOIN_PLACE[0] - 60, kCOIN_PLACE[1] + 100))
screen.blit(text_cell_btc, (13, kCELL_H))
screen.blit(text_cell_ltc, (13, kCELL_H * 2))
screen.blit(text_c_click, (kCELL_W // 2 + 20, kCELL_H * 0))
screen.blit(text_c_second, (3 * (kCELL_W // 2) + 10, kCELL_H * 0))
screen.blit(text_autoclick, (5 * (kCELL_W // 2) + 25, kCELL_H * 0))
screen.blit(text_amount, (7 * (kCELL_W // 2) + 30, kCELL_H * 0))

pygame.display.update()
clock = pygame.time.Clock()
is_work = True
sum_btc = 0
btc_per_click = 0.001
btc_autoclick = 0.0001

def mine_coins():
    global sum_btc
    global btc_per_click
    sum_btc += btc_per_click

def autominer():
    global sum_btc
    global btc_autoclick
    global amount_column
    global font_c_second
    sum_btc += btc_autoclick
    pygame.draw.rect(screen, kBLACK, (7 * (kCELL_W // 2) - 2, kCELL_H, kCELL_W, kCELL_H * 2 - 1))
    pygame.draw.line(screen, kWHITE, (kCELL_W // 2, kCELL_H), (9 * (kCELL_W // 2) - 3, kCELL_H), 1)
    pygame.draw.line(screen, kWHITE, (kCELL_W // 2, 2 * kCELL_H - 1), (9 * (kCELL_W // 2) - 3, 2 * kCELL_H - 1), 1)
    pygame.draw.line(screen, kWHITE, (kCELL_W // 2, 3 * kCELL_H - 2), (9 * (kCELL_W // 2) - 3, 3 * kCELL_H - 2), 1)
    pygame.draw.line(screen, kWHITE, (kCELL_W // 2 + 3 * kCELL_W, kCELL_H * 0), (kCELL_W // 2 + 3 * kCELL_W, 3 * kCELL_H - 2), 1)
    amount_btc = pygame.font.SysFont('arial', 15).render(str(sum_btc)[:6], False, kBTC_COLOR, None)
    screen.blit(amount_btc, (3.5 * kCELL_W + 1, kCELL_H))
    pygame.display.update()

counter = 0
while is_work:
    if is_work and counter > 40:
        autominer()
        counter = 0
    counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_work = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mine_coins()
        if btc_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
            mine_coins()
        if improve_btc_autoclick.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
            if sum_btc >= 0.05:
                sum_btc -= 0.05
                btc_autoclick += 0.0003

        amount_btc = pygame.font.SysFont('arial', 15).render(str(sum_btc)[:6], False, kBTC_COLOR, None)
        text_btc_c_click = pygame.font.SysFont('arial', 15).render(str(btc_per_click)[:6], False, kBTC_COLOR, None)

        amount_column = pygame.draw.rect(screen, kBLACK, (7 * (kCELL_W // 2) - 2, kCELL_H, kCELL_W, kCELL_H * 2 - 1))
        c_click_column = pygame.draw.rect(screen, kBLACK, (kCELL_W // 2 - 1, kCELL_H, kCELL_W, kCELL_H * 2 - 1))
        c_second_column = pygame.draw.rect(screen, kBLACK, (3 * (kCELL_W // 2) - 2, kCELL_H, kCELL_W, kCELL_H * 2 - 1))
        autoclick_column = pygame.draw.rect(screen, kBLACK, (5 * (kCELL_W // 2) - 2, kCELL_H, kCELL_W, kCELL_H * 2 - 1))

        btc_line = pygame.draw.line(screen, kWHITE, (kCELL_W // 2, kCELL_H), (9 * (kCELL_W // 2) - 3, kCELL_H), 1)
        ltc_line = pygame.draw.line(screen, kWHITE, (kCELL_W // 2, 2 * kCELL_H - 1), (9 * (kCELL_W // 2) - 3, 2 * kCELL_H - 1), 1)
        last_line = pygame.draw.line(screen, kWHITE, (kCELL_W // 2, 3 * kCELL_H - 2), (9 * (kCELL_W // 2) - 3, 3 * kCELL_H - 2), 1)

        first_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2, kCELL_H * 0), (kCELL_W // 2, 3 * kCELL_H - 2), 1)
        second_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2 + kCELL_W, kCELL_H * 0), (kCELL_W // 2 + kCELL_W, 3 * kCELL_H - 2), 1)
        third_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2 + 2 * kCELL_W, kCELL_H * 0), (kCELL_W // 2 + 2 * kCELL_W, 3 * kCELL_H - 2), 1)
        fourth_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2 + 3 * kCELL_W, kCELL_H * 0), (kCELL_W // 2 + 3 * kCELL_W, 3 * kCELL_H - 2), 1)
        last_bar = pygame.draw.line(screen, kWHITE, (kCELL_W // 2 + 4 * kCELL_W - 2, kCELL_H * 0), (kCELL_W // 2 + 4 * kCELL_W - 2, 3 * kCELL_H - 2), 1)

        count_autoclick_btc = pygame.font.SysFont('arial', 15).render(str(btc_autoclick)[:6], False, kBTC_COLOR, None)

        screen.blit(count_autoclick_btc, (2.5 * kCELL_W + 1, kCELL_H))
        screen.blit(amount_btc, (3.5 * kCELL_W + 1, kCELL_H))
        screen.blit(text_btc_c_click, (kCELL_W // 2 + 1, kCELL_H))
        pygame.display.update()

    clock.tick(kFPS)



