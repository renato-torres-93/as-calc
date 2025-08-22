class CMD():
  change = ('adicionar', 'mudar', 'add', 'change')
  delete = ('deletar', 'excluir', 'remover', 'delete', 'remove', 'del', 'rm')
  exit = ('0', 'exit', 'quit', 'sair')
  level = ('nível', 'nv', 'level', 'lv', 'lvl')
  load = ('abrir', 'carregar', 'load')
  new = ('create', 'new', 'criar', 'nova', 'novo')
  save = ('save', 'salvar')
  show = ('see', 'show', 'mostrar', 'ver', 'ficha')
  stats = ('atributos', 'atr', 'attr', 'stats')
  sub = ('secundários', 'secondary', 'sub', 'substats')

class Stats():
  lv = ('nível', 'nv', 'level', 'lv', 'lvl')
  str = ('força', 'for', 'strength', 'str')
  dex = ('destreza', 'des', 'dexterity', 'dex')
  int = ('inteligência', 'int', 'intelligence')
  agi = ('agilidade', 'agi', 'agility')
  res = ('resistência', 'res', 'resistance')

def input_processor():
  args = input()
  args = args.strip().split(' ')
  cmd_in = args.pop(0).lower()
  return cmd_in, args
