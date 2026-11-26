# Stack — entrevista e resolução (Frontend)

Leia quando o **Passo 1.5** disparar no `frontend-devx`.

## Ordem na Etapa 0

1. Inspeção + inferência de arquétipo → [product-scope.md](product-scope.md)
2. Passo 1.5 — stack por evidência (`docs/agents/stack.md` → Interface)
3. **Sabatina de escopo** (`$grill-me`, obrigatória) — **não gravar** `.agents/skills/<project>-frontend-devx/SKILL.md` antes
4. Redação sob medida da skill local

PWA, motion imersivo, a11y e i18n **não são default**; entram só se o usuário confirmar na sabatina.

## Entradas

- `docs/agents/stack.md` (**Core**)
- `.agents/skills/<project>-dev-devx/SKILL.md` (slug e regras compartilhadas)
- `package.json` dos apps web, rotas `app/`/`pages/`, Tailwind/design tokens, PWA **só se existir**

## Stack definida — documentar vigente

1. Extrair framework, CSS, libs **somente do manifest/código**.
2. Atualizar seção **Interface (Frontend)** em `stack.md` (incluir bloco **Escopo fechado** após sabatina: perfil, renderização, PWA sim/não, motion, a11y, i18n).
3. Se houver superfície pública (ver [product-scope.md](product-scope.md) — copy/arquétipos), incluir bloco **Conteúdo e arquétipos (copy / engine)** — obrigatório; se só backoffice, declarar `sem_paginas_indexaveis: sim`.

Modelo do bloco copy:

```markdown
### Conteúdo e arquétipos (copy / engine)
- perfil_ui: <product-scope>
- topologia_id: webapp | multi-app
- apps_marketing: [<app ou pasta>, ...]
- mapa_rotas:
  - rota | arquetipo_id | origem (confirmado|inferido)
- arquetipo_id_default_novas_paginas: <id ou n/a>
- site_par_v1_default: sim | nao
- sem_paginas_indexaveis: sim | nao
```

Origem `inferido` só vigora após confirmação na sabatina (gravar como `confirmado`).
3. Revisão crítica opcional: design system, SSR/CSR, performance.
4. Perguntar: adotar melhoria, **manter como está** ou adiar.

## Sugestões opcionais

Advisory; usuário pode manter stack atual sem bloquear setup.