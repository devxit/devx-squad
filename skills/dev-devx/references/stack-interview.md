# Stack — entrevista e resolução (Dev)

Leia quando o **Passo 1.5** disparar no `dev-devx`.

## Stack definida vs indefinida

**Indefinida** (entrevista ampla obrigatória) se qualquer um:

- Sem manifest (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, etc.).
- Manifest vazio/genérico ou README sem stack.
- Conflito entre manifests/README/docs.

**Já definida:** versões e frameworks identificáveis no repo + configs/ADRs coerentes.

## Stack definida — documentar vigente

1. Extrair Core de manifests, CI e amostra de código.
2. Atualizar `docs/agents/stack.md` → seção **Core** (criar arquivo com [stack-doc-template.md](stack-doc-template.md) se não existir).
3. Oferecer **revisão crítica opcional** (até 5 itens): deps, CI, observabilidade, testabilidade.
4. Perguntar: **adotar alguma melhoria**, **manter como está** ou **adiar** (arquivar em Sugestões arquivadas se o usuário quiser histórico).
5. Se **manter**: não reabrir entrevista completa; entrevista só para lacunas que impeçam redigir a skill.

## Greenfield — entrevista Dev

Via `$grill-me`, poucas perguntas por vez, com recomendação padrão:

- Linguagem/runtime e versão alvo
- Framework API / apps (se houver)
- ORM/DB, migrations
- Monorepo (sim/não, ferramenta)
- Auth/tenant/multi-tenant
- Integrações externas (filas, cache, terceiros)
- Gates CI obrigatórios

## Revisão crítica e sugestões opcionais

Cada sugestão: impacto, alternativa, trade-off, URL doc oficial (`WebFetch`). **Adotar** só com confirmação. Se o usuário mantém a stack atual, a skill local descreve **somente o vigente**.