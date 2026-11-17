# Perfil de produto e fechamento de escopo (Frontend)

Leia na Etapa 0 de `frontend-devx` após a inspeção do repositório.

## Arquétipos (inferência)

| Arquétipo | Sinais no repo |
| --- | --- |
| SaaS B2B / backoffice | rotas `admin`, tabelas, formulários longos, RBAC, drawers de filtro |
| Dashboard / analytics | charts, mapas, KPI cards, densidade de métricas |
| Vitrine / catálogo | listagem, busca, SEO, mídia, comparação, fichas de item |
| E-commerce / marketplace | carrinho, checkout, PDP, estoque |
| Landing / institucional | poucas rotas, hero, CTA, marketing, blog |
| Monorepo multi-app | vários `package.json` web com papéis distintos (portal + workspace) |

Registre um ou mais arquétipos. Repo vazio → não inventar; perguntar na sabatina.

## Sabatina (`$grill-me`) — obrigatória antes de gravar a skill local

1–2 blocos por vez, com recomendação por arquétipo. Fechar e registrar em `docs/agents/stack.md` → **Interface (Frontend)**:

| Dimensão | Opções |
| --- | --- |
| Perfil | confirmar inferência ou escolher arquétipo |
| Renderização | SSG, SSR/híbrido/RSC, SPA |
| Responsivo | mobile-first ou desktop-first com adaptação fluida |
| PWA | sim (instalação, SW, offline) ou **não se aplica** |
| Motion | funcional/micro-interações ou imersivo/parallax |
| a11y | exigida neste ciclo ou **não se aplica** |
| i18n | exigida ou **não se aplica** |

Radix, `lang`, pasta `locales` ou PWA no repo → recomendar; não aprovar automaticamente.

## Recomendações default por arquétipo (advisory)

| Arquétipo | Renderização | Responsivo | PWA | Motion |
| --- | --- | --- | --- | --- |
| SaaS / backoffice | SSR/híbrido ou SPA | desktop-first fluido | raro | funcional |
| Dashboard | SPA ou RSC | desktop-first | raro | funcional |
| Vitrine / catálogo | SSG/SSR (SEO) | mobile-first | opcional | funcional |
| E-commerce | SSR/híbrido | mobile-first | opcional | funcional |
| Landing | SSG | mobile ou desktop | raro | imersivo comum |
| Multi-app | por app | por app | por app | por app |

## Checklist da skill local (módulos)

**Sempre:** identidade + perfil, stack visual, fontes oficiais, barra de excelência, responsividade, componentes reutilizáveis, fidelidade Figma/HTML/imagem + design system, governança, 4 fases, menu.

**Só se escopo aprovar:** PWA, motion imersivo/parallax, a11y, i18n.

## Fidelidade visual (sempre na skill local e na esteira)

- Reproduzir Figma, HTML de exemplo e imagens: layout, espaçamento, tipografia, cor, estados e animações da referência.
- Mapear para tokens e componentes do design system; evitar CSS solto duplicado.
- Antes de codar: checar reuso (banner, input, tabela, título, card, lista, ícone, flag) em `packages/ui` ou `src/components`.
- Tela **foge** do design system → parar e `$grill-me` **antes de codar**:
  1. **Estender o sistema** — novo token ou componente reutilizável no design system existente.
  2. **Adaptar a tela** — reproduzir a referência usando só tokens/componentes já aprovados.
  3. **Exceção pontual** — só após o usuário autorizar; escolher uma das formas de **importar sem contaminar** as demais telas:
     - **CSS isolado + shell existente:** folha/escopo CSS dedicado à rota (ex. módulo CSS, layout wrapper), encaixar conteúdo em shell/layout já usado no projeto (header/sidebar/outlet) sem reutilizar tokens globais que a tela não respeita.
     - **Design system paralelo:** subconjunto de tokens/componentes com prefixo ou pacote separado (ex. `packages/ui-marketing`, tema `data-ds="campaign"`) aplicado só àquela tela ou app, com fronteira clara para não vazar estilos nas telas do sistema principal.
  Documentar a exceção em `docs/agents/stack.md` → Interface ou ADR curto (rota, motivo, estratégia escolhida).