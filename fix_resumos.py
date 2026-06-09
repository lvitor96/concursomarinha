#!/usr/bin/env python3
"""
fix_resumos.py — Corrige erros de acentuação e endereço em resumos.json.
Execute com: python3 fix_resumos.py
"""

import json, re, pathlib

BASE = pathlib.Path(__file__).parent
DEST = BASE / "data" / "resumos.json"

# ── Substituições de endereço (Bug 2) ───────────────────────────────────────
ENDERECO = [
    # r-lc-01 versaoCompleta
    (
        "Localizado no Eixo Cultural Sudoeste (SEPS 713/913, Asa Sul, Brasília)",
        "Localizado na SGAS 602, Via L2, Asa Sul, Brasília-DF",
    ),
    # r-lc-04 versaoCompleta
    (
        "Localizada na Asa Sul (602 Sul)",
        "Localizada na SGAS 602, Via L2, Asa Sul",
    ),
    # r-lc-04 versaoCurta
    (
        "fica na 602 Sul",
        "localizada na SGAS 602, Via L2, Asa Sul",
    ),
    # Typo de transposição
    (
        "transposi ao",
        "transposição",
    ),
]

# ── Pares de substituição de acentuação (Bug 3) ─────────────────────────────
# Formato: (palavra_errada, palavra_certa)
# Aplicados como \bpalavra\b para evitar falsos positivos.
ACENTOS = [
    # Substantivos / adjetivos comuns
    ("musica",         "música"),
    ("musicas",        "músicas"),
    ("Musica",         "Música"),
    ("Musicas",        "Músicas"),
    ("regencia",       "regência"),
    ("Regencia",       "Regência"),
    ("sinfonica",      "sinfônica"),
    ("sinfonico",      "sinfônico"),
    ("sinfonicas",     "sinfônicas"),
    ("sinfonicos",     "sinfônicos"),
    ("Sinfonica",      "Sinfônica"),
    ("Sinfonico",      "Sinfônico"),
    ("seculo",         "século"),
    ("Seculo",         "Século"),
    ("seculos",        "séculos"),
    ("pedagogica",     "pedagógica"),
    ("pedagogico",     "pedagógico"),
    ("pedagogicas",    "pedagógicas"),
    ("pedagogicos",    "pedagógicos"),
    ("Pedagogica",     "Pedagógica"),
    ("Pedagogico",     "Pedagógico"),
    ("teorica",        "teórica"),
    ("teorico",        "teórico"),
    ("teoricas",       "teóricas"),
    ("teoricos",       "teóricos"),
    ("Teorica",        "Teórica"),
    ("Teorico",        "Teórico"),
    ("tecnica",        "técnica"),
    ("tecnico",        "técnico"),
    ("tecnicas",       "técnicas"),
    ("tecnicos",       "técnicos"),
    ("Tecnica",        "Técnica"),
    ("Tecnico",        "Técnico"),
    ("pratica",        "prática"),
    ("pratico",        "prático"),
    ("praticas",       "práticas"),
    ("praticos",       "práticos"),
    ("Pratica",        "Prática"),
    ("Pratico",        "Prático"),
    ("publica",        "pública"),
    ("publico",        "público"),
    ("publicas",       "públicas"),
    ("publicos",       "públicos"),
    ("Publica",        "Pública"),
    ("Publico",        "Público"),
    ("especifica",     "específica"),
    ("especifico",     "específico"),
    ("especificas",    "específicas"),
    ("especificos",    "específicos"),
    ("Especifica",     "Específica"),
    ("Especifico",     "Específico"),
    ("Especificas",    "Específicas"),
    ("Especificos",    "Específicos"),
    ("basica",         "básica"),
    ("basico",         "básico"),
    ("basicas",        "básicas"),
    ("basicos",        "básicos"),
    ("Basica",         "Básica"),
    ("Basico",         "Básico"),
    ("classica",       "clássica"),
    ("classico",       "clássico"),
    ("classicas",      "clássicas"),
    ("classicos",      "clássicos"),
    ("Classica",       "Clássica"),
    ("Classico",       "Clássico"),
    ("historica",      "histórica"),
    ("historico",      "histórico"),
    ("historicas",     "históricas"),
    ("historicos",     "históricos"),
    ("Historica",      "Histórica"),
    ("Historico",      "Histórico"),
    ("periodo",        "período"),
    ("periodos",       "períodos"),
    ("Periodo",        "Período"),
    ("baritono",       "barítono"),
    ("Baritono",       "Barítono"),
    ("opera",          "ópera"),
    ("Opera",          "Ópera"),
    ("operas",         "óperas"),
    ("eufonio",        "eufônio"),
    ("eufonios",       "eufônios"),
    ("harmonico",      "harmônico"),
    ("harmonica",      "harmônica"),
    ("Harmonico",      "Harmônico"),
    ("tipica",         "típica"),
    ("tipico",         "típico"),
    ("tipicas",        "típicas"),
    ("tipicos",        "típicos"),
    ("Tipica",         "Típica"),
    ("Tipico",         "Típico"),
    ("academica",      "acadêmica"),
    ("academico",      "acadêmico"),
    ("Academica",      "Acadêmica"),
    ("Academico",      "Acadêmico"),
    ("ritmica",        "rítmica"),
    ("ritmico",        "rítmico"),
    ("Ritmica",        "Rítmica"),
    ("Ritmico",        "Rítmico"),
    ("ritmo",          "ritmo"),   # já correto — não alterar
    ("eletrico",       "elétrico"),
    ("eletrica",       "elétrica"),
    ("eletricos",      "elétricos"),
    ("eletricas",      "elétricas"),
    ("Eletrico",       "Elétrico"),
    ("cerimonias",     "cerimônias"),
    ("cerimonia",      "cerimônia"),
    ("Cerimonias",     "Cerimônias"),
    ("Cerimonia",      "Cerimônia"),
    ("pracas",         "praças"),
    ("praca",          "praça"),
    ("Pracas",         "Praças"),
    ("Praca",          "Praça"),
    ("metrica",        "métrica"),
    ("metrico",        "métrico"),
    ("Metrica",        "Métrica"),
    ("Metrico",        "Métrico"),
    ("timbristica",    "timbrística"),
    ("Timbristica",    "Timbrística"),
    ("interpretativa", "interpretativa"),  # já correto
    ("propria",        "própria"),
    ("proprio",        "próprio"),
    ("proprias",       "próprias"),
    ("proprios",       "próprios"),
    ("Propria",        "Própria"),
    ("Proprio",        "Próprio"),
    # Substantivos terminados em -ção / -ções
    ("percussao",      "percussão"),
    ("Percussao",      "Percussão"),
    ("educacao",       "educação"),
    ("Educacao",       "Educação"),
    ("formacao",       "formação"),
    ("Formacao",       "Formação"),
    ("composicao",     "composição"),
    ("Composicao",     "Composição"),
    ("coordenacao",    "coordenação"),
    ("Coordenacao",    "Coordenação"),
    ("atribuicao",     "atribuição"),
    ("Atribuicao",     "Atribuição"),
    ("atribuicoes",    "atribuições"),
    ("Atribuicoes",    "Atribuições"),
    ("comunicacao",    "comunicação"),
    ("Comunicacao",    "Comunicação"),
    ("edicao",         "edição"),
    ("Edicao",         "Edição"),
    ("transicao",      "transição"),
    ("Transicao",      "Transição"),
    ("producao",       "produção"),
    ("Producao",       "Produção"),
    ("distribuicao",   "distribuição"),
    ("Distribuicao",   "Distribuição"),
    ("regulamentacao", "regulamentação"),
    ("Regulamentacao", "Regulamentação"),
    ("organizacao",    "organização"),
    ("Organizacao",    "Organização"),
    ("articulacao",    "articulação"),
    ("Articulacao",    "Articulação"),
    ("avaliacao",      "avaliação"),
    ("Avaliacao",      "Avaliação"),
    ("tradicao",       "tradição"),
    ("Tradicao",       "Tradição"),
    ("relacao",        "relação"),
    ("Relacao",        "Relação"),
    ("selecao",        "seleção"),
    ("Selecao",        "Seleção"),
    ("preparacao",     "preparação"),
    ("Preparacao",     "Preparação"),
    ("apresentacao",   "apresentação"),
    ("Apresentacao",   "Apresentação"),
    ("notacao",        "notação"),
    ("Notacao",        "Notação"),
    ("correcao",       "correção"),
    ("Correcao",       "Correção"),
    ("afinacao",       "afinação"),
    ("Afinacao",       "Afinação"),
    ("aplicacao",      "aplicação"),
    ("Aplicacao",      "Aplicação"),
    ("adaptacao",      "adaptação"),
    ("Adaptacao",      "Adaptação"),
    ("exploracao",     "exploração"),
    ("Exploracao",     "Exploração"),
    ("expressao",      "expressão"),
    ("Expressao",      "Expressão"),
    ("funcao",         "função"),
    ("Funcao",         "Função"),
    ("funcoes",        "funções"),
    ("Funcoes",        "Funções"),
    ("solucao",        "solução"),
    ("Solucao",        "Solução"),
    ("informacao",     "informação"),
    ("Informacao",     "Informação"),
    ("utilizacao",     "utilização"),
    ("Utilizacao",     "Utilização"),
    ("situacao",       "situação"),
    ("Situacao",       "Situação"),
    ("instituicao",    "instituição"),
    ("Instituicao",    "Instituição"),
    ("repeticao",      "repetição"),
    ("Repeticao",      "Repetição"),
    ("repeticoes",     "repetições"),
    ("cancao",         "canção"),
    ("Cancao",         "Canção"),
    ("cancoes",        "canções"),
    ("Cancoes",        "Canções"),
    ("execucao",       "execução"),
    ("Execucao",       "Execução"),
    ("posicao",        "posição"),
    ("Posicao",        "Posição"),
    ("disposicao",     "disposição"),
    ("Disposicao",     "Disposição"),
    ("composicoes",    "composições"),
    ("Composicoes",    "Composições"),
    ("profissao",      "profissão"),
    ("Profissao",      "Profissão"),
    ("ampliacao",      "ampliação"),
    ("Ampliacao",      "Ampliação"),
    ("formacoes",      "formações"),
    ("Formacoes",      "Formações"),
    ("licao",          "lição"),
    ("Licao",          "Lição"),
    ("colocacao",      "colocação"),
    ("Colocacao",      "Colocação"),
    ("sensacao",       "sensação"),
    ("Sensacao",       "Sensação"),
    ("audição",        "audição"),  # já correto
    ("audicao",        "audição"),
    ("Audicao",        "Audição"),
    ("regiao",         "região"),
    ("Regiao",         "Região"),
    ("regioes",        "regiões"),
    ("Regioes",        "Regiões"),
    ("precisao",       "precisão"),
    ("Precisao",       "Precisão"),
    ("Manutencao",     "Manutenção"),
    ("manutencao",     "manutenção"),
    # Outros padrões comuns
    ("padrao",         "padrão"),
    ("padroes",        "padrões"),
    ("Padrao",         "Padrão"),
    ("Padroes",        "Padrões"),
    ("orgao",          "órgão"),
    ("orgaos",         "órgãos"),
    ("Orgao",          "Órgão"),
    # nao / não — muito cuidado: só substituir como palavra isolada
    # Feito via regex abaixo
]

def aplicar_substituicoes(texto: str) -> str:
    # Substituições de endereço (texto exato)
    for errado, certo in ENDERECO:
        texto = texto.replace(errado, certo)

    # Substituições de acento (palavra exata com word boundary)
    for errado, certo in ACENTOS:
        # \b funciona razoavelmente com Unicode no Python
        texto = re.sub(r'\b' + re.escape(errado) + r'\b', certo, texto)

    # "nao" → "não" como palavra isolada
    texto = re.sub(r'\bnao\b', 'não', texto)
    texto = re.sub(r'\bNao\b', 'Não', texto)
    texto = re.sub(r'\bNAO\b', 'NÃO', texto)

    # "O que e X" / "o que e X" → "é" (verbo ser, não conjunção)
    texto = re.sub(r'\bO que e\b', 'O que é', texto)
    texto = re.sub(r'\bo que e\b', 'o que é', texto)
    texto = re.sub(r'\bdo que e\b', 'do que é', texto)

    return texto

def main():
    with open(DEST, encoding="utf-8") as f:
        banco = json.load(f)

    # IDs afetados (regência + legislação CEP)
    IDS_AFETADOS = {
        "r-re-03", "r-re-04", "r-re-05", "r-re-06",
        "r-lc-01", "r-lc-02", "r-lc-03", "r-lc-04",
    }

    alterados = 0
    for resumo in banco["resumos"]:
        if resumo["id"] not in IDS_AFETADOS:
            continue

        original = json.dumps(resumo, ensure_ascii=False)

        for campo in ("nome", "versaoCurta", "versaoCompleta"):
            if campo in resumo and resumo[campo]:
                resumo[campo] = aplicar_substituicoes(resumo[campo])

        depois = json.dumps(resumo, ensure_ascii=False)
        if original != depois:
            print(f"  ✓ {resumo['id']} — corrigido")
            alterados += 1

    with open(DEST, "w", encoding="utf-8") as f:
        json.dump(banco, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {alterados} resumo(s) corrigido(s). Arquivo salvo.")

if __name__ == "__main__":
    main()
