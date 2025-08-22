import math
from system.controller import Stats


class Personagem():
  def __init__(self, **kwargs):
    self.nome = kwargs.get('nome') or 'Personagem'
    self.lv = kwargs.get('lv') or 1
    self.str = kwargs.get('str') or 0
    self.dex = kwargs.get('dex') or 0
    self.int = kwargs.get('int') or 0
    self.agi = kwargs.get('agi') or 0
    self.res = kwargs.get('res') or 0

  def total_stat(self):
    return 15 + self.lv - 1
  def pts_stat(self):
    return self.total_stat() - (self.str + self.dex + self.int + self.agi + self.res)
  def max_stat(self):
    return math.floor(7 + (self.lv * 0.6))

  def max_hp(self):
    return math.floor(40 + (self.lv / 2) + self.res)

  # def dmg_f(self):
  #   return self.str
  # def dmg_t(self):
  #   return self.dex
  # def dmg_b(self):
  #   return 'fixo'

  def arremesso(self):
    scaling = math.floor((self.str - 2) / 7)
    value = 2 + scaling
    value = max(2, min(value, 5))
    return value

  # def acc(self):
  #   return self.dex

  def evs(self):
    scaling = math.floor((self.agi - 2) / 7)
    scaling = max(0, min(scaling, 3)) * 10
    scaling = (50 + scaling) / 100
    value = math.floor(self.agi * scaling)
    return value

  def change_stat(self, stat, value):
    value = int(value)
    pts = self.pts_stat()
    max_stat = self.max_stat()
    if stat in Stats.lv:
      self.lv += value
      self.lv = max(0, self.lv)
    else:
      if pts - value >= 0:
        if stat in Stats.str:
          self.str += value
          self.str = max(0, min(self.str, max_stat))
          print(f'Força alterada para {self.str}')
        elif stat in Stats.dex:
          self.dex += value
          self.dex = max(0, min(self.dex, max_stat))
          print(f'Destreza alterada para {self.dex}')
        elif stat in Stats.int:
          self.int += value
          self.int = max(0, min(self.int, max_stat))
          print(f'Inteligência alterada para {self.int}')
        elif stat in Stats.agi:
          self.agi += value
          self.agi = max(0, min(self.agi, max_stat))
          print(f'Agilidade alterada para {self.agi}')
        elif stat in Stats.res:
          self.res += value
          self.res = max(0, min(self.res, max_stat))
          print(f'Resistência alterada para {self.res}')
        else:
          print(f'Atributo inválido: "{stat}"')
      else:
        print(f'Pontos insuficientes: {pts}')

  def out_level(self):
    out = f'\nLv.{self.lv}\n'
    out += f'Bônus HP: {self.lv / 2}\n'
    out += f'Pontos (Total): {self.total_stat()}\n'
    out += f'Limite: {self.max_stat()}\n'
    return out

  def out_stats(self):
    out = f'\nPontos: {self.pts_stat()} / {self.total_stat()}\n'
    out += f'Limite: {self.max_stat()}\n\n'
    out += f'Força: {self.str}\n'
    out += f'Destreza: {self.dex}\n'
    out += f'Inteligência: {self.int}\n'
    out += f'Agilidade: {self.agi}\n'
    out += f'Resistência: {self.res}\n'
    return out

  def out_sub(self):
    out = '\nDano Base:\n'
    out += f'- Físico: {self.str}\n'
    out += f'- Tiro: {self.dex}\n'
    out += f'Arremesso: {self.arremesso()}\n'
    out += f'Acerto Base: {self.dex}\n'
    out += f'Esquiva: {self.evs()}\n'
    return out

  def __str__(self):
    out = f'\nNome: {self.nome}\n'
    out += f'Lv.{self.lv}\n'
    out += f'HP: {self.max_hp()}\n'
    out += f'Força: {self.str}\n'
    out += f'Destreza: {self.dex}\n'
    out += f'Inteligência: {self.int}\n'
    out += f'Agilidade: {self.agi}\n'
    out += f'Resistência: {self.res}\n\n'
    out += 'Dano Base:\n'
    out += f'- Físico: {self.str}\n'
    out += f'- Tiro: {self.dex}\n'
    out += f'Arremesso: {self.arremesso()}\n'
    out += f'Acerto Base: {self.dex}\n'
    out += f'Esquiva: {self.evs()}\n'
    return out
