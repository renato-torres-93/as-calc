import json
import os
from entities.personagem import Personagem
from os.path import abspath, dirname
from slugify import slugify


ROOT = dirname(abspath(__file__))
PATH = f'{ROOT}/storage'.replace('system/', '')

if not os.path.isdir(PATH):
  os.makedirs(PATH)


def save(data):
  with open(f'{PATH}/{slugify(data.nome)}.json', 'w') as f:
    f.write(json.dumps(data.__dict__, indent=2, separators=(', ', ': '), ensure_ascii=False))
    print(f'SAVED {data.nome}')

def load(file):
  with open(f'{PATH}/{slugify(file)}.json', 'r') as f:
    data = json.loads(f.read())
    data = Personagem(**data)
    print(f'LOADED {data.nome}')
    return data

def delete(file):
  os.remove(f'{PATH}/{slugify(file)}.json')
  print(f'DELETED {file}')
