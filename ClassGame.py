import pygame
from ClassButton import BtcButton
from ClassButton import ImproveButton

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
        pygame.draw.rect(self.window_, self.black_, (self.w_sell_ // 2 - 1, self.h_sell_, 3 * self.w_sell_, self.h_sell_ * 1 - 1))
        pygame.draw.rect(self.window_, self.white_, (self.w_sell_ * 0, self.h_sell_, self.w_sell_ // 2, self.h_sell_ + 1), 1)

        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2, self.h_sell_), (7 * (self.w_sell_ // 2), self.h_sell_), 1)
        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2, 2 * self.h_sell_), (7 * (self.w_sell_ // 2), 2 * self.h_sell_), 1)
        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 - 1, self.h_sell_ * 0), (self.w_sell_ // 2 - 1, self.h_sell_), 1)

        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 + self.w_sell_, self.h_sell_ * 0), (self.w_sell_ // 2 + self.w_sell_, 2 * self.h_sell_), 1)
        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 + 2 * self.w_sell_, self.h_sell_ * 0), (self.w_sell_ // 2 + 2 * self.w_sell_, 2 * self.h_sell_), 1)
        pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 + 3 * self.w_sell_, self.h_sell_ * 0), (self.w_sell_ // 2 + 3 * self.w_sell_, 2 * self.h_sell_), 1)
        #pygame.draw.line(self.window_, self.white_, (self.w_sell_ // 2 + 4 * self.w_sell_ - 2, self.h_sell_ * 0), (self.w_sell_ // 2 + 4 * self.w_sell_ - 2, 2 * self.h_sell_), 1)

    def coin_name_in_table(self, name, color):
        text_cell_btc = pygame.font.SysFont('arial', 15).render(name, True, color, None)
        self.window_.blit(text_cell_btc, (13, self.h_sell_))

    def create_names_of_columns(self):
        text_c_click = pygame.font.SysFont('arial', 15).render("coins / click", True, self.white_, None)
        #text_c_second = pygame.font.SysFont('arial', 15).render("coins / second", True, self.white_, None)
        text_autoclick = pygame.font.SysFont('arial', 15).render("autoclick", True, self.white_, None)
        text_amount = pygame.font.SysFont('arial', 15).render("amount", True, self.white_, None)
        self.window_.blit(text_c_click, (self.w_sell_ // 2 + 20, self.h_sell_ * 0))
        #self.window_.blit(text_c_second, (3 * (self.w_sell_ // 2) + 10, self.h_sell_ * 0))
        self.window_.blit(text_autoclick, (3 * (self.w_sell_ // 2) + 25, self.h_sell_ * 0))
        self.window_.blit(text_amount, (5 * (self.w_sell_ // 2) + 30, self.h_sell_ * 0))

    def autominer(self):
        self.sum_coins_ += self.coins_autoclick_

    def run_game(self):
        self.coin_name_in_table("BTC", self.btc_colour_)
        self.create_names_of_columns()
        delay = 0
        while self.is_work_:
            self.create_table()
            coin = BtcButton(self.window_)
            coin.draw_button()
            improve_button = ImproveButton(self.window_)
            improve_button.draw_button()
            if self.is_work_ and delay > 40:
                self.autominer()
                delay = 0
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_work_ = False
                    break




            pygame.display.update()
        self.clock_.tick(self.fps_)
