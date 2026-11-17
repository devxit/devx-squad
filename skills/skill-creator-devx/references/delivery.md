# Destino da skill

Leia este arquivo na fase Destino, depois que a pessoa escolher repositório existente ou repositório novo.

A org é sempre https://github.com/devxit/. A instalação oficial é sempre `npx skills add`.

## Repositório novo

Nome padrão do remoto: `devxit/<nome-da-skill>`. Confirme o nome antes de criar pastas.

```text
<repo>/
├── README.md              # pessoas: resultado, instalação, um pedido de exemplo
├── LICENSE
└── skills/
    └── <nome-da-skill>/
        ├── SKILL.md       # obrigatório; name igual à pasta
        ├── references/    # só se algum ramo precisar
        ├── scripts/       # só para checagem determinística
        └── assets/        # só para modelo que a skill preenche
```

Não coloque `README.md` dentro de `skills/<nome-da-skill>/`.

O CLI encontra `SKILL.md` na raiz do repositório ou em `skills/<nome>/SKILL.md`. Use `skills/<nome>/`. Assim o README da raiz não entra na pasta da skill.

Crie o remoto e faça push só quando a pessoa pedir para publicar. Se ela não disser público ou privado, pergunte.

## Repositório existente

Confirme o caminho local e o slug `devxit/<repo>`.

1. Rode `npx skills add <caminho> --list`.
2. Se o comando já lista skills, grave a nova no mesmo tipo de caminho.
3. Se o repositório ainda não tem skill, use `skills/<nome>/SKILL.md`.
4. Atualize o README da raiz com o resultado da skill e esta linha:

```bash
npx skills add devxit/<repo> --skill <nome> -g -y
```

Não crie `README.md` na pasta da skill. Não troque o README inteiro do catálogo pelo modelo de skill única: preserve a forma do arquivo e acrescente a skill.

## Instalação global

```bash
npx skills add devxit/<repo> --skill <nome> -g -y
```

`-g` grava a skill em `~/.agents/skills` e a deixa disponível em todos os projetos. Sem `-g`, a instalação vale só para o projeto atual.
