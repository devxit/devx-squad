# README do repositório

Leia este arquivo ao escrever ou atualizar o README para pessoas. O guia da Anthropic separa os dois públicos: a pasta da skill não leva `README.md`; o repositório Git leva um README na raiz.

Escreva o resultado que a pessoa obtém. Não descreva a skill como "uma pasta com frontmatter YAML".

## O que o README da raiz contém

1. Título e um parágrafo: o que muda para quem usa a skill
2. Instalação com o comando exato `npx skills add`
3. Requisito: Node.js para o `npx`; GitHub CLI só se a skill publica repositório
4. Um pedido que a pessoa cola no agente
5. O que ela recebe
6. Árvore do repositório, com `SKILL.md` em `skills/<nome>/`
7. Licença, com link para `LICENSE`

Não invente captura de tela. Use imagem só se a pessoa fornecer o arquivo.

Não grave segredo, token, senha nem conteúdo de `.env`. Nomes de variável, se existirem, ficam como placeholder.

Idioma: o da pessoa. Se ela não escolher, use português.

## Comando

Repositório no GitHub:

```bash
npx skills add devxit/<repo> --skill <nome> -g -y
```

Checkout local:

```bash
npx skills add <caminho-do-repo> --skill <nome> -g -y
```

`-g` instala em `~/.agents/skills`.

## Catálogo que já tem README

Não substitua o README do catálogo pelo modelo de uma skill só. Acrescente a skill na lista e o comando `npx skills add`. O modelo em [assets/repo-readme.md](../assets/repo-readme.md) é para repositório novo, ou para a seção daquela skill.

## Pasta da skill

Se existir `README.md` dentro de `skills/<nome>/`, apague. O conteúdo para o agente vai para `SKILL.md` ou `references/`. O conteúdo para pessoas fica na raiz do repositório.
