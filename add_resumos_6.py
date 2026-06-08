#!/usr/bin/env python3
"""Batch 6: re-01 to re-06, lc-02 to lc-04"""
import json, pathlib
BASE = pathlib.Path(__file__).parent
SRC  = BASE / "data" / "resumos.json"
with open(SRC) as f: dados = json.load(f)
existentes = {r["topico"] for r in dados["resumos"]}
NOVOS = []

NOVOS.append({"id":"r-re-01","topico":"re-01","disciplina":"regencia","bloco":"especificos",
"nome":"Tecnica gestual basica: padroes metricos (2, 3 e 4 tempos)","incidencia":"alta",
"versaoCurta":"""# Regencia: Padrao Metrico Gestual

## Funcao do gesto do regente
- Indicar o andamento (pulso)
- Indicar a divisao metrica (compasso)
- Transmitir as intencoes expressivas
- Sincronizar o grupo (entrada, cortes, transicoes)

## Principios do gesto
- **Ponto de batida (Ictus)**: momento exato do tempo (o mais baixo do gesto)
- **Preparacao (Aufhebung)**: movimento ascendente antes do ictus (anticipa)
- **Rebote**: movimento de recuperacao apos o ictus
- Movimento do pulso para baixo = ictus; pulso para cima = recuperacao

## Padrao binario (2/4, 2/2)
- Tempo 1: PARA BAIXO (ictus no fundo)
- Tempo 2: PARA CIMA
- Gesto: baixo-cima / baixo-cima

## Padrao ternario (3/4)
- Tempo 1: PARA BAIXO
- Tempo 2: PARA O LADO DIREITO (ou diagonal direita)
- Tempo 3: PARA CIMA
- Gesto: baixo-direita-cima

## Padrao quaternario (4/4)
- Tempo 1: PARA BAIXO
- Tempo 2: PARA DENTRO (esquerda)
- Tempo 3: PARA FORA (direita)
- Tempo 4: PARA CIMA
- Memorizar: BAIXO-DENTRO-FORA-CIMA

## Gestual aplicado ao contexto pedagogico
- Regencia nao e so para orquestra profissional
- Professor regente de coral escolar, banda, conjunto de sala
- Gestual simplificado mas consistente e suficiente para grupos escolares
- Batuta opcional; rosto e corpo tambem comunicam

## Para a prova
- Padrao 4/4: baixo(1) - esquerda/dentro(2) - direita/fora(3) - cima(4)
- Preparacao (pickup): gesto ascendente ANTES do 1 tempo
- Ictus = o momento de ataque (ponto mais baixo)
- Fermata: mantem o gesto parado ate querer liberar
- Anacruse = nota(s) antes do primeiro tempo forte""",
"versaoCompleta":"""# Regencia: Padroes Metricos e Gestual Basico

## A Comunicacao Gestual na Regencia

O regente comunica com um conjunto musical (coral, orquestra, banda, conjunto de camera) principalmente atraves do gesto. A batuta e o corpo sao instrumentos de comunicacao; o gesto ideal e economico, claro e expressivo ao mesmo tempo.

A regencia pedagogica (contexto escolar) nao exige o nivel de refinamento tecnico de um regente profissional, mas exige clareza e consistencia. Um professor que rege um coral ou conjunto precisa dominar os padroes metricos basicos e os sinais de entrada, corte e expressao dinamica.

## Elementos do Gesto

**Ictus (ponto de batida)**: o momento exato em que o tempo ocorre. Corresponde ao ponto mais baixo do gesto para baixo (1 tempo) ou ao ponto de retorno nos outros tempos. Os instrumentistas e cantores tocam/cantam no ictus, nao antes nem depois.

**Preparacao (Aufhebung ou gesto preparatorio)**: o movimento que antecede o ictus do 1 tempo (ou de qualquer entrada). E ascendente, no andamento da musica, e "mostra" para o grupo o que esta por vir. Uma boa preparacao e metade do sucesso de qualquer entrada.

**Rebote**: o movimento de recuperacao apos o ictus. Deve ser elastico, como uma bola quicando, nao rigido.

## Padroes Metricos

**Compasso binario (2 tempos)**: gesto em forma de V invertido. Baixo (1) - Cima (2). E o mais simples.

**Compasso ternario (3 tempos)**: triangulo. Baixo (1) - Direita (2) - Cima (3). A passagem do tempo 2 para 3 deve ser suave, sem angulos bruscos.

**Compasso quaternario (4 tempos)**: o mais usado. Baixo (1) - Dentro/Esquerda (2) - Fora/Direita (3) - Cima (4). A direcao dos tempos 2 e 3 pode variar por escola de regencia, mas o padrao Baixo-Dentro-Fora-Cima e o mais ensinado no Brasil.

## Aplicacao em Sala de Aula

Para reger um coral escolar, o professor precisara dominar: preparacao da entrada; padrao do compasso (2, 3 ou 4); corte; dinâmicas expressas pelo tamanho do gesto (pequeno = suave; grande = forte); mudancas de andamento (acelerando/ritardando)."""})

NOVOS.append({"id":"r-re-02","topico":"re-02","disciplina":"regencia","bloco":"especificos",
"nome":"Entradas, fermatas, dinamica gestual","incidencia":"media",
"versaoCurta":"""# Regencia: Entradas, Fermatas e Dinamica

## Gesto de entrada
- Sempre precedido de **gesto preparatorio** (no andamento correto)
- Preparacao = 1 tempo antes da entrada (ou 2 se necessario)
- Mostra: andamento, dinamica, carater
- Olho no grupo: contato visual antes de qualquer entrada importante

## Tipos de entrada
- **Em tempo forte (1)**: preparacao no tempo 4 (ou no ultimo tempo do compasso)
- **Em tempo fraco (2, 3 ou 4)**: preparacao ainda um tempo antes
- **Anacruse**: entrada em tempo fraco antes do compasso completo; preparacao ajustada

## Corte (cutoff)
- Indica o fim do som
- Gesto circular ou de retorno ao eixo
- Deve ser preciso: o grupo corta exatamente onde o regente indica
- **Corte de fermata**: mais elaborado; sinaliza o fim da nota sustentada

## Fermata
- Nota sustentada alem do valor indicado
- Gesto: parar o movimento no ictus; manter o gesto suspenso
- Para liberar a fermata: gesto de corte seguido de preparacao para continuar (ou parar)
- Fermata em pausa: o silencio tambem e sustentado

## Dinamica gestual
- **Forte**: gesto maior, mais firme, mais distante do corpo
- **Piano**: gesto menor, perto do corpo, mais suave
- **Crescendo**: gesto cresce gradualmente
- **Diminuendo**: gesto diminui gradualmente
- **Sforzando (sfz)**: gesto brusco, de impulso seco

## Expressao facial e corporal
- Rosto comunica: legato (expressao suave), staccato (articulacao marcada)
- Postura: ereto, estavel; nao dancar (distrair o conjunto)
- Tensao muscular do regente reflete na tensao do som

## Para a prova
- Preparacao: obrigatoria antes de qualquer entrada
- Fermata: gesto parado + corte + preparacao
- Dinamica: tamanho do gesto proporcional ao volume desejado
- Cutoff circular: o mais ensinado nos metodos de regencia coral
- Legato vs. staccato: expressos pela fluidez ou articulacao do gesto""",
"versaoCompleta":"""# Regencia: Entradas, Fermatas e Dinamica Gestual

## A Importancia da Entrada

A entrada (do ingles "cue" ou do alemao "Einsatz") e o momento em que um grupo comeca a tocar ou cantar. E o momento mais critico da regencia: uma entrada mal preparada leva o grupo a entrar desunido, no andamento errado ou com o carater incorreto.

Uma boa entrada depende de tres elementos:
1. **Contato visual**: o regente deve olhar para o grupo (ou para a secao que vai entrar) antes de preparar
2. **Gesto preparatorio claro**: um tempo antes da entrada, no andamento exato
3. **Comunicacao de carater**: o gesto ja indica se e suave, forte, legato, marcato

## Anacruse e Preparacao

Quando a entrada ocorre em um tempo fraco (nota de anacruse), a preparacao precisa ser ajustada para caber no espaco disponivel. Se o grupo entra no tempo 4 de um compasso de 4/4, a preparacao ocorre no tempo 3. O movimento preparatorio ja deve indicar o carater do que vira.

## A Fermata em Detalhe

A fermata e um dos gestos mais complexos de executar bem. O regente precisa:
1. Sustentar o gesto no ponto do ictus sem movimentar
2. Manter contato visual para "segurar" o grupo
3. Quando quiser liberar: fazer um pequeno gesto de corte
4. Se a musica continua: imediatamente apos o corte, fazer o gesto preparatorio para o proximo tempo

Fermata em pausa (sobre um silencio): o gesto para no espaco, nao no ictus. O grupo entende que o silencio continua ate o regente se mover.

## Dinamica: O Espaco do Gesto

A relacao entre o espaco do gesto e o volume sonoro e direta: gestos maiores = sons mais fortes; gestos menores = sons mais suaves. Isso e intuitivo para a maioria dos grupos, mesmo sem treinamento formal.

O sforzando (sfz ou sf) exige um gesto brusco e de impulso — diferente do forte sustentado. O piano subito (fp: forte seguido de piano) exige dois gestos distintos em rapida sucessao."""})

NOVOS.append({"id":"r-re-03","topico":"re-03","disciplina":"regencia","bloco":"especificos",
"nome":"Trabalho com banda sinfonica","incidencia":"media",
"versaoCurta":"""# Regencia: Banda Sinfonica

## O que e banda sinfonica
- Conjunto instrumental de sopros (madeiras + metais) + percussao
- Sem cordas friccionadas (violinos, violas, cellos, contrabaixos)
- Origem: bandas militares europeias (seculo XVIII)
- No Brasil: tradicao de bandas municipais e escolares (bandas filarmônicas)

## Formacao da banda sinfonica
**Madeiras**: flautas, oboés, clarinetas (1ª e 2ª), fagotes, saxofones (soprano, alto, tenor, baritono)
**Metais**: trompetes/cornetas, trombones, eufônios/bombardinos, tubas, cornos
**Percussao**: timbales, bombo, caixa, pratos, xilofone, vibrafone, marimba
**Contrabaixo** (eletrico ou acustico) e piano: complementos eventuais

## Especificidades da regencia de banda
- Instrumentos transpositores: clarineta (Si b), saxofones, trompetes — soam diferente do que e escrito
- Partitura de regencia: combina todas as partes (full score)
- Preparacao de ensaio: regente estuda a partitura antes, marca entradas, verifica afinacao
- Equilíbrio: metais tendem a ser mais fortes; regente deve balancear

## Repertorio
- Arranjos de obras orquestrais e opera
- Musica original para banda (Wind Band repertoire)
- Musica popular brasileira (marchas, dobrados, choros)

## Contexto escolar e no DF
- CEPs no DF incluem bandas escolares (sopros + percussao)
- Projeto Bandas e Fanfarras: rede publica de alguns estados
- Banda filarmonica: tradicao nordestina; muito presente no CEP-EMB e no DF

## Para a prova
- Banda sinfonica: sopros + percussao (sem cordas friccionadas)
- Instrumentos transpositores: soam em altura diferente da escrita
- Regente de banda usa partitura full score (partitura completa)
- Equilíbrio timbrístico: desafio especifico da banda (metais dominam)
- Dobrado: marcha tipica brasileira; muito na tradicao de banda""",
"versaoCompleta":"""# Regencia: Trabalho com Banda Sinfonica

## Historia e Contexto

A banda sinfonica tem origens nas bandas militares europeias do seculo XVIII, usadas para comunicacao no campo de batalha e cerimonias. Com a paz, essas bandas migraram para o contexto civil e se tornaram conjuntos de entretenimento publico — as bandas municipais, que tocavam nos coretos das pracas.

No Brasil, a tradicao de banda e muito forte, especialmente no Nordeste (bandas filarmônicas) e no Centro-Oeste. No DF, os CEPs (Centros de Ensino Profissional) frequentemente tem conjuntos de sopros e percussao.

## Instrumentos Transpositores

Um dos maiores desafios do regente iniciante com banda e lidar com os instrumentos transpositores:

**Clarineta em Si b**: soa um tom abaixo do escrito. Para ouvir um La concerto, o clarinete le um Si.
**Saxofone alto em Mi b**: soa uma sexta maior abaixo do escrito.
**Trompete em Si b**: soa um tom abaixo do escrito (como a clarineta).
**Como (trompa) em Fa**: soa uma quinta abaixo do escrito.

A partitura de regencia (full score) mostra as partes em sua altura de concerto (soando real) OU em cada transposi ao — dependendo da edicao. O regente precisa saber "traduzir" o que cada instrumento le para o som real.

## Equilíbrio e Balanco na Banda

O desafio central da regencia de banda e o equilíbrio dinamico: metais (especialmente trombones e tubas) naturalmente projetam mais som que madeiras. O regente precisa:
- Pedir sistematicamente que os metais toquem piano relativo
- Reforcar as linhas melodicas nas madeiras
- Posicionar o conjunto para que as madeiras nao fiquem escondidas atras dos metais

## Preparacao de Ensaio

Uma regencia eficiente pressupoe ensaio bem preparado: estudo previo da partitura (marcacao de entradas, identificacao de dificuldades tecnicas), conhecimento do repertorio (para demonstrar o que quer), planejamento do tempo de ensaio (do mais difícil ao mais facil, ou inversamente para aquecer)."""})

NOVOS.append({"id":"r-re-04","topico":"re-04","disciplina":"regencia","bloco":"especificos",
"nome":"Trabalho com orquestra","incidencia":"media",
"versaoCurta":"""# Regencia: Trabalho com Orquestra

## Formacao orquestral
**Cordas**: violinos I, violinos II, violas, cellos, contrabaixos
**Madeiras**: flautas, oboés, clarinetas, fagotes
**Metais**: trompas, trompetes, trombones, tuba
**Percussao**: timbales + percussao complementar
**Teclado/Harpa**: eventuais

## Disposicao fisica
- Regente ao centro, de costas para o publico (geralmente)
- Violinos I a esquerda; violinos II a direita (ou invertido)
- Violas ao centro-direita; cellos a esquerda-frente
- Madeiras e metais no centro; percussao ao fundo

## Especificidades da regencia orquestral
- Trabalho com 4 naipes de cordas + sopros + percussao
- Comunicacao setorial: regente dirige naipes (secao de cordas, secao de sopros)
- Colega de concertino (spalla): representante das cordas; comunicacao direta
- Ensaio secional vs. ensaio completo

## Orquestra sinfonica vs. camera
- **Orquestra sinfonica**: grande (80-100+ musicos); repertorio romantico/moderno
- **Orquestra de camera**: menor (15-40); repertorio barroco/classico
- **Conjunto de cordas**: apenas cordas (sem sopros); musica de camera ampliada

## Orquestra no contexto do DF/CEP-EMB
- CEP-EMB forma instrumentistas de orquestra
- OSTNB (Orquestra Sinfonica do Teatro Nacional de Brasilia): orquestra profissional do DF
- Projeto Jovem Musico SESI/DF: orquestras jovens

## Para a prova
- Orquestra sinfonica: cordas + sopros + percussao
- Ordem dos naipes da frente para o fundo: cordas > madeiras > metais > percussao
- Spalla/concertino: 1 violinista, lider das cordas, fica de pe para sinais
- Baqueta do maestro: usado para clareza visual; nao e obrigatorio
- Regencia de orquestra: 4 padroes basicos + comunicacao setorial""",
"versaoCompleta":"""# Regencia: Trabalho com Orquestra

## A Orquestra Sinfonica

A orquestra sinfonica moderna e um conjunto de 60-100+ musicos dividido em quatro familias:
- **Cordas**: maior familia; violinos I e II, violas, cellos, contrabaixos
- **Madeiras**: flautas, oboés (e como ingles), clarinetas, fagotes (e contrafagote)
- **Metais**: trompas, trompetes, trombones, tuba
- **Percussao**: timbales (pauquistas), percussao diversa, harpa, piano

## Desenvolvimento Historico

A orquestra moderna se consolidou no periodo classico (Haydn, Mozart) com cerca de 35-40 musicos. Beethoven expandiu para 60-70. Brahms, Wagner e Mahler aumentaram para 80-100+. O repertorio barroco e tocado por orquestras de camera menores, com praticas historicamente informadas (HIP).

## A Comunicacao na Orquestra

O regente comunica com a orquestra por:
- **Gesto** (batuta e mao livre): padrao metrico, entradas, expressao
- **Contato visual**: sinais para naipes especificos (chama o oboé, sinaliza para as trompas)
- **Concertino/spalla**: o 1 violinista fica na 1 estante da esquerda; recebe sinais especiais do regente; representa as cordas em questoes de arcada e articulacao

O **ensaio secional** (apenas um naipe ou familia) permite trabalho detalhado sem o desgaste de toda a orquestra. O **ensaio geral** une tudo antes da apresentacao.

## Pratica de Regencia no CEP-EMB

No CEP-EMB e em cursos de licenciatura em musica, a regencia e disciplina obrigatoria. O estudante aprende os padroes metricos, estuda partituras completas (full scores) e dirige grupos reais ou simulados. O foco pedagogico e: tecnica gestual clara + capacidade de comunicar a intencao musical."""})

NOVOS.append({"id":"r-re-05","topico":"re-05","disciplina":"regencia","bloco":"especificos",
"nome":"Trabalho com coro","incidencia":"alta",
"versaoCurta":"""# Regencia: Trabalho com Coro

## O que e regencia coral
- Regencia de conjunto vocal (coro/coral)
- Contexto mais comum na escola e na comunidade
- Coro escolar: alunos de diferentes faixas etarias, treinamento variavel

## Tipos de coro
| Tipo | Vozes | Tessituras |
|---|---|---|
| **Infantil** | Vozes iguais (soprano) | Sol3-Ré5 aprox. |
| **Igual feminino** | SA (soprano + contralto) | Mi3-Lá5 aprox. |
| **Igual masculino** | TB (tenor + baritono) | La2-Fa4 aprox. |
| **Misto (SATB)** | Soprano, Alto, Tenor, Baixo | 4 naipes |

## Especificidades da regencia coral
- Respiracao coletiva: regente sinaliza quando o grupo respira
- Dicao e texto: articulacao das consoantes em conjunto; uniformidade vogal
- Afinacao: ajustes por naipe; ouvir o basse (baixo) como referencia
- Blend (fusao): timbres individuais se fundem no som do conjunto

## Vozes e mudanca de voz
- Alunos do EF Anos Finais/EM: passam por mudanca de voz
- Meninos: voz muda (breaking): graves ficam instáveis, agudos desaparecem
- Meninas: engrossamento da voz (menos drasmatico)
- Regente deve considerar isso no repertorio e na distribuicao de vozes

## Repertorio coral escolar
- Musica folklorica e regional: accessível, identidade cultural
- Musica popular brasileira com arranjos simples
- Canones (rounds): acessíveis; desenvolvem ouvido harmonico
- Evitar: tessitura extrema, harmonia muito complexa, longos trechos sem respiracao

## Para a prova
- SATB: soprano + alto + tenor + baixo (4 vozes do coro misto)
- Mudanca de voz: cuidado com repertorio para adolescentes masculinos
- Afinacao coral: ouvir o baixo; vozes iguais tendem a ser mais fáceis de afinar
- Dicao: principal diferencial do coro em relacao a instrumental
- Regente coral: menos batuta; mais expressao facial e gestual""",
"versaoCompleta":"""# Regencia: Trabalho com Coro

## O Coro como Instrumento Social

O coro e o conjunto musical mais democratico: nao requer instrumentos caros, pode ser formado em qualquer escola ou comunidade, e e acessível a pessoas de todas as idades. Por isso, a regencia coral e a habilidade musical mais diretamente aplicavel ao cotidiano do professor de musica.

## Organizacao por Vozes

**Soprano (S)**: voz feminina aguda. Tessiture tipica: Do4 (Do medio) a Sol5 ou La5.
**Contralto/Alto (A)**: voz feminina grave. Tessiture: Fa3 a Ré5.
**Tenor (T)**: voz masculina aguda. Soa uma oitava abaixo do escrito na partitura vocal. Tessiture real: Do3 a La4.
**Baixo (B)**: voz masculina grave. Tessiture: Fa2 a Ré4.

Em coros escolares, a divisao e frequentemente simplificada: Vozes Iguais (todos no mesmo naipe ou divididos em 2) ou, no Ensino Medio, SATB se ha vozes masculinas apos a mudanca.

## A Mudanca de Voz

A mudanca de voz (break) nos meninos ocorre geralmente entre 12 e 15 anos. Durante esse periodo:
- O controle vocal e instavel (voz "falha")
- O alcance agudo diminui drasticamente
- A voz "desce" ate 1,5 oitava

O regente sensível mantem esses alunos cantando com repertorio adaptado (nao os exclui do coro). Manter os meninos em transicao cantando e crucial para o desenvolvimento vocal continuo.

## Aspectos Tecnicos do Ensaio Coral

**Aquecimento vocal**: essencial antes de qualquer ensaio. Nao e luxo e e prevencao de lesoes e melhora da qualidade sonora.

**Uniformidade de vogal**: o som coral bonito vem de todas as vozes cantando as mesmas vogais (abertura, posicao). "A" aberto vs. "A" fechado — um naipe inteiro precisa soar igual.

**Afinacao**: o baixo e a referencia; soprana precisa escutar o contralto; ouvir o baixo e importante para todos. O professor comeca a trabalhar afinacao desde o unissono.

**Blend**: a fusao dos timbres individuais e o "Santo Graal" da regencia coral. Cada cantor precisa ouvir o conjunto mais do que a sua voz individual."""})

NOVOS.append({"id":"r-re-06","topico":"re-06","disciplina":"regencia","bloco":"especificos",
"nome":"Regencia aplicada ao contexto pedagogico","incidencia":"alta",
"versaoCurta":"""# Regencia no Contexto Pedagogico Escolar

## Regencia como competencia docente
- Todo professor de musica e, em alguma medida, regente
- Reger um coral, uma banda de aula, um conjunto ritmico = regencia pedagogica
- Competencia nao e exclusiva de musicos classicos/concertistas

## Adaptacoes para o contexto escolar
- **Coro escolar**: tecnica gestual simplificada; foco na expressao e na musica
- **Conjunto de sala**: percussao corporal + vozes + instrumentos simples
- **Banda de sopros**: contexto de CEP; regencia mais formal
- **Musica em roda**: disposicao circular; todos se ouvem; lider mais que regente

## Estrategias pedagogicas
- **Regencia diferencida**: cada aluno rege um compasso (desenvolve musicalidade)
- **Gesto como ferramenta de avaliacao**: aluno rege = demonstra compreensao rítmica e musical
- **Regencia como atividade de composicao**: criar padroes gestuais para sons inventados

## Funcoes do gesto no contexto escolar
- Chamar atencao (gesto de alerta)
- Indicar entrada de um grupo
- Indicar silencio (fermata ou corte)
- Indicar volume (grande = forte, pequeno = piano)
- Indicar carater (suave, vigoroso, staccato)

## Relacao com as metodologias
- **Dalcroze**: gesto e corpo como linguagem musical — fundamento direto
- **Orff**: percussao corporal + regencia informal
- **Koellreutter**: improviso + gestos nao-convencionais = explorar a expressao

## Para a prova
- Regencia pedagogica: professor de musica usa gestos para comunicar musicalmente
- Nao exige batuta ou formacao formal em regencia para contexto de sala de aula
- Dalcroze: base teorica para o uso do movimento na musica
- Questoes situacionais: "professor usa sinais gestuais para... = abordagem de regencia informal
- Regencia de coral escolar: habilidade prioritaria para o professor da EB""",
"versaoCompleta":"""# Regencia Aplicada ao Contexto Pedagogico

## Regencia como Pratica Docente

A regencia no contexto escolar nao se limita a concertos ou apresentacoes formais. O professor de musica "rege" constantemente: ao conduzir um aquecimento vocal, ao coordenar uma atividade ritmica em grupo, ao indicar quando o grupo deve parar de tocar, ao pedir mais volume a uma secao.

Desenvolver competencia gestual e uma das habilidades praticas mais importantes da licenciatura em musica.

## A Regencia Simplificada para o Contexto Escolar

No contexto da sala de aula regular (Ensino Fundamental e Medio), o professor nao precisa dominar toda a tecnica de regencia de orquestra. O que e necessario:

**Padrao metrico claro**: saber indicar o tempo 1 de cada compasso e o andamento.

**Gesto de preparacao eficaz**: o grupo precisa entrar junto.

**Sinal de corte**: parar o grupo de forma ordenada.

**Gestos expressivos**: grande/pequeno para volume; fluido/articulado para legato/staccato.

**Contato visual**: mais importante que qualquer gesto tecnico — o olhar conecta o regente ao grupo.

## Regencia como Ferramenta Pedagogica

A regencia pode ser usada como **estrategia de aprendizagem**: alunos regem uns aos outros. Quando um aluno rege um trecho, ele precisa: ter internalizado o pulso; entender a estrutura metrica; prever as entradas; comunicar a expressao musical. E uma forma de avaliacao formativa muito rica.

Em aulas de improvisacao (Koellreutter, Schafer), o "regente" pode usar gestos nao-convencionais para controlar parametros da improvisacao coletiva: levantar o braco = crescendo; mover as maos = mudar o timbre; silencio total = abaixar a palma.

## Regencia Coral como Prioridade

Para o professor de musica da Educacao Basica, a regencia de coral e a competencia mais diretamente aplicavel. Montar e ensaiar um coral escolar desenvolve: musicalidade dos alunos, sentido de coletividade, repertorio, expressao vocal e pratica de performance."""})

# ── Legislacao CEP-EMB ────────────────────────────────────────

NOVOS.append({"id":"r-lc-02","topico":"lc-02","disciplina":"legislacao-cep","bloco":"especificos",
"nome":"Portaria Conjunta no 40/2025 — Atribuicoes CEP-EMB (atualizada)","incidencia":"alta",
"versaoCurta":"""# Portaria Conjunta no 40/2025 — CEP-EMB

## O que e
- Portaria CONJUNTA: emitida por mais de uma secretaria/orgao
- Atualiza e substitui normas anteriores sobre atribuicoes no CEP-EMB
- Regula: carga horaria, funcoes, distribuicao de aulas no Conservatorio de Musica de Brasilia (EMB)

## CEP-EMB — Centro de Educacao Profissional
- **Escola de Musica de Brasilia (EMB)**: principal CEP de musica do DF
- Oferece: cursos basicos, tecnicos e de extensao em musica
- Vinculado a SEDF; nao e universidade (nao emite diplomas de ensino superior)
- Professores: habilitados em musica (licenciatura ou bacharelado)

## Atribuicoes regulamentadas
- **Regencia de classe**: numero de turmas e alunos por professor
- **Carga horaria**: horas-aula + horas de coordenacao + atividades extraclasse
- **Especialidades docentes**: instrumento (piano, violino, canto, violao etc.) vs. disciplinas teoricas (teoria, historia, percepcao)
- **Coordenacao pedagogica**: carga horaria e obrigacoes

## Diferencas do professor regular
- Professor do CEP-EMB tambem tem coordenacao, mas a natureza e diferente
- Ha mais especializacao por area (instrumento vs. teoria)
- Pode ter turmas de diferentes niveis (iniciante ao tecnico avancado)

## Para a prova
- Portaria 40/2025 = a mais recente sobre atribuicoes do CEP-EMB
- CEP-EMB oferece educacao profissional (nao superior) em musica
- Professor da EMB: mesmo estatuto do professor da EB do DF (magistério publico)
- Diferenca Portaria 38/2022 (professor EB geral) vs. Portaria 40/2025 (especifico CEP)
- Questoes cobram: o que esta e nao esta nas atribuicoes do professor do CEP""",
"versaoCompleta":"""# Portaria Conjunta no 40/2025 — CEP-EMB

## Contexto Institucional

O **CEP-EMB** (Centro de Educacao Profissional — Escola de Musica de Brasilia) e a principal instituicao de educacao musical profissional do Distrito Federal. Integra a rede publica da SEDF e oferece:
- **Cursos basicos**: introducao a musica; formacao geral; sem pre-requisito
- **Cursos tecnicos**: formacao profissional de nivel medio em musica (compativel com Ensino Medio)
- **Cursos de extensao**: aperfeicoamento, oficinas, masterclasses

O CEP-EMB e uma instituicao de **Educacao Profissional** (nivel medio), nao de Educacao Superior. Professores nao dao aulas universitarias; alunos nao recebem diplomas de bacharel ou licenciado.

## A Portaria Conjunta no 40/2025

A Portaria Conjunta, emitida em 2025, atualizou as normas que regem as atribuicoes dos profissionais do CEP-EMB. E "conjunta" pois e assinada por mais de uma autoridade da SEDF, refletindo a articulacao entre diferentes subsistemas da secretaria.

Os aspectos regulamentados incluem:
- Distribuicao de carga horaria por tipo de disciplina (instrumental, teorica, conjunto)
- Criterios para composicao de turmas (numero de alunos por nivel)
- Atribuicoes especificas do professor de instrumento vs. professor de disciplinas teoricas
- Horas de coordenacao pedagogica e atividades de ensaio fora da sala de aula

## Diferenca entre Portaria 38/2022 e Portaria 40/2025

A **Portaria 38/2022** regula as atribuicoes do Professor de Educacao Basica da SEDF em geral (ja coberta em lc-03). A **Portaria 40/2025** e especifica para o contexto do CEP-EMB, com suas particularidades de educacao musical profissional.

Para a prova, o candidato deve saber distinguir as duas e identificar qual se aplica a cada situacao."""})

NOVOS.append({"id":"r-lc-03","topico":"lc-03","disciplina":"legislacao-cep","bloco":"especificos",
"nome":"Portaria Conjunta SEDF no 38/2022 — Atribuicoes do Professor de EB","incidencia":"alta",
"versaoCurta":"""# Portaria Conjunta SEDF no 38/2022

## O que e
- Portaria que regulamenta as **atribuicoes do Professor de Educacao Basica** da SEDF
- Define: o que o professor DEVE fazer; o que NAO e atribuicao do professor; carga horaria
- Aplicavel a TODOS os professores da EB no DF (incluindo os do CEP-EMB, complementada pela Portaria 40)

## Atribuicoes do professor (principais)
- Regencia de classe (dar aula): nucleo central da funcao
- Planejamento das aulas (plano de aula, plano de ensino)
- Participacao nas coordenacoes pedagogicas
- Elaboracao e aplicacao de avaliacoes
- Registro de frequencia e aproveitamento dos alunos
- Participacao em Conselho de Classe
- Elaboracao do PPP (junto com a equipe)
- Atendimento aos pais/responsaveis

## Carga horaria (contexto SEDF)
- Jornada basica: 40h semanais (incluindo regencia e coordenacao)
- Horas de regencia: determinadas pelo numero de turmas
- Horas de coordenacao: proporcao definida pela portaria
- Complementacao de jornada: atividades extraclasse (preparacao, correc ao)

## O que NAO e atribuicao do professor
- Servicos administrativos gerais (limpeza, seguranca, secretaria)
- Substituicao rotineira de outros profissionais nao docentes
- Atividades incompatíveis com a funcao pedagogica

## Para a prova
- Portaria 38/2022 = atribuicoes do professor da EB do DF
- Coordenacao pedagogica: direito E dever do professor (nao e opcional)
- Professor NAO pode ser desviado para funcoes administrativas
- Regencia de classe: atividade-fim do professor
- Esta portaria regula o professor regular; Portaria 40/2025 especifica o CEP""",
"versaoCompleta":"""# Portaria Conjunta SEDF no 38/2022 — Atribuicoes do Professor de EB

## Fundamento Legal

A Portaria Conjunta SEDF no 38/2022 foi emitida no ambito da SEDF para regulamentar de forma clara as atribuicoes dos professores de Educacao Basica. Baseia-se na LDB (arts. 12-13), no Estatuto do Magisterio do DF, na Lei Organica do DF e nas diretrizes do PDE.

## As Atribuicoes Centrais

**Regencia de classe**: e a atividade-fim do professor. Inclui nao apenas "estar em sala" mas todo o ciclo: planejamento, execucao e avaliacao.

**Planejamento**: o professor deve elaborar planos de aula e de ensino (anual/semestral) como parte de sua carga horaria. Nao e atividade extra, e parte do trabalho docente remunerado.

**Coordenacao pedagogica**: a participacao nas coordenacoes coletivas e individuais e obrigatoria. O professor nao pode se recusar a participar nem a instituicao pode usar esse tempo para atividades administrativas.

**Conselho de Classe**: o professor participa das reunioes de Conselho de Classe, que sao instancias colegiadas de decisao sobre aprendizagem e progressao dos alunos.

**Atendimento a familias**: o professor deve estar disponivel para orientar pais e responsaveis sobre o progresso dos alunos, dentro do horario e das formas previstas pela escola.

## Limites das Atribuicoes

A portaria e importante tambem pelo que DELIMITA: o professor nao pode ser sistematicamente desviado para funcoes que nao sao de sua competencia. Atribuir ao professor tarefas de secretaria, vigilancia ou servicos gerais configura desvio de funcao.

## Importancia para o Concurso

Questoes de prova frequentemente apresentam situacoes em que o professor e colocado em posicoes inadequadas (fazendo servico de secretaria, sendo impedido de coordenacao) e perguntam se isso e legal. A Portaria 38/2022 e o instrumento para responder."""})

NOVOS.append({"id":"r-lc-04","topico":"lc-04","disciplina":"legislacao-cep","bloco":"especificos",
"nome":"Estrutura do ensino profissional de musica no DF","incidencia":"media",
"versaoCurta":"""# Estrutura do Ensino Profissional de Musica no DF

## O que e educacao profissional de musica
- Formacao de nivel tecnico em musica (nao superior)
- Prevista na LDB (art. 39-42) e DCNs para Ed. Profissional (Res. 6/2012)
- Integrada ao Ensino Medio ou ofertada de forma concomitante/subsequente

## CEPs de Musica no DF
- **EMB (Escola de Musica de Brasilia)**: principal; fundada em 1974; fica na 602 Sul
- **Outros CEPs com musica**: algumas unidades em regioes administrativas
- Vinculados a SEDF; gratuitos; de acesso por selecao/lista de espera

## Niveis de formacao no CEP-EMB
1. **Curso Basico**: formacao musical fundamental; nao e tecnico; sem pre-requisito
2. **Curso Tecnico em Instrumento Musical**: nivel medio tecnico; para quem ja tem formacao basica ou faz concomitantemente ao EM
3. **Cursos de Extensao e Aperfe icoamento**: oficinas, masterclasses, grupos artisticos

## Instrumentos e disciplinas oferecidas
- Instrumentos: piano, violino, viola, cello, contrabaixo, flauta, oboé, fagote, clarineta, saxofone, trompete, trombone, tuba, percussao, canto lirico, violao, guitarra, etc.
- Disciplinas teoricas: teoria musical, percepcao musical, historia da musica, harmonia, contraponto, regencia

## Professores do CEP-EMB
- Habilitados na area de musica (licenciatura em musica ou bacharelado + complementacao)
- Regidos pelo mesmo estatuto do magistério publico do DF
- Atribuicoes especificas regulamentadas pela Portaria 40/2025

## Para a prova
- EMB: fundada 1974; publico; gratuita; endereco no Plano Piloto
- Educacao profissional de musica: nivel medio tecnico (nao superior)
- CEP ≠ universidade; aluno nao recebe diploma de bacharel
- Acesso: selecao (audicao ou prova de aptidao, dependendo do curso)
- SEDF gere os CEPs de musica do DF""",
"versaoCompleta":"""# Estrutura do Ensino Profissional de Musica no DF

## Base Legal

A educacao profissional e tecnologica esta prevista nos arts. 39-42 da LDB e nas Diretrizes Curriculares Nacionais para Educacao Profissional Tecnica de Nivel Medio (Resolucao CNE/CEB no 6/2012). A musica, como area de formacao profissional, integra o eixo tecnologico "Producao Cultural e Design".

## A Escola de Musica de Brasilia (EMB)

A **Escola de Musica de Brasilia** foi fundada em 1974 e e a maior e mais tradicional instituicao de educacao musical do Centro-Oeste. Localizada na Asa Sul (602 Sul), oferece:

**Cursos Basicos**: aulas de instrumento e teoria para criancas, jovens e adultos sem pre-requisito musical. Nao conferem certificacao tecnica, mas formam a base para o acesso ao nivel tecnico.

**Cursos Tecnicos em Instrumento Musical**: habilitacao tecnica de nivel medio. Para alunos que ja tem formacao musical previa (ou que cursam concomitantemente ao Ensino Medio). O diploma e de Tecnico em Instrumento Musical — habilita para o exercicio profissional como musico, mas nao para o ensino (que requer licenciatura).

**Extensao**: masterclasses, cursos de curta duracao, grupos artisticos (orquestra jovem, coral, conjuntos de camera).

## Especificidades do Corpo Docente

Os professores do CEP-EMB sao servidores publicos do quadro do magisterio da SEDF. Sua formacao tipica e bacharelado em musica (instrumento especifico) + complementacao pedagogica, ou licenciatura em musica.

A Portaria 40/2025 especifica as atribuicoes, a carga horaria e os criterios de distribuicao de aulas para esse contexto especifico — diferenciando do contexto das escolas regulares de EB.

## Perspectivas

O DF e referencia nacional em educacao profissional de musica. A EMB e fonte de musicos que integram orquestras profissionais, grupos de camara e conjuntos de musica popular do DF e de todo o Brasil."""})

todos = dados["resumos"] + [r for r in NOVOS if r["topico"] not in existentes]
dados["resumos"] = todos
dados["versao"] = "2.6.0"
with open(SRC,"w",encoding="utf-8") as f: json.dump(dados,f,ensure_ascii=False,indent=2)
print("Batch 6 OK — total: %d" % len(todos))
