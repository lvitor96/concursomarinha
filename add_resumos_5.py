#!/usr/bin/env python3
"""Batch 5: hm-01, hm-02, hm-04 to hm-09, tm-01 to tm-08"""
import json, pathlib
BASE = pathlib.Path(__file__).parent
SRC  = BASE / "data" / "resumos.json"
with open(SRC) as f: dados = json.load(f)
existentes = {r["topico"] for r in dados["resumos"]}
NOVOS = []

NOVOS.append({"id":"r-hm-01","topico":"hm-01","disciplina":"historia-musica","bloco":"especificos",
"nome":"Periodo Medieval: cantochao, organum, troubadours, Ars Nova","incidencia":"media",
"versaoCurta":"""# Historia da Musica: Periodo Medieval (aprox. 500-1400)

## Cantochao (Canto Gregoriano)
- Canto monofônico (uma voz/linha) sem acompanhamento instrumental
- Modo modal (nao tonal) — escalas modais (dorico, frigio, lidio, mixolidio etc.)
- Ritmo livre, baseado na prosódia do latim litúrgico
- Papa Gregório I (590-604): codificação do repertório — dai "gregoriano"
- Cantado em latim; função litúrgica (missa, ofício divino)

## Organum
- Primeira forma de polifonia escrita (séc. IX em diante)
- Adição de uma 2ª voz ao cantochão (em paralelo, obliqua ou livre)
- Escola de Notre-Dame (Paris, séc. XII-XIII): Léonin e Perotin
- Perotin: organa a 3 e 4 vozes (organum triplum e quadruplum)

## Troubadours e trovadores
- Poetas-musicos seculares (fora da Igreja) do sul da Franca (occitano) — séc. XII
- Trovadores ao norte (língua d'oil); Minnesanger na Alemanha
- Temas: amor cortês, guerra, natureza (chanson, canso, sirventes)
- Musica monofonica; transmissão oral

## Ars Nova (séc. XIV)
- Termo do teórico Philippe de Vitry (c. 1322)
- Novas possibilidades rítmicas: divisão binaria do tempo (antes: só ternario)
- Guillaume de Machaut: principal compositor; Missa de Nostre Dame (1ª missa polifônica completa)
- Contraponto mais elaborado; isorhythm (padrão rítmico repetido)

## Para a prova
- Cantochao = monofônico + modal + ritmo livre + latim + liturgico
- Ars Nova vs. Ars Antiqua: Ars Nova = novas liberdades rítmicas
- Machaut: primeiro compositor com obra completa identificada
- Léonin e Perotin: Escola de Notre-Dame (nao confundir com renascimento)""",
"versaoCompleta":"""# Historia da Musica: Periodo Medieval

## O Contexto Histórico

A Musica medieval abrange aproximadamente mil anos (500-1400 d.C.), um periodo dominado pela Igreja Católica, que controlava a produção cultural. A musica escrita preservada é predominantemente religiosa, embora houvesse rica tradição secular (trovadores) da qual sobreviveu muito menos.

## Cantochao (Canto Gregoriano)

O cantochao é o repertório litúrgico monofônico da Igreja Católica Ocidental. Suas características:
- **Monofonia**: uma única linha melódica, sem harmonia nem acompanhamento
- **Modos eclesiásticos**: oito modos (dorico, hipodorico, frigio, hipofrigio, lidio, hipolidio, mixolidio, hipomixolidio) — precursores das escalas maior e menor
- **Ritmo livre**: a duração das notas segue a prosódia natural do latim
- **Função litúrgica**: Missa e Ofício Divino (matinas, laudes, vésperas etc.)

A codificação atribuída ao Papa Gregório I é mais lenda do que história — o repertório foi sistematizado ao longo dos séculos VIII-IX.

## Desenvolvimento da Polifonia

O organum surgiu como prática improvisatória de adicionar uma segunda voz ao cantochao. A Escola de Notre-Dame (Paris, c. 1160-1250) sistematizou a polifonia com os mestres **Léonin** (Magnus Liber Organi, c. 1170) e **Perotin** (organa a 3 e 4 vozes). O desenvolvimento do ritmo mensural (duração das notas medida por modos rítmicos) foi fundamental.

## Musica Secular: Trovadores e Troveiros

Os trovadores (sul da Franca, língua d'oc) e troveiros (norte, língua d'oil) eram poetas-musicos que cultivavam a canção secular. Temas principais: **amor cortês** (fin'amor), cruzadas, canções de alba (amanhecer), pastourelle (encontro com pastora). O repertório sobreviveu em manuscritos com notação sem indicação rítmica — a reconstrução rítmica é objeto de debate.

## Ars Nova

No séc. XIV, Philippe de Vitry codificou as novas práticas em seu tratado "Ars Nova" (c. 1322). A principal inovação: a divisão **binaria** do tempo, além da ternaria (considerada "perfeita" por simbolismo religioso). Guillaume de Machaut (c. 1300-1377) é o mestre do período — sua **Missa de Nostre Dame** é a primeira missa polifônica completa por um único compositor."""})

NOVOS.append({"id":"r-hm-02","topico":"hm-02","disciplina":"historia-musica","bloco":"especificos",
"nome":"Renascimento: polifonia vocal, madrigal, Palestrina, escola veneziana","incidencia":"media",
"versaoCurta":"""# Historia da Musica: Renascimento (aprox. 1400-1600)

## Caracteristicas gerais
- Polifonia vocal a cappella (sem acompanhamento) como forma dominante
- Humanismo: o ser humano no centro; temas seculares ganham espaço
- Contraponto imitativo: vozes imitam umas as outras (cânone, fuga incipiente)
- Sistema modal em transição para o tonal

## Gêneros sagrados
- **Missa**: ciclo de texto ordinário em polifonia (Kyrie, Gloria, Credo, Sanctus, Agnus Dei)
- **Moteto**: composição polifônica sobre texto latino religioso

## Compositores principais
- **Guillaume Dufay** (c. 1397-1474): Borgonha/Flandres; transição Medieval-Renascimento
- **Josquin des Prez** (c. 1450-1521): o maior da época; motetos e missas; Flandres
- **Giovanni Pierluigi da Palestrina** (c. 1525-1594): Roma; Missa Papae Marcelli; refinamento do contraponto
- **Orlando di Lasso** (1532-1594): polilingue; secular e sacro

## Polifonia secular: o madrigal
- Composição polifônica italiana sobre texto vernáculo (italiano)
- Séc. XVI-XVII: Madrigal italiano como forma sofisticada
- **Text painting (madrigalismo)**: música imita o texto (ascende = melodia sobe)
- Monteverdi (final do séc. XVI) leva o madrigal ao seu ápice

## Escola Veneziana
- San Marco, Veneza: uso de múltiplos coros (coro spezzati)
- Giovanni Gabrieli: música policoral antifonal; dinâmicas indicadas
- Precursor do estilo barroco: contraste, drama, espacialidade

## Para a prova
- Palestrina: símbolo do contraponto vocal puro; usado como modelo até hoje
- Madrigalismo: identificar nas questões de "texto painting"
- Escola Veneziana: policoralidade + antifonia = característica distintiva
- Josquin: "o primeiro compositor moderno" (segundo críticos da época)""",
"versaoCompleta":"""# Historia da Musica: Renascimento

## O Contexto

O Renascimento musical (c. 1400-1600) acompanhou o Renascimento artístico e literário, com o humanismo revalorizando a cultura clássica e o ser humano como medida. Na musica, isso se refletiu no desenvolvimento da polifonia secular e na codificação do contraponto vocal.

## A Escola Franco-Flamenga

Os compositores mais influentes do século XV-XVI vieram da região entre a Franca e a Flandres (atual Belgica/norte da Franca/Luxemburgo). **Guillaume Dufay** sintetizou elementos medievais e renascentistas. **Johannes Ockeghem** desenvolveu o contraponto complexo. **Josquin des Prez** foi considerado pelos contemporâneos o maior compositor de seu tempo — sua musica combina maestria contrapuntística com expressividade humanista.

## Palestrina e o Ideal Contrapontístico

Giovanni Pierluigi da Palestrina (c. 1525-1594) trabalhou em Roma e criou o que se tornaria o modelo de contraponto "correto" para séculos seguintes. Suas características:
- Dissonâncias cuidadosamente preparadas e resolvidas
- Movimento melódico predominantemente conjunto (por graus)
- Ritmo equilibrado, sem acentuações bruscas
- Texto litúrgico tratado com clareza

Sua **Missa Papae Marcelli** (c. 1562) é frequentemente citada como exemplo do ideal contrapontístico tridentino.

## O Madrigal

O madrigal foi o principal gênero secular do Renascimento italiano. Distingue-se do cantochão e do moteto por:
- Texto em italiano vernáculo (não latim)
- Expressividade emocional intensa
- **Text painting (madrigalismo)**: a musica ilustra literalmente o texto — palavras como "subir", "cair", "chorar", "rir" são musicadas com gestos correspondentes (melodia ascendente, cromatismo, dissonâncias)

**Luca Marenzio** e **Don Carlo Gesualdo** levaram o madrigal ao extremo cromático. **Claudio Monteverdi** (Livros de Madrigais I-VIII) representa a transição para o Barroco.

## Escola Veneziana e a Polifonia Espacial

A Basílica de San Marco em Veneza, com suas galerias opostas, inspirou a prática dos **cori spezzati** (coros divididos). **Giovanni Gabrieli** compôs para dois, três e até quatro coros posicionados em espaços diferentes, criando efeitos antifônicos e dinâmicos. Ele foi um dos primeiros a indicar dinâmicas (piano/forte) em partituras."""})

NOVOS.append({"id":"r-hm-04","topico":"hm-04","disciplina":"historia-musica","bloco":"especificos",
"nome":"Classicismo: forma sonata, sinfonia, Haydn, Mozart, Beethoven","incidencia":"alta",
"versaoCurta":"""# Historia da Musica: Classicismo (aprox. 1750-1820)

## Caracteristicas gerais
- Clareza, equilíbrio e proporção (ideal iluminista)
- Textura homofônica predominante (melodia + acompanhamento) — contraste com polifonia barroca
- Sistema tonal consolidado (maior/menor)
- Desenvolvimento das formas instrumentais: sonata, sinfonia, concerto, quarteto de cordas

## Forma-sonata (forma allegro de sonata)
- Estrutura tripartite de um movimento:
  1. **Exposição**: Tema 1 (tônica) + transição + Tema 2 (dominante ou relativa) + fechamento
  2. **Desenvolvimento**: elaboração e modulação dos temas
  3. **Recapitulação**: retorno dos temas na tônica
- Usada em: 1º movimento de sinfonias, sonatas, quartetos, concertos

## A triade classica
- **Joseph Haydn** (1732-1809): "pai da sinfonia e do quarteto"; 104 sinfonias; Criação, Estações
- **Wolfgang Amadeus Mozart** (1756-1791): opere (Nozze di Figaro, Don Giovanni, Flauta Mágica); sinfonias; concertos; Requiem
- **Ludwig van Beethoven** (1770-1827): transição classicismo-romantismo; 9 sinfonias; sonatas para piano (Patética, Lua de Sonata, Appassionata)

## Gêneros classicos
- **Sinfonia**: obra orquestral em 4 movimentos (rápido-lento-minueto-rápido)
- **Sonata**: obra para instrumento solo (ou duo) em 2-4 movimentos
- **Quarteto de cordas**: 2 violinos + viola + cello; música de câmara por excelência
- **Concerto**: solista + orquestra; 3 movimentos

## Para a prova
- Forma-sonata: EXPOSIÇÃO + DESENVOLVIMENTO + RECAPITULAÇÃO (saber os 3 momentos)
- Haydn = pai da sinfonia; Mozart = genio precoce; Beethoven = ponte Classicismo-Romantismo
- 9ª Sinfonia de Beethoven: primeira a usar coro/vozes na sinfonia ("Ode à Alegria")
- Período de Viena: os três grandes viveram em Viena (Escola de Viena Classica)""",
"versaoCompleta":"""# Historia da Musica: Classicismo

## Contexto Histórico

O Classicismo musical (c. 1750-1820) coincide com o Iluminismo europeu — o pensamento racional e a crença no progresso da humanidade pela razão. Na arte, isso se refletiu na busca por clareza, proporção e equilíbrio, em contraste com o ornamento exuberante do Barroco.

## A Questão do "Estilo Galante"

A transição do Barroco para o Classicismo passou pelo **estilo galante** (c. 1720-1760) — música mais leve, ornamental e voltada ao entretenimento, em contraste com a profundidade do contraponto bachiano. **Carl Philipp Emanuel Bach** (filho de J.S. Bach) foi figura central nessa transição.

## Forma-Sonata

A forma-sonata é a mais importante inovação estrutural do Classicismo. Ela não é apenas uma "forma" — é um princípio dinâmico de oposição, desenvolvimento e resolução de tensões tonais.

**Exposição**: apresenta dois temas em tensão tonal — Tema 1 na tônica (estabilidade) e Tema 2 na dominante (tensão). A finalidade é criar expectativa.

**Desenvolvimento**: os temas são fragmentados, combinados e modulam por tonalidades distantes, criando instabilidade máxima.

**Recapitulação**: os temas retornam, mas agora AMBOS na tônica — a tensão tonal é resolvida. Frequentemente seguida de uma coda conclusiva.

## Os Grandes Mestres

**Joseph Haydn** foi o arquiteto das formas clássicas. Suas 104 sinfonias desenvolveram progressivamente a orquestra e a forma. Seus quartetos de cordas (68 no total) estabeleceram o padrão do gênero.

**Mozart** foi o sintetizador universal — suas óperas, sinfonias, concertos e música de câmara representam o ideal clássico em seus melhores momentos. O Concerto para Piano K. 467, a Sinfonia "Jupiter" (nº 41) e "A Flauta Mágica" são obras-primas.

**Beethoven** expandiu todas as formas clássicas ao extremo. Sua 9ª Sinfonia (1824, composta já surdo) introduziu o coro e solistas na sinfonia com o texto da "Ode à Alegria" de Schiller."""})

NOVOS.append({"id":"r-hm-05","topico":"hm-05","disciplina":"historia-musica","bloco":"especificos",
"nome":"Romantismo: piano, lied, musica programatica, Wagner, Brahms","incidencia":"alta",
"versaoCurta":"""# Historia da Musica: Romantismo (aprox. 1820-1900)

## Caracteristicas gerais
- Expressão das emoções individuais; subjetividade; nacionalismo
- Expansão da orquestra (mais instrumentos, mais volume)
- Cromatismo harmônico crescente (Wagner: tonalidade suspensa)
- Virtuosismo instrumental (Paganini, Liszt)
- Música programática: musica descreve uma história/imagem extramusicual

## Piano no Romantismo
- Instrumento central do século XIX; desenvolvimento tecnológico (pedais, alcance)
- **Frédéric Chopin** (1810-1849): nocturnes, estudos, baladas, mazurcas, valsas
- **Franz Liszt** (1811-1886): poema sinfônico (piano → orquestra); virtuosismo extremo
- **Robert Schumann** (1810-1856): ciclos para piano (Carnaval, Kreisleriana); crítico musical

## Lied (pl. Lieder)
- Canção para voz e piano em alemão; forma típica do Romantismo
- **Franz Schubert** (1797-1828): 600+ Lieder; "Erlkönig", "Ave Maria", "Die Winterreise"
- Melodia + piano expressivo + poesia de qualidade (Goethe, Schiller)
- Ciclos de Lieder: "A Bela Moleira" e "A Viagem de Inverno" (Schubert)

## Musica Programática
- Musica instrumental que descreve narrativa, imagem ou programa extramusical
- **Hector Berlioz**: Sinfonia Fantastica (programa autobiografico)
- **Richard Strauss**: poemas sinfônicos (Don Quixote, Till Eulenspiegel)
- **Franz Liszt**: criou o "poema sinfônico" como gênero

## Wagner e o drama musical
- **Richard Wagner** (1813-1883): ópera reformada = "drama musical" (Gesamtkunstwerk)
- Leitmotiv: tema musical associado a personagem/ideia
- Cromatismo extremo: Tristan und Isolde (1865) = crise do sistema tonal
- Operas: Anel dos Nibelungos (ciclo de 4), Parsifal, Tristão e Isolda

## Para a prova
- Schubert = lied | Chopin = piano noturno/étude | Liszt = poema sinfônico | Berlioz = sinfonia programática
- Wagner: leitmotiv + Gesamtkunstwerk + cromatismo tonal extremo
- Romantismo = expressão subjetiva + expansão orquestral + nacionalismo
- Brahms: "classicismo romantic" — formas clássicas + linguagem romantica""",
"versaoCompleta":"""# Historia da Musica: Romantismo

## Contexto

O Romantismo musical (c. 1820-1900) surge em paralelo ao Romantismo literário e filosófico — a reação ao racionalismo iluminista com a valorização do sentimento, da natureza, do individual e do nacional. Na musica, isso se traduziu em expansão expressiva, de formas e de recursos orquestrais.

## O Piano como Instrumento do Século

O piano moderno, aperfeiçoado ao longo do séc. XIX, tornou-se o instrumento doméstico por excelência e o veículo da música romântica. Frédéric **Chopin** explorou as possibilidades líricas e técnicas do instrumento com seus nocturnos, estudos e prelúdios. Franz **Liszt** empurrou o virtuosismo ao limite e criou o "recital" como evento público.

## O Lied: Poesia e Música Fundidas

O Lied romântico alemão representa a síntese de música e poesia. Franz **Schubert** escreveu mais de 600 Lieder, muitos sobre poemas de Goethe e Schiller. A relação entre voz e piano é de parceria — o piano não acompanha apenas, mas comenta, antecipa e reage ao texto. Robert **Schumann** e Johannes **Brahms** também cultivaram o gênero.

## Música Programática

A musica programática é instrumental mas conta uma história ou descreve uma imagem. Hector **Berlioz** escreveu a "Sinfonia Fantástica" (1830) com um programa autobiografico explícito, com leitmotiv (idée fixe) da amada. Franz **Liszt** inventou o "poema sinfônico" — peça orquestral única em movimento baseada em programa literário ou pictórico.

## Wagner e a Crise da Tonalidade

Richard Wagner reformulou a ópera em "drama musical" (Musikdrama). Seu conceito de **Gesamtkunstwerk** (obra de arte total) visava fundir música, teatro, poesia, cenografia e dança em unidade. O **leitmotiv** (tema conductor) identificava personagens e ideias ao longo de operas enormes.

O cromatismo do prelúdio de "Tristão e Isolda" (1865) é considerado o ponto de ruptura da tonalidade funcional — a resolução é perpetuamente adiada. Esse "Tristão" abriu caminho para o atonalismo do séc. XX."""})

NOVOS.append({"id":"r-hm-06","topico":"hm-06","disciplina":"historia-musica","bloco":"especificos",
"nome":"Modernismo e vanguardas do seculo XX: impressionismo, expressionismo, neoclassicismo","incidencia":"media",
"versaoCurta":"""# Modernismo Musical (aprox. 1890-1945)

## Impressionismo
- **Claude Debussy** (1862-1918): recusa o rigor formal germanico; busca sonoridade, timbre, atmosfera
- Harmonias paralelas (quintas, acordes de nona); modalismo; escala de tons inteiros; pentatônica
- Obras: Prelúdio à Tarde de um Fauno, La Mer, Imagens, Préluds (piano)
- "Impressionismo" foi termo crítico (como para pintura); o próprio Debussy preferia "simbolismo"
- Maurice **Ravel**: próximo de Debussy; Bolero, Daphnis et Chloé; mais precisão formal

## Expressionismo
- Expressão da angustia interior; recusa do belo convencional
- **Arnold Schoenberg** (fase atonal livre): Pierrot Lunaire, Cinco Peças para Orquestra
- Sprechstimme (fala cantada): entre a declamação e o canto
- Contexto: Viena do início do séc. XX; influência da psicanálise

## Neoclassicismo
- Reação aos excessos romanticos; retorno a formas e procedimentos do passado
- **Igor Stravinsky**: Pulcinella (1920) = primeiro neoclassico; Sinfonia de Psalmos
- Objetividade, clareza, ironia
- Paul **Hindemith**: "Gebrauchsmusik" (musica utilitária); polissonal mas tonal

## Nacionalismo musical
- Compositores exploram folclore nacional como material
- Bartók (Hungria): pesquisa de campo; integração do folclore na linguagem contemporânea
- Villa-Lobos (Brasil): choros, Bachianas Brasileiras

## Para a prova
- Debussy = impressionismo = escalas paralelas + tons inteiros + modalismo
- Schoenberg = expressionismo (fase atonal) → dodecafonismo
- Stravinsky = fase russa (Sagração da Primavera) + neoclassicismo + serialismo
- Bartók = folclore + modalismo + polirritmia
- "A Sagração da Primavera" (Stravinsky, 1913) = escandalo histórico na estreia em Paris""",
"versaoCompleta":"""# Modernismo Musical: Impressionismo, Expressionismo e Neoclassicismo

## O Contexto do Modernismo

O final do séc. XIX e início do séc. XX marcaram a crise e dissolução do sistema tonal herdado do Barroco. As soluções propostas pelos compositores foram diversas e frequentemente opostas entre si — daí a fragmentação em "ismos" que caracteriza o período.

## Impressionismo

Claude Debussy redefine o projeto musical: em vez de narrativa dramática ou tensão formal, busca **atmosfera**, **timbre** e **instantâneo sonoro**. Seus recursos:
- Acordes paralelos sem resolução funcional
- Escalas de tons inteiros (6 notas equidistantes: dó-ré-mi-fá#-sol#-lá#)
- Modalismo; pentatônica
- Orquestração de câmara; timbres incomuns
- Estrutura fluida, sem desenvolvimento dramático claro

Maurice Ravel compartilha alguns procedimentos de Debussy mas mantém maior precisão formal e brilho técnico — o Bolero é o exemplo extremo de sua obsessão pela forma.

## Expressionismo

O expressionismo musical vienense rejeita tanto o Romantismo tardio quanto o Impressionismo. Quer expressar o mundo interior em sua crueza: angústia, fragmentação, inconsciente. Arnold Schoenberg (fase atonal livre, c. 1908-1923) abandona completamente a hierarquia tonal. Obras como "Pierrot Lunaire" (1912) utilizam o Sprechstimme — técnica vocal entre fala e canto.

## Neoclassicismo

Igor Stravinsky, após a fase folclórica russa ("Firebird", "Petruschka", "A Sagração da Primavera"), voltou-se para formas e procedimentos do passado com olhos irônicos — Neoclassicismo. "Pulcinella" (1920, baseado em Pergolesi) inaugurou a fase. O Neoclassicismo valoriza clareza estrutural, objetividade e distância emocional.

## Bartók e o Folclore como Modernismo

Béla Bartók (1881-1945) realizou pesquisa sistemática de campo coletando musicas folclóricas húngaras, romenas e búlgaras. Integrou escalas modais, ritmos irregulares e melodias folclóricas em uma linguagem harmonicamente avançada. Seus Quartetos de Cordas (6) são considerados as obras-primas do séc. XX nesse gênero."""})

NOVOS.append({"id":"r-hm-07","topico":"hm-07","disciplina":"historia-musica","bloco":"especificos",
"nome":"Dodecafonismo e serialismo: Schoenberg, Berg, Webern","incidencia":"media",
"versaoCurta":"""# Dodecafonismo e Serialismo

## Dodecafonismo (12 tons)
- Técnica criada por **Arnold Schoenberg** (1923) para organizar a atonalidade
- Série de 12 notas: usa-se cada uma das 12 notas da escala cromática exatamente uma vez antes de repetir
- A série pode ser apresentada em 4 formas: Original (O), Retrogrado (R), Inversao (I), Inversao Retrograda (RI)
- Objetivo: democracia entre os 12 sons (nenhum privilegiado como tônica)
- Primeiras obras: Suite para Piano op. 25; Quintet de Sopros

## A Segunda Escola de Viena
- **Schoenberg** + alunos diretos = Segunda Escola de Viena
- **Alban Berg** (1885-1935): dodecafonismo expressivo e comunicativo; Wozzeck (ópera, 1925); Concerto para Violino
- **Anton Webern** (1883-1945): radicalização; obras miniaturais; pontilhismo (pontos sonoros isolados)

## Serialismo Integral (pos-guerra)
- Pos-1945: serialismo não é apenas das alturas mas de TODOS os parâmetros
- Ritmo, dinâmica, articulação, timbre também serializados
- **Olivier Messiaen**: "Modos de Valores e Intensidades" (1949) — precursor
- **Pierre Boulez** e **Karlheinz Stockhausen**: serialismo total

## Para a prova
- Dodecafonismo = séries de 12 sons; Schoenberg criou em 1923
- Berg = dodecafonismo expressivo (emocional); Webern = pontilhismo (minimalismo sonoro)
- Serie: forma O, R, I, RI
- Serialismo integral = parâmetros totais; pós-Segunda Guerra
- Escola Serialista ≠ Musica Serial: serialismo abrange mais do que o dodecafonismo""",
"versaoCompleta":"""# Dodecafonismo e Serialismo

## A Crise da Tonalidade e a Solução Dodecafônica

Depois de uma fase de atonalidade livre (c. 1908-1923), Schoenberg precisou de um princípio organizador alternativo à tonalidade. O **dodecafonismo** (também chamado de método dos doze tons ou serialismo de alturas) foi a resposta: uma série (Reihe) de 12 notas, cada uma aparecendo exatamente uma vez, antes de qualquer repetição.

## A Série e suas Transformações

A série é a base de composição. Ela pode ser usada em quatro formas:
- **Original (O ou P)**: a série na ordem original
- **Retrogrado (R)**: a série de trás para frente
- **Inversão (I)**: os intervalos espelhados (o que era ascendente torna-se descendente)
- **Inversão Retrograda (IR)**: inversão + retrogrado

Cada uma dessas formas pode começar em qualquer das 12 notas, gerando 48 formas possíveis da série. O compositor organiza a harmonia e a melodia combinando essas formas.

## Berg, Webern e as Diferentes Direções

Os três membros da Segunda Escola de Viena usaram o dodecafonismo de maneiras muito diferentes:

**Berg** manteve vínculos com a expressividade romântica. "Wozzeck" (1925) é uma ópera sobre um soldado maltratado — angustiada, comunicativa, extremamente dramática. "Lulu" e o Concerto para Violino são obras igualmente expressivas dentro da técnica dodecafônica.

**Webern** levou o dodecafonismo à máxima concentração. Suas obras são brevíssimas — a Sinfonia Op. 21 dura menos de 10 minutos. O **pontilhismo** (sons isolados, amplamente espaçados) e a extrema rarefação são suas marcas. Após 1945, Webern tornou-se modelo para os compositores do serialismo integral.

## Serialismo Integral

Após a Segunda Guerra, compositores como Boulez e Stockhausen estenderam o princípio serial a todos os parâmetros sonoros: não apenas alturas, mas também ritmos, dinâmicas, articulações e timbres são organizados serialmente. Isso levou à extrema complexidade e ao debate sobre a percepção musical dessa música."""})

NOVOS.append({"id":"r-hm-08","topico":"hm-08","disciplina":"historia-musica","bloco":"especificos",
"nome":"Musica eletrônica: Pierre Schaeffer, musica concreta, Stockhausen","incidencia":"media",
"versaoCurta":"""# Musica Eletrônica e Eletroacústica

## Musica Concreta (a partir de 1948)
- **Pierre Schaeffer** (Paris, 1948): trabalha com sons gravados em fita magnética
- Sons concretos: sons do mundo real (nao sintetizados) manipulados no estúdio
- Acousmatic: musica para ser ouvida sem ver a fonte sonora
- Técnicas: loop, reverso, filtro, transposição de velocidade
- **Étude aux chemins de fer** (1948): sons de trem — primeiro trabalho de musica concreta

## Musica Eletrônica (sintese)
- Gerada por osciladores elétricos; nao parte de sons gravados
- **Studio für elektronische Musik** (Colônia, WDR, 1951): Stockhausen, Beyer
- **Karlheinz Stockhausen**: Studie I e II (1953-54); Gesang der Jünglinge (1956) — combina voz e sintese
- Europa vs. Paris: musica concreta (sons reais) vs. musica eletrônica (sintese pura)

## Musica Eletroacústica
- Fusão de sons concretos e eletrônicos
- Termo mais abrangente usado hoje
- Live electronics: processamento em tempo real no palco

## Instrumentos e tecnologias
- **Theremin** (Lev Theremin, 1920): primeiro instrumento eletrônico de palco
- **Ondas Martenot** (Maurice Martenot, 1928): teclado com glissando contínuo
- **Sintetizador Moog** (Robert Moog, 1964): popularizou a sintese subtrativa
- DAW (Digital Audio Workstation): produção musical digital atual

## Musica Eletroacústica Brasileira
- **Jorge Antunes**: pioneiro brasileiro em musica eletroacústica
- Centro de Musica Eletrônica da UnB

## Para a prova
- Schaeffer = musica concreta = sons reais gravados manipulados
- Stockhausen = musica eletrônica de sintese + serialismo
- Musica concreta: objeto sonoro + acousmatica
- Diferença: concreta (sons reais) vs. eletrônica pura (sintetizadores)
- Eletroacústica = termo que abrange ambas""",
"versaoCompleta":"""# Musica Eletrônica e Eletroacústica

## O Surgimento da Musica Concreta

Pierre Schaeffer, engenheiro de som da Radio Diffusion Française (RDF) em Paris, criou em 1948 o que chamou de **musica concreta** — musica composta diretamente com sons gravados ("sons concretos"), em oposição à musica abstrata escrita em partitura e depois realizada por instrumentistas.

Usando toca-discos e fita magnética, Schaeffer manipulava sons do mundo real (trens, sinos, instrumentos, vozes) por meio de: looping, reprodução reversa, transposição de velocidade, filtros, mixagem. A **Étude aux chemins de fer** (1948), composta com sons de locomotivas, é considerada a primeira obra de musica concreta.

O conceito de **objeto sonoro** (objet sonore) é central: qualquer som pode ser material musical se ouvido fora de seu contexto original, apenas em suas qualidades acústicas.

## Musica Eletrônica de Síntese

Em Colônia, o WDR (emissora pública alemã) criou o **Studio für elektronische Musik** em 1951. Aqui, a abordagem era oposta: criar sons inteiramente por meios eletrônicos (osciladores, geradores de ruído), sem recorrer a sons do mundo real. Stockhausen foi a figura central: suas "Studien" I e II (1953-54) são trabalhos de síntese pura.

O **Gesang der Jünglinge** (1956) de Stockhausen foi um marco: combinou voz (som concreto) com sons sintetizados, criando a primeira grande obra eletroacústica.

## Eletroacústica Contemporânea

Hoje, a distinção entre concreta e eletrônica praticamente desapareceu. "Música eletroacústica" é o termo amplo que abrange toda musica que usa eletricidade como meio de produção/transformação sonora. Live electronics (processamento em tempo real), síntese granular, laptop ensembles e performance com sensores são práticas atuais.

## Brasil

Jorge Antunes foi pioneiro da eletroacústica brasileira, com estudos no exterior e fundação do Centro de Musica Eletrônica da UnB nos anos 1970. O acervo de musica eletroacústica brasileira é rico e pouco divulgado."""})

NOVOS.append({"id":"r-hm-09","topico":"hm-09","disciplina":"historia-musica","bloco":"especificos",
"nome":"Musica contemporânea: minimalismo, musica aleatoria, John Cage","incidencia":"media",
"versaoCurta":"""# Musica Contemporânea: Minimalismo e Musica Aleatória

## John Cage e a Musica Aleatória
- **John Cage** (1912-1992): compositor americano; filosofia Zen; Escola de Nova York
- **4'33"** (1952): obra sem notas intencionais; performer senta ao piano sem tocar; o ambiente é a musica
- **Musica de acaso (chance music/aleatória)**: elementos determinados pelo acaso (dados, moedas, I Ching)
- Prepared piano: inserção de objetos (parafusos, borrachas) entre as cordas
- Coage: "Tudo que precisamos é prestar atenção; o mundo é incrivelmente belo"
- Influencia: Koellreutter (improv), Fluxus, arte conceitual

## Minimalismo
- Surgido nos EUA nos anos 1960-70
- Uso de materiais musicais mínimos; repetição e transformação gradual lenta
- Principais compositores:
  - **Terry Riley**: "In C" (1964) — 53 motivos repetidos à vontade pelos performers
  - **Steve Reich**: "Piano Phase", "Music for 18 Musicians"; phase shifting (desalinhamento progressivo)
  - **Philip Glass**: óperas minimalistas (Einstein on the Beach, Satyagraha); trilhas sonoras
  - **Arvo Pärt** (Estônia): tintinnabuli — harmonias simples + melodia diatônica; espiritualidade

## Espectralismo
- **Gérard Grisey** e **Tristan Murail** (França, anos 1970)
- Composição baseada na análise dos harmônicos do som
- A partitura deriva de espectrogramas de sons naturais

## Musica Pós-Moderna
- Colagem, intertextualidade, ironia
- **Alfred Schnittke**: policalifonia (citações de diferentes estilos)

## Para a prova
- Cage = 4'33" = silêncio como musica; acaso; Zen
- Minimalismo = repetição gradual; Terry Riley + Steve Reich + Philip Glass
- Fase de fase (phase shifting) = Steve Reich
- Tintinnabuli = Arvo Pärt
- "In C" = primeira obra minimalista canônica (1964)""",
"versaoCompleta":"""# Musica Contemporânea: Minimalismo e Musica Aleatória

## John Cage e a Redefiniçao da Musica

John Cage é a figura mais radical da musica do séc. XX. Influenciado pela filosofia Zen budista e pelo pensamento de Daisetz Suzuki, Cage questionou as premissas fundamentais da musica ocidental: o que é som? O que é silêncio? Quem decide o que é musica?

**4'33"** (1952) é sua obra mais famosa — e mais mal compreendida. O performer senta ao instrumento e não toca por exatamente quatro minutos e trinta e três segundos. O ponto não é o silêncio, mas a escuta do ambiente: tosse, respiração, chuva, carros — tudo isso É a musica. A obra força o ouvinte a prestar atenção ao que sempre ignorou.

O **prepared piano** alterou fisicamente o instrumento inserindo parafusos, borrachas e outros objetos entre as cordas, criando sons percussivos e incomuns. Sonatas e Entrelúdios (1946-48) é a principal obra para esse instrumento.

## Minimalismo: Repetição como Processo

O minimalismo surgiu como reação ao serialismo integral (complexo, cerebral, inacessível). Os minimalistas voltaram a harmonias simples e ritmos regulares, mas transformaram esse material lentamente.

**Terry Riley** em "In C" (1964) criou uma obra processual: 53 figuras musicais, tocadas em qualquer ordem e repetidas à vontade por qualquer número de performers. Cada execução é diferente.

**Steve Reich** desenvolveu o **phase shifting**: dois ou mais performers tocam o mesmo padrão, mas um vai gradualmente desalinhando do outro. Em "Piano Phase" (1967), dois pianistas tocam a mesma figura até que a diferença de meio tempo cria polirritmia.

**Philip Glass** desenvolveu progressões harmônicas repetidas com figuras em arpejo de rapidez crescente. Suas óperas colaborativas com Robert Wilson ("Einstein on the Beach", 1976) inauguraram um novo teatro musical.

**Arvo Pärt** criou o estilo **tintinnabuli** (sino): uma voz melódica diatônica + uma voz de arpejo que toca apenas as notas da tríade. Simplicidade espiritual como linguagem contemporânea."""})

# ── Teoria Musical ───────────────────────────────────────────

NOVOS.append({"id":"r-tm-01","topico":"tm-01","disciplina":"teoria-musical","bloco":"especificos",
"nome":"Elementos musicais: altura, duração, intensidade, timbre","incidencia":"alta",
"versaoCurta":"""# Elementos Musicais (Parâmetros do Som)

## Os 4 parâmetros básicos
| Parâmetro | Definicao | Notacao |
|---|---|---|
| **Altura** | Frequência de vibração (grave-agudo) | Posicao na pauta (notas) |
| **Duração** | Tempo de sustentação do som | Figuras rítmicas |
| **Intensidade** | Amplitude de vibração (fraco-forte) | p, mp, mf, f, ff |
| **Timbre** | Qualidade que diferencia fontes sonoras | Indicacao de instrumento |

## Altura
- Determinada pela **frequência** (Hz): mais vibrações = mais agudo
- **Nota La** = 440 Hz (afinação padrão)
- Oitavas: dobrar a frequência sobe uma oitava (440 Hz → 880 Hz)
- Nomes das notas: Do, Re, Mi, Fa, Sol, La, Si (sistema latino) / C, D, E, F, G, A, B (sistema americano)

## Duração
- **Pulso**: batida regular (referência de tempo)
- **Compasso**: agrupamento regular de pulsos (2/4, 3/4, 4/4, 6/8)
- **Ritmo**: padrão de durações (independe do pulso)
- **Andamento**: velocidade do pulso (Adagio, Andante, Moderato, Allegro, Presto)

## Intensidade
- **Dinâmicas** italianas: pp (pianíssimo), p (piano), mp, mf, f (forte), ff (fortíssimo)
- **Crescendo** (crescendo): aumento gradual
- **Decrescendo/diminuendo**: diminuição gradual

## Timbre
- Cada instrumento/voz tem timbre único (mesmo La 440 Hz soa diferente em flauta e violino)
- Determinado pela série harmônica (harmônicos presentes no som)
- Tessitura: extensão de alturas de um instrumento/voz

## Para a prova
- Altura = frequência = grave/agudo = posicao na pauta
- Intensidade = amplitude = fraco/forte = dinâmicas
- Timbre = qualidade sonora = harmônicos = identidade do instrumento
- Duração = figuras (semibreve, mínima, semínima, colcheia, semicolcheia)""",
"versaoCompleta":"""# Elementos Musicais: Parâmetros do Som

## Fundamentos Acústicos

O som é produzido por vibrações que se propagam em ondas pelo ar. Os parâmetros sonoros correspondem às características físicas dessas ondas:

**Frequência** (ciclos por segundo = Hz) determina a **altura**: quanto mais rápida a vibração, mais agudo o som. A nota La4 (La central) convencionalmente vibra a 440 Hz. Uma oitava acima (La5) = 880 Hz; uma oitava abaixo (La3) = 220 Hz. A relação é sempre de dobro/metade.

**Amplitude** (intensidade da vibração) determina o **volume** (intensidade musical): maior amplitude = maior volume.

**Forma de onda** e **série harmônica** determinam o **timbre**: quando um instrumento toca uma nota, além da frequência fundamental soam também os harmônicos (múltiplos da fundamental) em intensidades variadas. A proporção entre esses harmônicos é o que diferencia o som de um oboé do som de um clarinete na mesma nota.

**Duração** corresponde ao tempo que a vibração se sustenta.

## Altura na Música

A notação ocidental usa uma pauta de 5 linhas para representar altura. A posicao da nota na pauta (na linha ou no espaco) indica a altura. As claves (sol, fá, dó) definem a referência de qual nota fica em qual posicao.

Notas cromáticas (fora das 7 diatônicas) são representadas com alteracoes: sustenido (#) eleva meio tom; bemol (b) abaixa meio tom; bequadro cancela alteracao.

## Duração e Ritmo

As figuras rítmicas representam durações relativas (não absolutas — dependem do andamento):
- Semibreve = 4 tempos (na fórmula 4/4)
- Mínima = 2 tempos
- Semínima = 1 tempo (figura de referência mais comum)
- Colcheia = 1/2 tempo
- Semicolcheia = 1/4 tempo

O **compasso** agrupa pulsos em unidades regulares. Compasso simples (2/4, 3/4, 4/4): divisão binária do pulso. Compasso composto (6/8, 9/8, 12/8): divisão ternária do pulso."""})

NOVOS.append({"id":"r-tm-02","topico":"tm-02","disciplina":"teoria-musical","bloco":"especificos",
"nome":"Leitura e escrita musical (notacão tradicional)","incidencia":"alta",
"versaoCurta":"""# Notação Musical Tradicional

## A Pauta
- 5 linhas + 4 espaços (+ linhas adicionais acima/abaixo)
- Linhas numeradas de baixo para cima: 1ª, 2ª, 3ª, 4ª, 5ª
- Notas nas linhas ou nos espacos; linhas adicionais para extensao

## Claves
| Clave | Nota de referência | Uso |
|---|---|---|
| **Sol** (2ª linha) | Sol4 na 2ª linha | Violino, flauta, piano (clave aguda) |
| **Fá** (4ª linha) | Fá3 na 4ª linha | Cello, baixo, tuba, piano (baixo) |
| **Dó** (3ª linha) | Dó4 na 3ª linha | Viola (clave de viola) |
| **Dó** (4ª linha) | Dó4 na 4ª linha | Fagote, trombone tenor |

## Figuras rítmicas e pausas
| Figura | Duração (em 4/4) | Pausa |
|---|---|---|
| Semibreve ○ | 4 tempos | ▬ suspensa |
| Mínima ♩ (branca) | 2 tempos | ▬ apoiada |
| Semínima ♩ (negra) | 1 tempo | ♩ |
| Colcheia ♪ | 1/2 tempo | ♩ |
| Semicolcheia | 1/4 tempo | ♩ |

## Fórmula de compasso (fórmula de tempo)
- Numerador: quantos pulsos por compasso
- Denominador: qual figura vale 1 pulso (4 = semínima, 8 = colcheia)
- Exemplos: 2/4 (dois pulsos de semínima), 3/4 (três), 4/4 (quatro), 6/8 (seis colcheias = 2 grupos de 3)

## Alteracoes
- **Sustenido (#)**: eleva meio tom
- **Bemol (b)**: abaixa meio tom
- **Bequadro**: cancela alteracao
- **Armadura de clave**: alteracoes no início da pauta valendo para toda a peça

## Sinais de expressao
- **Ligadura de valor**: une duas notas de mesma altura (não toca de novo)
- **Ligadura de frase**: agrupa notas de alturas diferentes (legato)
- **Staccato**: ponto sobre a nota (som curto destacado)
- **Ponto de aumento**: aumenta 50% o valor da figura

## Para a prova
- Clave de Sol: 2ª linha = Sol4 (referência)
- Saber ler as notas nas 5 linhas + 4 espacos em clave de sol
- Compasso 6/8: COMPOSTO binário (2 tempos, cada um dividido em 3 colcheias)
- Ponto de aumento: semínima pontuada = 1 tempo e meio""",
"versaoCompleta":"""# Leitura e Escrita Musical: Notação Tradicional

## O Sistema de Notação Ocidental

O sistema de notação musical ocidental desenvolveu-se ao longo de séculos, com raízes no neumas do cantochao medieval e consolidação no Renascimento. É um sistema de notação aproximada: indica com precisão alturas e durações relativas, mas deixa muitos aspectos expressivos à interpretação do performer.

## A Pauta e as Claves

A pauta de 5 linhas é o suporte visual da notação. A clave, colocada no início da pauta, estabelece a referência:

**Clave de Sol** (a mais comum): o sinal da clave envolve a 2ª linha, indicando que aquela linha é Sol4. Lendo de baixo para cima, as linhas são: Mi4, Sol4, Si4, Re5, Fa5. Os espaços: Fa4, La4, Do5, Mi5.

**Clave de Fá**: o sinal indica Fá3 na 4ª linha. Usada para instrumentos graves.

## Figuras Rítmicas e o Pulso

As figuras rítmicas são proporcionais entre si. A semínima (negra) vale metade da mínima (branca), que vale metade da semibreve. A relação é sempre 2:1 (exceto nas pontuadas, que valem 3:2).

O ponto de aumento depois de uma figura adiciona metade do valor dela:
- Semínima pontuada = 1 + 1/2 = 1,5 tempos
- Mínima pontuada = 2 + 1 = 3 tempos
- Colcheia pontuada = 1/2 + 1/4 = 3/4 de tempo

## Compassos Simples e Compostos

**Compassos simples**: pulso divisível em 2 partes iguais. Fórmulas: 2/4, 3/4, 4/4, 2/2.
**Compassos compostos**: pulso divisível em 3 partes iguais. Fórmulas: 6/8, 9/8, 12/8.

Em 6/8: há 6 colcheias por compasso, agrupadas em 2 grupos de 3. O pulso real é a colcheia pontuada (= 3 colcheias). Portanto, 6/8 tem DOIS pulsos compostos por compasso — é binário composto, não seisavos literais.

## Armadura de Clave

As alterações (sustenidos ou bemóis) colocadas na armadura de clave valem para todas as notas daquele grau ao longo da peça, exceto quando canceladas por bequadro. A quantidade e tipo de alterações na armadura indica a tonalidade."""})

NOVOS.append({"id":"r-tm-03","topico":"tm-03","disciplina":"teoria-musical","bloco":"especificos",
"nome":"Escalas maiores, menores e modais","incidencia":"alta",
"versaoCurta":"""# Escalas Maiores, Menores e Modais

## Escala Maior
- Padrão de tons e semitons: **T-T-St-T-T-T-St** (Tom-Tom-Semitom-Tom-Tom-Tom-Semitom)
- Som "alegre", "brilhante" (convencionalmente)
- Exemplo: Dó Maior = Dó-Ré-Mi-Fá-Sol-Lá-Si-Dó (sem alteracoes)

## Escala Menor (3 tipos)
- **Menor natural**: **T-St-T-T-St-T-T** (La natural: La-Si-Dó-Ré-Mi-Fá-Sol-La)
- **Menor harmônica**: 7º grau elevado (Sol# em La menor) → 1,5 tom entre 6º e 7º
- **Menor melódica**: subindo = 6º e 7º elevados; descendo = igual à menor natural

## Tonalidade e Armadura
- Tonalidade = note central (tônica) + modo (maior ou menor)
- **Círculo de quintas**: relação entre tonalidades e armaduras
- Quintas ascendentes adicionam sustenidos: Dó → Sol(1#) → Ré(2#) → La(3#) → Mi(4#) → Si(5#)
- Quintas descendentes adicionam bemóis: Dó → Fá(1b) → Sib(2b) → Mib(3b) → Lab(4b)
- Relativas: maior e menor que compartilham a mesma armadura (Dó Maior / La menor)

## Modos Eclesiásticos (Gregos)
A escala diatônica de 7 notas, começando em cada grau diferente:
- **Jônio**: = Maior (I grau)
- **Dórico**: menor c/ 6º maior (II grau) — soa jazzístico
- **Frígio**: menor c/ 2º menor (III grau) — soa espanhol/flamencó
- **Lídio**: maior c/ 4º aumentado (IV grau)
- **Mixolídio**: maior c/ 7º menor (V grau) — muito no rock e blues
- **Eólio**: = Menor Natural (VI grau)
- **Lócrio**: diminuto (VII grau) — instável, raro em tônica

## Para a prova
- Escala Maior: T-T-St-T-T-T-St — decorar!
- Menor harmônica: 7º grau aumentado (cria sensível)
- Relativas: mesma armadura, tônicas diferentes (ex.: Dó M / La m)
- Dórico = segunda escala do jazz; Mixolídio = rock/blues
- Pentatônica maior = Do-Re-Mi-Sol-La (5 notas, sem semitons)""",
"versaoCompleta":"""# Escalas Maiores, Menores e Modais

## Fundamentos: Tom e Semitom

O sistema tonal ocidental usa a **escala cromática** de 12 semitons como conjunto total de alturas. De qualquer nota para a vizinha imediata (no piano: de uma tecla para a próxima, seja branca ou preta) é um **semitom**. Dois semitons formam um **tom**.

As escalas diatônicas selecionam 7 dessas 12 notas segundo um padrão específico de tons e semitons.

## Escala Maior

O padrão T-T-St-T-T-T-St é invariável para qualquer escala maior. Em Dó Maior: Dó-Ré-Mi-Fá-Sol-Lá-Si. Não há alterações porque o piano foi construído com as teclas brancas formando naturalmente esse padrão a partir de Dó.

Em Sol Maior: Sol-Lá-Si-Dó-Ré-Mi-Fá#. O Fá precisa ser aumentado para manter o padrão T-T-St antes do oitavo grau.

## Escalas Menores

A **escala menor natural** (Eólio) tem o padrão T-St-T-T-St-T-T. Em Lá menor: Lá-Si-Dó-Ré-Mi-Fá-Sol-Lá.

O problema da menor natural: o 7º grau (Sol, em Lá menor) está a um tom da tônica, não a um semitom. Isso enfraquece a "sensível" (nota que cria tensão para resolver na tônica). A **menor harmônica** resolve isso elevando o 7º grau (Sol → Sol#), criando o semitom de resolução — mas também o intervalo exótico de segunda aumentada entre o 6º e 7º graus (Fá-Sol#).

A **menor melódica** resolve a segunda aumentada elevando também o 6º grau ao subir (Fá → Fá#, Sol → Sol#) e revertendo ao natural ao descer.

## Círculo de Quintas

O círculo de quintas organiza as 24 tonalidades (12 maiores + 12 menores) em um círculo onde cada tonalidade adjacente difere por um acidente:
- Sentido horário (quintas ascendentes): adiciona sustenidos
- Sentido anti-horário (quintas descendentes): adiciona bemóis

Tonalidades em lados opostos do círculo têm 6 acidentes.

## Modos

Os sete modos diatônicos são gerados pela mesma escala de 7 notas, começando em graus diferentes. Em Dó: Dó=Jônio, Ré=Dórico, Mi=Frígio, Fá=Lídio, Sol=Mixolídio, Lá=Eólio, Si=Lócrio. O caráter diferente de cada modo vem da posição dos semitons em relação à tônica."""})

NOVOS.append({"id":"r-tm-04","topico":"tm-04","disciplina":"teoria-musical","bloco":"especificos",
"nome":"Intervalos musicais","incidencia":"alta",
"versaoCurta":"""# Intervalos Musicais

## O que e um intervalo
- Distância entre duas notas (simultaneas = harmônico; sucessivas = melódico)
- Classificado por: **quantidade** (nome) + **qualidade** (espécie)

## Quantidade (contagem de notas)
- Contar a nota inferior + a superior + todas as intermediárias
- Dó-Ré = 2ª | Dó-Mi = 3ª | Dó-Fá = 4ª | Dó-Sol = 5ª | Dó-Lá = 6ª | Dó-Si = 7ª | Dó-Dó = 8ª (oitava)

## Qualidade (espécie)
| Intervalo | Qualidades possíveis |
|---|---|
| 1ª, 4ª, 5ª, 8ª | Justo (J), Aumentado (A), Diminuto (D) |
| 2ª, 3ª, 6ª, 7ª | Maior (M), Menor (m), Aumentado (A), Diminuto (D) |

## Intervalos em Dó Maior (referência)
- Dó-Ré = 2ª Maior (1 tom)
- Dó-Mi = 3ª Maior (2 tons)
- Dó-Fá = 4ª Justa (2,5 tons)
- Dó-Sol = 5ª Justa (3,5 tons)
- Dó-Lá = 6ª Maior (4,5 tons)
- Dó-Si = 7ª Maior (5,5 tons)
- Dó-Dó = 8ª Justa (6 tons)

## Consonância e Dissonância
- **Consonantes**: 1ª J, 5ª J, 8ª J (perfeitos) e 3ª M/m, 6ª M/m (imperfeitos)
- **Dissonantes**: 2ª, 7ª, 4ª Aumentada/Trítono
- **Trítono**: 3 tons; 4ª A = 5ª D; instabilidade máxima

## Inversao de intervalos
- Inverter = colocar a nota de baixo uma oitava acima
- 1ª ↔ 8ª | 2ª ↔ 7ª | 3ª ↔ 6ª | 4ª ↔ 5ª
- Maior ↔ Menor | Justo ↔ Justo | Aumentado ↔ Diminuto

## Para a prova
- Trítono = 4ª Aumentada = 5ª Diminuta = 3 tons = "diabo na musica"
- 3ª Maior: 2 tons; 3ª Menor: 1,5 tom
- Saber inverter: 3ª M inverte em 6ª m; 4ª J inverte em 5ª J
- Intervalos justos: 1ª, 4ª, 5ª, 8ª (nao tem Maior/Menor, só Justo/A/D)""",
"versaoCompleta":"""# Intervalos Musicais

## Definição e Importância

O intervalo é a unidade fundamental da teoria musical. Toda melodia é uma successão de intervalos; toda harmonia é um conjunto de intervalos simultâneos. O domínio dos intervalos é pré-requisito para entender escalas, acordes e funções harmônicas.

## Quantidade: Contando Notas

A quantidade de um intervalo é determinada contando-se a nota de baixo, a nota de cima, e todas as notas intermediárias. Por isso, a distância de Dó a Mi é uma 3ª: Dó(1)-Ré(2)-Mi(3). Mesmo que alterações mudem a qualidade do intervalo, a quantidade permanece a mesma: Dó-Mi, Dó-Mi# e Dó-Mib são todas 3ás (de qualidades diferentes).

## Qualidade: Número de Semitons

A qualidade indica o tamanho exato do intervalo em semitons:

| Intervalo | Qualidade | Semitons |
|---|---|---|
| 2ª Menor | m2 | 1 |
| 2ª Maior | M2 | 2 |
| 3ª Menor | m3 | 3 |
| 3ª Maior | M3 | 4 |
| 4ª Justa | J4 | 5 |
| 4ª Aumentada / 5ª Diminuta (Trítono) | A4/D5 | 6 |
| 5ª Justa | J5 | 7 |
| 6ª Menor | m6 | 8 |
| 6ª Maior | M6 | 9 |
| 7ª Menor | m7 | 10 |
| 7ª Maior | M7 | 11 |
| 8ª Justa | J8 | 12 |

## O Trítono

O trítono (3 tons inteiros = 6 semitons) é o intervalo mais tenso do sistema tonal. Na Idade Média era chamado de "diabolus in musica" e era evitado. No sistema tonal funcional, o trítono entre o 7º grau (sensível) e o 4º grau cria a tensão fundamental que exige resolução na tônica.

## Consonância e Dissonância

Intervalos consonantes são percebidos como estáveis; dissonantes como tensos, exigindo resolução. 1ª, 5ª e 8ª são consonâncias perfeitas; 3ªs e 6ªs são consonâncias imperfeitas (menos estáveis). 2ªs, 7ªs e trítono são dissonantes."""})

NOVOS.append({"id":"r-tm-05","topico":"tm-05","disciplina":"teoria-musical","bloco":"especificos",
"nome":"Acordes e funcoes harmonicas","incidencia":"alta",
"versaoCurta":"""# Acordes e Funcoes Harmônicas

## O que e um acorde
- 3 ou mais notas tocadas simultaneamente
- **Tríade**: 3 notas (terças sobrepostas: tônica + terça + quinta)

## Tipos de tríade
| Tríade | Terça inferior | Terça superior | Exemplo |
|---|---|---|---|
| **Maior** | Maior (4 st) | Menor (3 st) | Dó-Mi-Sol |
| **Menor** | Menor (3 st) | Maior (4 st) | La-Dó-Mi |
| **Diminuta** | Menor + Menor | | Si-Ré-Fá |
| **Aumentada** | Maior + Maior | | Dó-Mi-Sol# |

## Funcoes harmônicas na tonalidade maior
- **Tônica (I)**: repouso, chegada (Dó-Mi-Sol em Dó Maior)
- **Dominante (V)**: tensão, pede resolução para a tônica (Sol-Si-Ré)
- **Subdominante (IV)**: pre-dominante, vai para V ou volta a I (Fá-La-Dó)
- **V7** (Dominante 7ª): adiciona 7ª menor → mais tensão

## Graus da escala e seus acordes (Dó Maior)
- I: Dó Maior | ii: Ré menor | iii: Mi menor | IV: Fá Maior
- V: Sol Maior | vi: La menor | vii°: Si diminuto

## Cifragem popular (americana)
- Maiúsculo = maior: C, G, F
- Minúsculo ou "m" = menor: Am, Dm, Em
- "7" = 7ª menor sobre acorde maior: G7, C7
- "m7" = 7ª menor sobre menor: Am7
- "dim" ou "°" = diminuto

## Para a prova
- Cadência I-IV-V-I = progressão fundamental da musica tonal
- V-I = cadência autêntica (resolução)
- IV-I = cadência plagal ("amem")
- Acorde maior: 3ª Maior + 5ª Justa | menor: 3ª Menor + 5ª Justa
- "Sensível" = 7º grau = nota Si (em Dó Maior); cria tensão que resolve em Dó""",
"versaoCompleta":"""# Acordes e Funcoes Harmônicas

## Construção de Acordes

Um acorde é formado pela superposição de intervalos, geralmente de terças. A tríade básica tem três notas: **fundamental** (nota que dá nome ao acorde), **terça** (3ª acima da fundamental) e **quinta** (5ª acima da fundamental).

A qualidade da tríade depende das terças:
- **Tríade Maior**: 3ª Maior + 3ª Menor (= 5ª Justa total). Som "alegre", "estável"
- **Tríade Menor**: 3ª Menor + 3ª Maior (= 5ª Justa total). Som "triste", "melancólico"
- **Tríade Diminuta**: 3ª Menor + 3ª Menor (= 5ª Diminuta). Som "tenso", "instável"
- **Tríade Aumentada**: 3ª Maior + 3ª Maior (= 5ª Aumentada). Som "suspenso"

## Acordes com 7ª

Adicionando mais uma terça à tríade, cria-se um acorde de 4 sons (7ª):
- **V7** (dominante com 7ª): Sol-Si-Ré-Fá (em Dó Maior). O acorde mais tenso da tonalidade — a 7ª (Fá) quer descer para Mi; o Si (sensível) quer subir para Dó.
- **m7** (menor com 7ª): usado no jazz e musica popular (La-Dó-Mi-Sol)
- **M7** (maior com 7ª maior): som jazzy, suave (Dó-Mi-Sol-Si)

## Funções Harmônicas

O sistema tonal organiza os acordes em três funções:

**Tônica (T)**: acordes de repouso e estabilidade. Inclui I e vi (relativo menor).

**Dominante (D)**: acordes de máxima tensão, pedindo resolução. Inclui V e vii°. O V7 é o acorde dominante por excelência.

**Subdominante (SD)**: acordes que criam movimento em direção à dominante. Inclui IV e ii.

A progressão básica da musica tonal: **T → SD → D → T** (I → IV → V → I).

## Inversões

Um acorde pode aparecer em posicao fundamental (fundamental no baixo) ou em inversão (outra nota no baixo):
- 1ª inversão: 3ª no baixo (acorde de 6ª)
- 2ª inversão: 5ª no baixo (acorde de 6/4)

As inversões afetam a estabilidade do acorde e criam movimento melódico no baixo."""})

NOVOS.append({"id":"r-tm-06","topico":"tm-06","disciplina":"teoria-musical","bloco":"especificos",
"nome":"Cifragem e leitura de cifras","incidencia":"media",
"versaoCurta":"""# Cifragem e Leitura de Cifras

## O que e cifragem
- Sistema de notacao simplificada de acordes, muito usado na musica popular
- Indica o acorde com uma letra (sistema americano) + modificadores
- Alternativa à partitura para músicos que improvisam ou acompanham

## Sistema de notas (americano × latino)
| Americano | Latino |
|---|---|
| C | Dó |
| D | Ré |
| E | Mi |
| F | Fá |
| G | Sol |
| A | Lá |
| B | Si |

## Símbolos básicos
| Símbolo | Significado | Exemplo |
|---|---|---|
| Letra maiúscula isolada | Acorde Maior | C = Dó Maior |
| "m" ou "-" | Acorde Menor | Am = Lá menor |
| "7" | Dominante 7ª (7ª menor sobre maior) | G7 = Sol com 7ª |
| "m7" | Menor com 7ª menor | Am7 |
| "M7" ou "maj7" | Maior com 7ª maior | CM7 |
| "dim" ou "°" | Diminuto | Bdim |
| "aug" ou "+" | Aumentado | Caug |
| "sus4" | Suspensa de 4ª | Gsus4 |
| "/" | Baixo pedal | G/B = Sol com Si no baixo |

## Sequências comuns (cifradas)
- **Anatole/Rhythm Changes**: C / Am / F / G (I-vi-IV-V em Dó)
- **Blues de 12 compassos**: I7-I7-I7-I7 / IV7-IV7-I7-I7 / V7-IV7-I7-I7
- **Bossa nova base**: Cmaj7 - A7 - Dm7 - G7

## Para a prova
- Cifras são SISTEMA DE NOTACAO POPULAR — valido e ensinável na escola
- BNCC aceita cifragem como forma de notacao e registro
- "7" em cifra popular = 7ª MENOR (G7 = Sol-Si-Ré-Fá)
- "maj7" = 7ª MAIOR (Cmaj7 = Dó-Mi-Sol-Si)
- Tablaturas: sistema similar para instrumentos de cordas (guitarra, violao)""",
"versaoCompleta":"""# Cifragem e Leitura de Cifras

## História e Contexto

A cifragem (chord notation) é um sistema de notação musical desenvolvido no contexto da música popular do século XX, especialmente no jazz americano. Permite que músicos leiam e improvisem acordes a partir de uma sequência de símbolos simples, sem a necessidade de partitura completa.

No Brasil, é amplamente usada em musica popular brasileira (MPB, samba, bossa nova, forró, sertanejo) e é o sistema de notação preferido por guitarristas e violonistas que acompanham por ouvido.

## Sistema de Notas

O sistema americano usa letras (C-D-E-F-G-A-B) em vez dos nomes latinos (Dó-Ré-Mi-Fá-Sol-Lá-Si). Alterações: # (sustenido) e b (bemol). Exemplos: F# = Fá#, Bb = Sib.

## Estrutura das Cifras

A cifra tem uma **letra base** (a fundamental do acorde) seguida de **modificadores** que descrevem a qualidade e as extensões:

**Qualidade básica**: letra maiúscula = maior; "m" = menor; "dim" = diminuto.

**7ªs**: o simples "7" adiciona 7ª MENOR (dominante) ao acorde maior — G7 = Sol dominante. "M7" ou "maj7" adiciona 7ª MAIOR — Cmaj7 = Sol maior com 7ª maior (acorde jazzístico de repouso).

**Extensões**: "9", "11", "13" adicionam notas além da 7ª. Am9 = Lá menor com 7ª e 9ª. São comuns no jazz e na bossa nova.

**Baixo pedal (slash chords)**: G/B significa Sol Maior com Si no baixo (1ª inversão). Cria movimento melódico na linha do baixo.

## Cifragem e Pedagogia

A BNCC reconhece a cifragem como forma legítima de notação e registro musical. No ensino de música em contexto de musica popular (violão, guitarra, teclado), a cifragem é a porta de entrada mais eficiente. Combinada com leitura de melodia em pauta convencional, forma um músico completo para o contexto brasileiro."""})

NOVOS.append({"id":"r-tm-07","topico":"tm-07","disciplina":"teoria-musical","bloco":"especificos",
"nome":"Formas musicais: sonata, fuga, rondo, tema e variacoes, suite","incidencia":"media",
"versaoCurta":"""# Formas Musicais

## Forma-Sonata (Classicismo)
- 1 movimento em 3 secoes: Exposicao + Desenvolvimento + Recapitulacao
- Exposicao: Tema 1 (tônica) + Tema 2 (dominante)
- Desenvolvimento: fragmentacao e modulacao
- Recapitulacao: ambos os temas na tônica
- Usada em: sinfonias, quartetos, concertos, sonatas

## Fuga (Barroco)
- Contraponto imitativo em varias vozes (2-5)
- Estrutura:
  - **Sujeito**: tema principal, apresentado por 1 voz
  - **Resposta**: sujeito em outra voz (na dominante)
  - **Contra-sujeito**: contraponto ao sujeito
  - **Episodios**: secoes de modulacao entre exposicoes
  - **Stretta**: entradas do sujeito sobrepostas (clímax)
- Bach: Das Wohltemperierte Klavier (48 Prelúdios e Fugas)

## Rondo
- Forma: A-B-A-C-A (ou ABACADA etc.)
- Tema principal (A) retorna intercalado por episódios (B, C, D)
- Comum em movimentos finais de sonatas e sinfonias classicas

## Tema e Variacoes
- Tema + série de variacoes que modificam o material
- Variacoes podem mudar: ritmo, modo (maior/menor), harmonia, tempo, ornamentacao
- Exemplos: Variacoes Goldberg (Bach), Variacoes Diabelli (Beethoven)

## Suite (Barroco)
- Sequência de dancas estilizadas (nao para dancar, mas para ouvir)
- Dancas típicas: Allemande-Courante-Sarabande-Gigue (núcleo básico)
- Bach: Suites para Cello Solo, Suites Inglesas, Francesas

## Para a prova
- Sonata: 3 secoes (Exposicao-Desenvolvimento-Recapitulacao)
- Fuga: sujeito + resposta; varias vozes; contraponto
- Rondo: A retorna sempre (ABACA)
- Suite: dancas barroca estilizadas
- Forma binaria (AB) e ternária (ABA) sao as mais simples""",
"versaoCompleta":"""# Formas Musicais

## Forma como Princípio

Forma musical refere-se à organização macro de uma obra — como ela se distribui no tempo, quais partes retornam, como as secoes se relacionam. Toda peça tem forma, mesmo que não siga um esquema pré-estabelecido.

## Forma-Sonata

A forma-sonata é o princípio estrutural dominante do Classicismo e Romantismo. É uma forma dinâmica baseada em tensão e resolução tonal:

**Exposicao**: apresenta dois temas em oposicao tonal. O Tema 1 (ou grupo de temas 1) está na tônica; o Tema 2 está na dominante (em obras em tonalidade maior) ou no relativo maior (em obras em tonalidade menor). A diferença de tonalidade cria tensão.

**Desenvolvimento**: os materiais temáticos são fragmentados, combinados, modulam por tonalidades distantes. É a secao de maior instabilidade.

**Recapitulacao**: ambos os temas retornam, mas agora NA TÔNICA — a tensão tonal é resolvida. A presenca do Tema 2 na tônica (antes estava na dominante) é a "resposta" à tensão da exposicao.

**Coda** (opcional): material conclusivo após a recapitulacao.

## Fuga

A fuga é o ápice do contraponto imitativo. Tem um **sujeito** (tema), apresentado por uma voz de cada vez em entradas sucessivas:
1. Voz 1: sujeito na tônica
2. Voz 2: resposta na dominante
3. Voz 3: sujeito na tônica
(e assim por diante)

Entre as entradas, **episódios** de modulação intercalam-se. O **contra-sujeito** é o contraponto regular ao sujeito quando outra voz o apresenta. A **stretta** ocorre quando as entradas do sujeito se sobrepõem antes do sujeito anterior terminar — gera clímax.

## Rondo e Tema com Variacoes

O **rondó** é baseado na recorrência do tema principal (A), interrompido por episódios (B, C). É frequentemente usado em movimentos finais, pelo caráter virtuosístico e alegre.

O **tema e variacoes** transforma progressivamente um tema simples. Cada variacao mantém a estrutura harmônica básica (e frequentemente a mesma duração) mas modifica melodia, ritmo, textura ou modo."""})

NOVOS.append({"id":"r-tm-08","topico":"tm-08","disciplina":"teoria-musical","bloco":"especificos",
"nome":"Compasso e ritmo","incidencia":"alta",
"versaoCurta":"""# Compasso e Ritmo

## Pulso e tempo
- **Pulso**: batida regular e constante; referência temporal da música
- **Andamento** (tempo): velocidade do pulso
  - Larghissimo (<40 bpm) → Largo → Larghetto → Adagio → Andante → Moderato → Allegro → Presto → Prestissimo (>200 bpm)
  - Indicacoes em bpm ou termos italianos
  - **Metrônomo**: dispositivo que marca o pulso; Metrônomo de Maelzel (M.M.)

## Compasso
- Agrupamento regular de pulsos em unidades (compassos)
- **Fórmula de compasso**: 2 números (numera/denominador)
  - Numerador = número de pulsos por compasso
  - Denominador = figura que vale 1 pulso (4 = semínima, 8 = colcheia, 2 = mínima)

## Compassos simples vs. compostos
| Tipo | Divisao do pulso | Exemplos |
|---|---|---|
| **Simples** | Binária (em 2) | 2/4, 3/4, 4/4 |
| **Composto** | Ternária (em 3) | 6/8, 9/8, 12/8 |

## Compassos irregulares e assimétricos
- 5/4 (3+2 ou 2+3), 7/8 (4+3 ou 3+4) — muito no jazz e musica folclorica
- Bartók, Stravinsky: compassos variáveis (mudanca de compasso frequente)

## Ritmo vs. métrica
- **Métrica**: padrão regular de acentos (tese = tempo forte; arsis = tempo fraco)
- **Ritmo**: o padrão real de durações (pode ou nao coincidir com a métrica)
- **Síncope**: acento no tempo fraco ou entre tempos (deslocamento do acento)
- **Hemíola**: 3 grupos de 2 sobre 2 grupos de 3 (6 colcheias em 6/8 vs. 3/4)

## Para a prova
- Compasso 4/4 = 4 semínimas = "compasso comum" (C)
- Compasso 2/2 = "alla breve" (¢) = 2 mínimas por compasso
- Sincope: sinal de acento em tempo fraco; característica do samba e jazz
- 6/8: composto binário (2 pulsos de colcheia pontuada, cada um dividido em 3)
- Polirritmia: dois ritmos diferentes simultaneos""",
"versaoCompleta":"""# Compasso e Ritmo

## Pulso, Andamento e Agógica

O **pulso** é a batida regular que organiza o tempo musical. É o que se bate ao compasso da música. O **andamento** é a velocidade desse pulso, medida em batidas por minuto (bpm) ou indicada por termos italianos.

A **agógica** refere-se às variações expressivas de andamento: ritardando (desacelerando), accelerando, rubato (liberdade rítmica expressiva), fermata (prolongamento de nota).

## A Fórmula de Compasso

A fórmula de compasso (ou fórmula de tempo) no início de uma peça indica como os pulsos são organizados:

- **4/4**: 4 semínimas por compasso. Compasso mais comum na música ocidental. Indicado também pela letra C (compasso común).
- **3/4**: 3 semínimas. Compasso típico da valsa, minueto, mazurca.
- **2/4**: 2 semínimas. Compasso típico da marcha, polca.
- **6/8**: 6 colcheias, agrupadas em 2 × 3. Pulso real = colcheia pontuada. Composto binário.
- **2/2** (alla breve): 2 mínimas. Leitura "em dois", mais rápida que 4/4.

## Acentuação Métrica

Dentro de cada compasso, os pulsos têm hierarquia:
- **Tese** (arsin): tempo forte (1º pulso do compasso) — recebe acento métrico
- **Arsis** (thesis): tempos fracos — menos acentuados

Em 4/4: o 1º e 3º tempos são fortes (o 1º mais do que o 3º). O 2º e 4º são fracos.

## Síncope

A síncope ocorre quando o acento recai sobre um tempo ou parte de tempo normalmente fraco. É o elemento rítmico mais característico da música popular brasileira (samba, bossa nova) e do jazz.

No samba, a síncopa é estrutural: o padrão rítmico "desloca" sistematicamente os acentos em relação à pulsação regular. Isso cria o balanço característico do gênero.

## Polirritmia

Polirritmia é a sobreposição de dois ou mais padrões rítmicos diferentes. A hemíola (3:2) é a mais comum: 3 grupos de 2 colcheias sobre 2 grupos de 3 colcheias. Presente no barroco (passacaglia, chacona) e na música africana."""})

todos = dados["resumos"] + [r for r in NOVOS if r["topico"] not in existentes]
dados["resumos"] = todos
dados["versao"] = "2.5.0"
with open(SRC,"w",encoding="utf-8") as f: json.dump(dados,f,ensure_ascii=False,indent=2)
print("Batch 5 OK — total: %d" % len(todos))
