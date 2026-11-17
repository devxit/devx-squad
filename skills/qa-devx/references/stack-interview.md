# Stack — entrevista e resolução (QA)

Leia quando o **Passo 1.5** disparar no `qa-devx`.

## Entradas obrigatórias

- `docs/agents/stack.md` (**Core** e **Interface (Frontend)**)
- `.agents/skills/<project>-dev-devx/SKILL.md` e `*-frontend-devx/SKILL.md` (se existirem)
- Manifests, pastas de teste, `playwright.config.*`, `vitest.config.*`, `docs/qa/`, workflows CI

**Setup parcial:** QA antes de Frontend → declarar lacuna de Interface; entrevista mínima para E2E/UI antes de gravar.

## Stack definida — documentar vigente

1. Mapear runners e pirâmide **como estão no repo** (não inventar).
2. Atualizar seção **Qualidade (QA)** em `stack.md`.
3. Revisão crítica opcional: gaps E2E, flakiness, fixtures/auth browser, Testcontainers, contratos HTTP.
4. Perguntar: adotar melhoria, **manter como está** ou adiar.
5. Skill local = stack vigente; sugestões não adotadas não viram regra.

## Gaps — entrevista QA

- Runners por camada (unit, integration, contract, e2e)
- Ferramentas banidas (ADRs/NFRs)
- Fixtures/auth E2E, `TESTCONTAINERS`, seeds
- Viewports e apps sob teste (alinhar com Frontend)
- Inventário `docs/qa/`

## Questionar o Core / Interface

Exemplos: runner cobre contrato HTTP? E2E cobre seams críticos? Stack UI permite testes estáveis?

Sugestões: impacto, alternativa, doc oficial. Conflito com Dev/Frontend → lado a lado; usuário decide.