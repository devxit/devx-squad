# Description

Leia este arquivo ao rascunhar ou corrigir o campo `description`.

O agente lê só `name` e `description` para decidir se carrega a skill. O campo carrega o disparo inteiro.

## Forma

Uma linha só, em terceira pessoa:

`[O que faz]. Use when [pedidos reais, inclusive paráfrase e o nome do domínio].`

Inclua frases que a pessoa diria, no idioma em que ela pede a skill. Se o público mistura português e inglês, cubra os dois no mesmo campo.

Limites da especificação:

- 1 a 1024 caracteres
- sem `<` e sem `>`
- diz o que a skill faz e quando usar

## Disparo

Escreva a favor de carregar. Liste contextos em que a skill serve mesmo sem o nome do domínio.

Depois revise com 6 pedidos:

- 3 que devem carregar: um direto, um parafraseado, um informal
- 3 quase-acertos que não devem carregar: compartilham vocabulário e pedem outra coisa

Pedido obviamente fora do tema não testa a description. Não copie palavras de um pedido que falhou para "consertar" o campo: generalize o caso.

## Exemplos

Serve:

```yaml
description: Extracts text and tables from PDF files, fills forms, and merges PDFs. Use when the user works with PDF documents or mentions PDFs, forms, or document extraction.
```

Não serve:

```yaml
description: Helps with documents.
```
