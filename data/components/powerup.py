import pygame
import random

class Powerup:
    def __init__(self, x, y, img):
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(random.randint(-1, 1), 2).normalize()
        self.img = img

    #Function Update
    #Function Update moves the spawned powerup, checks if it collided with the paddle, and deletes it if it drops below the paddle
    #Function Update also draws the powerup onto the screen
    def update(self, delta, paddle, pu_list):
        self.move(delta)
        self.check_activated(paddle, pu_list)
        if self.position.y > PADDLE_Y:
            self.delete(pu_list)
        SCREEN.blit(self.img, self.position)

    #Function Move
    #Function Move reverses the spawned powerups x velocity if it hits a wall and calculates its new position on the screen for the current frame
    def move(self, delta):
        self.position += self.velocity * delta * 0.25
        if self.position.x <= 0:
            self.velocity.x *= -1
        elif self.position.x + powerup_health_img.get_width() >= SCREEN_WIDTH:
            self.velocity.x *= -1

    #Function Check Activated
    #Function Check Activated checks if the spawned powerup collides with the paddle, and if it does it activates the powerup
    def check_activated(self, paddle, pu_list):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        if self.position.y + powerup_health_img.get_height() >= PADDLE_Y and self.position.y <= PADDLE_Y:
            if self.position.x >= paddle_pos and self.position.x + powerup_health_img.get_width() <= paddle_pos + paddle_width:
                self.activate(pu_list, paddle)

    #Function Delete
    #Function Delete removes the spawned powerup from the list of spawned powerups
    def delete(self, pu_list):
        pu_list.remove(self)


class HealthPowerup(Powerup):
    #Function Activate
    #Function Activate for the Health powerup adds a life to the current lives, and then deletes itself
    def activate(self, pu_list, paddle):
        Scorecard.add_life()
        self.delete(pu_list)


class IncreasePaddleSize(Powerup):
    #Function Activate
    #Function Activate for the IncreasePaddleSize powerup increases the paddles size if its not at maximum and then deletes itself
    def activate(self, pu_list, paddle):
        paddle.increase_paddle_size()
        self.delete(pu_list)


class DecreasePaddleSize(Powerup):
    #Function Activate
    #Function Activate for the DecreasePaddleSize powerup decreases the paddles size if its not at minimum and then deletes itself
    def activate(self, pu_list, paddle):
        paddle.decrease_paddle_size()
        self.delete(pu_list)

   
POWERUPS = {1: HealthPowerup, 2: IncreasePaddleSize, 3: DecreasePaddleSize}
PU_IMG = {1: powerup_health_img, 2: powerup_increase_paddle_img, 3: powerup_decrease_paddle_img}