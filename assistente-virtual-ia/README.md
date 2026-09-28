# Nina — Assistente Virtual de Apoio Pedagógico Escolar

Projeto desenvolvido para o Lab **"Construa Seu Assistente Virtual Com Inteligência Artificial"**.

## 🎯 Sobre o projeto

A **Nina** é um assistente virtual pensado para apoiar **professores, coordenadores pedagógicos e equipes de secretaria escolar** com dúvidas do dia a dia sobre processos pedagógicos e administrativos da escola — por exemplo: portfólio do aluno, calendário letivo, recuperação escolar, conselho de classe, PPP, entre outros.

O objetivo não é substituir a coordenação pedagógica, e sim **agilizar respostas para dúvidas recorrentes**, liberando tempo da equipe para questões mais complexas.

## 🧩 Como o projeto está organizado

```
assistente-virtual-ia/
├── README.md                      → este arquivo
├── data/
│   └── base_conhecimento.json     → base de conhecimento (perguntas/temas e respostas)
├── docs/
│   ├── documentacao.md            → o que o assistente faz e como se comporta
│   ├── avaliacao_metricas.md      → como o assistente foi testado
│   └── pitch.md                   → pitch final do projeto
└── src/
    └── app.py                     → aplicação funcional (chat via terminal)
```

Essa estrutura segue os 6 passos pedidos no desafio:

1. **Documentação** → `docs/documentacao.md`
2. **Base de conhecimento** → `data/base_conhecimento.json`
3. **Prompts / regras de resposta** → dentro de `docs/documentacao.md` (seção "Regras de comportamento") e comentados em `src/app.py`
4. **Aplicação funcional** → `src/app.py`
5. **Avaliação e métricas** → `docs/avaliacao_metricas.md`
6. **Pitch** → `docs/pitch.md`

## ▶️ Como executar

Pré-requisito: ter Python 3 instalado (não precisa de nenhuma biblioteca externa nem de chave de API).

```bash
cd assistente-virtual-ia
python3 src/app.py
```

Depois é só conversar com a Nina no terminal. Digite `sair` para encerrar.

### Exemplo de uso

```
Você: como funciona o portfólio do aluno?
Nina: [Assunto: Portfólio do aluno]
      O portfólio reúne produções do aluno ao longo do período letivo (...)

Você: qual é a previsão do tempo amanhã?
Nina: Não tenho informação suficiente sobre isso na minha base de conhecimento ainda (...)
```

## 🧠 Como a Nina decide o que responder

A Nina usa **correspondência de palavras-chave** entre a pergunta da pessoa usuária e os tópicos cadastrados em `data/base_conhecimento.json`. Se nenhum tópico atinge um número mínimo de palavras-chave em comum, ela **assume que não sabe** em vez de inventar uma resposta — esse é um requisito central do desafio (evitar respostas inventadas).

> 💡 Essa versão não depende de uma API de IA externa, o que facilita rodar o projeto sem custos e sem chaves. Uma evolução natural (comentada em `docs/pitch.md`) é trocar a busca por palavras-chave por uma chamada a um modelo de linguagem (ex.: API da Anthropic/OpenAI), mantendo a mesma base de conhecimento.

## 📌 Próximos passos possíveis

- Ampliar a base de conhecimento com mais tópicos reais da escola/secretaria.
- Conectar a um modelo de linguagem para respostas mais naturais, mantendo a mesma base como fonte da verdade.
- Criar uma interface web simples (ex.: Streamlit) no lugar do terminal.
