# Ponte copy / engine (frontend)

Leia no **setup** (`$frontend-devx`, Etapa 0) e na **skill local** `*-frontend-devx` ao implementar página pública ou acionar skills globais de copy/SEO.

## Dois níveis

| Nível | Campo | Onde gravar |
| --- | --- | --- |
| Topologia | `topologia_id` | `docs/agents/stack.md` — `webapp` (um deploy) ou `multi-app` (monorepo) |
| Página | `arquetipo_id` | mapa `rota → arquetipo_id` no mesmo bloco |

IDs de página (copy/engine): `landing-campaign`, `institutional`, `saas-marketing`, `catalog-vitrine`, `ecommerce`, `blog-editorial`, `webapp`, `multi-app`.

Detalhe copy: `copy-writer-devx/references/page-archetypes.md`. Detalhe SEO: `engine-discover-devx/references/discovery-archetypes.md`.

## Regra de ouro

Fechar mapa na **sabatina de setup** (`$grill-me`). Rascunho da inspeção com `confirmado` | `inferido` | `a_confirmar` — não gravar `stack.md` com linhas só `a_confirmar`.

Na **entrega** diária: ler `stack.md` primeiro. Rota fora do mapa → **perguntar ao usuário** (não chutar `arquetipo_id`).

## A. Perfil UI → default

| Arquétipo frontend | Topologia | `arquetipo_id` típico |
| --- | --- | --- |
| Webapp único | `webapp` | Home → `webapp`; `/pricing` → `saas-marketing` |
| Landing / institucional | `webapp` ou N/A | Por rota: `institutional` / `landing-campaign` |
| SaaS B2B / backoffice | `webapp` | Marketing → páginas web; logado → **microcopy** |
| Dashboard / analytics | `webapp` | Sem páginas indexáveis; microcopy + prompt UI |
| Vitrine / catálogo | `webapp` | `catalog-vitrine` |
| E-commerce | `webapp` | `ecommerce` |
| Monorepo multi-app | `multi-app` | Sub-ID por app + campo `app` |

## B. Heurísticas de rota (rascunho — só setup)

| Sinais no repo | `arquetipo_id` rascunho |
| --- | --- |
| `/`, `(marketing)/page` hero produto | `webapp` |
| `/sobre`, `/about` | `institutional` |
| `/pricing`, `/planos` | `saas-marketing` |
| `/blog/*` | `blog-editorial` |
| `/produto/[slug]`, PDP | `ecommerce` |
| `/categoria/*`, listagem | `ecommerce` ou `catalog-vitrine` |
| one-page campanha | `landing-campaign` |

Ambíguo (ex.: home institucional vs produto) → `a_confirmar` na sabatina.

## C. Qual skill acionar

| Situação | Skill | Modo copy-writer |
| --- | --- | --- |
| Erro, empty, label | copy-writer-devx | microcopy |
| Layout de tela (gerador UI) | copy-writer-devx | prompt UI |
| Página pública nova/rewrite | copy-writer-devx | página web |
| SEO/Schema/meta só | engine-discover-devx | — |
| Página indexável + copy | **site-par-v1** | copy FASE1 → engine §1–4 → copy FASE2 |

## D. Handoff

```text
topologia_id: webapp | multi-app
arquetipo_id: <id>
rota: <path>
app: <obrigatório se multi-app>
blocos_planejados: [bloco_id, ...]
modo: pagina_web | microcopy | prompt_ui
```

## Fluxo na skill local (entrega)

1. Ler `stack.md` → bloco **Conteúdo e arquétipos**.
2. Rota no mapa → usar `arquetipo_id` gravado.
3. Rota nova → perguntar; atualizar `stack.md` se o usuário fixar regra.
4. Página web: handoff + `$copy-writer-devx` / `$engine-discover-devx`; UI após copy aprovada (`$design-an-interface`, `$implement`).
5. Proibido inventar copy de marketing no código.