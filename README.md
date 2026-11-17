# devx-squad

Harness de agentes auto-adaptáveis da [DEVX IT](https://github.com/devxit), integrado às skills do Matt Pocock. Cada agente global lê o repositório em que é chamado e grava uma especialização local daquele projeto.

## Pré-requisito

As skills do Matt Pocock precisam estar instaladas antes de usar o squad:

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

O mesmo `--skill` vale para `devx-qa`, `devx-dev` e `devx-frontend`.

## Auto-Bootstrap

Ao rodar `$devx-po`, `$devx-qa`, `$devx-dev` ou `$devx-frontend` num projeto, o agente escaneia o repositório (docs, stack, testes e código) e gera a especialização local:

```text
.agents/skills/devx-<project>-<papel>/SKILL.md
```

Exemplos: `.agents/skills/devx-noah-po/SKILL.md`, `.agents/skills/devx-noah-qa/SKILL.md`.

Se esse arquivo já existe, o agente carrega a versão local e atende com ela. Se você pedir para recalibrar, ele compara o levantamento novo com o arquivo atual e só grava depois da sua aprovação. Nas sessões seguintes, invoque direto `$devx-<project>-po` (ou `-qa`, `-dev`, `-frontend`).

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
    └── devx-squad/
```

`devx-squad` é a skill que autora outras skills. As quatro acima são o harness.

## Licença

MIT. Veja [LICENSE](LICENSE).
