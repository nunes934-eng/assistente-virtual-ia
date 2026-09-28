# Documentação do Agente — Nina

## 1. O que o assistente faz

A Nina responde dúvidas de **professores, coordenadores pedagógicos e equipe de secretaria escolar** sobre processos pedagógicos e administrativos comuns no dia a dia da escola (ex.: portfólio do aluno, calendário letivo, recuperação escolar, conselho de classe, PPP, frequência, inclusão, entre outros).

## 2. Para quem ele serve

- **Público principal:** professores e coordenadores pedagógicos da rede municipal/estadual de ensino.
- **Público secundário:** equipe de secretaria escolar que lida com documentação e processos administrativos.

## 3. Como ele deve se comportar (regras de comportamento / "prompt" do agente)

Essas são as regras que orientam cada resposta da Nina (implementadas em `src/app.py` e refletidas na base de conhecimento):

1. **Responder apenas com base na base de conhecimento cadastrada** (`data/base_conhecimento.json`) — nunca inventar informações que não estejam lá.
2. **Assumir clareza e objetividade**: respostas curtas, diretas, sem jargão desnecessário.
3. **Dizer explicitamente quando não souber**, em vez de arriscar um "chute" — e indicar a quem a pessoa pode recorrer (coordenação/secretaria).
4. **Não emitir opinião pessoal nem decisão administrativa** — a Nina apoia com informação, mas não substitui a decisão da equipe gestora.
5. **Manter tom respeitoso e profissional**, adequado ao ambiente escolar.
6. **Registrar cada interação em log** (`docs/log_conversas.txt`), para permitir revisão posterior de quais dúvidas mais aparecem — isso também alimenta a etapa de avaliação.

## 4. O que ele NÃO faz (limites conhecidos)

- Não responde perguntas fora do escopo pedagógico/administrativo escolar (ex.: assuntos pessoais, notícias, outros domínios).
- Não decide casos individuais de alunos (ex.: "o aluno X deve ser retido?") — apenas explica o processo geral.
- Não substitui legislação oficial nem normas específicas da rede de ensino do usuário — a base de conhecimento é um ponto de partida genérico e deve ser adaptada à realidade local.
- Nesta versão, não usa um modelo de linguagem externo — a busca é feita por correspondência de palavras-chave (ver `README.md`).

## 5. Próxima decisão que o assistente ajuda a pessoa a tomar

Depois de entender o processo (ex.: como funciona a recuperação escolar), a pessoa usuária consegue decidir o próximo passo concreto — por exemplo, montar um plano de recuperação paralela para um aluno, ou levar uma dúvida específica para a coordenação com mais clareza sobre o processo geral.
