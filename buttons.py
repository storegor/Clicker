import pygame


class BtcButton:
    def __init__(self, screen):
        self.btc_surf_ = pygame.image.load("images/btc_button.png").convert_alpha()
        self.btc_colour_ = (255, 215, 0)
        self.place_ = (360, 450)
        self.click_zone_ = (410, 500)
        self.screen_ = screen
        self.target_ = self.btc_surf_.get_rect(centerx=self.click_zone_[0], centery=self.click_zone_[1])

    def draw_button(self):
        self.screen_.blit(self.btc_surf_, self.place_)


class ImproveButton:
    def __init__(self, screen):
        self.w_sell_ = 100
        self.h_sell_ = 20
        self.surf_ = pygame.Surface((self.w_sell_ + 50, self.h_sell_ + 2))
        self.red_ = (255, 0, 0)
        self.white_ = (255, 255, 255)
        self.screen_ = screen
        self.target_ = self.surf_.get_rect(x=self.w_sell_ // 2 + 3 * self.w_sell_ + 20, y=self.h_sell_ + 1)


    def draw_button(self):
        self.surf_.fill(self.red_)
        text_improve_btc_auto_click = pygame.font.SysFont('arial', 17).render('update autoclick', False, self.white_, None)
        self.screen_.blit(self.surf_, (self.w_sell_ // 2 + 4 * self.w_sell_, self.h_sell_))
        self.screen_.blit(text_improve_btc_auto_click, (self.w_sell_ // 2 + 4 * self.w_sell_ + 5, self.h_sell_))
