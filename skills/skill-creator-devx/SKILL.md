---
name: skill-creator-devx
description: Designs, writes, and packages Agent Skills for the DEVX GitHub organization following the Agent Skills specification. Use when the user asks to create a skill, author a SKILL.md, turn a workflow into a skill, package a skill repository, write the human README for a skill repo, or mentions skill-creator-devx, nova skill, criar skill, pacote de skill, or npx skills add. Asks whether the skill goes into an existing skills repository or a new repository before any file is written.
license: Proprietary
compatibility: Requires Node.js for npx skills add. Publishing a repository requires the GitHub CLI authenticated to github.com/devxit.
metadata:
  author: DEVX IT
  version: "1.0.0"
---

# skill-creator-devx

Você cria Agent Skills da DEVX no formato de [Agent Skills](https://agentskills.io/specification) e do guia *The Complete Guide to Building Skills for Claude*. `SKILL.md` ensina o agente. O `README.md` na raiz do repositório explica a instalação para uma pessoa.

Não grave arquivos antes de fechar a descoberta e de a pessoa escolher o destino.

## Regras fixas

1. Pergunte o destino antes de criar qualquer arquivo. As opções são um repositório de skills que já existe ou um repositório novo. Não deduza o destino pelo workspace aberto.
2. O repositório GitHub fica na org https://github.com/devxit/.
3. A instalação oficial é `npx skills add`. Instalação global acrescenta `-g -y`. Não descreva cópia manual de pasta como instalação oficial.
4. A pasta da skill não tem `README.md`. Texto para o agente fica em `SKILL.md` ou em `references/`. Texto para pessoas fica no `README.md` da raiz do repositório.
5. `name` é kebab-case, igual ao nome da pasta da skill, com 1–64 caracteres, sem hífen no início ou no fim e sem `--`. Não use `claude` nem `anthropic` no nome.
6. `description` está em terceira pessoa, diz o que a skill faz e quando usar, inclui frases que a pessoa diria, tem no máximo 1024 caracteres e não contém `<` nem `>`.
7. O `SKILL.md` fica abaixo de 500 linhas. Cada arquivo ligado a partir dele diz em que situação deve ser lido.

## Fluxo

Descoberta → Destino → Arquitetura → Escrita → Validação → Entrega

Avance só quando o critério da fase estiver satisfeito.

### 1. Descoberta

Pergunte um assunto por vez. Saia desta fase quando existirem:

- 2 ou 3 casos de uso, cada um com o pedido da pessoa, os passos e o resultado verificável
- as ferramentas que o fluxo usa
- o critério de sucesso: em quais pedidos a skill deve carregar, em quais não deve, e como é um resultado bom

Critério de saída: esses três itens estão escritos e a pessoa concordou.

### 2. Destino

Use o formulário de pergunta quando ele existir. A pergunta é: onde a skill será entregue.

- Repositório existente: peça o caminho local e o slug `devxit/<repo>`.
- Repositório novo: o nome padrão é `devxit/<nome-da-skill>`. Confirme o nome antes de criar a pasta.

Critério de saída: destino, slug e caminho local estão confirmados. Nenhum arquivo da skill existe ainda.

Leia [references/delivery.md](references/delivery.md) e aplique o layout do destino escolhido.

### 3. Arquitetura

Escolha um padrão principal: fluxo sequencial, refinamento iterativo, escolha conforme o contexto, ou conhecimento de domínio.

Separe o conteúdo:

- frontmatter: `name` e `description`
- `SKILL.md`: passos que valem em toda execução
- `references/`: material que só alguns ramos leem
- `scripts/`: checagem determinística
- `assets/`: modelo que a skill preenche

Rascunhe a `description` antes do corpo. Ao rascunhar, leia [references/description.md](references/description.md).

Critério de saída: padrão, árvore de pastas e `description` rascunhada.

### 4. Escrita

Escreva no imperativo. Cada passo termina com um critério que dá para verificar. Dê um padrão e uma saída de emergência, não um cardápio de ferramentas equivalentes. Coloque em `SKILL.md` o fato que o agente erraria se não estivesse escrito.

Ao escrever o README do repositório, leia [references/repo-readme.md](references/repo-readme.md) e preencha [assets/repo-readme.md](assets/repo-readme.md). Se o repositório já tem README, preserve a forma desse arquivo e inclua o resultado da skill e o comando `npx skills add`.

Critério de saída: `SKILL.md` existe, a pasta da skill não tem `README.md`, e o README da raiz cita o comando de instalação.

### 5. Validação

Rode o validador desta skill contra a pasta da skill nova:

```bash
python "<pasta-desta-skill>/scripts/validate_skill.py" "<pasta-da-skill-nova>"
```

O comando termina com `OK` e código 0. Corrija e rode de novo até passar.

Percorra [references/checklist.md](references/checklist.md). Inclua 3 pedidos que devem carregar a skill e 3 quase-acertos que não devem. Quase-acerto compartilha vocabulário e pede outra coisa.

Critério de saída: validador em `OK` e os 6 pedidos revisados.

### 6. Entrega

Mostre o comando oficial:

```bash
npx skills add devxit/<repo> --skill <nome> -g -y
```

Para conferir o que o CLI enxerga:

```bash
npx skills add devxit/<repo> --list
```

No checkout local, use o mesmo comando com o caminho do repositório no lugar de `devxit/<repo>`. A flag `-g` instala a skill para todos os projetos em `~/.agents/skills`.

Crie o remoto e faça push só quando a pessoa pedir para publicar. O remoto é `https://github.com/devxit/<repo>`. Se ela não disser se o repositório é público ou privado, pergunte. Não grave segredo, token ou conteúdo de `.env`.

Critério de saída: a pessoa recebeu o comando `npx skills add` e o caminho dos arquivos.

## Exemplos

### Repositório novo

Pedido: "Cria uma skill para revisar pull requests no padrão DEVX."

1. Feche 2 ou 3 casos de uso.
2. Pergunte se a entrega é num repositório existente ou num repositório novo.
3. No repositório novo, grave `skills/<nome>/SKILL.md` e deixe o `README.md` só na raiz.
4. Valide. Entregue `npx skills add devxit/<nome> --skill <nome> -g -y`.

### Repositório que já existe

Pedido: "Adiciona essa skill no repositório de skills da org."

1. Confirme o slug `devxit/<repo>` e o caminho local.
2. Grave a skill no caminho que `npx skills add <caminho> --list` já descobre. Se o repositório ainda não tem skills, use `skills/<nome>/`.
3. Atualize o README da raiz. Não crie `README.md` dentro da pasta da skill.
4. Entregue `npx skills add devxit/<repo> --skill <nome> -g -y`.

## Quando algo falha

`npx skills add --list` não mostra a skill. A `SKILL.md` não está na raiz do repositório nem em `skills/<nome>/SKILL.md`. Mova para `skills/<nome>/SKILL.md` e rode `--list` de novo.

A pasta da skill contém `README.md`. Apague esse arquivo. O texto para pessoas fica no README da raiz do repositório.

A skill não carrega no pedido certo. Reescreva a `description` com o que ela faz, quando usar e frases reais. Leia [references/description.md](references/description.md).
