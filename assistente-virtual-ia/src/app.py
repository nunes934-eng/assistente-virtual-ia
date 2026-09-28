"""
Nina - Assistente Virtual de Apoio Pedagógico Escolar
Aplicação funcional (passo 4 do desafio).

Regras de comportamento (ver docs/documentacao.md):
- Responder só com base na base de conhecimento (data/base_conhecimento.json).
- Nunca inventar resposta: se não houver correspondência suficiente,
  dizer claramente que não tem informação.
- Registrar cada pergunta em log para alimentar a avaliação (docs/avaliacao_metricas.md).
"""

import json
import os
import re
from datetime import datetime

CAMINHO_BASE = os.path.join(os.path.dirname(__file__), "..", "data", "base_conhecimento.json")
CAMINHO_LOG = os.path.join(os.path.dirname(__file__), "..", "docs", "log_conversas.txt")

# Número mínimo de palavras-chave em comum para considerar uma resposta confiável.
LIMIAR_CONFIANCA = 2

MENSAGEM_SEM_INFORMACAO = (
    "Não tenho informação suficiente sobre isso na minha base de conhecimento ainda. "
    "Recomendo consultar a coordenação pedagógica ou a secretaria escolar para essa questão específica, "
    "ou tente reformular a pergunta com outras palavras."
)


def carregar_base(caminho=CAMINHO_BASE):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^\w\s]", " ", texto)
    return texto


def pontuar_item(pergunta_usuario, item):
    palavras_usuario = set(normalizar(pergunta_usuario).split())
    palavras_chave = {normalizar(p) for p in item.get("palavras_chave", [])}
    return len(palavras_usuario & palavras_chave)


def buscar_resposta(pergunta_usuario, base):
    melhor_item = None
    melhor_pontuacao = 0
    for item in base:
        pontuacao = pontuar_item(pergunta_usuario, item)
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_item = item
    if melhor_item and melhor_pontuacao >= LIMIAR_CONFIANCA:
        return melhor_item["resposta"], melhor_item["topico"], melhor_pontuacao
    return None, None, melhor_pontuacao


def montar_resposta(resposta, topico):
    return f"[Assunto: {topico}]\n{resposta}"


def registrar_log(pergunta, topico, pontuacao):
    os.makedirs(os.path.dirname(CAMINHO_LOG), exist_ok=True)
    with open(CAMINHO_LOG, "a", encoding="utf-8") as arquivo:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        topico_registrado = topico if topico else "SEM_CORRESPONDENCIA"
        arquivo.write(f"{agora} | pergunta='{pergunta}' | topico='{topico_registrado}' | pontuacao={pontuacao}\n")


def executar_conversa():
    base = carregar_base()
    print("=" * 60)
    print("Nina - Assistente de Apoio Pedagógico Escolar")
    print("Digite sua dúvida ou 'sair' para encerrar.")
    print("=" * 60)
    while True:
        pergunta = input("\nVocê: ").strip()
        if pergunta.lower() in ("sair", "exit", "quit"):
            print("Nina: Até logo! 👋")
            break
        if not pergunta:
            continue
        resposta, topico, pontuacao = buscar_resposta(pergunta, base)
        if resposta:
            print(f"\nNina: {montar_resposta(resposta, topico)}")
        else:
            print(f"\nNina: {MENSAGEM_SEM_INFORMACAO}")
        registrar_log(pergunta, topico, pontuacao)


if __name__ == "__main__":
    executar_conversa()
