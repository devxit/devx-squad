# devx-squad

Harness de agentes da [DEVX IT](https://github.com/devxit), integrado às [skills do Matt Pocock](https://github.com/mattpocock/skills). O squad entrega **personas especializadas** (PO, Dev, Frontend, QA) que primeiro **aprendem o seu repositório** e depois operam nele com regras explícitas do projeto.

## Conceito: global × local

```mermaid
flowchart LR
  subgraph pacote ["Pacote devx-squad instalado"]
    gPO[po-devx]
    gDev[dev-devx]
    gFront[frontend-devx]
    gQA[qa-devx]
    gSetup[setup-devx]
  end

  subgraph repo ["Seu repositório"]
    docs["docs/agents/ issue-tracker, domain, stack"]
    local[".agents/skills/project-papel-devx/"]
  end

  gSetup -->|"1x onboarding"| docs
  gSetup -->|"gera"| local
  gPO --> local
  gDev --> local
  gFront --> local
  gQA --> local
  local -->|"dia a dia"| trabalho["$project-po-devx, $project-dev-devx, ..."]
```

| Camada | O quê | Quando usar |
| --- | --- | --- |
| **Skills globais** | Receitas de setup em `devx-squad/skills/*-devx` | Primeira vez no repo ou recalibração (`$po-devx`, `$setup-devx`, etc.) |
| **Skills locais** | `.agents/skills/<project>-<papel>-devx/SKILL.md` | Todo trabalho de esteira: stack, gates, vocabulário e fluxos **deste** projeto |
| **Matt Pocock** | `$tdd`, `$implement`, `$grill-me`, `$to-spec`, … | Execução técnica referenciada pelas skills locais |

Regra prática: se a skill local já existe, a global **não assume o papel** — você invoca `$<project>-<papel>-devx`. A global só volta com chamada explícita (ex.: `$dev-devx`) para recalibrar, regerar ou manter o arquivo local.

## Fluxo de uso no dia a dia

```mermaid
flowchart TD
  init{Projeto já tem setup?}
  setup["$setup-devx na raiz"]
  pronto["docs/agents + .agents/skills/*-devx"]
  tarefa[Nova demanda ou ticket]
  persona["Invoque $<project>-Papel-devx"]
  matt[Skills Matt conforme a fase]
  gates[Gates do repo typecheck test build]

  init -->|não| setup --> pronto
  init -->|sim| tarefa
  pronto --> tarefa
  tarefa --> persona --> matt --> gates
  gates --> tarefa
```

1. **Onboarding (uma vez):** `$setup-devx` — Matt no ambiente, `docs/agents/`, skills locais na ordem PO → Dev → Frontend → QA.
2. **Entrega contínua:** escolha a persona local alinhada à fase (spec, teste vermelho, código, UI, exploração, aceite).
3. **Evidência compartilhada:** `docs/agents/stack.md` (Core, Interface, Qualidade) e issue tracker em `docs/agents/`.

`copy-writer-devx` e `engine-discover-devx` são **paralelas à esteira técnica** — copy/CRO (`$copy-writer-devx`) e auditoria SEO, GEO, AEO (`$engine-discover-devx`); as duas se invocam mutuamente em LP completa, sem skill local por projeto.

## Exemplo: uma funcionalidade de ponta a ponta

Cenário fictício no projeto **`noah`**: *“Filtros avançados no catálogo de imóveis”*.

```mermaid
sequenceDiagram
  participant PO as noah-po-devx
  participant QA as noah-qa-devx
  participant Dev as noah-dev-devx
  participant Front as noah-frontend-devx
  participant Matt as Matt skills
  participant Repo as Repo e CI

  PO->>Matt: grill-me, to-spec, to-tickets
  PO->>Repo: spec e tickets no tracker
  QA->>Matt: tdd
  QA->>Repo: testes Red nos seams API e UI
  Dev->>Matt: implement, tdd
  Dev->>Repo: API e persistencia verde
  Front->>Matt: design-an-interface, implement
  Front->>Repo: filtros UI, responsivo, design system
  QA->>Matt: qa, tdd se gaps
  QA->>Repo: exploratorio E2E e docs/qa
  PO->>Repo: UAT e aceite no ticket
```

| Fase | Persona | Entregável típico |
| --- | --- | --- |
| 1. Discovery | `$noah-po-devx` | Escopo, critérios de aceite, tickets com label pronta para agente |
| 2. Red | `$noah-qa-devx` | Testes comportamentais falhando na pirâmide certa (contrato + E2E quando couber) |
| 3. Implementação | `$noah-dev-devx` | Backend/dominio verde, respeitando `stack.md` Core |
| 4. Interface | `$noah-frontend-devx` | Telas de filtro, estados vazio/erro, fidelidade ao design system |
| 5. Exploratório | `$noah-qa-devx` | Regressão, inventário `docs/qa/`, gates na ordem do projeto |
| 6. UAT | `$noah-po-devx` | Aceite ou devolução com evidência no tracker |

Ordem da **esteira técnica** (visão resumida):

```mermaid
flowchart LR
  D[Discovery PO]
  R[Testes Red QA]
  I[Implementacao Dev]
  U[UI Frontend]
  E[Exploratorio QA]
  A[UAT PO]

  D --> R --> I --> U --> E --> A
```

## Setup rápido (`setup-devx`)

```bash
npx skills add devxit/devx-squad --skill setup-devx -g -y
npx skills add mattpocock/skills -g -y   # se ainda nao tiver
```

Na raiz do projeto alvo: **`$setup-devx`**.

1. Verifica skills Matt (`grill-me`, `tdd`, `to-spec`, `setup-matt-pocock-skills`).
2. Grava `docs/agents/` (tracker, domínio) via fluxo Matt.
3. Gera skills locais: **po-devx → dev-devx → frontend-devx → qa-devx** (QA por último, alinhado à Interface para E2E).

### Diagrama do setup

```mermaid
flowchart TD
  start["$setup-devx na raiz do projeto"]
  e1["Etapa 1 — Skills Matt no ambiente"]
  e1ok{Todas presentes?}
  e1inst["Oferece npx skills add mattpocock/skills -g -y"]
  e1stop[Encerra se recusar instalar]
  e2["Etapa 2 — setup-matt-pocock-skills no repo"]
  e2ex{issue-tracker.md e domain.md existem?}
  e2ask[Pular ou refazer docs/agents]
  e2new[Explora, confirma e grava docs/agents e AGENTS.md]
  e3["Etapa 3 — Skills locais um papel por vez"]
  po["3a po-devx"]
  dev["3b dev-devx"]
  front["3c frontend-devx"]
  qa["3d qa-devx"]
  roleout["Criar, recalibrar, regerar ou manter"]
  endNode["Pronto: docs/agents + .agents/skills/*-devx"]

  start --> e1 --> e1ok
  e1ok -->|sim| e2
  e1ok -->|nao| e1inst
  e1inst -->|aceita| e1
  e1inst -->|recusa| e1stop
  e2 --> e2ex
  e2ex -->|sim| e2ask --> e3
  e2ex -->|nao ou refazer| e2new --> e3
  e3 --> po --> roleout --> dev --> roleout --> front --> roleout --> qa --> roleout --> endNode
```

Na Etapa 3, Dev/Frontend/QA podem preencher `docs/agents/stack.md`. O **frontend** fecha escopo (perfil, PWA, motion, a11y, i18n) antes de gravar a skill local; o **QA** usa a camada Interface para E2E/UI.

## Instalação

Método suportado: **`npx skills add`**.

```bash
# Pacote completo no projeto atual
npx skills add devxit/devx-squad

# Global (~/.agents/skills)
npx skills add devxit/devx-squad -g

# Uma skill
npx skills add devxit/devx-squad --skill po-devx
```

Skills disponíveis: `po-devx`, `dev-devx`, `frontend-devx`, `qa-devx`, `copy-writer-devx`, `engine-discover-devx`, `setup-devx`, `skill-creator-devx`.

## Stack com evidência (`docs/agents/stack.md`)

Camadas **Core** (Dev), **Interface** (Frontend), **Qualidade** (QA), mais **Decisões em aberto** / **Sugestões arquivadas**. Stack existente no repo é documentada como vigente; melhorias são sugestões opcionais. Libs e comandos **não são inventados** — manifests, ADRs e `WebFetch` na doc oficial antes da skill local.

## Personas do squad

| Skill global | Persona local | Foco |
| --- | --- | --- |
| `po-devx` | `$<project>-po-devx` | Discovery, spec, tickets, UAT |
| `qa-devx` | `$<project>-qa-devx` | Pirâmide de testes, risco, exploratório |
| `dev-devx` | `$<project>-dev-devx` | Implementação full stack e gates |
| `frontend-devx` | `$<project>-frontend-devx` | UI sob medida ao arquétipo; PWA/motion só no escopo fechado |
| `copy-writer-devx` | *(sem local)* | Copy de LP — CRO, tom, microcopy, prompts de tela |
| `engine-discover-devx` | *(sem local)* | Auditoria de conteúdo — SEO, GEO, AEO, metadados, Schema |

## Layout do repositório

```text
.
├── README.md
├── LICENSE
└── skills/
    ├── po-devx/
    ├── dev-devx/
    ├── frontend-devx/
    ├── qa-devx/
    ├── copy-writer-devx/
    ├── engine-discover-devx/
    ├── setup-devx/
    └── skill-creator-devx/
```

## Licença

MIT. Veja [LICENSE](LICENSE).