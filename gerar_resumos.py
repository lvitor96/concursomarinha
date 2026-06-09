#!/usr/bin/env python3
"""Gera resumos faltantes e atualiza data/resumos.json"""
import json, pathlib

BASE = pathlib.Path(__file__).parent
SRC  = BASE / "data" / "resumos.json"

with open(SRC) as f:
    dados = json.load(f)

existentes = {r["topico"] for r in dados["resumos"]}

NOVOS = []

# ════════════════════════════════════════════════════
# CONHECIMENTOS BÁSICOS — LÍNGUA PORTUGUESA
# ════════════════════════════════════════════════════

NOVOS.append({
  "id": "r-pt-01", "topico": "pt-01", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Interpretação de textos", "incidencia": "alta",
  "versaoCurta": """# Interpretação de Textos

## Tipos de questão
- **Tema/assunto central**: do que o texto trata em geral
- **Ideia principal**: tese ou argumento central do autor
- **Inferência**: conclusão que se deduz do texto (não está explícita)
- **Vocabulário em contexto**: sentido da palavra no trecho
- **Referência pronominal**: a quê/quem o pronome remete

## Estratégias de leitura
- Leia o enunciado **antes** do texto para saber o foco
- Sublinhe palavras-chave e operadores argumentativos (mas, porém, portanto, embora)
- Releia o trecho citado na questão com o parágrafo anterior e posterior
- Cuidado com alternativas que usam vocabulário do texto mas distorcem o sentido

## Armadilhas frequentes
- Alternativas **verdadeiras em geral** mas não sustentadas pelo texto
- Extrapolação: o texto não afirma isso, apenas sugere
- Inversão de causa e efeito
- Negação parcial: "apenas", "somente", "sempre", "nunca" exigem atenção

## Operadores argumentativos importantes
- Adição: e, além disso, também, ainda
- Oposição: mas, porém, contudo, entretanto, todavia
- Conclusão: portanto, logo, assim, então
- Concessão: embora, apesar de, ainda que

## Para a prova
- É o tópico mais cobrado de Língua Portuguesa na SEDF (≈17% das questões)
- A resposta correta está sempre sustentada pelo texto — nunca pelo conhecimento externo
- Questões de inferência pedem o que o texto **permite concluir**, não o que você acha""",
  "versaoCompleta": """# Interpretação de Textos — Estudo Completo

## Por que é o tópico mais cobrado

Nas provas da Quadrix para a SEDF, interpretação de textos responde por cerca de 17% das questões de Língua Portuguesa. A habilidade avaliada é sempre a mesma: extrair informações e sentidos a partir do que está efetivamente escrito — nem mais, nem menos.

## Tipos de questão e como resolvê-los

**Tema e assunto central**
O *assunto* é o objeto do texto (sobre o que fala). O *tema* é a abordagem do assunto (o que o texto diz sobre ele). Para identificar, pergunte: "Se fosse resumir este texto em uma frase, qual seria?"

**Ideia principal**
É o argumento central, a tese que o autor defende. Costuma aparecer na introdução ou na conclusão. Em textos jornalísticos, frequentemente está no primeiro parágrafo.

**Inferência e implicação**
A questão pede o que o texto *permite concluir* sem afirmar explicitamente. A resposta deve ser logicamente necessária a partir das informações dadas — não uma mera possibilidade nem uma extrapolação.

**Vocabulário em contexto**
A palavra é polissêmica (tem vários sentidos). O enunciado sempre aponta o parágrafo/linha. Releia o trecho substituindo mentalmente cada alternativa. A correta mantém o sentido coerente do trecho.

**Referência pronominal**
Identifique o antecedente do pronome. Leia a frase com o antecedente no lugar do pronome para confirmar.

## Operadores argumentativos

Os conectivos organizam a argumentação:
- **Adição/soma**: e, também, além disso, ainda, bem como
- **Oposição/contraste**: mas, porém, contudo, entretanto, todavia, no entanto
- **Conclusão**: portanto, logo, assim, então, por isso, consequentemente
- **Concessão**: embora, apesar de, ainda que, mesmo que
- **Explicação**: porque, pois, já que, visto que
- **Condição**: se, caso, desde que, a menos que

Questões frequentemente testam se o candidato percebe que a troca de um conector muda o sentido da relação entre ideias.

## Estratégia de resolução

1. Leia o enunciado e identifique o tipo de questão
2. Localize no texto o trecho relevante
3. Releia com o parágrafo de contexto (anterior + seguinte)
4. Elimine alternativas que contradizem o texto ou extrapolam
5. Confirme que a alternativa escolhida tem respaldo textual

## Erros frequentes dos candidatos

- Escolher alternativa verdadeira na vida real mas não fundamentada no texto
- Confundir "o texto afirma" com "o texto sugere/implica"
- Não perceber negações embutidas nas alternativas ("não é correto afirmar que...")
- Ignorar o contexto: uma palavra muda de sentido conforme o trecho"""
})

NOVOS.append({
  "id": "r-pt-02", "topico": "pt-02", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Reescrita de frases e substituição de palavras", "incidencia": "alta",
  "versaoCurta": """# Reescrita de Frases

## O que é avaliado
- Substituir palavra/expressão **sem alterar o sentido** original
- Reescrever frase em nova estrutura mantendo equivalência semântica
- Identificar qual reescrita **muda** o sentido (questões negativas)

## Operações frequentes
| Operação | Exemplo |
|---|---|
| Voz ativa → passiva | "A professora corrigiu a prova" → "A prova foi corrigida pela professora" |
| Substituição de conector | "Estudou, portanto passou" → "Como estudou, passou" |
| Nominalizações | "É necessário estudar" → "A necessidade de estudo" |
| Pronome relativo | "O aluno que chegou…" → "O aluno, chegando…" |

## Armadilhas
- Troca de conector que inverte a relação lógica (mas ↔ porque)
- Voz passiva analítica vs. sintética ("foi feito" vs. "fez-se")
- Mudança de sujeito na reestruturação
- Pronome que muda o referente

## Equivalências de conectores para decorar
- mas / porém / contudo / entretanto / todavia / no entanto → OPOSIÇÃO
- portanto / logo / assim / por isso / consequentemente → CONCLUSÃO
- porque / pois / já que / visto que / uma vez que → CAUSA/EXPLICAÇÃO
- embora / apesar de / ainda que / mesmo que → CONCESSÃO

## Para a prova
- 2ª questão mais cobrada de Português na SEDF (≈16%)
- Sempre verifique: sujeito e objeto mantidos? Relação lógica preservada?
- Questões de VOZ PASSIVA: o objeto direto vira sujeito; agente vai para "por"
- Desconfie de alternativas que parecem equivalentes mas trocam um conector""",
  "versaoCompleta": """# Reescrita de Frases — Estudo Completo

## O que a banca avalia

Reescrita de frases é o segundo tópico mais cobrado de Português nas provas da Quadrix. O que muda em relação à interpretação é que aqui o candidato precisa dominar a gramática estrutural: como reorganizar a frase mantendo o sentido, ou identificar quando a reorganização altera o sentido.

## Voz verbal: ativa, passiva e reflexiva

**Ativa para passiva analítica**
- Sujeito ativo → agente da passiva (precedido de "por/pelo/pela")
- Objeto direto → sujeito da passiva
- Verbo → auxiliar "ser" + particípio, concordando com o novo sujeito
- Exemplo: "O governo publicou a lei" → "A lei foi publicada pelo governo"

**Passiva sintética (voz média com "se")**
- "Publicou-se a lei" (= "A lei foi publicada")
- Somente com verbos transitivos diretos
- O "se" é partícula apassivadora, não pronome reflexivo

**Erro frequente na reescrita**: esquecimento do agente da passiva ou erro de concordância do particípio.

## Substituição de conectores

A troca de conector é a operação mais testada. O candidato deve saber:

| Relação | Conectores equivalentes |
|---|---|
| Oposição/adversidade | mas, porém, contudo, entretanto, todavia, no entanto, ao passo que |
| Conclusão | portanto, logo, assim, então, por isso, consequentemente, dessa forma |
| Causa/explicação | porque, pois, já que, visto que, uma vez que, dado que |
| Concessão | embora, apesar de (que), ainda que, mesmo que, conquanto |
| Finalidade | para que, a fim de que, com o objetivo de |
| Condição | se, caso, desde que, contanto que, a menos que |

**Atenção**: "pois" pode ser conclusivo (posposto ao verbo: "Estude, pois é importante") ou explicativo (anteposto: "Pois é importante, estude").

## Nominalização e transformações estruturais

Nominalizar = transformar verbo em substantivo:
- "É preciso revisar" → "A revisão é necessária"
- "O professor avaliou os alunos" → "A avaliação dos alunos pelo professor"

Essas transformações afetam a coesão e o estilo, mas não o sentido nuclear.

## Ordem dos termos e ênfase

A inversão da ordem sintática (hipérbato/anástrofe) é estilística mas não muda o sentido:
- "Estudou muito o candidato" = "O candidato estudou muito"
- Porém, pronomes oblíquos mudam de posição conforme a regência do verbo

## Estratégia de prova

Para cada alternativa de reescrita, pergunte:
1. O sujeito gramatical é o mesmo? (ou mudou quem pratica a ação)
2. A relação lógica é a mesma? (conector preservado ou equivalente)
3. O objeto/complemento está completo?
4. A negação está mantida?"""
})

NOVOS.append({
  "id": "r-pt-03", "topico": "pt-03", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Morfologia", "incidencia": "alta",
  "versaoCurta": """# Morfologia — Classes de Palavras

## As 10 classes gramaticais
| Classe | Flexiona em | Exemplos |
|---|---|---|
| **Substantivo** | gênero, número, grau | escola, professor, música |
| **Adjetivo** | gênero, número, grau | bom, musical, educativo |
| **Verbo** | modo, tempo, pessoa, número | estudar, é, foi aprovado |
| **Advérbio** | grau (intensidade) | muito, rapidamente, bem |
| **Pronome** | tipo, gênero, número | eu, meu, que, quem |
| **Artigo** | gênero, número | o/a/os/as, um/uma |
| **Numeral** | gênero, número | dois, primeiro, dobro |
| **Preposição** | invariável | de, em, para, com, por |
| **Conjunção** | invariável | e, mas, porque, embora |
| **Interjeição** | invariável | Ah!, Oba!, Silêncio! |

## Pontos mais cobrados
- **Verbo**: modo indicativo/subjuntivo/imperativo; formas nominais (infinitivo, gerúndio, particípio)
- **Pronome relativo**: que, quem, cujo, onde, o qual → importantíssimos para sintaxe
- **Advérbio vs. adjetivo**: "O aluno falou *errado*" (adv.) vs. "A resposta *errada*" (adj.)
- **Palavras invariáveis**: preposições e conjunções não têm gênero/número

## Formação de palavras
- **Derivação**: prefixal, sufixal, parassintética (en+gordar), regressiva, imprópria
- **Composição**: justaposição (girassol) e aglutinação (planalto)

## Para a prova
- Morfologia ≈ 14% das questões de Português — 3ª mais cobrada
- Questões de verbo: identifique o modo e o tempo (pretérito imperfeito do subjuntivo é muito testado)
- "Cujo" = de quem / do qual — nunca seguido de artigo ("cujo o" está errado)""",
  "versaoCompleta": """# Morfologia — Estudo Completo

## As Classes Gramaticais e suas características

**Substantivo**
Nome de seres, objetos, sentimentos, ações e qualidades. Flexiona em gênero (masculino/feminino), número (singular/plural) e grau (aumentativo/diminutivo). Pode ser: próprio/comum, concreto/abstrato, simples/composto, primitivo/derivado, coletivo.

**Adjetivo**
Caracteriza ou qualifica o substantivo. Concorda em gênero e número com o substantivo. Grau comparativo (mais… do que / tão… quanto) e superlativo (absoluto: muito belo / belíssimo; relativo: o mais belo de).

**Verbo**
Flexiona em: *pessoa* (1ª/2ª/3ª), *número* (singular/plural), *tempo* (presente/pretérito/futuro), *modo* (indicativo/subjuntivo/imperativo), *voz* (ativa/passiva/reflexiva).

Formas nominais: infinitivo (estudar), gerúndio (estudando), particípio (estudado). Verbos auxiliares: ser, estar, ter, haver.

Pontos mais testados: pretérito imperfeito do subjuntivo ("se ele estudasse"), futuro do subjuntivo ("quando ele estudar"), imperativo afirmativo e negativo.

**Pronome**
Pessoais retos (eu, tu, ele/ela, nós, vós, eles/elas) e oblíquos (me, te, se, lhe, nos, vos, os/as).
Possessivos: meu, teu, seu, nosso, vosso.
Demonstrativos: este/esse/aquele (este = perto de quem fala, esse = perto de quem ouve, aquele = longe dos dois).
Relativos: *que* (coisa/pessoa), *quem* (pessoa, com preposição), *cujo* (posse — nunca com artigo depois), *onde* (lugar), *o qual/a qual* (clareza de referência).
Indefinidos: alguém, ninguém, todo, qualquer, cada.
Interrogativos: que?, quem?, qual?, quanto?

**Advérbio**
Modifica verbo, adjetivo ou outro advérbio. Invariável em gênero e número; flexiona em grau (muito rapidamente / mais rapidamente). Classificação: lugar, tempo, modo, intensidade, negação, afirmação, dúvida.

**Preposição**
Relaciona termos da oração. Invariável. Principais: a, ante, até, após, com, contra, de, desde, em, entre, para, per, perante, por, sem, sob, sobre, trás. Contrações: ao (a+o), do (de+o), no (em+o), pelo (por+o).

**Conjunção**
Coordenativas: aditivas (e, nem), adversativas (mas, porém, contudo), alternativas (ou, ora), conclusivas (portanto, logo, pois), explicativas (porque, pois, que).
Subordinativas: causais, concessivas, condicionais, consecutivas, finais, temporais, comparativas, conformativas, proporcionais, integrantes.

## Formação de Palavras

**Derivação**
- Prefixal: in+feliz, des+fazer
- Sufixal: feliz+mente, professor+al
- Parassintética: prefixo+radical+sufixo simultâneos: en+nobrec+er
- Regressiva: verbo → substantivo (cobrar → cobra, ajudar → ajuda)
- Imprópria: mudança de classe (o jantar, o andar)

**Composição**
- Justaposição: elementos justapostos, mantêm sílaba tônica própria (girassol, passatempo)
- Aglutinação: fusão fonética (planalto < plano+alto, aguardente)"""
})

NOVOS.append({
  "id": "r-pt-04", "topico": "pt-04", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Sintaxe", "incidencia": "alta",
  "versaoCurta": """# Sintaxe

## Termos essenciais da oração
- **Sujeito**: de quem se fala — simples, composto, oculto/elíptico, indeterminado, inexistente
- **Predicado**: o que se diz do sujeito — verbal, nominal, verbo-nominal

## Termos integrantes
- **Objeto direto (OD)**: complementa VTD sem preposição ("Ela cantou *a música*")
- **Objeto indireto (OI)**: complementa VTI com preposição ("Ela gostou *da música*")
- **Complemento nominal (CN)**: complementa nome com preposição ("necessidade *de estudo*")
- **Agente da passiva**: "A lei foi aprovada *pelo Congresso*"

## Termos acessórios
- **Adjunto adnominal (AAN)**: modifica substantivo ("*bom* professor", "*meu* livro")
- **Adjunto adverbial (AAV)**: modifica verbo/adjetivo/advérbio ("Estudou *muito*", "*em casa*")
- **Aposto**: explica/especifica um termo ("Lucas, *o professor*, chegou")
- **Vocativo**: chama, independente da oração ("*Professor*, pode repetir?")

## Período composto
- **Coordenadas**: orações independentes — sindéticas (com conjunção) e assindéticas (sem)
- **Subordinadas substantivas**: sujeito, objeto, complemento nominal, predicativa, apositiva
- **Subordinadas adjetivas**: restritivas (sem vírgula) e explicativas (com vírgula)
- **Subordinadas adverbiais**: causais, concessivas, condicionais, consecutivas, finais, temporais

## Armadilhas
- Sujeito ≠ primeiro substantivo da frase; pode estar após o verbo
- "Cujo" é adjunto adnominal do substantivo seguinte
- Oração reduzida = sem conjunção + verbo em forma nominal

## Para a prova
- Sintaxe ≈ 9% das questões de Português
- Cai muito: identificar função sintática de pronome relativo
- "Que" pode ser conjunção integrante (OD) ou pronome relativo (AAN/AAV/sujeito)""",
  "versaoCompleta": """# Sintaxe — Estudo Completo

## Período e Oração

**Período simples**: uma oração (um único verbo ou locução verbal).
**Período composto**: duas ou mais orações. Coordenado (orações independentes) ou subordinado (dependência sintática).

## Termos Essenciais

**Sujeito**
- *Simples*: um único núcleo ("*O professor* chegou")
- *Composto*: dois ou mais núcleos ("*Lucas e Maria* chegaram")
- *Oculto/elíptico*: identificável pela desinência verbal ("*Ø* Chegamos cedo" = nós)
- *Indeterminado*: verbo na 3ª pessoa do plural sem referente, ou verbo + "se" com VTI ("Precisa-se de professores")
- *Inexistente*: verbos impessoais — haver existencial ("Há vagas"), fazer temporal ("Faz dois anos"), ser de tempo ("É tarde")

**Predicado**
- *Verbal*: verbo de ação, núcleo é verbo ("O aluno *estudou*")
- *Nominal*: verbo de ligação + predicativo do sujeito ("A música *é bela*")
- *Verbo-nominal*: dois núcleos — verbo + predicativo ("O aluno *chegou cansado*")

## Termos Integrantes

**Objeto direto**: complemento sem preposição de verbo transitivo direto. Pode ser pronome oblíquo (o, a, os, as, me, te, nos).

**Objeto indireto**: complemento com preposição de verbo transitivo indireto. Pronomes oblíquos: lhe, lhes, me, te, nos.

**Complemento nominal**: complementa substantivo, adjetivo ou advérbio com preposição. Diferença do adjunto adnominal: o CN é obrigatório para completar o sentido ("medo *de altura*" — sem "de altura", a frase fica incompleta).

**Agente da passiva**: termo que pratica a ação em oração na voz passiva, introduzido por "por/pelo/pela".

## Termos Acessórios

**Adjunto adnominal**: qualifica ou determina substantivo. Pode ser: artigo, adjetivo, pronome, numeral, locução adjetiva. Diferença do complemento nominal: AAN indica qualidade (adjunto) vs. CN indica relação necessária (complementa).

**Adjunto adverbial**: modifica verbo, adjetivo ou advérbio. Classificação: lugar, tempo, modo, intensidade, causa, concessão, finalidade, condição, instrumento, companhia, assunto.

**Aposto**: explica, resume ou especifica um substantivo/pronome. Entre vírgulas, parênteses ou após dois-pontos.

**Vocativo**: termo que chama ou interpela. Sempre separado por vírgulas. Não tem relação sintática com o restante da oração.

## Período Composto por Subordinação

**Orações subordinadas substantivas** funcionam como um substantivo (sujeito, OD, OI, predicativo, CN, apositiva). Introduzidas por "que" integrante, "se", pronomes/advérbios interrogativos.

**Orações subordinadas adjetivas**
- *Restritivas* (sem vírgula): restringem o sentido do antecedente — "Os alunos *que estudaram* passaram"
- *Explicativas* (com vírgula): acrescentam informação a um antecedente já definido — "Os alunos, *que estudaram bastante*, passaram"

**Orações subordinadas adverbiais**: exercem função de adjunto adverbial. Classificação: causal, concessiva, condicional, consecutiva, final, temporal, comparativa, conformativa, proporcional."""
})

NOVOS.append({
  "id": "r-pt-05", "topico": "pt-05", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Ortografia", "incidencia": "media",
  "versaoCurta": """# Ortografia

## Reforma Ortográfica de 2009 (Acordo de 1990)
- Eliminado o **trema** (ü) — exceto em nomes estrangeiros e seus derivados
- Eliminado o **acento** nos ditongos abertos **éi** e **ói** em palavras paroxítonas: *ideia, assembleia, jiboia, heroico*
- Eliminado acento diferencial em palavras homógrafas: *para/pára, pelo/pêlo, polo/pólo*
- Mantido: *pôr* (verbo) × *por* (preposição); *pôde* (passado) × *pode* (presente)

## Principais regras de acentuação
- **Oxítonas**: acentuam-se terminadas em a(s), e(s), o(s), em/ens: *café, avó, também*
- **Paroxítonas**: acentuam-se quando NÃO terminam em a(s), e(s), o(s), em/ens: *fácil, hífen, tórax*
- **Proparoxítonas**: TODAS são acentuadas: *música, lógico, público*
- **Hiato**: vogais i e u tônicas após vogal: *saída, país, baú*

## Uso do hífen (resumo)
- Com prefixos: **ante-, anti-, contra-, extra-, infra-, inter-, intra-, semi-, supra-, ultra-** + vogal igual ou h: *anti-inflamatório, semi-interno*
- **Sem hífen**: antes de consoante diferente ou vogal diferente: *antevejo, extraoficial*
- Exceção: prefixos **sub-, sob-, ob-** antes de b: *sub-base*

## Erros frequentes
- *Mas* (adversativo) × *mais* (adição/intensidade)
- *Porque* (explicação) × *por que* (interrogativo) × *por quê* (final de frase) × *porquê* (substantivo)
- *Há* (verbo haver — tempo passado) × *a* (preposição — distância/futuro)
- *Mau* (adjetivo) × *mal* (advérbio/substantivo)

## Para a prova
- Questões focam no pós-2009: ditongos abertos, trema e hifenação
- Decorar: *ideia, assembleia, jiboia, heroico* sem acento
- Decorar: *pôr* e *pôde* continuam com acento""",
  "versaoCompleta": """# Ortografia — Estudo Completo

## Acordo Ortográfico de 1990 (em vigor desde 2009 no Brasil)

O Acordo Ortográfico unificou a escrita nos países lusófonos. As principais mudanças foram:

**Fim do trema**: o ü deixou de ser usado em palavras portuguesas. Exceção: nomes próprios estrangeiros e seus derivados diretos (Müller, mülleriano).

**Fim do acento em ditongos abertos paroxítonos**: as sequências éi e ói em paroxítonas perderam o acento. Exemplos: *ideia, assembleia, plateia, epopeia, jiboia, heroico, paranoico*. Mas mantém-se em oxítonas: *anéis, papéis, herói, anzóis*.

**Fim do acento diferencial**: palavras antes diferenciadas por acento agora são escritas igualmente. Exemplos: *para/para, pelo/pelo, polo/polo, pelo/pelo*. Exceções mantidas: *pôr* (verbo) × *por* (preposição), *pôde* (pretérito perfeito) × *pode* (presente).

## Regras de Acentuação Gráfica

**Oxítonas** (última sílaba tônica): acentuam-se terminadas em: a(s), e(s), o(s), em, ens. Ex.: *café, avó, também, parabéns*.

**Paroxítonas** (penúltima sílaba tônica): acentuam-se quando terminam em qualquer coisa diferente de a(s), e(s), o(s), em/ens. Terminações acentuadas: l, r, n, x, ps, ã(s), ão(s), um/uns, i(s), us, ditongo. Ex.: *fácil, tórax, hífen, bênção, táxi, vírus, água*.

**Proparoxítonas** (antepenúltima tônica): todas recebem acento. Ex.: *música, público, lógico, ótimo, câmera*.

**Ditongos crescentes em hiatos**: vogais i e u tônicas que formam hiato recebem acento se estiverem sozinhas na sílaba ou seguidas de s. Ex.: *saída, país, baú, Luís*. Não acentua quando seguida de nh: *rainha, moinho*.

## Uso do Hífen com Prefixos

Principais prefixos e regras:

Com hífen quando o segundo elemento começa com a mesma vogal do prefixo ou com h: *anti-inflamatório, semi-interno, sobre-humano, contra-ataque*.

Sem hífen nos demais casos: *antevejo, antissocial (não mesma vogal), extraoficial, semiaberto*.

Prefixos que sempre usam hífen independente: *ex-* (ex-presidente), *vice-* (vice-diretor), *pré-* (pré-escola — ainda aceito com acento e hífen).

## Palavras Frequentemente Confundidas

| Forma | Uso |
|---|---|
| *mas* | conjunção adversativa (= porém) |
| *mais* | adição ou intensidade |
| *mau/maus* | adjetivo (= ruim) |
| *mal/males* | advérbio ou substantivo |
| *há* | verbo haver (tempo decorrido: *há dois anos*) |
| *a* | preposição (distância ou tempo futuro: *daqui a dois anos*) |
| *onde* | lugar determinado com verbo de estado |
| *aonde* | lugar com verbos de movimento (*Aonde você vai?*) |
| *porque* | explicação/causa (= pois) |
| *por que* | interrogação direta/indireta |
| *porquê* | substantivo (*o porquê do problema*) |
| *por quê* | interrogação no final da frase |"""
})

NOVOS.append({
  "id": "r-pt-06", "topico": "pt-06", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Coesão e coerência / conectores", "incidencia": "media",
  "versaoCurta": """# Coesão e Coerência

## Coerência (nível semântico)
- Relaciona-se ao **sentido global** do texto
- Texto coerente: informações não se contradizem, há unidade temática
- Depende de: conhecimento de mundo, contexto, intenção comunicativa

## Coesão (nível formal)
Mecanismos linguísticos que conectam as partes do texto:

### Coesão referencial
- **Anáfora**: retoma algo já dito ("O professor chegou. *Ele* sorriu.")
- **Catáfora**: antecipa algo que virá ("*Isso* é fundamental: estudar todos os dias.")
- **Substituição lexical**: sinônimo, hiperônimo, expressão nominal
- **Elipse**: omissão recuperável pelo contexto

### Coesão sequencial (conectores)
- **Aditiva**: e, também, além disso, ademais, ainda, bem como
- **Adversativa**: mas, porém, contudo, entretanto, todavia, no entanto, apesar disso
- **Conclusiva**: portanto, logo, assim, então, por isso, dessa forma
- **Explicativa**: porque, pois, já que, visto que, uma vez que
- **Concessiva**: embora, ainda que, mesmo que, apesar de, conquanto
- **Temporal**: quando, enquanto, depois que, antes que, logo que
- **Condicional**: se, caso, desde que, contanto que

## Problemas de coesão/coerência
- **Ambiguidade**: pronome com referente incerto
- **Contradição**: informações que se excluem
- **Quebra de isotopia**: mudança de assunto sem justificativa
- **Excesso de repetição**: prejudica fluência (falta de variação lexical)

## Para a prova
- Questões pedem: identificar o conector correto para relacionar duas ideias
- Ou: identificar o problema de coesão em um trecho
- Dica: a relação lógica entre as orações determina o conector — nunca o contrário""",
  "versaoCompleta": """# Coesão e Coerência — Estudo Completo

## Distinção fundamental

**Coerência** é a propriedade do texto no nível do sentido: as ideias se articulam de forma lógica e não contraditória, formando um todo compreensível. Um texto pode ser gramaticalmente correto mas incoerente.

**Coesão** é a propriedade textual no nível da forma linguística: os recursos que conectam explicitamente os elementos do texto — pronomes, conectivos, sinônimos, elipses.

## Mecanismos de Coesão

### Coesão referencial

**Referência pessoal**: uso de pronomes pessoais e possessivos para retomar ou antecipar participantes do texto.

**Referência demonstrativa**: uso de pronomes demonstrativos (*este, esse, aquele, isso, aquilo*) para retomar ou antecipar segmentos textuais.

**Referência comparativa**: establece identidade ou semelhança (*o mesmo, igual, semelhante, assim*).

**Substituição lexical**: troca de um item lexical por sinônimo, hipônimo, hiperônimo ou expressão nominal equivalente — fundamental para evitar repetição e criar progressão temática.

**Elipse**: omissão de um elemento recuperável pelo contexto. Pode ser nominal (*Comprei o livro e Ø li rapidamente* = o livro) ou verbal (*Ele estuda todos os dias; eu, Ø raramente*).

### Coesão sequencial

**Conectores aditivos**: somam informações — *e, também, além disso, ademais, ainda, bem como, não só...mas também*.

**Conectores adversativos**: opõem informações — *mas, porém, contudo, entretanto, todavia, no entanto, ao passo que*. Indicam contraste; a segunda informação é mais relevante.

**Conectores conclusivos**: introduzem conclusão decorrente de premissas anteriores — *portanto, logo, assim, então, por isso, consequentemente, dessa forma, destarte*.

**Conectores explicativos e causais**: introduzem justificativa ou causa — *porque, pois, já que, visto que, uma vez que, dado que, porquanto*.

**Conectores concessivos**: introduzem ressalva ou oposição parcial — *embora, ainda que, mesmo que, apesar de, conquanto, por mais que*. A concessiva admite a hipótese mas não muda a conclusão.

**Conectores temporais**: *quando, enquanto, depois que, antes que, logo que, assim que, desde que* (valor temporal), *sempre que, cada vez que*.

**Conectores condicionais**: *se, caso, desde que* (valor condicional), *contanto que, a menos que, a não ser que*.

## Progressão Temática

Um texto coeso progride de maneira organizada. Os principais padrões são:

- **Progressão linear**: o rema (informação nova) de uma oração torna-se o tema (ponto de partida) da próxima.
- **Progressão com tema constante**: o mesmo tema é retomado com remas diferentes.
- **Progressão com hipertema**: um macrotema desdobra-se em subtemas.

## Erros de Coesão e Coerência

**Ambiguidade referencial**: pronome que pode remeter a dois antecedentes diferentes.
**Contradição**: afirma e nega o mesmo conteúdo.
**Repetição excessiva**: mesmo vocábulo sem necessidade estilística.
**Quebra de registro**: mistura de linguagem formal e informal sem razão.
**Conectivo inadequado**: usar adversativo onde a relação é conclusiva, por exemplo."""
})

NOVOS.append({
  "id": "r-pt-07", "topico": "pt-07", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Pontuação", "incidencia": "media",
  "versaoCurta": """# Pontuação

## Vírgula — usos obrigatórios
- Isolar **aposto** e **vocativo**: "Lucas, *o professor*, chegou." / "*Alunos*, prestem atenção."
- Isolar **adjunto adverbial deslocado** (antes do verbo): "*Naquele dia*, todos estudaram."
- Isolar **orações intercaladas**: "O aluno, *que havia faltado*, foi reprovado." (explicativa)
- Separar termos de **enumeração**: "Trouxe lápis, borracha, caderno e caneta."
- Antes de **conjunções adversativas**: "Estudou muito, *mas* não passou."
- Antes de **conjunções conclusivas**: "Estudou, *portanto* passou." ← errado: vírgula antes de "portanto" é opcional mas depois é errada: "Estudou, portanto, passou." ← duas vírgulas: correto

## Vírgula — uso proibido
- Entre **sujeito e predicado**: ~~"O aluno, estudou."~~
- Entre **verbo e objeto**: ~~"Ele comprou, o livro."~~
- Entre **nome e adjunto adnominal** restritivo: ~~"O aluno, dedicado, passou."~~ ← se restritivo, sem vírgula

## Dois-pontos
- Enumerar: "Trouxe tudo: lápis, borracha e caderno."
- Explicar/exemplificar o que foi dito antes
- Antes de discurso direto: "Ele disse: 'Vou estudar.'"

## Ponto e vírgula
- Separar orações longas já com vírgulas internas
- Separar itens de lista

## Para a prova
- A vírgula é o sinal mais cobrado
- Frase mais testada: posição do adjunto adverbial deslocado
- "Todavia, portanto, entretanto" → vírgula antes E depois quando no meio da oração
- Oração adjetiva restritiva: SEM vírgula; explicativa: COM vírgula""",
  "versaoCompleta": """# Pontuação — Estudo Completo

## A Vírgula

A vírgula é o sinal de pontuação mais cobrado em provas de concurso. Seu uso obedece a regras sintáticas precisas.

**Usos obrigatórios:**

1. *Aposto explicativo*: "A música, arte do tempo, é universal."
2. *Vocativo*: "Professor, pode repetir?" / "Atenção, alunos."
3. *Adjunto adverbial deslocado*: quando o adjunto adverbial aparece antes do verbo ou entre sujeito e predicado, isola-se com vírgula. "Ontem, o professor chegou tarde." / "O professor, ontem, chegou tarde."
4. *Oração adjetiva explicativa*: acrescenta informação a um antecedente já definido — sempre entre vírgulas. "Os alunos, que haviam estudado muito, passaram."
5. *Enumeração*: separa termos coordenados sem conjunção. "Estudou gramática, interpretação, redação."
6. *Conjunções adversativas e conclusivas intercaladas*: "Estudou muito; todavia, não foi suficiente." — a conjunção intercalada recebe vírgula antes e depois.

**Usos proibidos (erros comuns):**

- Entre sujeito e predicado: ~~"O professor de música, chegou tarde."~~
- Entre verbo transitivo e seu objeto: ~~"Ela cantou, a música linda."~~
- Entre nome e oração adjetiva restritiva: "Os alunos *que estudaram* passaram" (sem vírgula — a restrição é necessária para definir quais alunos).

## Ponto e Vírgula

Separa partes de um período composto quando as orações já têm vírgulas internas:
"Estudei gramática, interpretação e redação; meu colega revisou ortografia, pontuação e sintaxe."

Separa itens de enumerações longas ou estruturadas:
"Os candidatos devem trazer: identidade com foto; comprovante de inscrição; caneta esferográfica preta."

## Dois-Pontos

Introduz enumeração: "São três os pilares: dedicação, disciplina e consistência."
Introduz explicação ou desenvolvimento: "A resposta é simples: quem estuda, passa."
Introduz discurso direto: O professor anunciou: "A prova será na próxima semana."

## Travessão

Isola aposto ou comentário parentético com mais ênfase que a vírgula:
"A BNCC — documento norteador do currículo — define competências gerais."
Introduz falas no discurso direto em narrativas.

## Parênteses

Isola explicação ou dado acessório de menor importância sintática:
"A Lei 9.394 (LDB) foi promulgada em 1996."

## Ponto de Exclamação e Interrogação

O ponto de exclamação aparece após vocativo isolado, interjeição ou frase exclamativa.
O ponto de interrogação aparece apenas em perguntas diretas — não em indiretas ("Perguntei *se ele viria*".)"""
})

NOVOS.append({
  "id": "r-pt-08", "topico": "pt-08", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Concordância verbal e nominal", "incidencia": "media",
  "versaoCurta": """# Concordância Verbal e Nominal

## Concordância nominal — regra geral
Adjetivo/artigo/numeral/pronome concordam em **gênero e número** com o substantivo.
- "Boas *aulas* musicais" ← todos femininos/plurais

## Casos especiais de concordância nominal
- Adjetivo após vários substantivos: concorda com o mais próximo ou vai para o plural masculino
- "Roupa e sapato *comprados*" (plural masc.) ou "Roupa e sapato *comprado*" (mais próximo)
- Predicativo do sujeito: concorda com o sujeito — "As professoras ficaram *satisfeitas*"
- Pronome "mesmo/próprio": concorda com o referente
- "Anexo/incluso": adjetivo — concorda ("*Anexas* as fotos")
- "Em anexo": locução — invariável ("Sigo *em anexo* as fotos")

## Concordância verbal — regra geral
Verbo concorda em **pessoa e número** com o sujeito.

## Casos especiais de concordância verbal
- **Sujeito composto antes do verbo** → verbo no plural
- **Sujeito composto após o verbo** → pode concordar com o mais próximo ou com o total
- **Pronome relativo "que"** → verbo concorda com o antecedente ("Fui eu *que fiz*" ou "Fui eu *que fiz*")
- **"Um dos que"** → verbo no plural: "Ela é uma das que *mais estudam*"
- **Expressões partitivas** ("a maioria de", "parte de") → singular ou plural (ambos aceitos)
- **Sujeito coletivo** → verbo no singular: "A turma *chegou*"
- **Verbos impessoais** → sempre na 3ª pessoa do singular: "Houve *vagas*" / "Faz dois anos"

## Para a prova
- Verbo HAVER existencial (= existir): impessoal → "Há muitos candidatos" (não "Hão")
- Verbo SER: pode concordar com o predicativo — "Tudo são flores" (aceito)
- "Mais de um" → verbo no singular: "Mais de um aluno *faltou*"
- "Nem um nem outro" → verbo no singular ou plural (ambos aceitos)""",
  "versaoCompleta": """# Concordância Verbal e Nominal — Estudo Completo

## Concordância Nominal

**Regra geral**: adjetivos, artigos, pronomes e numerais concordam em gênero e número com o substantivo a que se referem.

**Adjetivo predicativo**: quando o adjetivo é predicativo do sujeito ou do objeto, concorda com esse termo.
- "As professoras ficaram *satisfeitas*." (predicativo do sujeito)
- "Consideraram as propostas *inadequadas*." (predicativo do objeto)

**Adjetivo posposto a vários substantivos**: com gêneros diferentes, vai para o masculino plural. Com gêneros iguais, concorda com o substantivo mais próximo (facultativo concordar com todos).
- "Comprou roupa e sapato novo**s**" ou "Comprou roupa e sapato nova" (mais próximo feminino — pouco usado)

**Palavras de concordância especial:**
- *Obrigado/obrigada*: adjetivo — concorda com quem fala
- *Mesmo/próprio*: concorda com o referente
- *Quite*: adjetivo — concorda ("Estamos *quites*")
- *Anexo/incluso/junto*: adjetivos — concordam ("*Anexas* estão as fotos")
- *Em anexo, em junto*: locuções adverbiais — invariáveis
- *Menos, alerta, bastante* (= muito): invariáveis
- *Bastante* (= suficiente): variável ("Temos respostas *bastantes*")

## Concordância Verbal

**Regra geral**: o verbo concorda em número e pessoa com o sujeito.

**Sujeito composto:**
- Antes do verbo → plural: "O professor e os alunos *chegaram*."
- Após o verbo → plural ou concordância com o mais próximo: "Chegaram o professor e os alunos" ou "Chegou o professor e os alunos."
- Sujeito composto de pessoas diferentes: a 1ª pessoa prevalece sobre a 2ª e 3ª; a 2ª sobre a 3ª.

**Expressões partitivas e coletivas:**
- "A maioria dos alunos *foi* aprovada" (concorda com o coletivo) ou "A maioria dos alunos *foram* aprovados" (concorda com o complemento — ambos aceitos).
- Coletivo sem complemento → singular obrigatório: "A turma *viajou*."
- Coletivo com complemento especificador → plural facultativo: "Uma multidão de pessoas *gritou/gritaram*."

**Verbos impessoais (sempre 3ª singular):**
- *Haver* existencial (= existir): "Há vagas." / "Havia candidatos." → NUNCA "hão", "haviam"
- *Fazer* e *ir* de tempo: "Faz dois anos." / "Vai fazer uma semana."
- Fenômenos naturais: "Choveu muito."

**"Ser"**: pode concordar com o predicativo em certos contextos.
- "Tudo são flores." / "O problema são as faltas." (o verbo concorda com o predicativo nominal)

**Pronome relativo "que"**: o verbo concorda com o antecedente do relativo.
- "Fui eu que *fiz* o trabalho." (sujeito = eu → 1ª pessoa singular)
- "Foi você que *fez* o trabalho." (sujeito = você → 3ª pessoa singular)"""
})

NOVOS.append({
  "id": "r-pt-09", "topico": "pt-09", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Semântica", "incidencia": "media",
  "versaoCurta": """# Semântica

## Relações semânticas

### Sinonímia e antonímia
- **Sinônimos**: mesmo sentido ou sentido aproximado — *belo/bonito/formoso*
- **Antônimos**: sentidos opostos — *claro/escuro, sempre/nunca*

### Hiperonímia e hiponímia
- **Hiperônimo**: termo mais geral ("instrumento" é hiperônimo de "violão")
- **Hipônimo**: termo mais específico ("violão" é hipônimo de "instrumento")

### Polissemia e homonímia
- **Polissemia**: uma palavra com vários sentidos relacionados (*banco*: assento/instituição financeira)
- **Homonímia**: palavras iguais na forma mas sem relação semântica
  - Homófonas: mesmo som, grafia diferente (*concerto/conserto*)
  - Homógrafas: mesma grafia, som diferente (*colher-verbo/colher-substantivo*)
  - Homônimas perfeitas: mesma grafia e som

### Paronímia
- Palavras parecidas na forma mas com sentidos diferentes
- *Eminente* (notável) × *iminente* (prestes a acontecer)
- *Descriminar* (inocentar) × *discriminar* (distinguir/segregar)
- *Tráfego* (trânsito) × *tráfico* (comércio ilícito)
- *Comprimento* (extensão) × *cumprimento* (saudação/realização)

## Denotação e conotação
- **Denotação**: sentido literal, dicionarizado
- **Conotação**: sentido figurado, contextual, subjetivo

## Figuras de linguagem (mais cobradas)
- **Metáfora**: comparação implícita — "Sua voz é música"
- **Metonímia**: substituição por relação de contiguidade — "Leu *Machado de Assis*" (= obras de)
- **Ironia**: dizer o contrário do que se pensa
- **Eufemismo**: suavizar algo desagradável — "passou para melhor"
- **Hipérbole**: exagero expressivo — "Esperou uma eternidade"
- **Antítese**: oposição de ideias — "O amor e o ódio coexistem"

## Para a prova
- Paronímia: decorar os pares mais comuns (eminente/iminente, descriminar/discriminar)
- Figuras: identificar pelo efeito de sentido, não pelo nome
- Polissemia em questões de interpretação: o sentido é sempre o contextual""",
  "versaoCompleta": """# Semântica — Estudo Completo

## Relações entre Palavras

### Sinonímia
Relação entre palavras com significado igual ou muito próximo. A sinonímia perfeita é rara — na prática, sinônimos têm nuances de uso (registro, conotação, frequência).
- *Morrer / falecer / perecer / finar-se* — mesmo sentido, registros diferentes

### Antonímia
Relação de oposição de sentido. Tipos:
- *Complementares*: a negação de um implica o outro (*vivo/morto* — não há meio-termo)
- *Gradativos*: admitem gradação (*quente/morno/frio*)
- *Recíprocos*: pressupõem relação mútua (*comprar/vender, professor/aluno*)

### Hiperonímia e Hiponímia
Relação hierárquica de inclusão semântica. O hiperônimo (termo genérico) inclui os hipônimos (termos específicos). Exemplo: *instrumento musical* (hiperônimo) → *violão, piano, flauta* (hipônimos).

Essa relação é fundamental para coesão textual: a substituição de um hipônimo por seu hiperônimo (ou vice-versa) é recurso de variação lexical muito cobrado.

### Polissemia vs. Homonímia
**Polissemia**: uma mesma palavra tem múltiplos sentidos que derivam historicamente de uma origem comum. Ex.: *cabo* (extremidade geográfica, patente militar, objeto para segurar). Os sentidos têm relação entre si.

**Homonímia**: palavras com mesma forma mas origem e significado independentes.
- *Homófonas*: mesmo som, escrita diferente — *acender (ligar) / ascender (subir)*, *concerto (musical) / conserto (reparo)*
- *Homógrafas*: mesma escrita, pronúncia diferente — *colher* (sílaba tônica muda conforme a função)
- *Homônimas perfeitas*: mesma escrita e pronúncia — *são* (verbo ser / adjetivo sadio / santo)

### Paronímia
Palavras semelhantes na forma mas distintas no sentido:
- *Eminente* (ilustre, notável) × *iminente* (que está prestes a ocorrer)
- *Descriminar* (inocentar de crime) × *discriminar* (diferenciar; segregar)
- *Infligir* (impor pena) × *infringir* (transgredir)
- *Comprimento* (medida de extensão) × *cumprimento* (saudação; realização)
- *Mandato* (prazo de exercício de cargo) × *mandado* (ordem judicial)

## Denotação e Conotação

**Denotação**: sentido objetivo, literal, dicionarizado. Base da linguagem científica e técnica.

**Conotação**: sentido figurado, dependente do contexto, carregado de subjetividade. Base da linguagem literária e publicitária.

Exemplo: *Leão* — denotação: animal felino; conotação: pessoa corajosa, pessoa nascida em Agosto.

## Figuras de Linguagem

**Figuras de pensamento** (afetam o conteúdo):
- *Ironia*: dizer o contrário do que se pensa — "Que pontualidade! Chegou apenas duas horas atrasado."
- *Eufemismo*: suavizar o desagradável — "Passou desta para melhor."
- *Antítese*: oposição de ideias — "O amor nasceu e morreu na mesma tarde."
- *Paradoxo*: contradição aparente com sentido profundo — "Amor é fogo que arde sem se ver."
- *Hipérbole*: exagero — "Repeti mil vezes a mesma explicação."

**Figuras de linguagem** (afetam a forma de expressar):
- *Metáfora*: comparação implícita — "Sua voz é puro mel."
- *Comparação/símile*: comparação explícita com "como" — "Canta como um anjo."
- *Metonímia*: substituição por relação real de contiguidade — "Li *Guimarães Rosa*" (= obras do autor); "Bebeu um *copo*" (= o conteúdo do copo).
- *Sinédoque*: parte pelo todo ou todo pela parte — "O *Brasil* ganhou" (= a seleção brasileira)."""
})

NOVOS.append({
  "id": "r-pt-10", "topico": "pt-10", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Regência verbal e nominal", "incidencia": "media",
  "versaoCurta": """# Regência Verbal e Nominal

## Regência verbal — verbos mais cobrados
| Verbo | Regência | Exemplo |
|---|---|---|
| **Assistir** (ver) | a | Assistiu *ao* filme |
| **Aspirar** (almejar) | a | Aspira *ao* cargo |
| **Visar** (ter como meta) | a | Visa *ao* lucro |
| **Obedecer/desobedecer** | a | Obedece *às* regras |
| **Implicar** (acarretar) | sem prep. | Implica mudança |
| **Preferir** | a | Prefere música *a* silêncio |
| **Ir / chegar** | a | Foi *ao* mercado / Chegou *ao* destino |
| **Namorar** (coloq.) | sem prep. | Namora Maria |
| **Simpatizar/antipatizar** | com | Simpatiza *com* o projeto |
| **Informar/comunicar** | de/sobre | Informou-o *do* ocorrido |

## Verbos com sentido duplo
- **Assistir**: OD = ajudar ("Assistiu o ferido"); OI com *a* = ver ("Assistiu ao filme")
- **Aspirar**: OD = inalar ("Aspirou o pó"); OI com *a* = desejar ("Aspira ao cargo")

## Crase — resumo
- Só ocorre com palavras femininas que aceitam artigo *a*
- **Obrigatória**: antes de substantivos femininos que exigem *a*: "Fui *à* escola"
- **Proibida**: antes de masculinos, pronomes, verbos, palavras indefinidas
- Teste: substituir por "ao" (masc.) — se cabe, há crase no feminino

## Regência nominal — mais cobrados
- **Acessível, necessário, agradável** → a: "*acessível às* pessoas"
- **Ansioso, curioso** → por: "*ansioso pelo* resultado"
- **Capaz, digno, passível** → de: "*capaz de* resolver"
- **Favorável, contrário** → a: "*favorável à* proposta"

## Para a prova
- Decorar: assistir/aspirar/visar + "a" quando significam ver/almejar/ter como meta
- Crase antes de horas: sempre — "às 8 horas", "às 14h"
- Crase antes de "a senhora" → "à senhora"; antes de "você" → sem crase""",
  "versaoCompleta": """# Regência Verbal e Nominal — Estudo Completo

## Regência Verbal

A regência verbal define qual preposição (ou ausência dela) o verbo exige para introduzir seu complemento.

**Verbos que mais caem em prova:**

*Assistir*
- Transitivo indireto (= ver, presenciar): exige preposição *a* — "Assistiu *ao* jogo."
- Transitivo direto (= ajudar, socorrer): sem preposição — "O médico assistiu os feridos."

*Aspirar*
- Transitivo indireto (= almejar, desejar): exige *a* — "Aspira *ao* cargo de diretor."
- Transitivo direto (= inalar): sem preposição — "Aspirou o perfume da flor."

*Visar*
- Transitivo indireto (= ter como objetivo/meta): exige *a* — "O projeto visa *ao* desenvolvimento."
- Transitivo direto (= mirar, dar visto): sem preposição — "Visou o alvo."

*Preferir*: transitivo direto e indireto — "Prefere música *a* silêncio." (*a* = do que — nunca "do que" ou "mais do que" com "preferir").

*Implicar* (= acarretar, resultar em): transitivo direto — "A reforma implica mudanças."
*Implicar* (= irritar): transitivo direto; *implicar com* (= ter implicância): transitivo indireto.

*Obedecer / desobedecer*: transitivos indiretos — "Obedece *às* normas." NUNCA "obedecer as normas" (sem a preposição).

*Ir / vir / chegar*: regem *a* (não *em*) na norma culta escrita — "Fui *ao* banco." (porém o uso com *em* é aceito na fala e em textos informais).

*Simpatizar/antipatizar*: regem *com* — "Simpatizou *com* a ideia."

## A Crase

A crase é a fusão da preposição *a* com o artigo *a* (→ à) ou com pronomes demonstrativos *a/aquele/aquela* (→ àquele/àquela).

**Condições para a crase:**
1. O termo anterior exige preposição *a*
2. O termo seguinte aceita artigo *a*
3. Ambas as condições ocorrem simultaneamente

**Usos obrigatórios:**
- Antes de substantivos femininos precedidos de artigo: "Fui *à* escola."
- Antes de horas: "Às 8h da manhã."
- Expressões adverbiais femininas: "à tarde, à noite, às vezes, à toa, à vontade"
- Antes de "a(s) + substantivo feminino" em locuções prepositivas: "em relação *à* música"

**Usos proibidos:**
- Antes de substantivos masculinos: "Fui *a* pé." (não *à*)
- Antes de verbos: "Começo *a* estudar." (não *à*)
- Antes de pronomes: "Entreguei *a* ela." (não *à ela*)
- Antes de artigo indefinido: "Refiro-me *a uma* proposta." (não *à uma*)
- Antes de pronome demonstrativo *esta/essa*: "Prefiro *esta* proposta *a essa*."

**Usos facultativos:**
- Antes de pronomes possessivos femininos: "Refiro-me *à/a* sua proposta."
- Antes de nomes próprios femininos sem artigo: "Escrevi *a/à* Maria."

## Regência Nominal

Substantivos, adjetivos e advérbios também podem exigir complementos com preposição específica:

- *Medo de*, *dúvida sobre/acerca de*, *necessidade de*
- *Acessível a*, *benéfico a*, *prejudicial a*, *favorável a*, *contrário a*
- *Ansioso por*, *curioso por*, *ávido por*
- *Capaz de*, *digno de*, *passível de*, *hábil em*
- *Paralelo a*, *similar a*, *diferente de*"""
})

NOVOS.append({
  "id": "r-pt-11", "topico": "pt-11", "disciplina": "portugues",
  "bloco": "basicos", "nome": "Tipologia e gênero textual", "incidencia": "baixa",
  "versaoCurta": """# Tipologia e Gênero Textual

## Tipos textuais (formas de organização)
| Tipo | Características | Estrutura |
|---|---|---|
| **Narração** | Fatos em sequência temporal | Apresentação → conflito → clímax → desfecho |
| **Descrição** | Retrato de pessoas, lugares, objetos | Enumeração de características |
| **Dissertação** | Exposição/defesa de ideia | Tese → argumentos → conclusão |
| **Argumentação** | Convencer o leitor | Tese → argumentos → contra-argumentos → conclusão |
| **Injunção** | Instruir, orientar | Sequência de ações, imperativo |

## Gêneros textuais (realizações concretas)
- Os tipos são abstratos; os gêneros são concretos e circulam socialmente
- Cada gênero tem: estrutura composicional, estilo e conteúdo temático (Bakhtin)

### Exemplos por esfera social
- **Jornalística**: notícia, reportagem, editorial, crônica, artigo de opinião
- **Literária**: conto, romance, poema, crônica literária
- **Científica**: artigo, monografia, resenha, resumo
- **Publicitária**: anúncio, slogan, folder
- **Oficial**: ofício, memorando, ata, edital, portaria
- **Digital**: e-mail, blog, tweet, post

## Gêneros da Redação Oficial
- **Ofício**: comunicação externa entre órgãos ou para particulares
- **Memorando**: comunicação interna, mesmo órgão
- **Ata**: registro de reunião
- **Parecer**: opinião técnica fundamentada
- **Portaria**: ato normativo de autoridade administrativa

## Para a prova
- Questões pedem: identificar o tipo/gênero de um texto apresentado
- Dissertação ≠ narração: ausência de enredo e personagens; presença de tese e argumentos
- Crônica = híbrido: pode ser narrativa, argumentativa ou descritiva""",
  "versaoCompleta": """# Tipologia e Gênero Textual — Estudo Completo

## Tipos Textuais

Os tipos textuais são estruturas composicionais abstratas que organizam o discurso. Não são exclusivos — um texto real frequentemente combina vários tipos.

**Narração**: relata eventos em sequência (cronológica ou não). Elementos: narrador, personagens, tempo, espaço, enredo (complicação-clímax-desfecho). Usa verbos de ação no passado predominantemente.

**Descrição**: caracteriza seres, objetos, ambientes, sentimentos. Usa verbos de estado (ser, estar, parecer) e adjetivos. Pode ser estática (foto) ou dinâmica (retrato em movimento).

**Exposição/dissertação expositiva**: apresenta, explica ou analisa um tema sem necessariamente tomar partido. Estrutura: introdução (apresentação do tema) → desenvolvimento (explicação) → conclusão (síntese).

**Argumentação**: defende um ponto de vista, tenta persuadir. Estrutura: tese → argumentos → contra-argumentos (refutação) → conclusão (reafirmação da tese). Muito presente no texto dissertativo-argumentativo da redação oficial e do ENEM.

**Injunção**: instrui, orienta, prescreve ações. Verbos no imperativo ou infinitivo. Exemplos: receita, manual, regulamento, bula.

## Gêneros Textuais

O conceito de gênero vem de Mikhail Bakhtin: gêneros são formas relativamente estáveis de enunciados, determinadas pela esfera de atividade humana. Todo gênero tem três dimensões: *conteúdo temático* (o que se pode dizer), *estilo* (escolhas linguísticas) e *construção composicional* (estrutura).

Os gêneros se renovam histórica e socialmente — novos gêneros emergem (meme, podcast, tweet) enquanto outros se tornam obsoletos.

**Distinção tipo vs. gênero**: "narração" é um tipo; "conto de fadas", "notícia policial" e "relato pessoal" são gêneros que usam a narração.

## Intertextualidade e Interdiscursividade

**Intertextualidade explícita**: citação, referência, epígrafe — o texto fonte é identificado.
**Intertextualidade implícita**: alusão, paródia, pastiche — o texto fonte não é citado mas reconhecível.
**Paródia**: recria um texto para subverter seu sentido original.
**Pastiche**: imita o estilo de outro autor ou gênero sem intenção de crítica."""
})

# ── Redação Oficial ──────────────────────────────────────────

NOVOS.append({
  "id": "r-ro-01", "topico": "ro-01", "disciplina": "redacao-oficial",
  "bloco": "basicos", "nome": "Manual de Redação da Presidência da República", "incidencia": "media",
  "versaoCurta": """# Manual de Redação da Presidência da República

## O que é
- Documento normativo que padroniza a comunicação oficial no Poder Executivo Federal
- 3ª edição revisada e atualizada (2018) — é a versão cobrada em provas
- Aplicável a todos os órgãos do Poder Executivo; referência para demais poderes

## Princípios da redação oficial
1. **Clareza**: facilitar a compreensão imediata
2. **Precisão**: usar termos técnicos corretos; evitar ambiguidade
3. **Concisão**: dizer o necessário sem excessos
4. **Impessoalidade**: o comunicador é o órgão, não o servidor
5. **Formalidade e uniformidade**: padrão linguístico formal; estrutura padronizada
6. **Uso da norma culta**: ortografia, gramática e pontuação corretas

## Impessoalidade
- Evitar 1ª pessoa do singular ("*Eu* determino" → "Determina-se")
- O documento expressa a posição do órgão, não do servidor
- Exceção: exposição de motivos, que pode usar 1ª pessoa

## Estrutura dos documentos
- **Cabeçalho**: brasão, nome do órgão
- **Identificação do expediente**: tipo, número, data, origem
- **Endereçamento**: destinatário
- **Assunto**: linha de referência
- **Texto**: introdução, desenvolvimento, conclusão
- **Fecho**: "Respeitosamente" (inferior para superior) / "Atenciosamente" (mesmo nível ou superior para inferior)
- **Assinatura**: nome e cargo

## Para a prova
- O "vocativo" nas comunicações oficiais: "Senhor Presidente" (com vírgula)
- Fecho simplificado: apenas 2 expressões — Respeitosamente e Atenciosamente
- Documentos oficiais NÃO usam "Ilustríssimo" ou "Excelentíssimo" (exceto para Presidente, Vice, chefes do Congresso e do STF)""",
  "versaoCompleta": """# Manual de Redação da Presidência da República — Estudo Completo

## Contexto e Importância

O Manual de Redação da Presidência da República (3ª edição, 2018) é o documento normativo que padroniza a comunicação oficial no âmbito do Poder Executivo Federal. Serve de referência para concursos públicos de todo o Brasil, sendo cobrado nas provas da Quadrix para a SEDF.

O manual unificou os padrões que antes variavam entre órgãos, criando um sistema coerente de documentos e procedimentos.

## Princípios da Redação Oficial

**Clareza**: o texto deve ser facilmente compreendido na primeira leitura. Evite construções rebuscadas, ambiguidades e palavras desnecessárias. A clareza favorece a eficiência administrativa.

**Precisão**: cada termo deve ser empregado no seu sentido exato. Prefira o termo técnico correto ao sinônimo popular. Evite expressões vagas ("o mais breve possível" → especifique o prazo).

**Concisão**: o texto deve conter apenas o que é necessário. Evite redundâncias ("subir para cima", "reiterar novamente"), pleonasmos e frases de preenchimento.

**Impessoalidade**: a comunicação oficial representa o órgão, não o servidor. Evite a 1ª pessoa do singular; use construções passivas ou impessoais. Exceção: mensagens presidenciais e exposições de motivos podem usar a 1ª pessoa.

**Formalidade e padronização**: uso da norma culta; estrutura padronizada dos documentos; tratamento uniforme aos destinatários.

## Formas de Tratamento

**"Vossa Excelência" (V. Exa.)**: Presidente e Vice-Presidente da República, Ministros de Estado, Governadores, Senadores, Deputados, Magistrados, etc.

**"Vossa Senhoria" (V. Sa.)**: demais autoridades e particulares.

O tratamento "Ilustríssimo Senhor" e "Digníssimo" foram abolidos pela 3ª edição — são considerados excessivamente cerimoniosos.

## Fecho

A 3ª edição simplificou para apenas dois fechos:
- **"Respeitosamente"**: autoridade de hierarquia inferior para superior
- **"Atenciosamente"**: autoridade de mesma hierarquia ou superior para inferior

Não se usam mais: "Cordialmente", "Com os protestos de estima e consideração", etc.

## Estrutura do Padrão Ofício

O padrão ofício unifica ofício, memorando e aviso em um único formato:
1. Cabeçalho (brasão e identificação do órgão)
2. Tipo e número do expediente / local e data
3. Endereçamento (A/Ao + cargo + nome)
4. Assunto (linha de referência obrigatória)
5. Vocativo (ex.: "Senhor Ministro,")
6. Texto (introdução + desenvolvimento + conclusão)
7. Fecho
8. Assinatura (nome + cargo)"""
})

NOVOS.append({
  "id": "r-ro-02", "topico": "ro-02", "disciplina": "redacao-oficial",
  "bloco": "basicos", "nome": "Tipos de documentos oficiais", "incidencia": "media",
  "versaoCurta": """# Tipos de Documentos Oficiais

## Padrão Ofício (3ª edição do Manual — unificação)
A 3ª edição unificou **ofício, memorando e aviso** em um único "padrão ofício"

### Antes da unificação:
| Doc. | Uso | Destino |
|---|---|---|
| **Ofício** | Comunicação externa | Outros órgãos ou particulares |
| **Memorando** | Comunicação interna | Mesmo órgão |
| **Aviso** | Entre Ministros/autoridades | Ministérios |

## Outros documentos
- **Exposição de Motivos (EM)**: documento que encaminha projeto de lei ou ato normativo ao Presidente; pode ser em 1ª pessoa; assinado pelo Ministro
- **Mensagem**: comunicação oficial do Presidente ao Congresso
- **Telegrama**: comunicação urgente; linguagem concisa
- **E-mail**: Assunto obrigatório; "prezado/prezada" no vocativo; formatação similar ao ofício
- **Ata**: registro de reunião; redigida em parágrafo único (ou não) sem rasuras; lavrada pelo secretário
- **Parecer**: opinião técnica fundamentada de servidor sobre matéria de sua competência
- **Despacho**: decisão ou encaminhamento de processo
- **Portaria**: ato normativo do Ministro ou dirigente; define normas, designa servidores, cria grupos de trabalho
- **Instrução Normativa**: ato de caráter normativo de órgão da Administração Pública

## Para a prova
- Memorando: interno (mesmo órgão); Ofício: externo
- Ata: sem rasuras; espaços em branco preenchidos com traço; erro = inutilize com "digo"
- Exposição de Motivos: único documento que admite 1ª pessoa
- Portaria: instrumento de gestão interna dos órgãos""",
  "versaoCompleta": """# Tipos de Documentos Oficiais — Estudo Completo

## O Padrão Ofício Unificado

A 3ª edição do Manual de Redação da Presidência da República (2018) unificou ofício, memorando e aviso em um único formato chamado **padrão ofício**. Essa unificação simplificou a burocracia ao criar um padrão único de estrutura, eliminando as diferenças formais entre os três.

Historicamente, as diferenças eram:
- **Ofício**: comunicação oficial para destinatários externos ao órgão (outros órgãos públicos, entidades privadas, cidadãos)
- **Memorando**: comunicação oficial interna, dentro do mesmo órgão, podendo ser de setor a setor
- **Aviso**: expedido exclusivamente por Ministros de Estado para destinatários de mesma hierarquia

## Exposição de Motivos

Documento pelo qual os Ministros de Estado (ou eventualmente outros altos dirigentes) submetem ao Presidente da República projetos de lei, medidas provisórias ou atos normativos para apreciação e assinatura. É o único documento oficial em que o uso da primeira pessoa do singular é admitido. Deve indicar claramente o que está sendo proposto e os fundamentos da proposta.

## Mensagem Presidencial

Instrumento de comunicação oficial entre o Chefe do Poder Executivo e o Congresso Nacional. Pode encaminhar projetos de lei, vetos, planos e relatórios.

## Ata

Registro escrito de reunião, sessão ou assembleia. Características:
- Redigida em ordem cronológica dos fatos ocorridos
- Sem rasuras: erros são corrigidos com "digo" (se percebido durante a redação) ou "em tempo" (ao final)
- Espaços em branco são preenchidos com traço
- Assinada pelo secretário e, quando necessário, pelos presentes
- Pode ser registrada em livro próprio ou em folhas soltas autenticadas

## Parecer

Opinião técnica de servidor ou colegiado sobre matéria de sua competência, fundamentada em normas e precedentes. Não é vinculante por si só — precisa ser aprovado pela autoridade competente.

## Despacho

Decisão ou encaminhamento dado a processo ou documento. Pode ser decisório (deferindo ou indeferindo) ou de mero trâmite (encaminhando ao setor competente).

## Portaria

Ato administrativo de competência dos Ministros de Estado ou outros dirigentes, usado para: designar servidores para funções, fixar normas de procedimento interno, criar grupos de trabalho, conceder férias, etc.

## E-mail no Padrão Oficial

O Manual dedica seção ao e-mail, tratando-o como documento oficial quando produzido por servidor em funções oficiais. Requisitos: campo "assunto" preenchido; vocativo adequado; texto formal com as partes do padrão ofício; assinatura com nome, cargo e contato."""
})

NOVOS.append({
  "id": "r-ro-03", "topico": "ro-03", "disciplina": "redacao-oficial",
  "bloco": "basicos", "nome": "Linguagem e formatação oficial", "incidencia": "baixa",
  "versaoCurta": """# Linguagem e Formatação Oficial

## Características da linguagem oficial
- **Formal**: uso da norma culta; sem gírias, regionalismos ou coloquialismos
- **Impessoal**: evita-se 1ª pessoa singular; usa-se "esta Secretaria", construções passivas
- **Clara e objetiva**: frases curtas e diretas; parágrafos temáticos
- **Técnica quando necessário**: termos técnicos são adequados e esperados

## Evitar na redação oficial
- Gerundismo: "Vou estar enviando" → "Enviarei" ou "Estou enviando"
- Voz passiva excessiva quando a ativa é mais clara
- Expressões redundantes: "a nível de", "no sentido de", "por força de"
- Adjetivos desnecessários: "grande desafio", "relevante questão"
- Siglas sem explicação na primeira menção

## Formatação (padrão ofício)
- **Papel**: A4 (29,7 × 21 cm)
- **Margem**: 2,5 cm (superior e esquerda) / 1,5 cm (inferior e direita)
- **Fonte**: Calibri ou Arial, tamanho 12 para texto; 11 para citações; 10 para rodapé
- **Espaçamento entre linhas**: 1,5 para texto; simples para citações e rodapés
- **Parágrafo**: sem recuo; espaço entre parágrafos = 6pt ou linha em branco

## Siglas e numerais
- Sigla: na primeira menção, escrever por extenso + sigla entre parênteses
- Números ordinais até décimo: por extenso; do 11º em diante: algarismo
- Valor monetário: R$ 10.000,00 (com ponto como separador de milhar, vírgula para centavos)

## Para a prova
- Gerundismo é o principal erro a identificar
- Vocativo: "Senhor Diretor," (com vírgula após o cargo)
- Data no documento: "Brasília, 8 de junho de 2025."
- Não se usa "prezado" para autoridades — use o tratamento correto (Senhor/Senhora + cargo)""",
  "versaoCompleta": """# Linguagem e Formatação Oficial — Estudo Completo

## Princípios Linguísticos da Redação Oficial

**Formalidade**: a linguagem oficial exige o padrão culto formal da língua portuguesa. Isso significa respeito às normas gramaticais, uso do vocabulário preciso e evitação de expressões coloquiais, regionalismos e gírias. A formalidade não implica artificialismo ou rebuscamento — ao contrário, o estilo deve ser natural dentro do registro formal.

**Impessoalidade**: a comunicação oficial é atribuída ao órgão, não ao servidor. Por isso evita-se a primeira pessoa do singular. Recursos para a impessoalidade:
- Construções passivas: "Informa-se que..." / "Foi aprovado..."
- Referência ao órgão: "Esta Secretaria comunica..." / "O Ministério solicita..."
- Locuções impessoais: "Cumpre informar que..." / "Torna-se necessário..."

**Concisão**: parágrafos curtos, frases objetivas, sem digressões. Cada parágrafo deve tratar de uma única ideia.

**Clareza**: prefira o vocabulário comum ao rebuscado quando o sentido for o mesmo. A clareza beneficia o leitor e acelera o processo administrativo.

## Erros Linguísticos Frequentes

**Gerundismo**: o uso excessivo e inadequado do gerúndio como substituto de formas verbais simples.
- Errado: "Estarei enviando o documento amanhã."
- Correto: "Enviarei o documento amanhã." / "Envio o documento amanhã."

**Expressões desgastadas**: "a nível de" (= em termos de / no âmbito de), "no sentido de" (= para / a fim de), "implementar" em lugar de "executar" ou "realizar", "problemática" em lugar de "problema".

**Pleonasmos**: "subir para cima", "descer para baixo", "retornar de volta", "há anos atrás".

**Cacofonia**: combinação de sílabas que forma sons desagradáveis ou palavrões — revisar o texto em voz alta ajuda a identificar.

## Formatação Básica

**Identificação**: o número do expediente segue o padrão: tipo/número/sigla do órgão/ano. Ex.: "Ofício nº 15/2025/SEDF".

**Local e data**: escrita por extenso — "Brasília, 8 de junho de 2025." — com ponto final.

**Vocativo**: cargo ou função do destinatário com letra maiúscula inicial — "Senhor Diretor," (vírgula obrigatória).

**Assunto**: sintetiza o conteúdo do documento em uma linha — "Assunto: Solicitação de cessão de servidores."

**Assinatura**: nome completo em maiúsculas, abaixo a função/cargo. Sem linha para assinatura (desnecessária em documentos digitais).

**Anexos**: indicados ao final, abaixo da assinatura — "Anexo: Relatório de atividades (5 folhas)." """
})

print(f"CB - Português e Redação Oficial: {len(NOVOS)} resumos escritos até aqui")
print("Continuando com Realidade do DF e demais blocos...")

# Adiciona ao JSON e salva parcialmente para teste
novos_topicos = {r["topico"] for r in NOVOS}
todos = dados["resumos"] + [r for r in NOVOS if r["topico"] not in existentes]
dados["resumos"] = todos
dados["versao"] = "2.0.0"
with open(SRC, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)
print(f"Salvo! Total de resumos agora: {len(todos)}")
