#!/usr/bin/env python3
"""Batch 4: gp-05 to gp-08, me-07, me-08, bm-02 to bm-07"""
import json, pathlib
BASE = pathlib.Path(__file__).parent
SRC  = BASE / "data" / "resumos.json"
with open(SRC) as f: dados = json.load(f)
existentes = {r["topico"] for r in dados["resumos"]}
NOVOS = []

NOVOS.append({"id":"r-gp-05","topico":"gp-05","disciplina":"gestao-pedagogica","bloco":"complementares",
"nome":"Coordenação pedagógica","incidencia":"media",
"versaoCurta":"""# Coordenação Pedagógica

## O que é
- Espaço e tempo destinados ao trabalho coletivo dos professores
- Na SEDF: **3 dias/semana** de coordenação (terça, quarta e quinta)
- Coordenador Pedagógico: articulador do trabalho coletivo da escola

## Funções da coordenação pedagógica
- **Formação continuada** in loco dos professores
- **Planejamento coletivo** de aulas, projetos e eventos
- **Reflexão sobre a prática** — análise de dados de aprendizagem
- **Articulação curricular** — integração entre componentes
- **Atendimento a necessidades especiais** — AEE, inclusão

## Coordenador Pedagógico (CP)
- Na SEDF: função de confiança exercida por professor efetivo
- Não é superior hierárquico dos professores — é **parceiro de formação**
- Atribuições: orientar o planejamento; mediar conflitos pedagógicos; acompanhar a prática docente; organizar estudos coletivos
- Diferente do supervisor e do diretor

## Modelos de coordenação
- **Coletiva (geral)**: toda a equipe docente reunida
- **Por área/componente**: professores da mesma disciplina
- **Individual**: atendimento específico a um professor

## Para a prova
- Na SEDF: coordenação é direito e dever do professor (não é opcional)
- CP não pode ser substituído por atividades administrativas (desvio de função)
- Coordenação pedagógica ≠ reunião administrativa
- Tempo de coordenação = parte da carga horária remunerada (jornada ampliada)
- Portaria 38/2022: regulamenta atribuições do professor, incluindo coordenação""",
"versaoCompleta":"""# Coordenação Pedagógica

## Conceito e Importância

A coordenação pedagógica é o espaço-tempo de formação e trabalho coletivo dos professores dentro da escola. É um dos diferenciais do sistema público do DF em relação a outras redes: a SEDF garante, por lei e regulamento, um número expressivo de horas semanais de coordenação remunerada para os docentes.

A coordenação pedagógica é espaço de:
- Formação contínua baseada nas necessidades reais da escola
- Planejamento coletivo e articulação curricular
- Reflexão crítica sobre a prática docente
- Construção e revisão do PPP
- Discussão sobre resultados de aprendizagem

## O Coordenador Pedagógico

O Coordenador Pedagógico (CP) é o articulador da coordenação. Na SEDF, é um professor efetivo que exerce a função em designação temporária ou por eleição (conforme a escola).

O CP não é um "fiscal" dos professores. Sua função é formativa: apoiar os docentes na reflexão sobre a prática, articular saberes, mediar conflitos pedagógicos e garantir que o tempo de coordenação seja efetivamente pedagógico.

## Coordenação na SEDF

A carga horária de coordenação dos professores da SEDF está organizada em:
- **Coordenação coletiva**: participação de todos os professores (início de turno)
- **Coordenação por área**: professores do mesmo componente ou área
- **Coordenação individual**: planejamento e estudo autônomo do professor

A Portaria Conjunta nº 38/2022 regulamenta as atribuições do professor, incluindo a participação nas coordenações como dever funcional. Professores do CEP-EMB têm coordenações específicas para a área de Música/Arte.

## Desafios

O principal desafio é garantir que o tempo de coordenação não seja absorvido por demandas administrativas. Reuniões de pais, preenchimento de formulários e outras tarefas burocráticas desviam a coordenação de sua finalidade pedagógica."""})

NOVOS.append({"id":"r-gp-06","topico":"gp-06","disciplina":"gestao-pedagogica","bloco":"complementares",
"nome":"Tendências pedagógicas contemporâneas","incidencia":"alta",
"versaoCurta":"""# Tendências Pedagógicas Contemporâneas

## Classificação (Libâneo)
### Liberais (reproduzem a ordem social)
- **Tradicional**: transmissão de conteúdos pelo professor; aluno passivo
- **Renovada progressista (Dewey)**: aprender fazendo; experiência como base
- **Renovada não-diretiva (Rogers)**: educação centrada no aluno
- **Tecnicista**: eficiência; objetivos comportamentais; instrução programada

### Progressistas (transformam a sociedade)
- **Libertadora (Freire)**: educação como prática de liberdade; diálogo; temas geradores
- **Libertária**: autogestão; poder ao aluno/grupo
- **Crítico-social dos conteúdos (Saviani)**: conteúdos históricos + prática social

## Abordagens contemporâneas
- **Construtivismo (Piaget/Vygotsky)**: aluno constrói o conhecimento; ZDP; mediação
- **Sociointeracionismo (Vygotsky)**: aprendizagem social; linguagem como ferramenta
- **Aprendizagem significativa (Ausubel)**: novo conhecimento âncora no que já existe
- **Pedagogia de projetos**: aprendizagem ativa; resolução de problemas reais
- **Metodologias ativas**: sala invertida, PBL (Problem-Based Learning), gamificação

## Para a prova
- **ZDP (Vygotsky)**: zona entre o que o aluno já sabe (zona real) e o que pode aprender com ajuda (zona proximal)
- **Mediação**: papel do professor e dos pares no sociointeracionismo
- Paulo Freire: "educação bancária" (modelo a superar) vs. "educação libertadora"
- Currículo em Movimento do DF: base sociointeracionista e crítica
- BNCC valoriza: protagonismo, criatividade, pensamento crítico (competências gerais)""",
"versaoCompleta":"""# Tendências Pedagógicas Contemporâneas

## A Classificação de Libâneo

José Carlos Libâneo propõe uma classificação das tendências pedagógicas que divide as abordagens em dois grandes blocos: as **liberais** (que se destinam a adaptar os indivíduos à sociedade existente) e as **progressistas** (que visam à transformação social).

Essa classificação, embora simplificadora, é amplamente usada em concursos e na formação docente.

## Tendências Liberais

**Pedagogia Tradicional**: o professor é o detentor do saber e o aluno é receptáculo passivo. Foco na transmissão de conteúdos, memorização e disciplina. Avaliação classificatória.

**Escola Nova (Dewey)**: reação ao formalismo tradicional. "Learning by doing" — o aluno aprende pela experiência ativa. O professor passa a ser facilitador. Ênfase nos interesses do aluno e na resolução de problemas.

**Humanismo (Rogers)**: educação centrada no estudante. O professor cria condições afetivas para o desenvolvimento espontâneo. Crítica ao autoritarismo pedagógico.

**Tecnicismo**: eficiência como valor central. Objetivos operacionais, materiais programados, avaliação por comportamentos observáveis. Inspirado no behaviorismo (Skinner).

## Tendências Progressistas

**Pedagogia Libertadora (Freire)**: educação como ato político. Crítica à "educação bancária" (depósito de conteúdos no aluno). Propõe o diálogo e os "temas geradores" — problemas da realidade dos educandos como ponto de partida.

**Pedagogia Histórico-Crítica (Saviani)**: síntese dialética. O professor deve garantir o acesso ao saber historicamente produzido pela humanidade, com criticidade. A prática social é ponto de partida e chegada.

## Construtivismo e Sociointeracionismo

**Piaget**: o conhecimento é construído pelo sujeito em interação com o objeto. Estágios de desenvolvimento cognitivo.

**Vygotsky**: o conhecimento é construído na interação social. A Zona de Desenvolvimento Proximal (ZDP) é a distância entre o que o aluno faz sozinho e o que faz com ajuda — é onde o ensino deve atuar. Mediação simbólica (linguagem) é central.

**Ausubel**: aprendizagem significativa ocorre quando o novo conhecimento se ancora em conceitos que o aluno já possui (subsunçores). O ensino deve partir do conhecimento prévio."""})

NOVOS.append({"id":"r-gp-07","topico":"gp-07","disciplina":"gestao-pedagogica","bloco":"complementares",
"nome":"Inclusão e atendimento à diversidade","incidencia":"alta",
"versaoCurta":"""# Inclusão e Atendimento à Diversidade

## Marcos legais
- **CF/88 art. 208, III**: AEE preferencialmente na rede regular
- **LDB art. 58-60**: Educação Especial como modalidade transversal
- **Lei 13.146/2015** (LBI): sistema educacional inclusivo
- **Resolução CNE/CEB 4/2009**: AEE nas escolas regulares
- **Política Nacional de Educação Especial na Perspectiva Inclusiva (PNEE 2008)**

## Educação Especial na SEDF
- Modalidade que perpassa todas as etapas e níveis
- Público: deficiência, TEA, altas habilidades/superdotação
- AEE em Salas de Recursos Multifuncionais (SRM) — contraturno
- O AEE NÃO substitui o ensino regular — é complementar/suplementar

## Diversidade na escola
- **Étnico-racial**: Lei 10.639/2003 (cultura afro-brasileira); Lei 11.645/2008 (indígena)
- **Gênero e sexualidade**: BNCC e DCNs orientam respeito às diversidades
- **Sociocultural**: valorização dos saberes populares; diálogo com a comunidade
- **Linguística**: Libras como língua; surdez não é deficiência de linguagem

## Adaptações curriculares
- **Grandes adaptações**: modificações no currículo (objetivo, conteúdo)
- **Pequenas adaptações**: mudanças metodológicas e de avaliação (sem alterar objetivos)
- DI (Deficiência Intelectual): pode requerer objetivos diferenciados
- DA (Deficiência Auditiva): uso de Libras, intérprete, texto visual

## Para a prova
- Inclusão ≠ integração: integração = aluno se adapta; inclusão = escola se adapta
- AEE: direito; custeado pelo Estado; não pode ser cobrado de famílias
- Laudo médico NÃO é obrigatório para matrícula (LBI art. 2º)
- "Sala especial" ≠ "sala regular com apoio" — modelo inclusivo é o segundo""",
"versaoCompleta":"""# Inclusão e Atendimento à Diversidade

## Da Integração à Inclusão

O modelo de **integração** pressupunha que o aluno com deficiência deveria se adaptar à escola "normal". O de **inclusão** (PNEE 2008, LBI 2015) pressupõe que a escola deve se transformar para acolher todos os alunos. A mudança é mais do que semântica: implica reformas na formação de professores, na infraestrutura, no currículo e na avaliação.

## O Atendimento Educacional Especializado (AEE)

O AEE é o conjunto de atividades e recursos pedagógicos e de acessibilidade organizados para complementar (para alunos com deficiência) ou suplementar (para superdotados) a escolarização regular. Características:
- Ocorre preferencialmente nas **Salas de Recursos Multifuncionais (SRM)** das próprias escolas
- Em turno contrário ao do ensino regular
- Não substitui a classe comum
- Previsto no PPP da escola
- O professor especializado elabora o Plano de AEE individualizado

## Diversidade Étnico-Racial

A Lei 10.639/2003 tornou obrigatório o ensino de História e Cultura Afro-Brasileira e Africana em toda a Educação Básica. A Lei 11.645/2008 estendeu essa obrigatoriedade para a cultura indígena. No ensino de música, isso implica incluir manifestações da música africana, afro-brasileira e indígena no currículo — não como curiosidade, mas como patrimônio legítimo.

## Diversidade e Música

O professor de música tem papel especial na promoção da diversidade: o currículo musical pode incluir ritmos afro-brasileiros (samba, maracatu), música indígena, músicas de matriz africana (jùjú, highlife), culturas populares regionais (baião, frevo). A BNCC orienta explicitamente a valorização das **matrizes estéticas e culturais** diversas.

## Altas Habilidades/Superdotação

Frequentemente esquecido, o atendimento a alunos com altas habilidades também é parte da Educação Especial. O AEE para esses alunos tem caráter **suplementar** (enriquecimento curricular), não remedial. No contexto musical, pode incluir participação em projetos avançados, grupos especiais e programas de aceleração."""})

NOVOS.append({"id":"r-gp-08","topico":"gp-08","disciplina":"gestao-pedagogica","bloco":"complementares",
"nome":"Gestão democrática","incidencia":"media",
"versaoCurta":"""# Gestão Democrática

## Base legal
- **CF/88 art. 206, VI**: gestão democrática do ensino público como princípio
- **LDB art. 14**: sistemas de ensino definirão normas de gestão democrática com:
  - Participação dos profissionais da educação na elaboração do PPP
  - Participação da comunidade escolar e local em Conselhos Escolares
- **LDB art. 15**: escolas terão progressivos graus de autonomia pedagógica, administrativa e financeira

## Instrumentos de gestão democrática
- **Conselho Escolar**: órgão máximo de deliberação coletiva da escola; representa todos os segmentos
- **Grêmio Estudantil**: representação dos estudantes (Lei 7.398/1985)
- **Associação de Pais e Mestres (APM)**: participação das famílias
- **PPP participativo**: construção coletiva

## Diretor de escola
- Na SEDF: provimento por **eleição direta** da comunidade escolar
- Alternativa: concurso público para diretor (modelo de alguns estados)
- Mandato com prestação de contas ao Conselho Escolar

## Autonomia escolar (art. 15)
- **Pedagógica**: elaborar o PPP, definir metodologias, projetos
- **Administrativa**: gerir pessoal, espaço, calendário (com autonomia relativa)
- **Financeira**: gerir recursos do PDDE, FNDE e outras fontes

## Para a prova
- Gestão democrática ≠ gestão participativa: democrática implica direito; participativa é possibilidade
- Conselho Escolar: composição paritária (ou não) varia por sistema — verificar regulamento local
- Lück (Heloísa Lück): referência em gestão escolar democrática
- SEDF: diretores eleitos = modelo de gestão democrática
- Autonomia da escola é limitada: deve respeitar LDB, BNCC, normas do sistema""",
"versaoCompleta":"""# Gestão Democrática

## Fundamento Constitucional e Legal

A gestão democrática do ensino público está consagrada como princípio constitucional (CF/88, art. 206, VI) e detalhada na LDB (arts. 14-15). O princípio parte do reconhecimento de que a escola pública pertence à comunidade — não ao diretor nem ao sistema burocrático — e que as decisões sobre a vida escolar devem envolver todos os que nela têm interesse.

## Os Sujeitos da Gestão Democrática

**Professores e equipe pedagógica**: participam da elaboração do PPP, das reuniões de Conselho de Classe e das coordenações coletivas.

**Estudantes**: têm o direito de constituir o Grêmio Estudantil (Lei 7.398/1985) e de participar do Conselho Escolar. A voz dos alunos deve ser considerada nas decisões pedagógicas.

**Famílias**: participam da APM, do Conselho Escolar e de reuniões pedagógicas. Têm direito à informação sobre o desempenho dos filhos.

**Funcionários**: integram o Conselho Escolar e contribuem com perspectivas sobre o funcionamento da escola.

## O Conselho Escolar

O Conselho Escolar é o órgão máximo de deliberação coletiva da escola. Suas funções são: deliberativa (toma decisões sobre o PPP, o orçamento e questões disciplinares graves), consultiva (emite pareceres), fiscal (acompanha a execução financeira) e mobilizadora (articula a participação da comunidade).

A composição varia: em muitos sistemas, é paritária (50% servidores + 50% comunidade). Na SEDF, os Conselhos Escolares têm regulamentação específica.

## Autonomia Escolar (Art. 15)

O art. 15 da LDB prevê progressivos graus de autonomia. Na prática, a autonomia escolar é relativa: a escola pode inovar no currículo (parte diversificada), na metodologia e nos projetos, mas deve respeitar a BNCC, as DCNs, as normas do sistema e as orientações da secretaria. A autonomia financeira é limitada aos recursos descentralizados (PDDE, por exemplo)."""})

# ── CE Metodologias ──────────────────────────────────────────

NOVOS.append({"id":"r-me-07","topico":"me-07","disciplina":"metodologias-ensino","bloco":"especificos",
"nome":"Hans-Joachim Koellreutter: criatividade e improvisação","incidencia":"media",
"versaoCurta":"""# Koellreutter — Criatividade e Improvisação

## Quem é
- **Hans-Joachim Koellreutter** (1915-2005): compositor e educador alemão radicado no Brasil
- Fundador do **Grupo Música Viva** (1939) — introdutor do dodecafonismo no Brasil
- Professor em Salvador, São Paulo, Rio de Janeiro, Índia; grande influência na pedagogia musical brasileira

## Concepção pedagógica
- **Educação musical como formação do ser humano completo** — não apenas treinamento técnico
- Música como meio para desenvolver: criatividade, senso crítico, consciência social
- Educador deve ser **parceiro** do aluno, não transmissor de verdades
- **Aula aberta**: sem roteiro fixo; parte das questões trazidas pelos alunos

## Improvisação e criatividade
- Improvisação como **ferramenta pedagógica central** — não só para "avançados"
- A partir de **pré-compositores** (estruturas parcialmente definidas)
- Objetivo: liberar a expressão criativa; trabalhar com sons antes de símbolos
- Aproximação com **estética contemporânea**: sons não-convencionais, ruído, silêncio

## Relação com Cage e Schafer
- Koellreutter, Cage e Schafer compartilham: abertura ao ruído; questionamento da música tonal
- Koellreutter: mais foco na interação pedagógica e no ser humano

## Para a prova
- Koellreutter ≠ método rígido: é **postura filosófica** sobre o ensino musical
- Palavra-chave: **sensibilização**, criatividade, improvisação, pré-compositores
- Diferença de Orff: Orff tem método estruturado; Koellreutter rejeita métodos fechados
- Influência: geração de educadores musicais brasileiros (décadas de 1970-90)
- Associado à ideia de "educação não-diretiva" aplicada à música""",
"versaoCompleta":"""# Hans-Joachim Koellreutter: Criatividade e Improvisação

## Trajetória

Hans-Joachim Koellreutter nasceu em Freiburg, Alemanha, em 1915. Fugindo do nazismo, chegou ao Brasil em 1937. Fundou em 1939, com Cláudio Santoro e outros, o **Grupo Música Viva**, que introduziu o dodecafonismo e as vanguardas europeias no cenário musical brasileiro.

Além de compositor, Koellreutter dedicou a maior parte de sua vida à **pedagogia musical**. Lecionou em Salvador (Seminários Livres de Música), São Paulo, Rio de Janeiro, Nova Delhi e em diversas universidades. Seu pensamento pedagógico amadureceu nas décadas de 1970-1990 e influenciou profundamente educadores musicais brasileiros.

## Filosofia Pedagógica

Para Koellreutter, a educação musical não deve ter como objetivo principal a formação de músicos profissionais, mas sim o **desenvolvimento integral do ser humano**. A música é meio, não fim.

Sua pedagogia parte de princípios:
- **Não há método**: métodos fechados são contraproducentes. O educador deve criar situações de aprendizagem abertas
- **Parceria**: professor e aluno são co-investigadores — o professor não sabe tudo
- **Relevância**: o conteúdo deve ter significado para o aluno no presente, não apenas como preparação para o futuro
- **Sensibilização**: educar a percepção antes de teorizar

## Improvisação como Pedagogia

Koellreutter desenvolveu a ideia dos **pré-compositores** — estruturas parcialmente definidas que deixam espaço para a decisão do performer/estudante. Isso permite trabalhar improvisação mesmo com iniciantes: não há certo ou errado absoluto, há intenção e expressão.

A improvisação serve para:
- Liberar a criatividade reprimida por anos de ensino normativo
- Desenvolver o ouvido de forma ativa
- Trabalhar conceitos (dinâmica, forma, textura) de forma vivencial
- Integrar sons não-convencionais e ruídos ao vocabulário musical

## Influência no Brasil

A geração de educadores formados por Koellreutter ou sob sua influência transformou o ensino de música no Brasil nas décadas de 1970-1990. Muitos professores dos CEPs e conservatórios foram impactados por sua visão de que o ensino musical deve ser experiencial, crítico e criativo."""})

NOVOS.append({"id":"r-me-08","topico":"me-08","disciplina":"metodologias-ensino","bloco":"especificos",
"nome":"Aplicação de metodologias em contexto escolar (questões situacionais)","incidencia":"alta",
"versaoCurta":"""# Aplicação de Metodologias em Contexto Escolar

## Como as questões situacionais funcionam
- Descrevem uma situação de sala de aula e perguntam QUAL metodologia melhor se aplica
- Ou descrevem uma prática e perguntam de qual autor ela deriva
- Exigem que você relacione prática ↔ teoria

## Mapa de correspondência prática → metodologia
| Prática descrita | Metodologia |
|---|---|
| Trabalho com sons do ambiente, gravações do entorno | **Schafer** (paisagem sonora) |
| Aluno avança por espiral (apreciação → performance → composição) | **Swanwick** (C(L)A(S)P / espiral) |
| Uso de instrumentos de percussão fáceis + movimento + fala | **Orff** (Schulwerk) |
| Solfejo relativo (Dó móvel) + fononímia + canções folclóricas | **Kodály** |
| Movimento corporal + ritmo + expressão pelo corpo | **Dalcroze** (euritmia) |
| Audiação; escuta interna antes de tocar; padrões tonais | **Gordon** (GIML) |
| Improvisação livre, pré-compositores, estética contemporânea | **Koellreutter** |

## Quando combinar metodologias
- A prova pode descrever uma aula que usa elementos de dois ou mais métodos
- Ex.: "professor usa movimento corporal (Dalcroze) + fononímia (Kodály)"
- Isso é válido! Cada método contribui com uma dimensão diferente

## Fatores de contexto que influenciam a escolha
- **Faixa etária**: Orff e Dalcroze são mais usados com crianças menores
- **Objetivo**: sensibilização sonora (Schafer) × formação técnica (Kodály) × apreciação crítica (Swanwick)
- **Recursos disponíveis**: Orff exige instrumentarium; Kodály pode ser feito só com voz
- **Contexto escolar regular × CEP**: CEP pode aprofundar teoria; escola regular foca em vivência

## Para a prova
- Leia a situação e identifique o ELEMENTO CENTRAL (o que o professor valoriza)
- Schafer: ouvido ativo, sons do cotidiano
- Swanwick: progressão do desenvolvimento; CLAPS
- Kodály: canção folclórica + solfejo relativo + fononímia
- Gordon: audiação = escuta interna ativa""",
"versaoCompleta":"""# Aplicação de Metodologias em Contexto Escolar

## A Natureza das Questões Situacionais

As questões situacionais apresentam um cenário pedagógico e pedem que o candidato identifique a fundamentação teórica, avalie a adequação da prática ou sugira alternativas. São mais complexas que questões de memorização porque exigem compreensão dos princípios — não apenas dos nomes.

## Princípios de Cada Método Aplicados

**Schafer**: o ponto de partida é o ambiente sonoro. Uma aula inspirada em Schafer começa com escuta ativa do espaço — sons da escola, do bairro, da natureza. O professor não diz o que é "bom" ou "mau" som; desenvolve a consciência sonora. Aplicações: mapas sonoros, gravações de campo, análise da poluição sonora.

**Swanwick**: o modelo C(L)A(S)P (Composição, Literatura, Apreciação, Skill-técnica, Performance) organiza as atividades em cinco áreas, com composição e apreciação como centrais. A espiral do desenvolvimento orienta expectativas para cada faixa etária: do domínio sensorial ao formal e de valores. Uma aula "swanwickiana" avalia se o aluno progrediram na espiral.

**Orff**: ritmo, fala, movimento e instrumentação simples. A sequência começa com o ostinato rítmico (padrão repetido) e vai adicionando camadas. O professor usa bordões (dó-sol), pentatônica. Aplicação: criação de acompanhamentos em xilofone + percussão corporal + canto.

**Kodály**: da canção folclónica ao solfejo. A criança aprende a cantar canções do repertório folclórico, depois o professor nomeia os intervalos e introduz fononímia (gestos das mãos). O solfejo relativo (Dó móvel) facilita a compreensão das relações tonais.

**Dalcroze**: o corpo como instrumento de aprendizagem. O professor canta ou toca enquanto os alunos expressam a música com o corpo inteiro — caminhada, salto, gestos, dança. Aprende-se ritmo e dinâmica com o corpo antes de nomear teoricamente.

**Gordon**: a audiação (escuta interna) precede a performance. O professor trabalha padrões tonais e rítmicos curtos, canta sem texto, varia contextos harmônicos. O aluno internaliza antes de executar.

## Escolha Contextualizada

Na prova, a resposta correta depende do elemento central da situação descrita. Se a questão descreve uma criança de 6 anos explorando sons de objetos cotidianos e o professor estimulando essa exploração sem corrigir, a referência é Schafer + Koellreutter. Se descreve adolescentes analisando estrutura de peças por nível de complexidade, a referência é Swanwick."""})

# ── BNCC Música ──────────────────────────────────────────────

NOVOS.append({"id":"r-bm-02","topico":"bm-02","disciplina":"bncc-musica","bloco":"especificos",
"nome":"Objetos de conhecimento: contextos e práticas, elementos da linguagem, materialidades","incidencia":"alta",
"versaoCurta":"""# BNCC Música — Objetos de Conhecimento

## O que são objetos de conhecimento
- São os conteúdos, conceitos e processos que estruturam as habilidades da BNCC
- Na Arte, organizam-se por linguagem (Artes Visuais, Dança, Música, Teatro)
- Para Música, os principais objetos de conhecimento são:

## Contextos e práticas
- Situações de apreciação, criação e performance musical em diferentes contextos
- Inclui: música do cotidiano, manifestações culturais, estilos e gêneros
- Contextualizar a música no tempo e no espaço
- Relacionar música com cultura, história e sociedade

## Elementos da linguagem musical
- **Altura**: grave-agudo; melodia; escalas; tonalidade
- **Duração**: ritmo; compasso; pulso; andamento
- **Intensidade**: dinâmica (piano-forte); expressão
- **Timbre**: qualidade sonora; fontes sonoras; texturas
- **Forma**: estrutura da peça (introdução, tema, seções)
- **Harmonia**: acordes; funções; progressões

## Materialidades
- Fontes e materiais sonoros: instrumentos convencionais e não-convencionais
- Voz humana como instrumento
- Objetos sonoros; sons eletrônicos; sons do ambiente
- Tecnologia: uso de aplicativos, DAWs, looperas no ensino de música

## Para a prova
- "Elementos da linguagem" = parâmetros sonoros: altura, duração, intensidade, timbre
- "Materialidades" = os meios e materiais para fazer música
- "Contextos e práticas" = onde e como a música acontece socialmente
- BNCC organiza esses objetos por etapa — progressão do simples ao complexo
- Habilidades = o que o aluno faz com esses objetos (EF15AR14, EF69AR25 etc.)""",
"versaoCompleta":"""# BNCC Música — Objetos de Conhecimento

## Estrutura das Habilidades na BNCC

A BNCC organiza o ensino de Arte em dois níveis: os **objetos de conhecimento** (o que se ensina) e as **habilidades** (o que o aluno aprende a fazer). As habilidades são codificadas: por exemplo, EF15AR14 = Ensino Fundamental 1º-5º ano, Área: Arte, habilidade número 14.

Para Música no EF, os objetos de conhecimento recorrentes são: Contextos e Práticas; Elementos da Linguagem; Materialidades; Notação e Registro Musical; Processos de Criação; Matrizes Estéticas e Culturais; Patrimônio Cultural; Arte e Tecnologia.

## Contextos e Práticas

"Contextos e práticas" refere-se à música como fenômeno cultural, histórico e social. Ensinar música nessa perspectiva significa não apenas tocar ou cantar, mas compreender:
- As condições de produção da música (quem faz, para quem, em que época)
- Os diferentes contextos de escuta (concerto, igreja, festa popular, rádio, streaming)
- As manifestações musicais da própria comunidade do aluno

Na BNCC, habilidades relacionadas a esse objeto pedem que o aluno **explore, identifique e analise** músicas em diferentes contextos e compare práticas musicais de distintas culturas.

## Elementos da Linguagem Musical

Os elementos da linguagem musical são os parâmetros constitutivos do som e da música:

- **Altura**: percepção de grave/agudo; melodia; intervalos; escalas; modos
- **Duração**: pulso, ritmo, compasso, andamento, figuras rítmicas
- **Intensidade**: dinâmica (piano, forte, crescendo, decrescendo)
- **Timbre**: qualidade que distingue instrumentos e vozes; textura
- **Forma**: estrutura de uma peça (A-B-A, tema e variações, rondó)
- **Harmonia**: relações entre sons simultâneos; acordes; tonalidade

As habilidades da BNCC pedem que o aluno perceba, nomeie e utilize esses elementos em atividades práticas.

## Materialidades

"Materialidades" são os meios, suportes e materiais para produzir música. Inclui:
- Instrumentos musicais tradicionais (violão, flauta, piano)
- Instrumentos alternativos/não-convencionais (objetos percussivos, corpo)
- Voz humana em suas possibilidades tímbricas
- Recursos tecnológicos: instrumentos eletrônicos, aplicativos, produção musical digital
- Sons eletroacústicos e sons do cotidiano (Schafer)"""})

NOVOS.append({"id":"r-bm-03","topico":"bm-03","disciplina":"bncc-musica","bloco":"especificos",
"nome":"Notação e registro musical; processos de criação na BNCC","incidencia":"media",
"versaoCurta":"""# BNCC — Notação, Registro e Criação

## Notação e registro musical
- A BNCC NÃO exige notação tradicional como pré-requisito para fazer música
- Valoriza **múltiplas formas de registro**: gráfico, corporal, digital, convencional
- Tipos de notação na BNCC:
  - **Convencional**: clave, figuras rítmicas, armadura de clave (abordagem progressiva)
  - **Não-convencional/gráfica**: símbolos próprios do aluno para representar sons
  - **Cifras e tablaturas**: notação popular; funcional para guitarra, violão
  - **Registro digital**: loops, gravações, sequenciamento

## Por que múltiplas notações
- Alunos chegam à escola com diferentes músicas (funk, sertanejo, pop) — grafias diversas
- Notação convencional é um sistema entre muitos; cada cultura tem o seu
- Objetivo: **letramento musical** no sentido amplo, não só leitura de pauta

## Processos de criação
- A BNCC valoriza explicitamente a **criação** como dimensão fundamental do fazer artístico
- Composição, improvisação e arranjo são processos criativos legítimos
- Mesmo na EI e EF1: experimentos sonoros, jogos musicais, invenção de melodias simples
- Criação coletiva: turma compõe juntos (arranjo, letra, beat)

## Dimensões da criação na BNCC
1. **Fruição**: apreciar, perceber, sentir
2. **Criação**: compor, improvisar, arranjar
3. **Reflexão**: pensar sobre o processo e o produto
4. **Expressão**: comunicar com a música

## Para a prova
- Criação ≠ virtuosismo: alunos sem experiência TAMBÉM criam
- Registro gráfico é válido e encorajado nos anos iniciais
- Notação convencional: introduzida progressivamente, não como porta de entrada
- Habilidades de criação: EF15AR16, EF69AR31 (entre outras) — ler os códigos""",
"versaoCompleta":"""# BNCC — Notação, Registro e Processos de Criação

## A Questão da Notação Musical

Historicamente, o ensino de música nas escolas foi confundido com o ensino de solfejo e leitura de partitura. A BNCC rompe com essa tradição ao reconhecer que a notação convencional é apenas um dos muitos sistemas de representação musical.

O objetivo da BNCC não é que todos os alunos leiam partituras, mas que desenvolvam **literacia musical** — a capacidade de criar, apreciar, refletir e expressar-se musicalmente usando os recursos disponíveis em seu contexto.

## Tipos de Registro Musical

**Notação convencional**: o sistema europeu ocidental de partitura. Inclui figuras rítmicas (semínima, colcheia), claves (sol, fá, dó), dinâmica, articulação. É um sistema preciso mas abstrato — exige aprendizagem sistemática.

**Notação gráfica não-convencional**: desenhos, símbolos inventados, mapas sonoros. Permite que crianças pequenas e iniciantes representem suas criações sem precisar dominar o sistema convencional. Murray Schafer foi pioneiro no uso pedagógico de notações gráficas.

**Cifras e tablaturas**: sistemas de notação popular muito usados no contexto da música popular brasileira (violão, guitarra). A cifragem funcional (C, Am, G7) é um sistema legítimo de representação harmônica.

**Registro digital**: gravações de áudio, sequenciamento em DAWs (programas de produção), loops. Constitui o "papel e lápis" dos músicos contemporâneos.

## Processos de Criação

A BNCC inclui a **criação** como dimensão central das competências específicas de Arte. Criar não significa ter talento especial — é processo que pode ser ensinado e praticado por todos.

Processos criativos musicais na escola:
- **Composição**: criar uma peça original (letra + melodia; peça instrumental)
- **Improvisação**: criação em tempo real, dentro de parâmetros (tonalidade, modo, ritmo base)
- **Arranjo**: recriar uma peça existente para o contexto/recursos disponíveis
- **Transformação sonora**: modificar sons com tecnologia (efeitos, equalização)"""})

NOVOS.append({"id":"r-bm-04","topico":"bm-04","disciplina":"bncc-musica","bloco":"especificos",
"nome":"Competências e habilidades por etapa (EF1-EF5, EF6-EF9, EM)","incidencia":"alta",
"versaoCurta":"""# BNCC — Competências e Habilidades de Música por Etapa

## Estrutura
- EF1-5 (1º-5º ano): habilidades EF15AR__ (Arte geral, inclui Música)
- EF6-9 (6º-9º ano): habilidades EF69AR__ (Arte geral, inclui Música)
- EM: habilidades EM13AR__ (Arte geral)

## EF Anos Iniciais (EF15AR) — foco em Música
- Exploração sonora e percepção de parâmetros (altura, duração, intensidade, timbre)
- Músicas do cotidiano; canções folclóricas; jogos musicais
- Criação de sons com corpo, voz e objetos
- Registro gráfico de sons (notação não-convencional)
- Exemplos: EF15AR14 (explorar instrumentos); EF15AR16 (improvisar sonoridades)

## EF Anos Finais (EF69AR) — foco em Música
- Análise de elementos da linguagem musical em repertório diverso
- Relação música-contexto histórico e cultural
- Prática vocal e/ou instrumental (coletiva e individual)
- Processos de criação: composição, arranjo, improvisação
- Notação (convencional + alternativa)
- Tecnologia musical; música eletrônica

## Ensino Médio (EM13AR)
- Arte como produção cultural e expressão do pensamento
- Aprofundamento das linguagens escolhidas
- Relações entre Arte, Ciência, Tecnologia e Inovação
- Projetos criativos de maior complexidade
- Itinerários formativos: Arte pode ser componente de aprofundamento

## Para a prova
- Habilidades são numeradas (EF15AR14) — decorar os temas, não todos os números
- Progressão: simples (EF1-5) → complexo (EF6-9) → autônomo (EM)
- No EM, Arte pode aparecer como componente do itinerário de Linguagens
- CEP-EMB vai além da BNCC: oferece ensino técnico/profissional de Música""",
"versaoCompleta":"""# BNCC — Competências e Habilidades de Música por Etapa

## Lógica da Progressão

A BNCC organiza as habilidades em blocos de anos e pressupõe progressão: habilidades dos anos iniciais são mais concretas e exploratórias; nos anos finais, tornam-se mais analíticas e criativas; no Ensino Médio, espera-se maior autonomia e aprofundamento.

## EF Anos Iniciais (1º ao 5º ano)

As habilidades de Arte dos anos iniciais (EF15AR) cobrem as quatro linguagens artísticas de forma integrada. As habilidades de Música pedem que o aluno:
- Explore e identifique elementos da música no cotidiano (sons da natureza, da cidade, instrumentos)
- Experimente formas de produção sonora com diferentes materiais e o próprio corpo
- Crie e improvise pequenas sequências sonoras
- Conheça e aprecie músicas de diferentes culturas, incluindo folclore brasileiro
- Registre suas criações com notações próprias ou gráficas

Nessa etapa, não há exigência de leitura de partitura. O professor deve priorizar a vivência musical prazerosa e exploratória.

## EF Anos Finais (6º ao 9º ano)

As habilidades (EF69AR) aprofundam o trabalho com elementos da linguagem, processos de criação e reflexão crítica. O aluno deve:
- Identificar e analisar elementos musicais (melodia, ritmo, harmonia, forma, timbre) em repertório diverso
- Pesquisar e contextualizar gêneros e estilos musicais em seu contexto histórico-cultural
- Praticar a música de forma coletiva (canto coral, banda, conjunto)
- Desenvolver processos de composição e arranjo
- Usar tecnologia musical de forma criativa
- Relacionar música com outras linguagens artísticas e com movimentos culturais

## Ensino Médio

No EM, Arte integra a Área de Linguagens e suas Tecnologias. As habilidades (EM13AR) são transversais às linguagens. Além disso, a Música pode ser aprofundada no **itinerário de Linguagens** — tanto no componente de Arte quanto, especificamente, em componentes eletivos relacionados à produção musical e tecnologia."""})

NOVOS.append({"id":"r-bm-05","topico":"bm-05","disciplina":"bncc-musica","bloco":"especificos",
"nome":"Integração com outras linguagens artísticas","incidencia":"media",
"versaoCurta":"""# BNCC — Integração das Linguagens Artísticas

## Por que integrar
- BNCC concebe Arte como área com QUATRO linguagens: Artes Visuais, Dança, Música, Teatro
- As linguagens não são estanques — dialogam historicamente e pedagogicamente
- Integração enriquece a experiência artística; evita fragmentação excessiva

## Conexões Música ↔ outras linguagens
| Música + | Conexão |
|---|---|
| **Dança** | Ritmo, tempo, espaço, expressão corporal; Dalcroze é elo natural |
| **Teatro** | Sonoplastia, música cênica, ópera, trilha sonora |
| **Artes Visuais** | Notação gráfica, capas de álbuns, videoclipes, instalações sonoras |
| **Literatura** | Letra de música, canção, poesia musicalizada, libreto |

## Artes integradas na escola
- **Performances interdisciplinares**: espetáculo com música, dança e teatro
- **Projetos temáticos**: ex. "Música e Resistência" (história + música + literatura)
- **Festivais escolares**: integram todas as linguagens da Arte
- **Trilha sonora para teatro**: alunos de Música criam música para peça teatral

## Dimensões compartilhadas
- **Fruição**: apreciar obras de diferentes linguagens
- **Criação**: criar em uma linguagem usando elementos de outra
- **Reflexão**: analisar as relações entre as artes

## Para a prova
- BNCC enfatiza: professor especialista em uma linguagem deve ter visão das quatro
- Integração ≠ diluição: cada linguagem mantém sua especificidade
- Música na dança: ritmo como organizador do movimento
- PCN de Arte (1997) já propunha integração; BNCC aprofundou
- Questões podem pedir exemplo de integração produtiva entre Música e Dança/Teatro""",
"versaoCompleta":"""# BNCC — Integração das Linguagens Artísticas

## Concepção Integrada de Arte

A BNCC adota a visão de Arte como área de conhecimento que abrange quatro linguagens: Artes Visuais, Dança, Música e Teatro. Essa visão, já presente nos PCN de Arte de 1997, reconhece que as linguagens artísticas não são compartimentos isolados, mas modos de expressão e criação que dialogam entre si e com outras áreas do conhecimento.

## Relações Históricas entre Linguagens

Na história da arte, as linguagens sempre se cruzaram. A **ópera** é síntese de música, teatro, cenografia (artes visuais) e movimento cênico. O **cinema** integra imagem, música, texto e interpretação. O **balé** combina dança e música de forma inseparável. As **instalações sonoras** de artistas contemporâneos são simultaneamente arte sonora e visual.

Na educação, essa integração oferece oportunidades pedagógicas ricas: uma aula sobre Carnaval pode envolver história, música (samba), dança (coreografia de bloco), artes visuais (fantasia, adereços) e teatro (narrativa do enredo).

## Relações Pedagógicas

**Música e Dança**: a euritmia de Dalcroze é o exemplo mais sistemático de integração corpo-música. Mas qualquer trabalho com ritmo corporal (Orff), com movimento expressivo ao som de música ou com criação coreográfica envolve ambas as linguagens.

**Música e Teatro**: a sonoplastia (criação de efeitos sonoros para cenas) é atividade pedagógica rica que desenvolve escuta criativa, expressão sonora e consciência dramática.

**Música e Artes Visuais**: notação gráfica experimental (Schafer), criação de capas de álbuns, representação visual de estruturas musicais (diagramas de forma), criação de videoclipes artísticos.

## Implicações para o Professor de Música

O professor de Música no contexto da BNCC não pode trabalhar apenas dentro da sua linguagem. As competências específicas de Arte exigem que o aluno compreenda a Arte em suas múltiplas dimensões. Isso não significa que o professor de música deva dominar Dança ou Teatro, mas que deve ter visão integrada e saber criar pontes."""})

NOVOS.append({"id":"r-bm-06","topico":"bm-06","disciplina":"bncc-musica","bloco":"especificos",
"nome":"Percussão corporal, improvisação, criação coletiva em contexto pedagógico","incidencia":"media",
"versaoCurta":"""# Percussão Corporal, Improvisação e Criação Coletiva

## Percussão corporal
- Uso do **corpo como instrumento de percussão**: palmas, pés, coxas, peito, boca
- Referência metodológica: **Carl Orff** (corpo como primeiro instrumento)
- Técnicas específicas: **body percussion** (projeto Barbatuques, Keith Terry)
- Vantagens pedagógicas:
  - Sem custo de instrumentos
  - Todos participam simultaneamente
  - Trabalha: ritmo, pulso, coordenação motora, atenção, coletividade

## Improvisação em sala de aula
- Improvisação não exige conhecimento prévio avançado
- Estratégias para iniciantes:
  - **Pergunta e resposta** (aluno responde o que professor "pergunta" ritmicamente)
  - **Improvisação dentro de estrutura**: pentatônica (escala sem semitons — difícil errar)
  - **Pré-compositores** (Koellreutter): parâmetros parcialmente definidos
  - **Escuta e resposta**: aluno improvisa sobre base gravada
- Desenvolvimento: do rítmico → ao melódico → ao harmônico

## Criação coletiva
- Processo de criação onde TODA a turma contribui
- Princípios: respeito às ideias de todos; registro das decisões; revisão coletiva
- Produtos: composição coletiva, arranjo de canção, trilha sonora, peça rítmica
- **Processo** importa tanto quanto o produto final

## Para a prova
- Body percussion: Orff + Barbatuques (influência no cenário brasileiro)
- Improvisação pentatônica: primeira forma de improvisar melodicamente (não há notas "erradas")
- Criação coletiva: metodologia ativa; contrasta com aula expositiva
- BNCC valoriza: criação, protagonismo estudantil, trabalho colaborativo
- Diferença: improvisação (em tempo real) × composição (produto finalizado)""",
"versaoCompleta":"""# Percussão Corporal, Improvisação e Criação Coletiva

## Percussão Corporal como Pedagogia

Carl Orff foi o educador que sistematizou o uso do corpo como instrumento de percussão dentro de uma metodologia educacional. O princípio é simples: o instrumento mais acessível de todos já está disponível — o próprio corpo. Palmas simples, palmas nos joelhos, estalar de dedos e batidas no peito são as quatro fontes básicas da percussão corporal (correspondendo, grosseiramente, a quatro timbres distintos).

No contexto contemporâneo, o **Barbatuques** (grupo brasileiro fundado em 1995 por Fernando Barba) elevou a percussão corporal a uma forma de arte elaborada e influenciou fortemente a educação musical no Brasil. Keith Terry, nos EUA, desenvolveu o **body music** de forma sistemática.

Pedagogicamente, a percussão corporal permite:
- Trabalho rítmico sem custo de instrumentos
- Participação simultânea de toda a turma
- Integração de movimento e música
- Desenvolvimento de atenção, coordenação motora e coletividade

## Improvisação Estruturada

O grande medo de professores e alunos na improvisação é "errar". A pedagogia musical contemporânea resolveu esse problema com técnicas que reduzem o risco de dissonâncias indesejadas:

**Escala pentatônica**: ao usar apenas as cinco notas da pentatônica maior (dó-ré-mi-sol-lá), qualquer combinação é aceitável — não há semitons que criem tensão irresolvida.

**Estrutura de pergunta e resposta (call and response)**: o professor ou um aluno "pergunta" ritmicamente e outro "responde". Cria estrutura e diálogo sem exigir elaboração complexa.

**Bordão**: um grupo mantém uma base rítmica ou harmônica simples (ostinato) enquanto outros improvisam sobre ela.

## Criação Coletiva como Metodologia Ativa

A criação coletiva coloca os alunos no papel de criadores — não apenas intérpretes. É uma forma de **aprendizagem ativa** que desenvolve competências criativas, negociação, escuta e síntese.

O processo típico: o professor propõe um desafio (criar uma peça de 16 compassos sobre determinado tema), os alunos propõem ideias, o grupo decide coletivamente, registra, toca, revisa e apresenta."""})

NOVOS.append({"id":"r-bm-07","topico":"bm-07","disciplina":"bncc-musica","bloco":"especificos",
"nome":"PCN de Arte — especificidades da música","incidencia":"baixa",
"versaoCurta":"""# PCN de Arte — Especificidades da Música

## O que são os PCN
- **Parâmetros Curriculares Nacionais** (1997-1998): documentos orientadores do MEC
- Não são normativos como a BNCC — são referenciais/sugestivos
- PCN de Arte (1ª a 4ª série e 5ª a 8ª série): específicos para Arte
- Foram a principal referência para o ensino de Arte antes da BNCC (2017)

## PCN de Arte — estrutura
- Arte organizada em 4 linguagens: **Artes Visuais, Música, Teatro, Dança**
- Para cada linguagem: objetivos, conteúdos, orientações didáticas, critérios de avaliação

## Especificidades da Música nos PCN
- Três eixos norteadores:
  1. **Fazer artístico** (produção musical, performance, criação)
  2. **Apreciação** (escuta ativa e reflexiva)
  3. **Reflexão** (contextualização histórica e cultural)
- Propõe atividades de: improvisação, composição, execução, apreciação orientada
- Valoriza o repertório musical do aluno como ponto de partida

## Diferenças PCN × BNCC
| PCN (1997) | BNCC (2017) |
|---|---|
| Referencial/sugestivo | Normativo/obrigatório |
| Linguagens separadas por caderno | Área integrada (4 linguagens) |
| Eixos: fazer/apreciar/refletir | Dimensões: criar/fruir/refletir/expressar |
| Não tem habilidades codificadas | Tem habilidades codificadas (EF15AR) |

## Para a prova
- PCN foi substituído como referência principal pela BNCC em 2017
- Os princípios dos PCN ainda aparecem em questões históricas ou comparativas
- Eixos PCN música: produção / apreciação / reflexão
- A estrutura dos PCN influenciou diretamente a BNCC""",
"versaoCompleta":"""# PCN de Arte — Especificidades da Música

## Contexto dos PCN

Os Parâmetros Curriculares Nacionais foram publicados pelo MEC em 1997 (1ª a 4ª séries) e 1998 (5ª a 8ª séries), durante o governo FHC. Representaram a primeira grande tentativa de sistematização nacional do currículo escolar brasileiro após a LDB/96. Os PCN de Arte trouxeram um avanço significativo: reconheceram quatro linguagens artísticas (Artes Visuais, Música, Teatro e Dança) como áreas legítimas de conhecimento escolar, rompendo com a tradição de reduzir Arte à Educação Artística polivalente.

Embora tenham sido orientações referenciais (não normas obrigatórias), os PCN influenciaram fortemente a formação docente e a produção de materiais didáticos por duas décadas.

## Os Três Eixos da Música nos PCN

**Fazer artístico**: atividades práticas de criação e performance musical — tocar, cantar, improvisar, compor. A ênfase é no fazer como forma de conhecimento, não apenas na teoria.

**Apreciação**: escuta ativa e reflexiva de diferentes repertórios musicais. O PCN distingue apreciação de simples audição: apreciar significa ouvir com atenção e intenção analítica.

**Contextualização/reflexão**: relacionar a música com seu contexto de produção — histórico, social, cultural. Inclui: história da música, análise de estilos e gêneros, reflexão sobre o papel da música na sociedade.

## Conteúdos de Música nos PCN

Para os Anos Iniciais: exploração de sons e silêncio; canções folclóricas; percepção dos elementos da música (ritmo, melodia); criação de músicas simples; iniciação à notação.

Para os Anos Finais: elementos da linguagem musical com maior precisão técnica; apreciação de repertório erudito e popular; improvisação e composição mais elaboradas; história da música brasileira e ocidental.

## Transição para a BNCC

A BNCC incorporou os princípios fundamentais dos PCN (quatro linguagens, integração entre produção/apreciação/reflexão) e os aprofundou com as seis dimensões do conhecimento artístico e o sistema de habilidades codificadas."""})

todos = dados["resumos"] + [r for r in NOVOS if r["topico"] not in existentes]
dados["resumos"] = todos
dados["versao"] = "2.4.0"
with open(SRC,"w",encoding="utf-8") as f: json.dump(dados,f,ensure_ascii=False,indent=2)
print(f"Batch 4 OK — total: {len(todos)}")
