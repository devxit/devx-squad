# Schema por arquétipo

Leia ao preencher **§3 Metadados e Schema** em `engine-discover-devx`.

Regra global: **espelhamento visível** — todo campo no JSON-LD existe no HTML/copy ou usa placeholder explícito visível ao usuário.

## Por arquetipo_id

| arquetipo_id | Tipos JSON-LD primários | Notas |
| --- | --- | --- |
| `landing-campaign` | `WebPage`, `FAQPage` (se FAQ visível) | FAQPage sem rich snippet garantido |
| `institutional` | `Organization`, `WebSite` | Logo e sameAs só se URLs reais |
| `saas-marketing` | `SoftwareApplication`, `Product`, `FAQPage` | Pricing em `Offer` só se visível |
| `catalog-vitrine` | `ItemList`, `WebPage` | Itens da lista devem existir na página |
| `ecommerce` | `Product`, `Offer`, `BreadcrumbList` | Offer exige price + availability visíveis |
| `blog-editorial` | `Article`, `Person` (author) | dateModified se houver revisão documentada |
| `multi-app` | Conforme subsite | Um grafo por app; não misturar @id de entidades |

## Combinações comuns

- **PDP:** `Product` + `Offer` + opcional `AggregateRating` (reviews na página).
- **PLP:** `CollectionPage` ou `WebPage` + `ItemList` (links visíveis).
- **Artigo:** `Article` + `author` + `publisher` (`Organization`).
- **Pricing SaaS:** tabela HTML de planos antes de `Offer` múltiplos.

## Anti-patterns

- `AggregateRating` sem reviews visíveis.
- `FAQPage` com perguntas ausentes no corpo.
- `Product` com SKU/preço só no JSON-LD.
- Misturar `SoftwareApplication` e `Product` sem critério (escolha um primário por página).

## Saída §3 mínima

- Title (contagem 50–60 caracteres sugerida).
- Meta Description (140–155 caracteres sugerida).
- Tipos recomendados + JSON-LD válido ou esqueleto com placeholders nomeados.