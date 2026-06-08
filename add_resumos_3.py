#!/usr/bin/env python3
"""Batch 3: pp-01, pp-02, pp-04, pp-05, pp-06, gp-01 to gp-04"""
import json, pathlib
BASE = pathlib.Path(__file__).parent
SRC  = BASE / "data" / "resumos.json"
with open(SRC) as f: dados = json.load(f)
existentes = {r["topico"] for r in dados["resumos"]}
NOVOS = []

NOVOS.append({"id":"r-pp-01","topico":"pp-01","disciplina":"politicas-publicas","bloco":"complementares",
"nome":"BNCC — Base Nacional Comum Curricular (completa, ênfase em Arte/Música)","incidencia":"alta",
"versaoCurta":"""# BNCC — Base Nacional Comum Curricular

## O que é
- Documento normativo que define competências e habilidades para toda a EB
- Aprovado pelo CNE, homologado pelo MEC em **2017 (EI+EF)** e **2018 (EM)**
- Referência obrigatória para elaboração de currículos de redes públicas e privadas
- NÃO é currículo — é base mínima (60% do currículo); parte diversificada = 40%

## Estrutura
- **10 Competências Gerais** (transversais a todas as etapas)
- Organizada por **Áreas de Conhecimento** e **Componentes Curriculares**
- EF: Línguas | Matemática | Ciências | Ciências Humanas | **Arte**
- **Arte** inclui 4 linguagens: Artes Visuais, Dança, Música, Teatro

## Arte na BNCC — estrutura
- Objeto de conhecimento: **Contextos e Práticas / Elementos da Linguagem / Materialidades / Notação e Registro / Processos de Criação**
- Competências específicas de Arte: 9 no EF
- Dimensões do conhecimento artístico: criação, crítica, estesia, expressão, fruição, reflexão

## Música especificamente
- Componente Arte com ênfase em Música nos CEPs (CEP-EMB)
- Habilidades musicais: apreciação, criação, performance, reflexão
- Do EF1 ao EM: progressão de habilidades

## Para a prova
- BNCC: competências e habilidades (habilidades = mais específicas, com código EF/EM)
- Arte = área que abrange QUATRO linguagens — não só Artes Visuais
- "Competências gerais" são 10 e valem para TODAS as etapas
- BNCC orienta mas não determina metodologia — professor tem autonomia didática
- Currículo em Movimento do DF deve ser compatível com a BNCC""",
"versaoCompleta":"""# BNCC — Base Nacional Comum Curricular

## Contexto e Aprovação

A Base Nacional Comum Curricular (BNCC) é um documento normativo previsto na CF/88 (art. 210), na LDB (art. 26) e no PNE (Meta 7). Após intenso processo de consulta pública e debates, foi homologada pelo MEC:
- **Versão para Educação Infantil e Ensino Fundamental**: dezembro de 2017
- **Versão para Ensino Médio**: dezembro de 2018

## As 10 Competências Gerais

As competências gerais são transversais e devem ser desenvolvidas ao longo de toda a Educação Básica:
1. Conhecimento
2. Pensamento científico, crítico e criativo
3. Repertório cultural
4. Comunicação
5. Cultura digital
6. Trabalho e projeto de vida
7. Argumentação
8. Autoconhecimento e autocuidado
9. Empatia e cooperação
10. Responsabilidade e cidadania

## Estrutura Curricular

O EF é organizado em 5 áreas: Linguagens (LP, Arte, EF, LI); Matemática; Ciências da Natureza; Ciências Humanas; Ensino Religioso. A área de **Linguagens** inclui o componente **Arte**, que é o mais relevante para o professor de música.

## Arte na BNCC

A BNCC reconhece a Arte como área de conhecimento com **quatro linguagens artísticas**: Artes Visuais, Dança, Música e Teatro. Essa concepção é herdada dos PCN de Arte (1997) e consolidada na BNCC.

As **dimensões do conhecimento artístico** são: criação, crítica, estesia, expressão, fruição e reflexão. Elas orientam o desenvolvimento das habilidades ao longo das etapas.

Os **objetos de conhecimento** da Arte incluem: Contextos e Práticas; Elementos da Linguagem; Materialidades; Notação e Registro Musical (específico de música); Processos de Criação; Matrizes Estéticas e Culturais; Patrimônio Cultural; Arte e Tecnologia.

## Relação com o Currículo

A BNCC não é o currículo — define o mínimo comum (60%). Os outros 40% são definidos pelas redes de ensino e escolas, considerando as especificidades locais. O **Currículo em Movimento** do DF foi reformulado para incorporar as competências e habilidades da BNCC."""})

NOVOS.append({"id":"r-pp-02","topico":"pp-02","disciplina":"politicas-publicas","bloco":"complementares",
"nome":"Diretrizes Curriculares Nacionais Gerais para Educação Básica","incidencia":"media",
"versaoCurta":"""# DCNs — Diretrizes Curriculares Nacionais Gerais

## O que são
- **Resolução CNE/CEB nº 4/2010** + Pareceres complementares
- Documento do Conselho Nacional de Educação que orienta a organização, articulação, desenvolvimento e avaliação da Educação Básica
- Complementam a LDB e antecedem a BNCC

## Princípios das DCNs
- Ética: autonomia, responsabilidade, solidariedade, respeito ao bem comum
- Políticos: direitos de cidadania, exercício da criticidade, respeito à ordem democrática
- Estéticos: sensibilidade, criatividade, ludicidade, liberdade de expressão

## Concepção de currículo
- Currículo como experiências escolares em todas as interações
- Vinculação com o mundo do trabalho e a prática social
- Articulação entre conhecimentos escolares e cotidiano
- Deve contemplar: Base Nacional Comum + Parte Diversificada

## DCNs específicas relevantes para música
- **DCN para Arte** (Parecer CNE/CEB 22/2005 + Resolução 4/2006): orientações para Arte como área do conhecimento
- **DCN para Educação Profissional** (Resolução CNE/CEB 6/2012): inclui cursos de música nos CEPs

## Relação entre documentos
- CF/88 → LDB → DCNs → BNCC → Currículo das redes → PPP das escolas

## Para a prova
- DCNs = normas do CNE; BNCC = documento de referência curricular do MEC
- DCNs gerais (Res. 4/2010) + DCNs específicas por etapa/modalidade
- Hierarquia: CF → LDB → DCNs → currículos locais
- Princípios das DCNs: éticos, políticos e estéticos (tríade recorrente)""",
"versaoCompleta":"""# Diretrizes Curriculares Nacionais Gerais para Educação Básica

## Base Legal

As Diretrizes Curriculares Nacionais (DCNs) são elaboradas pelo **Conselho Nacional de Educação (CNE)** com base no art. 9º, IV da LDB, que atribui à União (por meio do CNE) a responsabilidade de estabelecer diretrizes para a educação nacional. A Resolução CNE/CEB nº 4/2010 institui as DCNs Gerais para a Educação Básica.

## Função das DCNs

As DCNs não são currículo — são **normas obrigatórias** que orientam o planejamento, desenvolvimento e avaliação das práticas pedagógicas. Elas orientam:
- A elaboração dos projetos políticos-pedagógicos das escolas
- A formação inicial e continuada de professores
- A produção de materiais didáticos
- A avaliação em larga escala

## Os Três Princípios Fundamentais

As DCNs organizam o trabalho pedagógico a partir de três dimensões:

**Éticas**: autonomia, responsabilidade, solidariedade e respeito ao bem comum.

**Políticas**: direitos de cidadania, exercício da criticidade, respeito à ordem democrática.

**Estéticas**: sensibilidade, criatividade, ludicidade e liberdade de expressão nas diferentes manifestações artísticas e culturais.

A dimensão estética é especialmente relevante para o ensino de Arte e Música.

## Concepção de Currículo

As DCNs adotam uma concepção ampla de currículo: o conjunto de valores e práticas que proporciona a produção, a socialização de significados no espaço social e contribui para a construção da identidade sociocultural do educando.

A organização curricular contempla a **Base Nacional Comum** (competências e saberes definidos nacionalmente) e a **Parte Diversificada** (saberes que atendem às especificidades regionais e locais — mínimo 20% da carga horária).

## DCNs Específicas para Arte

A Resolução CNE/CEB nº 4/2006 (complementada pelo Parecer 22/2005) estabelece as DCNs para o ensino de Arte nas escolas públicas de Educação Básica. Reconhece as quatro linguagens artísticas (Artes Visuais, Dança, Música e Teatro) e a necessidade de professores habilitados por linguagem."""})

NOVOS.append({"id":"r-pp-04","topico":"pp-04","disciplina":"politicas-publicas","bloco":"complementares",
"nome":"Diretrizes de Avaliação Educacional da SEDF","incidencia":"media",
"versaoCurta":"""# Diretrizes de Avaliação Educacional da SEDF

## O que são
- Documento da SEDF que orienta as práticas avaliativas nas escolas do DF
- Fundamentadas na LDB, BNCC, DCNs e Currículo em Movimento
- Concebem avaliação como **processo contínuo, diagnóstico e formativo**

## Três dimensões da avaliação
1. **Avaliação da aprendizagem** (nível da sala de aula)
   - Contínua, processual, formativa
   - Uso de instrumentos diversificados: provas, portfolios, autoavaliação, projetos
   - Feedback como instrumento pedagógico

2. **Avaliação institucional** (nível da escola)
   - Auto-avaliação da escola (processos, estrutura, gestão)
   - Participação de toda a comunidade escolar
   - Alimenta o PPP

3. **Avaliação em larga escala** (nível dos sistemas — externo)
   - SAEB, PISA, AVALIAÇÃO DISTRITAL
   - Fornece dados para políticas públicas
   - NÃO deve ser a única referência para avaliação do aluno

## Princípios
- Avaliação a **serviço da aprendizagem** (não como punição ou classificação)
- Caráter **diagnóstico**: identifica o que o aluno sabe e o que precisa aprender
- Caráter **formativo**: orienta o processo de ensino-aprendizagem
- Caráter **somativo** (no final do processo): registra o resultado final para promoção

## Para a prova
- Avaliação diagnóstica: ANTES do ensino (para planejar)
- Avaliação formativa: DURANTE o ensino (para ajustar)
- Avaliação somativa: AO FINAL (para verificar o resultado)
- Nota/conceito: instrumento de registro, não fim da avaliação
- SEDF usa tanto nota (1-10) quanto conceitos (EB, EI) conforme etapa""",
"versaoCompleta":"""# Diretrizes de Avaliação Educacional da SEDF

## Fundamentos

As Diretrizes de Avaliação Educacional da SEDF partem de um conceito ampliado de avaliação, em que avaliar significa produzir informações para tomar decisões pedagógicas, não apenas classificar ou reprovar alunos. Estão fundamentadas no art. 24, V da LDB (critérios de avaliação para promoção) e nas DCNs.

## As Três Dimensões

**Avaliação da Aprendizagem**

No nível da sala de aula, a avaliação deve ser contínua e usar instrumentos diversificados. A SEDF orienta que nenhuma avaliação seja pontual ou isolada — cada instrumento deve dialogar com os objetivos de aprendizagem do componente curricular. São reconhecidos como instrumentos válidos: provas escritas e orais, trabalhos individuais e coletivos, portfólios, apresentações, projetos, autoavaliação e coavaliação.

O **feedback** é elemento central: a avaliação formativa só cumpre seu papel quando o professor retorna a informação ao aluno de forma que ele possa refletir sobre seu processo e retomar o aprendizado.

**Avaliação Institucional**

A avaliação institucional é a autoavaliação da escola. Envolve a análise de indicadores como: frequência, aprovação, abandono, clima escolar, uso do tempo pedagógico, condições de infraestrutura. Deve ser realizada pela comunidade escolar (professores, gestão, pais, alunos) e alimenta a revisão do PPP.

**Avaliação em Larga Escala**

Os sistemas externos (SAEB, PISA, Avaliação Distrital da SEDF) produzem dados sobre o desempenho dos estudantes em escala nacional e distrital. Esses dados informam políticas públicas mas não devem substituir a avaliação formativa. O professor não pode orientar o ensino exclusivamente para a prova externa ("teaching to the test").

## Progressão e Retenção

O sistema do DF combina avaliação contínua com o registro de notas/conceitos ao final de cada período. As diretrizes orientam que a retenção seja decisão colegiada (Conselho de Classe), precedida de recuperação paralela e ao final do período."""})

NOVOS.append({"id":"r-pp-05","topico":"pp-05","disciplina":"politicas-publicas","bloco":"complementares",
"nome":"Decreto nº 44.918/2023 — valorização das mulheres na SEEDF","incidencia":"baixa",
"versaoCurta":"""# Decreto nº 44.918/2023 — Mulheres na SEEDF

## O que é
- Decreto do Governador do DF que institui a **Política de Valorização das Mulheres** no âmbito da Secretaria de Estado de Educação
- Foco: garantir condições equânimes para profissionais da educação do sexo feminino

## Contexto
- Maioria dos professores da rede pública é mulher (≈ 75%)
- Decreto reconhece a **feminização do magistério** como fenômeno histórico
- Propõe ações afirmativas e medidas de combate à discriminação de gênero

## Medidas previstas
- Formação continuada com perspectiva de gênero
- Combate ao assédio moral e sexual no ambiente escolar
- Garantia de licenças e afastamentos previstos em lei
- Criação de espaços de discussão sobre equidade de gênero
- Integração com o Plano Distrital de Política para as Mulheres

## Princípios
- Igualdade de gênero
- Não discriminação
- Equidade
- Valorização profissional

## Para a prova
- Decreto 44.918/2023 = política de gênero para SERVIDORAS da educação do DF
- Não é política para alunas — é para profissionais da educação
- Contexto: feminização do magistério público
- Articulado com o Plano Distrital de Política para Mulheres (2020-2023)
- Questões cobram: objeto do decreto, público-alvo, princípios""",
"versaoCompleta":"""# Decreto nº 44.918/2023 — Valorização das Mulheres na SEEDF

## Contexto da Feminização do Magistério

O ensino público brasileiro, especialmente na Educação Básica, é predominantemente exercido por mulheres. Dados nacionais indicam que cerca de 80% dos professores do Ensino Fundamental são mulheres. Esse fenômeno — a **feminização do magistério** — tem raízes históricas no século XIX, quando o ensino primário foi gradualmente cedido às mulheres como extensão "natural" do cuidado doméstico e da maternidade.

Essa feminização coexiste com desigualdades: as mulheres ocupam menos cargos de direção e gestão; acumulam trabalho doméstico e profissional (dupla jornada); estão sujeitas a assédio moral e sexual no ambiente de trabalho.

## O Decreto 44.918/2023

O decreto do Governador do DF institui, no âmbito da SEEDF, uma política de valorização voltada especificamente para as profissionais da educação. Reconhece que a maioria dos servidores da Secretaria é mulher e que as políticas institucionais precisam contemplar essa realidade.

As medidas incluem:
- Inclusão da perspectiva de gênero na formação continuada oferecida pela EAPE
- Mecanismos de denúncia e apuração de assédio moral e sexual
- Facilitação do acesso às licenças previstas em lei (licença-maternidade, licença para tratamento de saúde, etc.)
- Integração com a rede de proteção à mulher do GDF

## Articulação com Outros Instrumentos

O decreto deve ser lido em conjunto com o **Plano Distrital de Política para as Mulheres (2020-2023)** e com a Lei Maria da Penha (Lei 11.340/2006), que prevê medidas protetivas para mulheres vítimas de violência doméstica — incluindo garantias no emprego durante o período de afastamento."""})

NOVOS.append({"id":"r-pp-06","topico":"pp-06","disciplina":"politicas-publicas","bloco":"complementares",
"nome":"Plano Distrital de Política para Mulheres 2020-2023","incidencia":"baixa",
"versaoCurta":"""# Plano Distrital de Política para Mulheres 2020-2023

## O que é
- Instrumento de planejamento do GDF para garantir direitos e promover equidade de gênero
- Articulado com a **Política Nacional para as Mulheres** e com a **CEDAW** (Convenção da ONU)
- Coordenado pela **Secretaria da Mulher do DF**

## Eixos temáticos
1. Saúde das mulheres
2. Educação inclusiva e não sexista
3. Enfrentamento à violência
4. Trabalho, emprego e autonomia econômica
5. Participação política e poder
6. Cultura, comunicação e mídia não sexista
7. Desenvolvimento sustentável

## Educação no Plano
- Promover educação não sexista em todos os níveis
- Incluir perspectiva de gênero na formação de professores
- Combater o sexismo nos materiais didáticos e nas práticas pedagógicas
- Garantir ambientes escolares seguros para meninas e mulheres

## Relação com a SEDF
- Decreto 44.918/2023 operacionaliza o eixo de educação no âmbito da SEDF
- Formação continuada da EAPE deve incluir temática de gênero e equidade

## Para a prova
- Vigência: 2020-2023 (pode haver nova versão)
- Secretaria da Mulher do DF coordena
- Eixo educação = combate ao sexismo, formação docente com perspectiva de gênero
- Questões cobram relação entre o Plano e a política educacional da SEDF
- Articulado com: Decreto 44.918/2023, Lei Maria da Penha, Convenção de Belém do Pará""",
"versaoCompleta":"""# Plano Distrital de Política para Mulheres 2020-2023

## Contexto

O Plano Distrital de Política para as Mulheres (PDPM) é o instrumento de planejamento plurianual do Governo do Distrito Federal para a promoção da igualdade de gênero. Integra um sistema de políticas públicas que inclui a Política Nacional para as Mulheres e os compromissos internacionais do Brasil, em especial a **CEDAW** (Convenção sobre a Eliminação de Todas as Formas de Discriminação contra a Mulher) e a **Convenção de Belém do Pará** (que trata da violência contra a mulher).

## Estrutura e Eixos

O PDPM organiza-se em sete eixos temáticos, cada um com objetivos, metas e estratégias específicas. O eixo de maior relevância para o contexto educacional é o **Eixo 2 — Educação Inclusiva e Não Sexista**.

**Eixo 2 — Educação:**
- Promover revisão dos materiais didáticos para eliminar representações sexistas
- Incluir a perspectiva de gênero na formação inicial e continuada de docentes
- Criar programas de combate ao assédio e à violência de gênero nas escolas
- Garantir acesso equânime de meninas e mulheres a todas as etapas e modalidades de ensino
- Apoiar meninas em situação de violência ou gravidez na adolescência

## A Secretaria da Mulher

A **Secretaria de Estado da Mulher do DF** coordena a implementação, o monitoramento e a avaliação do PDPM. Articula-se com outras secretarias — especialmente a SEDF — para implementar as medidas nos eixos de educação e trabalho.

## Relevância para o Professor

O professor de Educação Básica é agente fundamental da educação não sexista. O PDPM orienta que a formação docente deve capacitar professores para:
- Identificar e questionar estereótipos de gênero no currículo
- Promover ambientes de aprendizagem seguros e inclusivos para meninas
- Intervir em situações de assédio ou violência de gênero no ambiente escolar"""})

# ── Gestão Pedagógica ─────────────────────────────────────────

NOVOS.append({"id":"r-gp-01","topico":"gp-01","disciplina":"gestao-pedagogica","bloco":"complementares",
"nome":"Planejamento escolar (concepção, modalidades, importância)","incidencia":"alta",
"versaoCurta":"""# Planejamento Escolar

## O que é
- Processo de antecipação, organização e tomada de decisões pedagógicas
- Instrumento que orienta a prática docente de forma intencional
- Baseia-se em: diagnóstico da realidade + objetivos + estratégias + avaliação

## Modalidades de planejamento
| Modalidade | Abrangência | Instrumento |
|---|---|---|
| **Planejamento de sistema** | Nacional/estadual/municipal | PNE, PDE, currículos |
| **Planejamento escolar** | Toda a escola | PPP |
| **Planejamento curricular** | Componente / área | Plano curricular anual |
| **Planejamento de ensino** | Professor / turma | Plano de aula, plano de unidade |

## Plano de aula — elementos básicos
1. Identificação (turma, componente, data)
2. Objetivos de aprendizagem
3. Conteúdos/habilidades (BNCC)
4. Metodologia/estratégias
5. Recursos didáticos
6. Avaliação (instrumentos e critérios)
7. Referências

## Características do bom planejamento
- **Flexível**: pode ser ajustado à realidade da turma
- **Coerente**: objetivos, metodologia e avaliação alinhados
- **Participativo**: envolve os sujeitos (quando possível)
- **Contínuo**: processo permanente, não eventual
- **Diagnóstico**: parte do que o aluno já sabe

## Para a prova
- Planejamento é mediação entre o ideal (currículo) e o real (sala de aula)
- Plano de aula ≠ planejamento — o plano é o registro escrito; planejamento é o processo
- Coordenação pedagógica: espaço para planejamento coletivo na SEDF
- Planejamento por projetos, sequências didáticas e situações de aprendizagem são formas organizativas""",
"versaoCompleta":"""# Planejamento Escolar

## Conceito e Fundamentos

O planejamento escolar é a atividade intencional de organização do trabalho pedagógico. Não se restringe ao preenchimento de formulários — é processo reflexivo em que o professor (e a equipe) define o que ensinar, como ensinar, para quem ensinar, com quais recursos e como avaliar se os objetivos foram alcançados.

O planejamento fundamenta-se em uma **concepção de educação**: quem planeja de forma tecnicista segue roteiros prescritos; quem planeja de forma crítico-reflexiva parte do diagnóstico da realidade dos alunos e articula o conhecimento escolar com a vida social.

## Modalidades e Hierarquia

O planejamento opera em diferentes níveis, do mais abrangente ao mais específico:

**Planejamento de Sistema**: define as políticas educacionais em nível nacional (PNE), estadual/distrital (PDE) e municipal (PME). Define o currículo comum (BNCC).

**Planejamento Escolar**: traduz as diretrizes do sistema na realidade específica da escola, através do **Projeto Político-Pedagógico (PPP)**.

**Planejamento Curricular**: organiza os componentes curriculares, sequências de conteúdos e objetivos por etapa/ano. É elaborado coletivamente na coordenação pedagógica.

**Planejamento de Ensino**: do professor para a turma. Pode ser: plano anual/semestral (visão geral), plano de unidade (período temático), plano de aula (encontro específico).

## Elementos do Plano de Aula

Um plano de aula bem estruturado inclui: identificação; objetivos claros e mensuráveis; habilidades da BNCC; conteúdos; estratégias metodológicas; recursos; duração prevista para cada etapa; e formas de avaliação. Os objetivos devem ser formulados com verbos de ação que indiquem o nível cognitivo (lembrar, compreender, aplicar, analisar, avaliar, criar — Taxonomia de Bloom revisada).

## Planejamento e Coordenação na SEDF

Na SEDF, as coordenações pedagógicas coletivas são espaços privilegiados para o planejamento colaborativo. O professor de música, especialmente no CEP-EMB, participa de coordenações específicas da área junto com os pares."""})

NOVOS.append({"id":"r-gp-02","topico":"gp-02","disciplina":"gestao-pedagogica","bloco":"complementares",
"nome":"Projeto Político-Pedagógico (PPP)","incidencia":"alta",
"versaoCurta":"""# Projeto Político-Pedagógico (PPP)

## O que é
- Documento que expressa a **identidade, os valores e as intencionalidades pedagógicas** de uma escola
- Base legal: LDB art. 12-14 (autonomia da escola, participação docente e da comunidade)
- É **político** (expressa opções de valor) e **pedagógico** (orienta a prática educativa)
- Construção coletiva: envolve professores, gestão, pais e alunos

## O que contém (elementos obrigatórios)
1. **Diagnóstico da realidade escolar** (perfil da comunidade, dados de aprovação, evasão)
2. **Marco referencial** (concepção de educação, homem, sociedade)
3. **Marco operacional** (metas, objetivos, estratégias)
4. **Proposta curricular** (organização dos componentes, carga horária)
5. **Gestão e organização** (conselho escolar, grêmio, AP)
6. **Avaliação do próprio PPP** (mecanismos de revisão)

## Princípios (segundo Veiga)
- Igualdade de condições de acesso e permanência
- Qualidade para todos
- Gestão democrática
- Liberdade
- Valorização do magistério

## Gestão democrática e PPP
- LDB art. 14: sistemas garantirão participação de **docentes** na elaboração do PPP
- E participação da **comunidade escolar** e local em conselhos
- PPP não é documento do diretor — é da comunidade escolar

## Para a prova
- PPP ≠ Regimento Escolar: PPP = intencionalidades / Regimento = normas de funcionamento
- PPP deve ser revisado periodicamente (não é estático)
- Art. 12, I, LDB: escola deve elaborar e executar sua proposta pedagógica
- Art. 13, I: professor deve participar da elaboração do PPP""",
"versaoCompleta":"""# Projeto Político-Pedagógico (PPP)

## Natureza e Fundamentos

O PPP é o documento de identidade da escola — uma espécie de "constituição" que orienta todas as decisões pedagógicas, administrativas e comunitárias. Ilma Passos Veiga, referência teórica fundamental sobre o tema, define o PPP como uma ação intencional com sentido explícito e compromisso coletivo.

A dimensão **política** remete ao compromisso com a formação cidadã: o PPP expressa a visão de sociedade e de pessoa que a escola quer ajudar a construir. A dimensão **pedagógica** refere-se à organização do trabalho escolar para alcançar esses objetivos.

## Base Legal

O art. 12 da LDB obriga as escolas a elaborar e executar sua proposta pedagógica. O art. 13 impõe aos professores a obrigação de participar da elaboração dessa proposta. O art. 14 exige que os sistemas de ensino garantam a participação dos profissionais da educação e da comunidade na gestão escolar.

## Estrutura Típica

O PPP inclui diagnóstico da realidade (contexto socioeconômico, indicadores de aprendizagem, necessidades identificadas), marco referencial (concepção de educação e de homem) e marco operacional (objetivos, metas, estratégias, cronograma).

## Gestão Democrática

A construção do PPP é, em si, um ato de gestão democrática. Quando elaborado apenas pela equipe diretiva, o PPP perde legitimidade e se torna documento burocrático. A participação efetiva de professores, pais e alunos — inclusive por meio do Conselho Escolar — é requisito de validade democrática, não apenas formalidade legal.

## PPP e o Professor de Música

No CEP-EMB e nas escolas com ensino de música, o PPP deve contemplar as especificidades do ensino de Arte/Música: estrutura dos cursos (básico, técnico), carga horária, recursos e instrumentos, espaços físicos, integração com a comunidade."""})

NOVOS.append({"id":"r-gp-03","topico":"gp-03","disciplina":"gestao-pedagogica","bloco":"complementares",
"nome":"Currículo: concepções e organização","incidencia":"alta",
"versaoCurta":"""# Currículo: Concepções e Organização

## Definições de currículo
- **Formal/prescrito**: o que a legislação e os documentos oficiais determinam (BNCC, DCNs)
- **Real/vivido**: o que de fato acontece na sala de aula (pode diferir do formal)
- **Oculto**: mensagens implícitas transmitidas pela escola (valores, normas não escritas)

## Principais concepções
| Concepção | Enfoque | Referência |
|---|---|---|
| **Tecnicista** | Conteúdos + objetivos mensuráveis | Tyler, Bloom |
| **Humanista** | Experiência e desenvolvimento do aluno | Dewey |
| **Crítica** | Currículo como construção social e política | Apple, Giroux |
| **Pós-crítica** | Identidade, diferença, multiculturalismo | Silva |

## Organização curricular
- **Por disciplinas**: fragmentação do conhecimento; mais tradicional
- **Por áreas do conhecimento**: integração entre disciplinas afins (BNCC)
- **Por projetos/temas transversais**: integração ampla; mais complexo de implementar
- **Ciclos**: agrupamento por fases de desenvolvimento (não por ano/série)

## Currículo e diversidade
- Currículo não é neutro: sempre reflete escolhas políticas e culturais
- Diversidade étnico-racial, de gênero e de deficiência devem estar no currículo
- Lei 10.639/2003: história e cultura afro-brasileira obrigatórias
- Lei 11.645/2008: cultura indígena também obrigatória

## Para a prova
- "Currículo oculto" = Phillip Jackson (1968) — conceito teórico importante
- BNCC é currículo formal prescrito; não determina metodologia
- Transversalidade: temas que atravessam todas as disciplinas (ex.: educação ambiental)
- Currículo em Movimento do DF: concepção crítico-emancipatória""",
"versaoCompleta":"""# Currículo: Concepções e Organização

## O Que É Currículo

A palavra "currículo" vem do latim *curriculum* (corrida, percurso). Na educação, designa o conjunto de experiências de aprendizagem organizadas pela escola. Mas o conceito foi ampliado ao longo do século XX: o currículo não é apenas lista de conteúdos, mas o projeto de formação que a escola oferece — incluindo o que não está escrito.

## As Três Dimensões

**Currículo Formal (Prescrito)**: documentos oficiais que definem o que deve ser ensinado — CF/88, LDB, DCNs, BNCC, currículos das redes. É o nível das intenções.

**Currículo Real (Vivido)**: o que acontece concretamente nas salas de aula. Depende da formação do professor, dos materiais disponíveis, do tempo pedagógico e da dinâmica com os alunos. Pode diferir substancialmente do formal.

**Currículo Oculto**: mensagens implícitas transmitidas pela escola sem estar no currículo formal. Phillip Jackson (1968) identificou que a escola ensina além dos conteúdos: ensina obediência, pontualidade, competição, hierarquia. Pode reproduzir preconceitos de classe, gênero e raça se não houver reflexão crítica.

## Concepções Teóricas

As **teorias tradicionais** (Tyler) focam na eficiência: defina objetivos, organize conteúdos, desenvolva atividades, avalie. O currículo é visto como técnico e neutro.

As **teorias críticas** (Apple, Giroux, Freire) questionam: quem escolhe o que é ensinado? O currículo sempre reflete relações de poder. A escola pode reproduzir a ideologia dominante ou ser espaço de resistência.

As **teorias pós-críticas** (Tomaz Tadeu da Silva) acrescentam: currículo é local de construção de identidades. Questões de gênero, sexualidade, etnia e diferença cultural também são questões curriculares.

## Organização no Brasil

A BNCC organiza o currículo por **Áreas de Conhecimento** (não apenas disciplinas isoladas), o que favorece a integração. O **Currículo em Movimento** do DF adota perspectiva crítico-emancipatória, valorizando a diversidade e a formação para a cidadania."""})

NOVOS.append({"id":"r-gp-04","topico":"gp-04","disciplina":"gestao-pedagogica","bloco":"complementares",
"nome":"Avaliação escolar: concepções e modalidades","incidencia":"alta",
"versaoCurta":"""# Avaliação Escolar: Concepções e Modalidades

## Funções da avaliação
- **Diagnóstica**: identifica o ponto de partida do aluno (antes do ensino)
- **Formativa**: acompanha o processo e orienta ajustes (durante o ensino)
- **Somativa**: registra o resultado final (ao fim de um período)

## Concepções
| Concepção | Avaliação é... | Foco |
|---|---|---|
| **Classificatória** | Hierarquizar alunos | Produto/nota |
| **Formativa** | Melhorar a aprendizagem | Processo |
| **Emancipatória** | Tomada de consciência crítica | Sujeito/contexto |

## Modalidades / instrumentos
- **Provas** (objetivas e dissertativas): testam conhecimentos específicos
- **Portfólio**: registro progressivo de produções; evidencia desenvolvimento
- **Autoavaliação**: aluno reflete sobre sua própria aprendizagem
- **Coavaliação**: avaliação entre pares
- **Projetos e trabalhos**: avaliação por competências
- **Observação e registro**: especialmente na EI e anos iniciais

## Conselho de Classe
- Instância coletiva de avaliação institucional
- Participam: professores, coordenação, gestão (e em alguns sistemas, alunos e pais)
- Decisão sobre aprovação/retenção deve ser colegiada

## Para a prova
- Avaliação formativa ≠ avaliação contínua (embora sejam complementares)
- Luckesi: avaliação como "ato amoroso" — a serviço do crescimento
- Perrenoud: avaliação formativa regulada = feedback que o aluno usa para aprender
- Recuperação paralela: LDB art. 24, V, e — obrigatória, não punitiva
- "Avaliação a serviço da aprendizagem": princípio das Diretrizes de Avaliação da SEDF""",
"versaoCompleta":"""# Avaliação Escolar: Concepções e Modalidades

## Por Que a Avaliação Importa

A avaliação é o componente do processo pedagógico que revela os pressupostos do professor sobre o papel da escola. Quem avalia apenas com provas ao final do bimestre transmite uma mensagem implícita: o que importa é o produto (a nota), não o processo. Quem avalia de forma contínua e diversificada coloca a aprendizagem no centro.

## As Três Funções Clássicas

**Avaliação Diagnóstica**: realizada antes do início de uma unidade ou ano letivo. Seu objetivo é identificar o que os alunos já sabem (conhecimentos prévios), lacunas de aprendizagem e dificuldades específicas. É a base para o planejamento.

**Avaliação Formativa**: ocorre ao longo do processo de ensino-aprendizagem. Não visa classificar — visa regular. O professor observa, registra, fornece feedback e ajusta as estratégias. Philippe Perrenoud define avaliação formativa como "toda prática de avaliação contínua que pretenda contribuir para melhorar as aprendizagens em curso".

**Avaliação Somativa**: resume o nível de aprendizagem ao final de um período (bimestre, semestre, ano). É a avaliação "de produto" que resulta em notas e conceitos. Não deveria ser a única, mas é a mais presente na escola tradicional.

## A Avaliação em Luckesi

Cipriano Luckesi critica a "pedagogia do exame" — o ensino organizado para a aprovação nas provas, não para o aprendizado. Propõe que a avaliação seja um "ato amoroso" de acolhimento do aluno em seu processo, baseado em diagnóstico e não em julgamento.

## Instrumentos Diversificados

A BNCC e as DCNs orientam o uso de múltiplos instrumentos porque diferentes competências exigem diferentes formas de expressão. Um aluno que domina música pode não demonstrar isso bem em uma prova escrita, mas demonstra em uma performance ou em um portfólio de produções.

## Recuperação Paralela

O art. 24, V, "e" da LDB obriga as escolas a oferecer recuperação de estudos de forma paralela ao processo de ensino — não apenas ao final do período. A recuperação deve ser pedagógica (retomada de conteúdos com novas estratégias), não apenas uma segunda chance de prova."""})

todos = dados["resumos"] + [r for r in NOVOS if r["topico"] not in existentes]
dados["resumos"] = todos
dados["versao"] = "2.3.0"
with open(SRC,"w",encoding="utf-8") as f: json.dump(dados,f,ensure_ascii=False,indent=2)
print(f"Batch 3 OK — total: {len(todos)}")
