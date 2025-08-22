# Astral Sea Calculator

* Calculador básico de stats
* Uso baseado em Command Line Interface (*pt/en*)
* Arquivos salvos localmente

## Instruções
* O sistema trabalha com apenas um personagem na memória por vez
* É possível criar, ver, salvar, carregar e deletar qualquer personagem
* Quando um personagem está carregado na memória, é possível mexer nos stats e ver alguns cálculos básicos
* Use os comandos **Save/Load** pra salvar um personagem e usar depois

## Exemplo de uso
```
> criar Uzma
> add lv 9
> ver
> mudar for 10
> mudar for -3
> ver stats
> save
> criar Chiyome
> save
> load Uzma
> sair
```

## Glossário
* **Exit**
  * >0, exit, quit, sair
  * Encerra o programa
* **New**
  * >create, new, criar, nova, novo
  * Cria nova personagem
* **Save**
  * >save, salvar
  * Salva personagem em arquivo
* **Load**
  * >abrir, carregar, load
  * Carrega arquivo para a memória
* **Show**
  * >see, show, mostrar, ver, ficha
    >* Nível (nível, nv, level, lv, lvl)
    >* Stats (atributos, atr, attr, stats)
    >* Substats (secundários, secondary, sub, substats)
  * Mostra o que estiver na memória
  * Pode ser usado com comandos adicionais pra ver informações diferentes
  * Ex.: *show* (mostra a ficha básica)  
    *show substats* (mostra info de stats secundários)
* **Change**
  * >adicionar, mudar, add, change
    >* Nível (nível, nv, level, lv, lvl)
    >* Força (força, for, strength, str)
    >* Destreza (destreza, des, dexterity, dex)
    >* Inteligência (inteligência, int, intelligence)
    >* Agilidade (agilidade, agi, agility)
    >* Resistência (resistência, res, resistance)
  * Altera os stats da personagem
  * Pode ser usado com valores positivos ou negativos
  * Ex.: Remanejar 2 pontos de agi para int:  
    *change agi -2*  
    *change int 2*
* **Delete**
  * >deletar, excluir, remover, delete, remove, del, rm
  * Exclui arquivo de personagem
