from entities.personagem import Personagem
from system.controller import *
from system.storage import delete, load, save


data = None
cmd_in = None

print('Digite um comando:')
while cmd_in not in CMD.exit:
  print('> ', end='')
  cmd_in, args = input_processor()

  if cmd_in in CMD.new:
    if len(args) > 0:
      data = Personagem(nome=args[0])
    else:
      data = Personagem()

  elif cmd_in in CMD.delete:
    if len(args) > 0:
      delete(args[0])
      data = None

  elif cmd_in in CMD.load:
    if len(args) > 0:
      data = load(args[0])

  elif cmd_in in CMD.save:
    save(data)

  elif cmd_in in CMD.show:
    if len(args) > 0 and data:
      if args[0] in CMD.level:
        print(data.out_level())
      elif args[0] in CMD.stats:
        print(data.out_stats())
      elif args[0] in CMD.sub:
        print(data.out_sub())
    else:
      print(str(data))

  elif cmd_in in CMD.change and data:
    if len(args) > 1:
      data.change_stat(args[0], args[1])

  else:
    pass
