# devx-squad

Harness de agentes auto-adaptáveis da [DEVX IT](https://github.com/devxit), integrado às skills do Matt Pocock. Cada agente global lê o repositório em que é chamado e grava uma especialização local daquele projeto.

## Setup rápido (`devx-setup`)

A skill `devx-setup` faz o onboarding completo do projeto, novo ou existente:

1. Verifica se o pacote [mattpocock/skills](https://github.com/mattpocock/skills/tree/main) está no ambiente; se faltar, oferece `npx skills add mattpocock/skills -g -y`.
2. Executa o fluxo de `setup-matt-pocock-skills` no repositório (`docs/agents/`, issue tracker, domínio). Se `docs/agents/` já existir, pergunta se pula ou refaz.
3. Aciona **um por vez** as globais `devx-po` → `devx-dev` → `devx-qa` → `devx-frontend` para criar ou atualizar `.agents/skills/devx-<project>-<papel>/SKILL.md`.

```bash
npx skills add devxit/devx-squad --skill devx-setup -g -y
```

No agente, invoque `$devx-setup` na raiz do projeto alvo.

## Pré-requisito (uso manual)

Se não usar `devx-setup`, instale o Matt antes do squad:

```bash
npx skills add mattpocock/skills
```

## Instalação

O único método suportado é `npx skills add`.

Repositório inteiro, no projeto atual:

```bash
npx skills add devxit/devx-squad
```

Global, disponível em todos os projetos (`~/.agents/skills`):

```bash
npx skills add devxit/devx-squad -g
```

Uma skill específica:

```bash
npx skills add devxit/devx-squad --skill devx-po
```

O mesmo `--skill` vale para `devx-qa`, `devx-dev`, `devx-frontend` e `devx-setup`.

## Auto-Bootstrap

Ao rodar `$devx-po`, `$devx-qa`, `$devx-dev` ou `$devx-frontend` num projeto, o agente escaneia o repositório (docs, stack, testes e código) e gera a especialização local:

```text
.agents/skills/devx-<project>-<papel>/SKILL.md
```

Exemplos: `.agents/skills/devx-noah-po/SKILL.md`, `.agents/skills/devx-noah-qa/SKILL.md`.

Essas skills globais existem só para o setup. Se `.agents/skills/devx-<project>-<papel>/SKILL.md` já existe e a global não foi chamada de forma explícita, ela é ignorada. O trabalho segue na skill local (`$devx-<project>-po`, `$devx-<project>-qa`, `$devx-<project>-dev` ou `$devx-<project>-frontend`).

Se a global for chamada de propósito (`$devx-po`, `$devx-qa`, `$devx-dev` ou `$devx-frontend`) e a local já existir, ela não assume o papel. Oferece três caminhos, porque os requisitos do projeto podem ter mudado: recalibrar a skill local, gerar uma nova no lugar, ou manter a atual. Sem essa escolha, o arquivo local não muda.

## Esteira

| Agente | Papel | Onde entra na esteira |
| --- | --- | --- |
| `devx-po` | Product Owner: discovery, spec, tickets e aceite | Discovery e UAT |
| `devx-qa` | QA: pirâmide de testes, risco e exploração | Testes Red e QA exploratório |
| `devx-dev` | Dev full stack: pattern mining e implementação | Implementação (DEV) |
| `devx-frontend` | UI, PWA, responsividade fluida e motion 60fps | UI/PWA |

Fluxo completo:

```text
Discovery → Testes Red → Implementação (DEV) → UI/PWA → QA Exploratório → UAT
```

`devx-po` abre o discovery e fecha o UAT. `devx-qa` escreve os testes no vermelho e faz o QA exploratório. `devx-dev` implementa a fatia. `devx-frontend` constrói a interface, o PWA e o motion.

## Layout

```text
.
├── README.md
├── LICENSE
└── skills/
    ├── devx-po/SKILL.md
    ├── devx-qa/SKILL.md
    ├── devx-dev/SKILL.md
    ├── devx-frontend/SKILL.md
    ├── devx-setup/SKILL.md
    └── devx-skill-creator/
```

`devx-setup` orquestra Matt + bootstrap das quatro skills locais. `devx-skill-creator` autora outras Agent Skills DEVX. As quatro primeiras são o harness da esteira.

## Licença

MIT. Veja [LICENSE](LICENSE).
