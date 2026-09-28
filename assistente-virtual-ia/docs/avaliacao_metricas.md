# Avaliação e Métricas

## Como a Nina foi testada

Foi montado um pequeno conjunto de perguntas de teste, cobrindo três situações:

1. Perguntas **dentro** do escopo (devem receber resposta da base de conhecimento).
2. Perguntas **fora** do escopo (devem receber a mensagem de "não sei").
3. Perguntas **ambíguas/mal formuladas** (verificar se o limiar de confiança evita respostas erradas).

## Casos de teste e resultado

| # | Pergunta | Esperado | Resultado obtido | ✅/❌ |
|---|----------|----------|-------------------|-------|
| 1 | "como funciona o portfólio do aluno?" | Explicar o portfólio | Respondeu corretamente sobre portfólio | ✅ |
| 2 | "quando é o conselho de classe?" | Explicar conselho de classe | Respondeu corretamente | ✅ |
| 3 | "o que é o PPP da escola?" | Explicar PPP | Respondeu corretamente | ✅ |
| 4 | "quantos dias letivos tem o ano?" | Explicar calendário letivo | Respondeu corretamente | ✅ |
| 5 | "qual é a previsão do tempo amanhã?" | Dizer que não sabe | Retornou mensagem de "não sei" | ✅ |
| 6 | "aluno" (palavra solta) | Não deveria "chutar" um tópico só com 1 palavra-chave | Retornou "não sei" (abaixo do limiar) | ✅ |
| 7 | "reunião" (palavra solta) | Ambíguo entre "conselho de classe" e "reunião de pais" | Retornou "não sei" (abaixo do limiar) | ✅ |

## Métrica usada

Como o protótipo é baseado em correspondência de palavras-chave (e não em um modelo probabilístico), a métrica adotada foi simples e observacional:

- **Taxa de acerto nos casos dentro do escopo:** 4/4 (100%) nos testes realizados.
- **Taxa de recusa correta nos casos fora do escopo:** 3/3 (100%) — a Nina não inventou resposta em nenhum caso fora da base.

> Em uma base de conhecimento maior e com perguntas mais variadas de usuários reais, o ideal é registrar as interações via `docs/log_conversas.txt` (gerado automaticamente pela aplicação) e revisar periodicamente quais perguntas caíram em "não sei" — isso indica onde a base de conhecimento precisa crescer.

## Limitações identificadas

- O `LIMIAR_CONFIANCA` (mínimo de 2 palavras-chave em comum) é um ajuste manual: baixo demais gera respostas erradas; alto demais faz a Nina dizer "não sei" para perguntas válidas. Vale recalibrar conforme a base crescer.
- A busca por palavras-chave não entende sinônimos que não estejam cadastrados (ex.: se alguém disser "boletim" em vez de "nota", pode não encontrar recuperação escolar). Isso poderia ser resolvido futuramente com um modelo de linguagem.
