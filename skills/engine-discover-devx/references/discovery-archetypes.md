# Arquétipos de descoberta (SEO / GEO / AEO)

Leia após triagem de **arquetipo_id** em `engine-discover-devx`. IDs idênticos a `copy-writer-devx/references/page-archetypes.md`.

## Triagem

1. Inferir `arquetipo_id` ou confirmar em uma pergunta.
2. Intenção típica: informacional / comercial / transacional / navegacional.
3. Aplicar ramo deste arquivo **antes** de keywords genéricas na FASE 2.
4. Em `site-par-v1`, receber `arquetipo_id` e `blocos_planejados` da irmã; §4 deve usar os mesmos `bloco_id`.

---

## `landing-campaign`

- **Intenção:** comercial / transacional.
- **Headings:** H1 comercial alinhado a Title; H2 objeção/benefício.
- **GEO/AEO:** FAQ de objeções; comparativo citável; lead direto no hero.
- **Schema:** `FAQPage` só se FAQs visíveis; `WebPage` + entidade produto/oferta quando couber.
- **Gaps típicos:** stuffing; FAQ só no JSON-LD; comparativo sem dados.
- **Checklist extra:** consistência Title ↔ H1; CTA não duplica keyword principal.

---

## `institutional`

- **Intenção:** navegacional / informacional leve.
- **GEO/AEO:** E-E-A-T institucional; pouca agressividade comercial.
- **Schema:** `Organization`, `WebSite`; `AboutPage` em Sobre quando aplicável.
- **Gaps típicos:** home sem entidade organização; thin content em Sobre.
- **Checklist extra:** links de confiança (contato, políticas) com âncoras claras.

---

## `saas-marketing`

- **Intenção:** comercial.
- **GEO/AEO:** entidades produto + categoria + ICP; pricing como texto comparável.
- **Schema:** `SoftwareApplication` ou `Product` quando factível; evitar claims não visíveis.
- **Gaps típicos:** features sem entidade; pricing invisível ao crawler.
- **Checklist extra:** páginas de integração com links internos temáticos.

---

## `catalog-vitrine`

- **Intenção:** comercial / descoberta.
- **GEO/AEO:** intro indexável; facetas em linguagem natural; listas escaneáveis.
- **Schema:** `ItemList` quando lista de itens é visível.
- **Gaps típicos:** PLP só grid sem intro; facetas só em JS sem texto.
- **Checklist extra:** evitar duplicar H1 em filtros como keyword stuffing.

---

## `ecommerce`

- **Intenção:** transacional (PDP); comercial (PLP).
- **GEO/AEO:** PDP com specs factuais; PLP com parágrafo introdutório.
- **Schema:** `Product`, `Offer` (preço/disponibilidade **visíveis**); `AggregateRating` só com reviews na página.
- **Gaps típicos:** Offer no JSON-LD sem preço no HTML; thin category.
- **Checklist extra:** bloquear `Offer` se preço ausente — use placeholder visível ou omitir.

---

## `blog-editorial`

- **Intenção:** informacional.
- **GEO/AEO:** pirâmide invertida; H2 em pergunta; links internos temáticos.
- **Schema:** `Article`, `Person`/`author`, `datePublished` espelhados na página.
- **Gaps típicos:** FAQ comercial forçado; autor ausente; lead após 3 parágrafos.
- **Checklist extra:** não recomendar `FAQPage` comercial em artigo educativo.

---

## `multi-app`

- **Intenção:** por subsite.
- **GEO/AEO:** entidades e keywords **não fundidas** entre apps.
- **Schema:** por domínio/rota; `canonical` e `hreflang` quando multilíngue.
- **Gaps típicos:** meta genérica compartilhada; sitemap misturando intents.
- **Checklist extra:** auditoria **uma URL + um app** por vez.

---

## §4 — Diretrizes por bloco (formato)

Para cada `bloco_id` acordado:

```text
bloco_id | entidades a nomear | keywords/prompts | FAQ/objeções | formato GEO (tabela/lista/definição)
```

Não redija a copy do bloco; só diretrizes para a irmã `copy-writer-devx`.