import random

import Tkinter as tk

import board


class App(object):
  def __init__(self):
    self.width = 500
    self.height = 400
    self.player_x = 0
    self.player_y = 0

    self.master = tk.Tk()
    self.window = tk.Frame(self.master)
    self.window.pack()

    self.canvas = tk.Canvas(
      self.window, width=self.width, height=self.height, bg='#FFFFFF')
    self.canvas.pack()

    self.board = board.Board(canvas=self.canvas)

    self.board.set_tile(122, 47, 'active')
    self.board.set_tile(222, 147, 'active')

    self.canvas.after(0, self.animate)
    self.handle_keys()

    self.window.mainloop()

  def render(self):
    self.board.render()
    self.canvas.create_rectangle(
      self.player_x, self.player_y, self.player_x+20, self.player_y+20,
      fill='red', width=0)

  def update(self):
    self.board.update()

  def animate(self):
    self.canvas.delete(tk.ALL)

    if self.player_x < self.width:
      self.player_x += 10
    else:
      self.player_x = 0

    if self.player_y < self.height:
      self.player_y += 10
    else:
      self.player_y = 0

    self.master.after(60, self.animate)
    self.update()
    self.render()

  def handle_keys(self):
    self.canvas.bind('<Button-1>', self.handle_mouse)

  def handle_mouse(self, event):
    # self.player_x = event.x
    # self.player_y = event.y
    self.board.toggle_active(event.x, event.y)


if __name__ == '__main__':
  app = App()
