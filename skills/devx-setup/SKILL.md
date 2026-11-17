---
name: devx-setup
description: Orquestra o setup completo de um projeto com o harness DEVX squad. Verifica e instala o pacote mattpocock/skills se faltar, executa setup-matt-pocock-skills no repositório e aciona devx-po, devx-dev, devx-qa e devx-frontend um por vez para gerar skills locais. Use quando o usuário pede setup do projeto, bootstrap do devx-squad, $devx-setup, configurar projeto novo ou existente para a esteira DEVX.
license: MIT
compatibility: Requer Node.js para npx skills add. Requer skills devx-squad (devx-po, devx-dev, devx-qa, devx-frontend) instaladas globalmente ou no projeto.
metadata:
  author: DEVX IT
  version: "1.0.0"
---

# devx-setup

Você conduz o **setup ponta a ponta** de um projeto (novo ou existente) para o harness DEVX + Matt Pocock. Você não faz discovery, testes, implementação nem UI — só instala dependências de skills, configura `docs/agents/` via setup do Matt e gera as quatro skills locais da squad **um papel por vez**.

## Guardrail

- Não pule etapas sem confirmação quando a etapa pedir escolha (instalar Matt, pular/refazer setup Matt, recalibrar skill local).
- Não reescreva `.agents/skills/devx-*-<papel>/SKILL.md` por conta própria: use as skills globais `devx-po`, `devx-dev`, `devx-qa`, `devx-frontend` como especificado abaixo.
- Não copie o conteúdo das skills do Matt para o repositório do usuário além do que `setup-matt-pocock-skills` já grava em `docs/agents/` e ponteiros em `AGENTS.md` / `CLAUDE.md`.

## Progresso

Copie e atualize a cada etapa concluída:

```text
devx-setup:
- [ ] Etapa 1 — Pacote Matt Pocock no ambiente
- [ ] Etapa 2 — Setup Matt no repositório (docs/agents/)
- [ ] Etapa 3a — Skill local PO
- [ ] Etapa 3b — Skill local Dev
- [ ] Etapa 3c — Skill local QA
- [ ] Etapa 3d — Skill local Frontend
```

## Etapa 1 — Pacote Matt Pocock no ambiente

### 1.1 Verificação

Confirme que as skills abaixo estão acessíveis ao agente (lista de skills do harness **e**, se existirem no disco, pastas em `~/.agents/skills/` ou `.agents/skills/` do projeto):

- `setup-matt-pocock-skills`
- `grill-me`
- `tdd`
- `to-spec`

Se **todas** estiverem presentes, marque a Etapa 1 como concluída e siga para a Etapa 2.

### 1.2 Instalação (se faltar)

Se **qualquer uma** estiver ausente, informe o usuário e ofereça instalar o **pacote completo**:

```text
As skills do Matt Pocock não estão completas neste ambiente.
Deseja instalar o pacote completo agora?

npx skills add mattpocock/skills -g -y
```

Fonte: https://github.com/mattpocock/skills/tree/main

- Se o usuário **aceitar**, execute o comando no terminal (com aprovação, se o harness exigir), releia a Etapa 1.1 e só então avance.
- Se o usuário **recusar**, encerre o `devx-setup` com instrução para instalar manualmente e invocar `$devx-setup` de novo.

Não instale subconjuntos arbitrários: use o comando acima para o repositório inteiro.

## Etapa 2 — Setup Matt no repositório

A skill `setup-matt-pocock-skills` é invocação manual (`disable-model-invocation`). Como o usuário chamou `devx-setup`, você **executa o procedimento** lendo o `SKILL.md` instalado de `setup-matt-pocock-skills` (em `~/.agents/skills/` ou equivalente) e seguindo-o no repositório atual.

### 2.1 Projeto existente

Se **ambos** existirem:

- `docs/agents/issue-tracker.md`
- `docs/agents/domain.md`

Pergunte:

1. **Pular** — manter a configuração atual e ir para a Etapa 3.
2. **Refazer** — executar de novo o fluxo de `setup-matt-pocock-skills` (explorar, apresentar, confirmar, gravar), por exemplo para trocar issue tracker ou recomeçar `docs/agents/`.

Sem escolha, não sobrescreva esses arquivos.

### 2.2 Projeto novo ou configuração incompleta

Execute o processo completo de `setup-matt-pocock-skills`:

- Explorar: `git remote`, `AGENTS.md` / `CLAUDE.md`, glossário (`GLOSSARY.md`, legado `CONTEXT.md`), `docs/agents/`, `.scratch/`, monorepo.
- Apresentar e perguntar: issue tracker (GitHub, GitLab, local markdown ou outro), labels de triagem (se `triage` instalado), layout de domínio (single-context vs multi-context).
- Confirmar rascunhos antes de gravar.
- Gravar: `docs/agents/issue-tracker.md`, `docs/agents/domain.md`, `docs/agents/triage-labels.md` (se aplicável), bloco `## Agent skills` em `CLAUDE.md` ou `AGENTS.md` conforme a regra da skill do Matt.

Critério de saída: `issue-tracker.md` e `domain.md` existem e o arquivo de instruções do harness aponta para eles.

## Etapa 3 — Skills locais da squad (um papel por vez)

Ordem fixa: **PO → Dev → QA → Frontend**. Só inicie o próximo papel quando o atual tiver um desfecho explícito (skill criada, recalibrada com aprovação, gerada de novo com confirmação, ou mantida).

Para cada papel:

1. Leia integralmente o `SKILL.md` global correspondente instalado (`devx-po`, `devx-dev`, `devx-qa`, `devx-frontend`).
2. Trate a invocação como **explícita** (`$devx-po`, `$devx-dev`, `$devx-qa`, `$devx-frontend`), conforme o Caso A dessas skills.
3. Procure `.agents/skills/devx-*-<papel>/SKILL.md` no repositório atual.

| Ordem | Global | Arquivo local esperado |
| --- | --- | --- |
| 3a | `devx-po` | `.agents/skills/devx-<project>-po/SKILL.md` |
| 3b | `devx-dev` | `.agents/skills/devx-<project>-dev/SKILL.md` |
| 3c | `devx-qa` | `.agents/skills/devx-<project>-qa/SKILL.md` |
| 3d | `devx-frontend` | `.agents/skills/devx-<project>-frontend/SKILL.md` |

### Se a skill local **não** existir

Execute somente a **Etapa 0 / Caso B** da skill global daquele papel (levantamento + gravação do `SKILL.md` local + sabatina quando prevista). Pare nesse papel; não assuma a esteira (spec, testes, código, UI).

### Se a skill local **já** existir

Não assuma a persona da esteira. Ofereça exatamente:

1. **Recalibrar** — protocolo de levantamento da global, diff com o `SKILL.md` atual, gravar só após aprovação.
2. **Gerar de novo** — protocolo completo e substituir o arquivo após confirmação.
3. **Manter** — não alterar o arquivo.

Sem escolha, não altere o arquivo. Depois do desfecho, avance para o próximo papel na ordem.

### Slug `<project>`

Mantenha o **mesmo** `<project>` em todas as quatro skills locais. Se o PO já definiu o slug em `.agents/skills/devx-<project>-po/`, as demais devem usar o mesmo slug, alinhando com as outras skills locais já existentes quando relevante.

## Etapa 4 — Encerramento

Apresente um resumo objetivo:

- Matt: instalado ou já presente.
- `docs/agents/`: arquivos gravados ou mantidos.
- Tabela das quatro skills locais: caminho, ação (criada / recalibrada / regerada / mantida).

Instrua o uso no dia a dia:

```text
Product Owner:  $devx-<project>-po
Dev:            $devx-<project>-dev
QA:             $devx-<project>-qa
Frontend:       $devx-<project>-frontend
```

Mencione que novos setups parciais podem usar cada `$devx-<papel>` global de forma explícita, ou `$devx-setup` de novo para repetir o fluxo completo.

## Inicialização

Ao ser invocado via `$devx-setup` ou pedido de setup do devx-squad:

1. Confirme que está no **repositório alvo** (raiz do projeto onde `.agents/skills/` e `docs/` serão criados).
2. Mostre o checklist de progresso vazio e inicie a Etapa 1.