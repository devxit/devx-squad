# Checklist

Leia este arquivo na fase Validação, depois que `scripts/validate_skill.py` imprimir `OK`.

## Antes de gravar

- [ ] 2 ou 3 casos de uso, com pedido, passos e resultado
- [ ] Ferramentas do fluxo identificadas
- [ ] Destino confirmado: repositório existente ou repositório novo em `github.com/devxit`
- [ ] Árvore de pastas definida

## Arquivos

- [ ] Pasta em kebab-case, igual ao campo `name`
- [ ] Arquivo chamado exatamente `SKILL.md`
- [ ] Frontmatter entre `---`
- [ ] `description` diz o que faz e quando usar, em terceira pessoa, com frases reais, até 1024 caracteres, sem `<` ou `>`
- [ ] Nome sem `claude` e sem `anthropic`
- [ ] `SKILL.md` abaixo de 500 linhas
- [ ] Nenhum `README.md` dentro da pasta da skill
- [ ] README na raiz do repositório com `npx skills add`
- [ ] Instruções no imperativo, com critério de saída em cada fase
- [ ] Exemplo de pedido e de resultado
- [ ] Referências ligadas com a situação em que devem ser lidas

## Disparo

- [ ] Carrega num pedido direto
- [ ] Carrega numa paráfrase
- [ ] Não carrega num quase-acerto que compartilha vocabulário e pede outra coisa

## Entrega

- [ ] Comando mostrado: `npx skills add devxit/<repo> --skill <nome> -g -y`
- [ ] `npx skills add <caminho> --list` encontra a skill
- [ ] Push só se a pessoa pediu para publicar
