# Informações Rodadas BTD6 

## Descrição
Um projeto da diciplina de C14 do inatel. Esse projeto tem como objetivo mostras informações e estatisticas das rodadas do jogo **Bloons Tower Defense 6**.

O projeto é feito em Python3, com o auxilio de bibliotecas externas.

## Clonando o Projeto Para Sua Maquina
Para poder contribuir nesse projeto basta clicar no botão ***Fork*** localizado no canto superior direito dessa pagina (web), e coloque esse comando no terminal:
```bash
git clone https://github.com/<seu-usuario>/<nome-repositorio-forkado>/.git
```

Depois basta criar uma ***Branch*** para trabalhar na *feature* do projeto.
```bash
git checkout -b <nome-da-feature>
```

Depois de criar ou mudar a *feature* basta enviar.
```bash
git push origin <nome-da-feature>
```

## Dependencias

### Python3
Versão do Python utilizada no projeto ``` Python=3.12.9 ```

### [Tabela Usada no Projeto](https://docs.google.com/spreadsheets/d/1SAoPy9T2tyURlwY0pSDOOG-zrkMZi8xf4i0L74jdaZM/edit?gid=0#gid=0)

### Bibliotecas
Todas as bibliotecas estão no arquivo [requirements.txt](./auxiliar/requirements.txt) na pasta "auxiliar", porém podem serem instaladas pelo comando:
```bash
pip install -r requirements.txt
```

### Resolvendo Conflitos
Algumas vezes, ao realizar um processo de ***merge***, pode ocorrer um conflito entre arquivos.
Nesses casos, é necessário resolvê-lo manualmente. Isso pode ser feito tanto pelo GitHub quanto de forma local, mas, na minha opinião, a melhor opção é resolver localmente.

Para isso basta seguir essa sequencia de commandos:
```bash
git checkout -b <nome-branch-resolvendo-conflito>
git clone <link-repositorio>
```
**Resolva o conflito de forma manual, escolhendo qual das duas versões irá continuar.**

```bash
git commit -m "texto resolvendo o conflito"
git checkout <branch-que-houve-o-conflito>
git merge --no-ff <nome-branch-resolvendo-conflito>
git push origin <branch-que-houve-o-conflito>
```

### Voltando Para Um commit
Voltar a um commit específico no Git é fundamental para corrigir problemas no projeto. Quando um commit introduz erros ou falhas, reverter para um ponto estável garante que o código volte a funcionar corretamente, evitando que bugs se espalhem. Essa prática ajuda a manter a integridade do histórico do projeto e permite que a equipe avance com mais segurança, já que sempre é possível recuperar versões anteriores confiáveis do código.

```bash
git log --oneline
git revert <hash-commit> #o commit tem que ser o que gerou o erro, então vai voltar logo antes dele: (commit-1)
```

### Git Stash
O git stash é um comando do Git usado quando você está no meio de uma modificação mas não quer commitar ainda e precisa mudar de branch ou puxar atualizações. Ele guarda suas mudanças temporariamente em uma “pilha” (stash) e deixa o diretório de trabalho limpo.

```bash
git stash
```