from colors import colors


class Board(object):
  def __init__(self, width=500, height=500, nx=20, ny=20, canvas=None):
    self.width = width
    self.height = height
    self.nx = nx
    self.ny = ny
    self.wx = self.width/self.nx
    self.wy = self.height/self.ny
    self.canvas = canvas
    self.tile_types = {
      'blank': 'blank',
      'active': 'active',
    }
    self._init_tiles()

  def _init_tiles(self):
    self.tiles = []
    for i in range(self.nx):
      self.tiles.append([])
    for i in self.tiles:
      for i in range(self.ny):
        self.tiles[i].append(self.tile_types['blank'])

  def _render_background(self):
    color = ''
    for i, _ in enumerate(self.tiles):
      for j, type in enumerate(self.tiles[i]):

        if type == 'blank':
          # if j % 2 == 1:
          #   if i % 2 == 0:
          #     color = colors['lightblue']
          #   else:
          #     color = colors['darkblue']
          # else:
          #   if i % 2 == 1:
          #     color = colors['lightblue']
          #   else:
          #     color = colors['darkblue']
          color = colors['lightblue']
        elif type == 'active':
          # if j % 2 == 1:
          #   if i % 2 == 0:
          #     color = colors['lightred']
          #   else:
          #     color = colors['darkred']
          # else:
          #   if i % 2 == 1:
          #     color = colors['lightred']
          #   else:
          #     color = colors['darkred']
              color = colors['darkred']

        self.canvas.create_rectangle(
          i*self.wx, j*self.wy, i*self.wx+self.wx, j*self.wy+self.wy,
          fill=color, outline=colors['darkgray'])

  def update(self):
    for i, _ in enumerate(self.tiles):
      for j, type in enumerate(self.tiles[i]):
        if type == self.tile_types['active']:
          if (self.tiles[i-1][j] == self.tile_types['active'] and
              self.tiles[i][j-1] == self.tile_types['active']):
            self.set_tile_xy(i-1, j, self.tile_types['blank'])

  def render(self):
    self._render_background()

  def set_tile_xy(self, x, y, type):
    try:
      self.tiles[x][y] = type
    except Exception:
      pass

  def set_tile(self, x, y, type):
    self.tiles[int(round(x/self.wx))][int(round(y/self.wy))] = type

  def toggle_active(self, x, y):
    i = int(round(x/self.wx))
    j = int(round(y/self.wy))
    if self.tiles[i][j] == self.tile_types['active']:
      self.set_tile(x, y, self.tile_types['blank'])
    else:
      self.set_tile(x, y, self.tile_types['active'])
