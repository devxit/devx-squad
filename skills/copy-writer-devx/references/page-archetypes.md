# Arquétipos de página (copy)

Leia após triagem **modo página web** em `copy-writer-devx`. IDs idênticos em `engine-discover-devx/references/discovery-archetypes.md`.

Alinhado a `frontend-devx/references/product-scope.md` (marketing público; backoffice = microcopy + prompt UI). Inferência de rota/topologia no setup: `frontend-devx/references/copy-engine-bridge.md`.

## Taxonomia (IDs congelados)

| ID | Rótulo | Páginas típicas | Objetivo copy |
| --- | --- | --- | --- |
| `landing-campaign` | Landing / campanha | LP, lead magnet | Conversão |
| `institutional` | Institucional | Home corporate, Sobre, Contato, Carreiras | Confiança + clareza |
| `saas-marketing` | SaaS marketing | Produto, soluções, integrações, Pricing | Comercial |
| `catalog-vitrine` | Vitrine / catálogo | Home catálogo, listagem, ficha resumo | Descoberta |
| `ecommerce` | E-commerce | PDP, PLP (categoria) | Transação |
| `blog-editorial` | Blog / editorial | Artigo, hub de conteúdo | Autoridade |
| `webapp` | Webapp único | Home do produto, signup/login, onboarding público no mesmo deploy | Produto + conversão signup |
| `multi-app` | Monorepo multi-app | Vários packages web (portal + workspace, etc.) | Por subsite/app |

## Triagem rápida

1. Pedido cita **uma URL ou tipo de página** → mapeie para ID.
2. Ambíguo (ex.: “home”) → pergunte: institucional, catálogo ou campanha?
3. **Anti-pattern:** não usar `landing-campaign` para Sobre, artigo ou PDP.
4. Registre na FASE 1: `arquetipo_id` + lista de `bloco_id` planejados (handoff `site-par-v1`).

## Quando invocar engine-discover-devx

- Página indexável + SEO/GEO/AEO explícito ou implícito.
- Arquétipos: `catalog-vitrine`, `ecommerce`, `blog-editorial`, `saas-marketing` (pricing), `landing-campaign`, home `institutional`.
- Modo microcopy e prompt UI: **não** invocar irmã salvo pedido de meta/SEO no mesmo ticket.

---

## `landing-campaign`

**Blocos (`bloco_id`):**

| bloco_id | Conteúdo |
| --- | --- |
| `hero` | H1, subheadline, CTA principal, confiança imediata |
| `problem` | Cenário e dor do lead |
| `mechanism` | Passos / como funciona (doc) |
| `comparison` | Vs. alternativas (tabela ou bullets) |
| `social-proof` | Cases, métricas ou placeholders |
| `offer` | Oferta, garantia, CTA final |
| `faq` | FAQ; abertura 40–60 palavras (perguntas da irmã) |

**Pronto:** UVP em &lt;5s no hero; CTA único primário; oferta alinhada ao hero.

**Anti-patterns:** jargão vazio; FAQ sem objeções reais; comparativo inventado.

**Insumos FASE 1:** (1) briefing; (2) foco; (3) público; (4) objetivo de conversão.

---

## `institutional`

**Blocos:**

| bloco_id | Conteúdo |
| --- | --- |
| `hero` | Proposta institucional clara, sem hype de campanha |
| `mission` | Missão / o que fazemos |
| `proof` | Trajetória, clientes, certificações documentadas |
| `people-values` | Equipe ou valores (só fatos do material) |
| `contact-cta` | CTA suave (contato, carreiras, falar conosco) |

**Pronto:** tom confiável; sem dobras de agitação comercial agressiva.

**Anti-patterns:** 7 dobras de LP; CTA “compre agora” em Sobre; depoimentos inventados.

**Insumos FASE 1:** marca, foco institucional, público (stakeholders), objetivo (confiança/navegação).

---

## `saas-marketing`

**Blocos (produto / solução):**

| bloco_id | Conteúdo |
| --- | --- |
| `hero` | Categoria + benefício para persona |
| `problem` | Dor do ICP |
| `capabilities` | Features como outcomes |
| `proof` | Logos, métricas documentadas |
| `faq` | Objeções técnicas e comerciais |

**Pricing (`bloco_id` adicional em página de planos):**

| `pricing-table` | Planos, limites, diferenciais factuais |
| `pricing-faq` | Billing, trial, segurança |

**Pronto:** capabilities ligadas a docs; pricing sem feature inventada.

**Anti-patterns:** lista de features sem benefício; comparativo de concorrente sem fonte.

---

## `catalog-vitrine`

**Blocos:**

| bloco_id | Conteúdo |
| --- | --- |
| `intro` | Intro indexável (o que o catálogo oferece) |
| `filters-language` | Rótulos humanos de filtros/facetas |
| `listing-cards` | Título curto + dado por card (preço, área, status) |
| `secondary-cta` | Contato, favoritar, comparar |

**Pronto:** intro não vazia; linguagem de filtro compreensível sem stuffing.

**Anti-patterns:** parágrafo longo por card; CTA primário de “comprar agora” em listagem genérica.

---

## `ecommerce`

**PDP — blocos:**

| bloco_id | Conteúdo |
| --- | --- |
| `pdp-hero` | Nome, benefício principal, preço se documentado |
| `pdp-specs` | Specs da ficha técnica |
| `pdp-trust` | Entrega, garantia, políticas |
| `pdp-cta` | Adicionar ao carrinho / comprar |

**PLP — blocos:**

| bloco_id | Conteúdo |
| --- | --- |
| `plp-intro` | Texto introdutório da categoria |
| `plp-facets` | Copy de facetas |
| `plp-grid` | Micro-títulos de listagem |

**Pronto:** specs só do material; urgência honesta (sem falso escassez).

**Anti-patterns:** review inventado; preço não confirmado.

---

## `blog-editorial`

**Blocos:**

| bloco_id | Conteúdo |
| --- | --- |
| `lead` | Resposta direta 40–60 palavras |
| `outline` | H2/H3 (perguntas ou tópicos) |
| `body` | Desenvolvimento por seção (copy na FASE 2) |
| `conclusion` | Próximo passo (link interno, CTA editorial) |

**Pronto:** lead citável; conclusão com ação única.

**Anti-patterns:** FAQ comercial no fim; hero estilo LP; 7 dobras.

**Insumos FASE 1:** tema, keyword ou pergunta-alvo, público, fontes/documentação.

---

## `webapp`

Aplicação web **única** (um deploy, um package): marketing + área logada no mesmo repo. Diferente de `multi-app` (monorepo com vários apps).

**Blocos:**

| bloco_id | Conteúdo |
| --- | --- |
| `product_home` | Proposta do produto, para quem, CTA signup/login |
| `auth_entry` | Copy de login, registro, recuperação (público) |
| `feature_surface` | Capacidades como outcomes (não lista técnica solta) |
| `onboarding_teaser` | Primeiros passos pós-cadastro (marketing, não tutorial in-app) |

**Pronto:** um deploy = um tom de produto; rotas autenticadas (`/app`, dashboard) → modo **microcopy**, não página web.

**Anti-patterns:** tratar como LP institucional pura; usar `multi-app` sem monorepo; 7 dobras de campanha na home do produto.

**Insumos FASE 1:** produto, persona, objetivo (signup, trial, ativação), documentação de features.

**Rotas típicas no mesmo app:** `/` → `webapp`; `/pricing` → `saas-marketing`; `/sobre` → `institutional` (use o ID da rota, não só `webapp`).

---

## `multi-app`

**Somente monorepo** com vários `package.json` web.

1. Identifique **subsite/app** (portal vs workspace vs vitrine).
2. Escolha um ID da tabela acima **por app**; não misture tom B2B e varejo na mesma entrega.
3. Declare `topologia_id: multi-app`, `arquetipo_id` + nome do `app` no handoff.

**Pronto:** uma entrega por app/página; vocabulário consistente dentro do app.

**Anti-pattern:** usar `multi-app` para um único Next/Vite app — use topologia `webapp`.

---

## Handoff site-par-v1

Na conclusão da FASE 1, envie à irmã:

```text
topologia_id: webapp | multi-app  # setup frontend; webapp = deploy único
arquetipo_id: <id>
blocos_planejados: [bloco_id, ...]
app: <se multi-app>
foco, publico, objetivo: <resumo>
```

A irmã devolve §4 indexado pelos mesmos `bloco_id`. Se divergir, realinhe antes da FASE 2.