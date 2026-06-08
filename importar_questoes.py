#!/usr/bin/env python3
"""
importar_questoes.py — Importador em lote para data/questoes.json

Uso:
  python3 importar_questoes.py questoes_novas.csv
  python3 importar_questoes.py questoes_novas.json
  python3 importar_questoes.py questoes_novas.csv --dry-run   # valida sem gravar

Formatos aceitos:
  • CSV  — separado por ; (ponto-e-vírgula), encoding UTF-8
  • JSON — lista de objetos com os mesmos campos do CSV

Campos obrigatórios: enunciado, A, B, C, D, E, gabarito, explicacao,
                     banca, ano, edital, tipo, bloco, disciplina,
                     topico, incidencia, origem

Campos opcionais:
  F  — quinta alternativa (deixe em branco se a questão tiver só A–D)
"""

import csv
import json
import pathlib
import sys
import argparse

BASE = pathlib.Path(__file__).parent
DEST = BASE / "data" / "questoes.json"

CAMPOS_OBRIGATORIOS = [
    "enunciado", "A", "B", "C", "D", "gabarito", "explicacao",
    "banca", "ano", "edital", "tipo", "bloco", "disciplina",
    "topico", "incidencia", "origem",
]

BLOCOS_VALIDOS      = {"basicos", "complementares", "especificos"}
INCIDENCIAS_VALIDAS = {"alta", "media", "baixa"}
TIPOS_VALIDOS       = {"efetivo", "temporario"}

# ──────────────────────────────────────────────────────────────
def carregar_csv(caminho: pathlib.Path) -> list[dict]:
    with open(caminho, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        return [dict(row) for row in reader]

def carregar_json(caminho: pathlib.Path) -> list[dict]:
    with open(caminho, encoding="utf-8") as f:
        dados = json.load(f)
    if not isinstance(dados, list):
        raise ValueError("O arquivo JSON deve conter uma lista de objetos.")
    return dados

def validar_linha(row: dict, num: int) -> list[str]:
    erros = []
    for campo in CAMPOS_OBRIGATORIOS:
        if not str(row.get(campo, "")).strip():
            erros.append(f"  Linha {num}: campo '{campo}' está vazio ou ausente")

    bloco = str(row.get("bloco", "")).strip()
    if bloco and bloco not in BLOCOS_VALIDOS:
        erros.append(f"  Linha {num}: bloco '{bloco}' inválido. Use: {BLOCOS_VALIDOS}")

    inc = str(row.get("incidencia", "")).strip()
    if inc and inc not in INCIDENCIAS_VALIDAS:
        erros.append(f"  Linha {num}: incidencia '{inc}' inválida. Use: {INCIDENCIAS_VALIDAS}")

    gab = str(row.get("gabarito", "")).strip().upper()
    alts = {"A", "B", "C", "D"}
    if row.get("E", "").strip():
        alts.add("E")
    if row.get("F", "").strip():
        alts.add("F")
    if gab not in alts:
        erros.append(f"  Linha {num}: gabarito '{gab}' não corresponde a nenhuma alternativa presente")

    try:
        int(row.get("ano", ""))
    except (ValueError, TypeError):
        erros.append(f"  Linha {num}: 'ano' deve ser um número inteiro (ex.: 2022)")

    return erros

def montar_questao(row: dict, novo_id: str) -> dict:
    alts = {
        "A": str(row.get("A", "")).strip(),
        "B": str(row.get("B", "")).strip(),
        "C": str(row.get("C", "")).strip(),
        "D": str(row.get("D", "")).strip(),
    }
    if str(row.get("E", "")).strip():
        alts["E"] = str(row["E"]).strip()
    if str(row.get("F", "")).strip():
        alts["F"] = str(row["F"]).strip()

    return {
        "id":           novo_id,
        "enunciado":    str(row["enunciado"]).strip(),
        "alternativas": alts,
        "gabarito":     str(row["gabarito"]).strip().upper(),
        "explicacao":   str(row["explicacao"]).strip(),
        "banca":        str(row["banca"]).strip(),
        "ano":          int(row["ano"]),
        "edital":       str(row["edital"]).strip(),
        "tipo":         str(row.get("tipo", "efetivo")).strip(),
        "bloco":        str(row["bloco"]).strip(),
        "disciplina":   str(row["disciplina"]).strip(),
        "topico":       str(row["topico"]).strip(),
        "incidencia":   str(row["incidencia"]).strip(),
        "origem":       str(row["origem"]).strip(),
    }

def proximo_id(existentes: list[dict]) -> str:
    """Gera o próximo ID sequencial (q001, q002 …)."""
    numeros = []
    for q in existentes:
        qid = str(q.get("id", ""))
        if qid.startswith("q") and qid[1:].isdigit():
            numeros.append(int(qid[1:]))
    base = max(numeros, default=0) + 1
    return base  # retorna int; gerado como f"q{n:03d}" abaixo

# ──────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Importa questões em lote para questoes.json")
    parser.add_argument("arquivo", help="CSV ou JSON com as questões a importar")
    parser.add_argument("--dry-run", action="store_true", help="Valida sem gravar")
    args = parser.parse_args()

    caminho = pathlib.Path(args.arquivo)
    if not caminho.exists():
        print(f"❌ Arquivo não encontrado: {caminho}")
        sys.exit(1)

    # Carrega novas questões
    ext = caminho.suffix.lower()
    if ext == ".csv":
        novas_raw = carregar_csv(caminho)
    elif ext == ".json":
        novas_raw = carregar_json(caminho)
    else:
        print("❌ Formato não suportado. Use .csv ou .json")
        sys.exit(1)

    print(f"📂 {len(novas_raw)} questão(ões) encontrada(s) em '{caminho.name}'")

    # Valida
    todos_erros = []
    for i, row in enumerate(novas_raw, start=2):  # linha 1 = cabeçalho CSV
        todos_erros.extend(validar_linha(row, i))

    if todos_erros:
        print(f"\n⚠️  {len(todos_erros)} erro(s) de validação:")
        for e in todos_erros:
            print(e)
        print("\nCorriga os erros acima e tente novamente.")
        sys.exit(1)

    # Carrega banco atual
    with open(DEST, encoding="utf-8") as f:
        banco = json.load(f)

    existentes = banco.get("questoes", [])
    proximo_num = proximo_id(existentes)

    # Monta novas questões
    adicionadas = []
    for i, row in enumerate(novas_raw):
        qid = f"q{proximo_num + i:03d}"
        adicionadas.append(montar_questao(row, qid))

    if args.dry_run:
        print(f"\n✅ Validação OK — {len(adicionadas)} questão(ões) pronta(s) para importar.")
        print("   (use sem --dry-run para gravar)")
        return

    # Grava
    banco["questoes"] = existentes + adicionadas

    total_por_bloco = {}
    for q in banco["questoes"]:
        b = q.get("bloco", "?")
        total_por_bloco[b] = total_por_bloco.get(b, 0) + 1

    with open(DEST, "w", encoding="utf-8") as f:
        json.dump(banco, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Importação concluída!")
    print(f"   + {len(adicionadas)} questão(ões) adicionada(s)")
    print(f"   = {len(banco['questoes'])} total no banco")
    print(f"   Distribuição por bloco: {total_por_bloco}")

if __name__ == "__main__":
    main()
