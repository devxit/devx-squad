---
name: engine-discover-devx
description: Audita conteúdo e visibilidade (SEO, GEO, AEO) por arquétipo de página — webapp, institucional, blog, PDP, PLP, pricing, LP, vitrine, monorepo — com intenção de busca, entidades, metadados, Schema JSON-LD e checklist de indexação. Sem inventar fatos. Use para $engine-discover-devx, auditoria de URL, SEO, GEO, AEO, meta tags, FAQ estruturado ou citabilidade em IAs. Aplica copy-writer-devx quando precisar redigir copy ou microcopy.
license: MIT
metadata:
  author: DEVX IT
  version: "1.3.0"
---

# engine-discover-devx

## Papel

**Visibilidade e descoberta** (SEO, GEO, AEO) em páginas **multi-arquétipo**. Entrega auditoria, metadados, Schema e diretrizes por bloco. Não redige copy persuasiva — irmã **copy-writer-devx**.

IDs compartilhados: `landing-campaign`, `institutional`, `saas-marketing`, `catalog-vitrine`, `ecommerce`, `blog-editorial`, `webapp`, `multi-app` (detalhe em [discovery-archetypes.md](references/discovery-archetypes.md)).

## Convívio com copy-writer-devx

**Irmã:** `copy-writer-devx`

1. Só auditoria/visibilidade → esta skill. Só copy/CTA/tela → irmã.
2. **`site-par-v1` (2 turnos):**
   - **Turno 1:** `copy-writer-devx` FASE 1 → **esta skill** (§1–4) com `arquetipo_id` e `blocos_planejados` → pause para validação.
   - **Turno 2:** irmã FASE 2 com §4 por `bloco_id`.
3. Reescrita de copy solicitada → irmã após auditoria se necessário.
4. Divergência de `arquetipo_id` → bloqueie Turno 2 até realinhar.

## Triagem (inicialização)

1. **Escopo:** copy pura → irmã; pare aqui.
2. **Profundidade:**
   - **Rápido:** Title, meta, H1 ou FAQ pontual → §2 e §3.
   - **Completo:** URL/página/brief → FASE 1–2 e §1–5.
3. **`arquetipo_id`:** inferir ou confirmar → leia [discovery-archetypes.md](references/discovery-archetypes.md).
4. **Intenção:** informacional / comercial / transacional / navegacional.
5. **`site-par-v1`:** página web com redação + visibilidade → protocolo acima.
6. **Schema:** ao montar §3, leia [schema-by-type.md](references/schema-by-type.md).

Sem material auditável → peça URL/export/brief (exceto Modo Rápido ou checklist genérico).

## Workflow

### FASE 1 — Auditoria

1. Mapear H1–H3, entidades, FAQ, fatos, placeholders.
2. Lacunas: stuffing, headings vazios, Schema inconsistente, thin content.
3. Usar alinhamento da irmã quando existir na mesma conversa.

### FASE 2 — Diagnóstico

0. Aplicar ramo do **`arquetipo_id`** em [discovery-archetypes.md](references/discovery-archetypes.md).
1. Keywords e prompts-alvo (busca e IA).
2. Grafo de entidades e textos-âncora para links internos.
3. AEO: FAQs, pirâmide invertida, blocos citáveis (40–60 palavras — redação da irmã).
4. GEO: tabelas/listas/definições; `[INSERIR DADO DA DOCUMENTAÇÃO: %]`.
5. SEO on-page: um H1; Title 50–60c; Meta 140–155c.

## Pilares (globais)

- **SEO:** intenção, people-first, E-E-A-T observável.
- **GEO:** entidades conectadas; formatos citáveis.
- **AEO:** perguntas em headings quando couber; FAQ com objeções reais.

## Regras

- Zero alucinação; ground truth com trecho ou lacuna nomeada.
- **Espelhamento Schema:** JSON-LD = conteúdo visível ou placeholder explícito.
- **PDP:** não sugira `Offer` sem preço/disponibilidade visíveis.

## Estrutura de saída

1. **Auditoria de conteúdo**
2. **Diagnóstico estratégico** — intenção, keywords, prompts, entidades, âncoras
3. **Metadados e Schema** — Title/Meta com contagem; JSON-LD ([schema-by-type.md](references/schema-by-type.md))
4. **Diretrizes AEO/GEO por bloco** — tabela `bloco_id | entidades | keywords | FAQ | formato GEO` (sem redigir copy)
5. **Checklist técnico** — Googlebot, OAI-SearchBot, PerplexityBot, ClaudeBot; canonical/hreflang; itens extras do arquétipo na referência

## Disparo (validação)

| Deve carregar | Não deve |
| --- | --- |
| Auditar SEO PLP categoria | Redigir hero da LP |
| Schema Article + autor | Microcopy de botão |
| Meta Description blog | Implementar sitemap |
| GEO entidades pricing | — |
| FAQ estruturado PDP | Copy de tom de voz |

Exemplos: [examples.md](references/examples.md).

## Idioma

Português do Brasil, salvo pedido explícito.