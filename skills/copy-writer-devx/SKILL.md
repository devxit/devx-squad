---
name: copy-writer-devx
description: Redige copy web multi-arquetipo (webapp, institucional, SaaS, vitrine, e-commerce, blog, LP, monorepo), microcopy/UX writing e prompts de interface minimalistas. Tom, wireframe textual e CRO. Fase 1 obrigatória para páginas web. Sem inventar fatos. Use para $copy-writer-devx, copy de webapp, página, sobre, pricing, PDP, PLP, artigo, LP, microcopy ou prompt de tela. Aplica engine-discover-devx quando precisar de SEO, GEO, AEO, metadados ou Schema.
license: MIT
metadata:
  author: DEVX IT
  version: "2.3.0"
---

# copy-writer-devx

## Papel

**Copywriter web** e **CRO**: páginas de marketing/conteúdo por arquétipo, microcopy de produto e prompts de tela. Visibilidade (SEO, GEO, AEO, Schema) é da irmã **engine-discover-devx**.

IDs de arquétipo compartilhados: `landing-campaign`, `institutional`, `saas-marketing`, `catalog-vitrine`, `ecommerce`, `blog-editorial`, `webapp`, `multi-app`. Topologia (setup frontend): `webapp` = deploy único; `multi-app` = monorepo.

## Modos de entrega

| Modo | Quando usar |
| --- | --- |
| **Página web** | Copy de site: LP, institucional, pricing, blog, vitrine, PDP/PLP |
| **Microcopy / UX** | Erros, empty, onboarding, tooltips, modais — leia [microcopy.md](references/microcopy.md) |
| **Prompt de interface** | Uma tela para gerador UI/dev — [UI minimalista](#diretivas-de-ui-minimalista) |

Não misture modos na mesma entrega.

## Triagem (inicialização)

1. **Modo** (tabela acima).
2. Se **página web:** inferir `arquetipo_id` → leia [page-archetypes.md](references/page-archetypes.md).
3. **Objetivo primário:** conversão, confiança, educação, transação ou navegação.
4. **`site-par-v1`:** página indexável, SEO pedido ou arquétipos vitrine/blog/e-commerce/SaaS/LP → FASE 1 + irmã + validação + FASE 2.
5. **Microcopy:** turno único; [microcopy.md](references/microcopy.md). **Prompt UI:** restrições abaixo.

## Convívio com engine-discover-devx

**Irmã:** `engine-discover-devx`

1. Redação/CRO/UI → esta skill. Auditoria/Schema → irmã (`engine-discover-devx/SKILL.md` em `~/.agents/skills/` ou `skills/`).
2. **`site-par-v1` (2 turnos):**
   - **Turno 1:** FASE 1 (inclua `arquetipo_id` + `blocos_planejados`) → irmã (§1–4) → pause para validação.
   - **Turno 2:** FASE 2 usando §4 da irmã indexado por `bloco_id`.
3. SEO explícito em página web → invoque a irmã antes da FASE 2.
4. Se `arquetipo_id` divergir entre turnos, realinhe antes de redigir.

## Workflow — página web

**Não entregue copy final** na primeira interação, salvo contexto completo (ver insumos em [page-archetypes.md](references/page-archetypes.md)) ou microcopy pontual.

### FASE 1 — Alinhamento

1. Ler documentação e exemplos de marca.
2. Mapear tom, conversão e vocabulário.
3. Fixar foco, público, objetivo e **`arquetipo_id`**; listar **`blocos_planejados`**.

### FASE 2 — Redação

1. Diagnóstico de tom.
2. Se `site-par-v1` e sem §4 da irmã, invoque **engine-discover-devx**.
3. Entregar wireframe + copy por **blocos do arquétipo** (não usar 7 dobras fora de `landing-campaign`).

**`landing-campaign`:** blocos equivalentes às dobras 1–7 (`hero` … `faq`) conforme [page-archetypes.md](references/page-archetypes.md).

## Protocolo e CRO

- **Ground truth** só do material fornecido.
- **CRO (LP/campanha):** UVP &lt;5s, CTA benefício, prova social documentada ou `[INSERIR DEPOIMENTO OU MÉTRICA VALIDADA]`.
- **Metadados/JSON-LD:** não duplique; cite a irmã em uma linha.

## Estrutura de saída (FASE 2 — página web)

1. **Tom de voz** — tom, melhorias, vocabulário.
2. **Wireframe e copy** — por `bloco_id` do arquétipo.
3. **Referência cruzada** — metadados/Schema da irmã se existir.

## Diretivas de UI minimalista

**Só** modo prompt de interface (não microcopy de produto).

- Uma tela; H1/H2 ≤4 palavras; CTAs 1–2 palavras; cards: ícone + título 2–3 palavras + métrica.
- Injete bloco **Restrições de Texto e Densidade** no prompt final.
- Revisão: uma tela por prompt; corte explicações vagas; enxugue exemplos.

## Disparo (validação)

| Deve carregar | Não deve (use irmã ou outra skill) |
| --- | --- |
| Copy página Sobre / institucional | Auditar só Schema e meta |
| Artigo de blog (outline + lead) | Implementar componente React |
| Microcopy erro 403 | Keyword research isolado |
| LP campanha 7 blocos | — |
| Prompt dashboard minimalista | — |
| Pricing SaaS (tabela + copy) | SEO técnico sem redação |

Exemplos: [examples.md](references/examples.md).

## Idioma

Português do Brasil, salvo pedido explícito de outro idioma.