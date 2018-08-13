from Config import settings
from Objects.Forest import Forest


class Ecology:
  def __init__(self):
    self.Forest = Forest(settings.grid_size, settings.grid_dimensions)
    self.tree_count = self.Forest.grid_dimensions / 2  # 50%
    self.lumberjack_count = self.Forest.grid_dimensions / 100 * 10  # 10%
    self.bear_count = self.Forest.grid_dimensions / 100 * 2  # 2%
