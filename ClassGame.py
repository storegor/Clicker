import pygame
from buttons import BtcButton
from buttons import ImproveButton

class Game:
    def __init__(self):
        pygame.init()
        self.black_ = (0, 0, 0)
        self.white_ = (255, 255, 255)
        self.btc_colour_ = (255, 215, 0)
        self.w_sell_ = 100
        self.h_sell_ = 20
        self.is_work_ = True
        self.clock_ = pygame.time.Clock()
        self.coins_per_click_ = 0.001
        self.coins_autoclick_ = 0.0001
        self.price_to_update_ = 0.05
        self.upgrade_value_ = 0.0002
        self.sum_coins_ = 0
        self.fps_ = 30
        self.width_ = 800
        self.height_ = 600
        self.window_ = pygame.display.set_mode((self.width_, self.height_), pygame.SCALED)
        pygame.display.set_caption("Miner")
        self.icon_ = pygame.image.load("images/pick.png").convert_alpha()
        pygame.display.set_icon(self.icon_)
        self.bg_surf_ = pygame.image.load("images/mine_wallpaper.png").convert()
        self.window_.blit(self.bg_surf_, [0, 0])

    def create_table(self):
        pygame.draw.rect(self.window_, self.black_, (self.w_sell_ // 2 - 1, self.h_sell_, 4 * self.w_sell_, self.h_sell_ * 1 - 1))
        pygame.draw.rect(self.window_, self.white_, (self.w_sell_ * 0, self.h_sell_, self.w_sell_ // 2, self.h_sell_ + 1), 1)

        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2, self.h_sell_), (9 * (self.w_sell_ // 2) - 2, self.h_sell_), 1)
        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2, 2 * self.h_sell_), (9 * (self.w_sell_ // 2) - 2, 2 * self.h_sell_), 1)
        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 - 1, self.h_sell_ * 0), (self.w_sell_ // 2 - 1, self.h_sell_), 1)

        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 + self.w_sell_, self.h_sell_ * 0), (self.w_sell_ // 2 + self.w_sell_, 2 * self.h_sell_), 1)
        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 + 2 * self.w_sell_, self.h_sell_ * 0), (self.w_sell_ // 2 + 2 * self.w_sell_, 2 * self.h_sell_), 1)
        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 + 3 * self.w_sell_, self.h_sell_ * 0), (self.w_sell_ // 2 + 3 * self.w_sell_, 2 * self.h_sell_), 1)
        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 + 4 * self.w_sell_ - 2, self.h_sell_ * 0), (self.w_sell_ // 2 + 4 * self.w_sell_ - 2, 2 * self.h_sell_), 1)

    def coin_name_in_table(self, name, color):
        text_cell_btc = pygame.font.SysFont('arial', 15).render(name, True, color, None)
        self.window_.blit(text_cell_btc, (13, self.h_sell_))

    def create_names_of_columns(self):
        text_c_click = pygame.font.SysFont('arial', 15).render("coins / click", True, self.white_, None)
        text_update_price = pygame.font.SysFont('arial', 15).render("price to update", True, self.white_, None)
        text_autoclick = pygame.font.SysFont('arial', 15).render("autoclick", True, self.white_, None)
        text_amount = pygame.font.SysFont('arial', 15).render("amount", True, self.white_, None)
        self.window_.blit(text_c_click, (self.w_sell_ // 2 + 20, self.h_sell_ * 0))
        self.window_.blit(text_update_price, (5 * (self.w_sell_ // 2) + 10, self.h_sell_ * 0))
        self.window_.blit(text_autoclick, (3 * (self.w_sell_ // 2) + 25, self.h_sell_ * 0))
        self.window_.blit(text_amount, (7 * (self.w_sell_ // 2) + 30, self.h_sell_ * 0))

    def show_amount(self):
        amount_btc = pygame.font.SysFont('arial', 15).render(str(self.sum_coins_)[:6], False, self.btc_colour_, None)
        self.window_.blit(amount_btc, (3.5 * self.w_sell_ + 1, self.h_sell_))

    def show_autoclick(self):
        count_autoclick_btc = pygame.font.SysFont('arial', 15).render(str(self.coins_autoclick_)[:6], False, self.btc_colour_, None)
        self.window_.blit(count_autoclick_btc, (1.5 * self.w_sell_ + 1, self.h_sell_))

    def show_coins_per_click(self):
        text_btc_c_click = pygame.font.SysFont('arial', 15).render(str(self.coins_per_click_)[:6], False, self.btc_colour_, None)
        self.window_.blit(text_btc_c_click, (self.w_sell_ // 2 + 1, self.h_sell_))

    def show_price_to_update(self):
        price_to_update_text = pygame.font.SysFont('arial', 15).render(str(self.price_to_update_)[:6], False, self.btc_colour_, None)
        self.window_.blit(price_to_update_text, (2.5 * self.w_sell_ + 1, self.h_sell_))


    def autominer(self):
        self.sum_coins_ += self.coins_autoclick_

    def click_to_mine(self):
        self.sum_coins_ += self.coins_per_click_

    def run_game(self):
        self.coin_name_in_table("BTC", self.btc_colour_)
        self.create_names_of_columns()
        delay = 0
        is_pressed = False
        while self.is_work_:
            self.create_table()
            coin = BtcButton(self.window_)
            coin.draw_button()
            improve_button = ImproveButton(self.window_)
            improve_button.draw_button()
            if self.is_work_ and delay > 350:
                self.autominer()
                delay = 0
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_work_ = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.click_to_mine()
                if coin.target_.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and is_pressed:
                    self.click_to_mine()
                    is_pressed = False
                elif coin.target_.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 0 and not is_pressed:
                    is_pressed = True
                if improve_button.target_.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and is_pressed:
                    if self.sum_coins_ >= self.price_to_update_:
                        self.sum_coins_ -= self.price_to_update_
                        self.coins_autoclick_ += self.upgrade_value_
                        self.price_to_update_ *= 2
                    is_pressed = False
                elif improve_button.target_.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 0 and not is_pressed:
                    is_pressed = True
            self.show_price_to_update()
            self.show_coins_per_click()
            self.show_autoclick()
            self.show_amount()
            pygame.display.update()
        self.clock_.tick(self.fps_)
