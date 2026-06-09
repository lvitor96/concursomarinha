#!/usr/bin/env python3
"""Batch 2: le-06, le-07, le-08, eca-01 to eca-05"""
import json, pathlib
BASE = pathlib.Path(__file__).parent
SRC  = BASE / "data" / "resumos.json"
with open(SRC) as f: dados = json.load(f)
existentes = {r["topico"] for r in dados["resumos"]}
NOVOS = []

NOVOS.append({"id":"r-le-06","topico":"le-06","disciplina":"legislacao-educacional","bloco":"complementares",
"nome":"PNE — Plano Nacional de Educação (Lei 13.005/2014)","incidencia":"alta",
"versaoCurta":"""# PNE 2014-2024 (Lei 13.005/2014)

## O que é
- Plano com vigência **2014-2024** (10 anos), aprovado pela Lei 13.005/2014
- **20 metas** nacionais de educação com estratégias de execução
- Base para elaboração dos Planos Estaduais (PEEs) e Municipais (PMEs)

## Metas principais (mais cobradas)
| Meta | Objetivo |
|---|---|
| 1 | Universalizar pré-escola (4-5 anos) e ampliar creche a 50% das crianças 0-3 |
| 2 | Universalizar EF 9 anos para 6-14 anos; 95% concluindo até 16 |
| 3 | Universalizar EM para 15-17 anos; 85% concluindo até 19 |
| 4 | Educação inclusiva para pessoas com deficiência |
| 5 | Alfabetização até o final do 3º ano do EF |
| 6 | **50% de alunos** em educação integral até 2024 |
| 7 | Melhorar IDEB (metas específicas por etapa) |
| 15 | Garantir política de formação docente |
| 16 | 50% dos professores com pós-graduação |
| 17 | Equiparar salário docente à média de outros profissionais |
| 20 | **10% do PIB** em educação até 2024 |

## Diretrizes (art. 2º)
- Erradicação do analfabetismo
- Universalização do atendimento escolar
- Superação das desigualdades educacionais com foco na equidade
- Melhoria da qualidade da educação
- Formação para o trabalho e para a cidadania
- Promoção da diversidade

## Para a prova
- Vigência: 2014-2024 (o plano atual expira em 2024, novo em discussão)
- 20 metas (não 10 nem 25)
- Meta 6: tempo integral = 7h ou mais de permanência na escola
- Meta 20: PIB (indicador financeiro) — ainda não atingido
- PDE (Plano Distrital) deve ser compatível com o PNE""",
"versaoCompleta":"""# PNE — Plano Nacional de Educação (Lei 13.005/2014)

## Contexto e Base Legal

O PNE 2014-2024 foi aprovado pela Lei 13.005, de 25 de junho de 2014. Representa o segundo PNE da história brasileira (o primeiro foi aprovado em 2001). O art. 214 da CF/88 determina que a lei estabelecerá o PNE com vigência de 10 anos. O plano tem força de lei ordinária e é vinculante para todos os entes federativos.

## Estrutura: 20 Metas

O PNE organiza-se em **20 metas** com centenas de estratégias. As metas se agrupam em três dimensões: educação básica (Metas 1-11), educação profissional e superior (Metas 12-14), valorização dos profissionais (Metas 15-18) e financiamento (Metas 19-20).

**Metas da Educação Básica mais cobradas:**
- Meta 1: Universalizar a Educação Infantil (4-5 anos) e ampliar o acesso à creche para 50% das crianças de 0-3 anos
- Meta 5: Alfabetizar todas as crianças até o final do 3º ano do EF
- Meta 6: 50% dos alunos em educação integral (7h ou mais) com prioridade para escolas em áreas de vulnerabilidade
- Meta 7: Elevar o IDEB do EF Anos Iniciais para 6,0; EF Anos Finais para 5,5; EM para 5,2

**Metas de Valorização Docente:**
- Meta 15: Todo professor da educação básica com formação em nível superior na área em que leciona (prazo: 1 ano após a aprovação)
- Meta 16: 50% dos professores com pós-graduação
- Meta 17: Equiparar o salário médio dos professores com o salário médio dos demais profissionais com escolaridade equivalente
- Meta 18: Existência de planos de carreira em todos os entes federativos

**Meta de Financiamento:**
- Meta 20: Ampliação do investimento público em educação para 10% do PIB (ainda não atingida em 2024)

## Articulação com Outros Planos

Os **PEEs** (Planos Estaduais de Educação) e **PMEs** (Planos Municipais de Educação) devem ser elaborados em consonância com o PNE. O **PDE** (Plano Distrital de Educação do DF) é o equivalente estadual/municipal do DF.

## Avaliação e Monitoramento

O INEP, o IPEA, o Fórum Nacional de Educação e a sociedade civil monitoram o cumprimento das metas. Os relatórios bienais avaliam avanços e dificuldades."""})

NOVOS.append({"id":"r-le-07","topico":"le-07","disciplina":"legislacao-educacional","bloco":"complementares",
"nome":"PDE — Plano Distrital de Educação 2015-2024","incidencia":"media",
"versaoCurta":"""# PDE — Plano Distrital de Educação 2015-2024

## O que é
- Plano de educação do Distrito Federal para o período **2015-2024**
- Aprovado pela **Lei Distrital nº 5.499/2015**
- Equivalente ao PNE no âmbito do DF; deve ser compatível com o PNE
- **36 metas** (mais detalhado que o PNE nacional, que tem 20)

## Estrutura
- Dividido em metas e estratégias específicas para o contexto do DF
- Contempla particularidades: CEPs (educação profissional), CEE-EE (inclusão), CEP-EMB (artes)
- Articulado com as Diretrizes Pedagógicas da SEDF e com o Currículo em Movimento

## Metas prioritárias (mais cobradas para a SEDF)
- Universalizar a Educação Infantil (4-5 anos) no DF
- Alcançar 50% das matrículas em tempo integral
- Garantir formação continuada para todos os professores
- Ampliar o atendimento educacional especializado (AEE)
- Erradicar o analfabetismo funcional no DF

## Instâncias de governança
- **Fórum Distrital de Educação (FDE)**: monitoramento e avaliação
- **Comissão de Monitoramento e Avaliação do PDE**: dentro da SEDF
- Relatórios bienais de acompanhamento

## Para a prova
- Lei Distrital 5.499/2015 = PDE
- 36 metas (PNE tem 20; PDE tem 36)
- Vigência: 2015-2024 (alinhada ao PNE)
- O PDE fundamenta as políticas da SEDF: cronograma de formação, metas de IDEB, educação integral
- Questões cobram: base legal, número de metas, relação com PNE""",
"versaoCompleta":"""# PDE — Plano Distrital de Educação 2015-2024

## Base Legal e Contexto

O Plano Distrital de Educação foi aprovado pela **Lei Distrital nº 5.499, de 14 de julho de 2015**. É o instrumento normativo que orienta as políticas educacionais do Distrito Federal pelo período de dez anos (2015-2024), em consonância com o Plano Nacional de Educação (PNE, Lei 13.005/2014).

Por ser a unidade federativa que acumula competências estaduais e municipais, o DF elabora um único plano que equivale simultaneamente ao Plano Estadual de Educação e ao Plano Municipal de Educação.

## Estrutura e Metas

O PDE-DF é estruturado em **36 metas** com estratégias detalhadas para cada uma delas. O número superior ao PNE (20 metas) reflete a necessidade de detalhar ações específicas para o contexto distrital.

As metas cobrem as mesmas dimensões do PNE, mas com indicadores e prazos ajustados à realidade local:
- Educação Infantil e anos iniciais do EF
- Alfabetização na idade certa
- Ensino Médio regular e profissional (CEPs)
- Educação de jovens e adultos (EJA)
- Educação especial e inclusão
- Educação integral
- Valorização e formação docente
- Gestão democrática
- Financiamento

## Articulação com a SEDF

O PDE é o documento de planejamento que sustenta as ações da Secretaria de Estado de Educação do Distrito Federal (SEDF). O **Currículo em Movimento**, as **Diretrizes de Avaliação** e os planos de formação docente da EAPE (Escola de Aperfeiçoamento dos Profissionais da Educação) derivam das metas do PDE.

## Monitoramento

O **Fórum Distrital de Educação (FDE)** e a **Comissão de Monitoramento e Avaliação** da própria SEDF acompanham o cumprimento das metas bienalmente. Os resultados do SAEB e do IDEB são os principais indicadores de referência."""})

NOVOS.append({"id":"r-le-08","topico":"le-08","disciplina":"legislacao-educacional","bloco":"complementares",
"nome":"Resolução CEDF nº 2/2023","incidencia":"media",
"versaoCurta":"""# Resolução CEDF nº 2/2023

## O que é o CEDF
- **Conselho de Educação do Distrito Federal**
- Órgão normativo, deliberativo, consultivo e fiscalizador do sistema de ensino do DF
- Vinculado à SEDF; membros nomeados pelo Governador

## Resolução nº 2/2023
- Atualiza e revisa normas do sistema de ensino do DF
- Abrange: organização da Educação Básica no sistema público do DF
- Inclui diretrizes para: calendário escolar, organização curricular, avaliação, progressão e certificação
- Compatível com as Diretrizes Curriculares Nacionais e com o Currículo em Movimento

## Pontos-chave para a prova
- **Organização do ano letivo**: mínimo 200 dias letivos / 800 horas anuais (EB)
- **Avaliação**: processo contínuo e diagnóstico; instrumentos diversificados
- **Progressão**: critérios de aprovação e retenção definidos pelo regimento escolar
- **Ensino Médio**: itinerários formativos alinhados com a reforma (Lei 13.415/2017)
- Normas sobre **educação especial** integrada à rede regular
- Diretrizes para **educação em tempo integral**

## Papel do CEDF
- Aprova normas para o sistema de ensino do DF
- Autoriza funcionamento de instituições privadas de ensino no DF
- Julga recursos de instituições e profissionais
- Fiscaliza a qualidade da educação no DF

## Para a prova
- CEDF = órgão normativo do sistema de ensino do DF (≠ MEC, que é nacional)
- Resoluções do CEDF têm força de lei para o sistema distrital
- Resolução 2/2023 é a mais recente — substituiu normas anteriores
- Questões cobram: competência do CEDF, força normativa, relação com LDB e DCNs""",
"versaoCompleta":"""# Resolução CEDF nº 2/2023

## O Conselho de Educação do Distrito Federal

O **CEDF** é o órgão normativo e deliberativo do sistema de ensino do Distrito Federal, criado pela Lei Orgânica do DF. Suas atribuições incluem: estabelecer normas complementares às diretrizes nacionais para o sistema de ensino local; autorizar o funcionamento de instituições privadas de ensino; emitir pareceres; e fiscalizar a qualidade do ensino.

O CEDF é composto por conselheiros representativos de diferentes segmentos (professores, pais, diretores, poder público) nomeados pelo Governador do DF.

## Resolução nº 2/2023

A Resolução CEDF nº 2/2023 é o principal instrumento normativo do sistema de ensino distrital em vigor. Ela atualiza as normas para a organização da Educação Básica no DF, adaptando as Diretrizes Curriculares Nacionais e a legislação federal ao contexto local.

**Principais disposições:**

*Organização do ano letivo*: confirma o mínimo de 200 dias letivos e 800 horas anuais para a Educação Básica, conforme a LDB. Define as condições para reposição de aulas e calendários alternativos.

*Avaliação*: a avaliação deve ser contínua, diagnóstica e formativa. A resolução orienta o uso de instrumentos diversificados — provas, portfólios, projetos, autoavaliação — em consonância com as Diretrizes de Avaliação da SEDF.

*Progressão e retenção*: os critérios são definidos nos regimentos escolares, observadas as normas do CEDF. A progressão automática sem critérios pedagógicos não é prevista.

*Ensino Médio*: alinha o sistema distrital com a Lei 13.415/2017, orientando a implantação dos itinerários formativos e a distribuição entre BNCC e componentes optativos.

*Educação Especial*: estabelece que o atendimento educacional especializado (AEE) deve ocorrer preferencialmente em salas de recursos multifuncionais das escolas regulares, em turno contrário.

## Articulação com o Sistema Nacional

As resoluções do CEDF devem estar em conformidade com a LDB, as DCNs (Resoluções CNE/CEB) e o PDE-DF. O sistema de ensino do DF é único — não há municípios com sistemas próprios."""})

NOVOS.append({"id":"r-eca-01","topico":"eca-01","disciplina":"eca","bloco":"complementares",
"nome":"ECA — Convivência familiar e comunitária (arts. 19-52-D)","incidencia":"media",
"versaoCurta":"""# ECA — Convivência Familiar e Comunitária (Arts. 19-52-D)

## Direito fundamental (art. 19)
- Toda criança e adolescente tem direito a ser criado e educado **no seio de sua família**
- Preferência pela **família natural**; excepcionalmente, família substituta
- Acolhimento institucional: medida **excepcional e provisória** — último recurso

## Família natural vs. família substituta
- **Família natural**: pai e mãe (ou apenas um) e filhos
- **Família extensa**: parentes próximos com quem a criança mantém vínculos afetivos (avós, tios)
- **Família substituta**: guarda, tutela ou adoção por terceiros

## Guarda, tutela e adoção
| Modalidade | Característica |
|---|---|
| **Guarda** | Obriga à prestação de assistência; pode ser revogada |
| **Tutela** | Implica representação legal; extingue o poder familiar |
| **Adoção** | Vínculo definitivo; iguala adotado a filho biológico |

## Acolhimento institucional
- Art. 19, §3º: máximo **18 meses** (prorrogáveis por exceção fundamentada)
- Proibida separação de irmãos no acolhimento
- Objetivo: retorno à família natural ou encaminhamento para adoção

## Cadastro Nacional de Adoção (CNA)
- Sistema unificado de pretendentes habilitados e crianças disponíveis
- Respeita: preferência por crianças mais velhas, grupos de irmãos, com deficiência

## Para a prova
- Acolhimento é excepcional e provisório; institucionalização é último recurso
- Adoção: vínculo irrevogável; iguala adotado a filho (sem distinção de direitos)
- Família extensa tem preferência sobre família substituta desconhecida
- Art. 23: pobreza isolada NÃO é motivo para perda do poder familiar""",
"versaoCompleta":"""# ECA — Convivência Familiar e Comunitária (Arts. 19-52-D)

## O Direito à Convivência Familiar

O art. 19 do ECA consagra o direito de toda criança e adolescente de ser criada no seio de sua família e, excepcionalmente, em família substituta. A convivência familiar e comunitária é um dos direitos fundamentais da criança, ao lado do direito à vida, à saúde, à educação e ao lazer.

A **família natural** — formada por um ou ambos os genitores e seus filhos — é prioridade absoluta. A **família extensa** (parentes com quem a criança mantém vínculos afetivos: avós, tios, primos) tem precedência sobre a família substituta desconhecida.

## Acolhimento: Medida Excepcional

O acolhimento familiar ou institucional é medida de proteção de caráter excepcional e provisório. O art. 19, §3º estabelece que a permanência em programa de acolhimento institucional não deve se prolongar por mais de **18 meses**, salvo comprovada necessidade fundamentada.

O princípio da excepcionalidade impede a institucionalização por simples falta de recursos financeiros da família. O art. 23 é categórico: a falta ou carência de recursos materiais **não constitui motivo suficiente para a perda ou a suspensão do poder familiar**. Nesse caso, a criança deve ser incluída em programas de auxílio à família.

## Formas de Família Substituta

A **guarda** confere à família o dever de assistência material, moral e educacional. É revogável e pode ser concedida judicial ou administrativamente. O guardião tem a obrigação legal de comunicar ausências escolares injustificadas.

A **tutela** é mais abrangente: pressupõe o falecimento ou a destituição do poder familiar dos pais. O tutor tem poderes de representação legal.

A **adoção** é irrevogável e estabelece vínculo de filiação definitivo. O adotado tem exatamente os mesmos direitos que o filho biológico, extinguindo qualquer vínculo com a família de origem (salvo impedimentos matrimoniais). Pessoas com 18 anos ou mais podem adotar, com diferença mínima de 16 anos entre adotante e adotado."""})

NOVOS.append({"id":"r-eca-02","topico":"eca-02","disciplina":"eca","bloco":"complementares",
"nome":"ECA — Direito à educação, cultura, esporte e lazer (arts. 53-59)","incidencia":"alta",
"versaoCurta":"""# ECA — Educação, Cultura, Esporte e Lazer (Arts. 53-59)

## Art. 53 — Direito à educação
- Direito ao acesso à escola, permanência e aprendizagem
- Inciso I: igualdade de condições no acesso e permanência
- Inciso II: direito de ser respeitado por seus educadores
- Inciso III: contestar critérios avaliativos, com recurso às instâncias superiores
- Inciso IV: organização e participação em entidades estudantis
- Inciso V: acesso à escola pública e gratuita próxima à residência

## Art. 54 — Deveres do Estado (eco do art. 208 da CF)
- I: Educação Básica obrigatória e gratuita dos 4 aos 17 anos
- II: Progressiva universalização do EM
- III: Atendimento educacional especializado para pessoas com deficiência
- IV: Atendimento em creche e pré-escola para 0-5 anos
- V: Acesso aos níveis mais elevados
- VII: Atendimento ao educando por transporte, alimentação, material e saúde
- §1º: acesso ao EF obrigatório é **direito público subjetivo**

## Art. 55 — Obrigação dos pais
- Matricular e garantir frequência nos estabelecimentos de ensino

## Art. 56 — Comunicação ao Conselho Tutelar
Os diretores de escola devem comunicar ao CT:
- Maus-tratos envolvendo alunos
- **Reiterada falta injustificada** e evasão escolar
- Elevados níveis de repetência

## Art. 57 — Programas complementares
O Poder Público estimulará pesquisa, ensino e difusão de arte e cultura

## Para a prova
- Art. 53, V: escola pública próxima à residência (**mesmo texto** do art. 4º, X da LDB)
- Art. 56: diretor que NÃO comunica o CT comete irregularidade
- Art. 55: obrigação de **matricular** E garantir **frequência**
- §1º do art. 54: EF obrigatório = direito subjetivo (pode ir ao MP)""",
"versaoCompleta":"""# ECA — Educação, Cultura, Esporte e Lazer (Arts. 53-59)

## Art. 53 — O Direito à Educação da Criança e do Adolescente

O ECA trata o direito à educação como instrumento fundamental para o pleno desenvolvimento da pessoa. O art. 53 não é mera repetição da Constituição: ele detalha direitos dentro do ambiente escolar, como o direito de ser **respeitado pelos educadores** (inciso II) e de **contestar critérios avaliativos** recorrendo às instâncias superiores (inciso III).

O inciso IV — direito de organizar entidades estudantis — fundamenta grêmios e associações estudantis nas escolas, reconhecidos como espaços de formação cidadã.

O inciso V — acesso à escola pública próxima à residência — é texto idêntico ao do art. 4º, X da LDB. A repetição em dois diplomas reforça a obrigação do Estado de não designar escola distante quando houver vaga próxima.

## Art. 54 — Deveres do Estado

O art. 54 reproduz, no âmbito do ECA, os deveres do Estado previstos no art. 208 da CF/88. O §1º transforma o acesso ao Ensino Fundamental em **direito público subjetivo** — o cidadão pode exigir judicialmente a vaga. O §2º responsabiliza a autoridade competente pelo não-oferecimento ou irregularidade no fornecimento do ensino obrigatório.

## Art. 55 — Dever dos Pais

Os pais ou responsáveis têm duas obrigações distintas: **matricular** a criança e **garantir sua frequência** na escola. O descumprimento pode ensejar comunicação ao Conselho Tutelar e até aplicação de medidas protetivas à criança.

## Art. 56 — Obrigação do Diretor de Escola

O art. 56 impõe aos dirigentes de estabelecimentos de ensino fundamental a obrigação de comunicar ao Conselho Tutelar:
1. Maus-tratos envolvendo alunos
2. **Reiteração de faltas injustificadas e evasão escolar**
3. Elevados níveis de repetência

Essa comunicação não é discricionária — é dever legal. O diretor que silencia perante casos de evasão escolar descumpre o ECA.

## Arts. 57-59 — Cultura, Esporte e Lazer

O Poder Público deve estimular programas culturais, esportivos e de lazer para a criança e o adolescente. O art. 59 enfatiza que os municípios devem estimular e facilitar a destinação de recursos para esse fim, inclusive por meio de políticas de acesso ao patrimônio cultural."""})

NOVOS.append({"id":"r-eca-03","topico":"eca-03","disciplina":"eca","bloco":"complementares",
"nome":"ECA — Disposições preliminares (arts. 1-6)","incidencia":"media",
"versaoCurta":"""# ECA — Disposições Preliminares (Arts. 1-6)

## Art. 1º — Objeto
- Lei 8.069/1990 — Estatuto da Criança e do Adolescente
- Dispõe sobre a proteção integral à criança e ao adolescente

## Art. 2º — Definições
- **Criança**: pessoa até 12 anos incompletos
- **Adolescente**: pessoa de 12 a 18 anos incompletos
- §único: nos casos expressos em lei, o ECA aplica-se às pessoas entre 18 e 21 anos

## Art. 3º — Direitos fundamentais
- Criança e adolescente gozam de todos os direitos fundamentais inerentes à pessoa humana
- Sem prejuízo da proteção integral
- Assegura: desenvolvimento físico, mental, moral, espiritual e social
- Em condições de liberdade e dignidade

## Art. 4º — Dever compartilhado (família, sociedade e Estado)
- É dever da **família, da comunidade, da sociedade e do poder público** assegurar os direitos
- Prioridade absoluta: efetivação dos direitos à vida, saúde, alimentação, educação, esporte, lazer, cultura, dignidade, respeito, liberdade e convivência familiar
- Parágrafo único: garantia de prioridade inclui:
  a) primazia de receber proteção e socorro
  b) precedência no atendimento por serviços públicos
  c) preferência na formulação de políticas públicas
  d) destinação privilegiada de recursos

## Art. 5º — Omissão e abuso
- Nenhuma criança será objeto de qualquer forma de negligência, discriminação, exploração, violência, crueldade e opressão
- Punição prevista para omissão ou ato comissivo

## Art. 6º — Interpretação
- Na interpretação do ECA, consideram-se: fins sociais, exigências do bem comum, **direitos e deveres individuais e coletivos**, condição peculiar da criança e adolescente como **pessoas em desenvolvimento**

## Para a prova
- Criança: até 12 anos incompletos | Adolescente: 12 a 18 anos incompletos
- "Prioridade absoluta" não é apenas do Estado — é de todos (família, comunidade, sociedade)
- Art. 6º: "condição peculiar como pessoa em desenvolvimento" — fundamenta tratamento diferenciado""",
"versaoCompleta":"""# ECA — Disposições Preliminares (Arts. 1-6)

## A Doutrina da Proteção Integral

O ECA (Lei 8.069/1990) substituiu o antigo Código de Menores (1979) e a "doutrina da situação irregular", que tratava crianças e adolescentes em situação de pobreza, abandono ou infração como objeto de tutela do Estado. A nova doutrina — **proteção integral** — reconhece crianças e adolescentes como **sujeitos de direitos**, titulares de todos os direitos fundamentais, com prioridade absoluta.

## Art. 2º — Distinção Etária

A distinção entre criança (até 12 anos incompletos) e adolescente (12 a 18 anos) tem consequências jurídicas concretas:
- Criança que pratica ato infracional: medidas de proteção (sem internação)
- Adolescente que pratica ato infracional: medidas socioeducativas (podendo incluir internação)

O parágrafo único amplia a aplicação do ECA a jovens de 18-21 anos nos casos expressos — como no cumprimento de medida socioeducativa iniciada antes dos 18 anos.

## Art. 4º — Prioridade Absoluta

A prioridade absoluta é o princípio estruturante do ECA. Ela implica que, em caso de conflito entre necessidades da criança/adolescente e outros grupos, aquelas têm precedência. O parágrafo único especifica quatro dimensões:

(a) Primazia de receber proteção em situação de risco
(b) Precedência no atendimento em serviços públicos de saúde, educação, etc.
(c) Preferência na formulação de políticas sociais
(d) Destinação privilegiada de recursos orçamentários

Essa prioridade é **exigível judicialmente**: cortes orçamentários que prejudiquem programas para crianças podem ser contestados.

## Art. 6º — Condição Peculiar

A cláusula "condição peculiar de pessoa em desenvolvimento" é fundamental. Ela justifica o tratamento diferenciado em relação a adultos: crianças e adolescentes estão em processo de formação cognitiva, emocional e social. Por isso, a responsabilização deve ser pedagógica e não meramente punitiva."""})

NOVOS.append({"id":"r-eca-04","topico":"eca-04","disciplina":"eca","bloco":"complementares",
"nome":"ECA — Direito à vida e à saúde (arts. 7-14)","incidencia":"baixa",
"versaoCurta":"""# ECA — Direito à Vida e à Saúde (Arts. 7-14)

## Art. 7º — Direito à vida e à saúde
- Criança e adolescente têm direito à proteção à vida e à saúde
- Mediante políticas sociais públicas que permitam nascimento e desenvolvimento sadio
- Em condições dignas de existência

## Art. 8º — Atenção à gestante
- É assegurado a todas as mulheres o **acesso a programas e políticas de saúde** da mulher e planejamento reprodutivo
- Atenção ao pré-natal, ao parto e ao pós-parto
- Registro de nascimento deve ser feito imediatamente após o parto

## Art. 9º — Aleitamento materno
- O Poder Público, as instituições e os empregadores propiciarão condições para o aleitamento materno

## Art. 10 — Obrigações dos estabelecimentos de saúde
- Manter registro de nascimentos
- Fornecer declaração de nascido vivo
- Comunicar à autoridade judiciária casos de denúncia de maus-tratos
- Guardar sigilo das informações

## Art. 11 — Atendimento médico
- Criança e adolescente têm acesso universal e igualitário às ações e serviços de saúde
- Crianças com deficiência: acesso a tratamento especializado

## Art. 13 — Notificação de maus-tratos
- **Obrigatória** a notificação de casos de suspeita ou confirmação de maus-tratos contra criança/adolescente
- Por profissionais de saúde, educação e demais que atendam a esse público
- Guarda de sigilo protege o notificante

## Para a prova
- Art. 13: profissional de **educação também é obrigado** a notificar (não só de saúde!)
- Notificação = dever legal, não discricionário
- Art. 5º + art. 13: par fundamental sobre proteção contra violência
- Maus-tratos = qualquer ação ou omissão que cause dano à criança""",
"versaoCompleta":"""# ECA — Direito à Vida e à Saúde (Arts. 7-14)

## Saúde como Direito Integral

O ECA trata o direito à saúde de forma abrangente, desde o pré-natal até a adolescência. O art. 7º enuncia o direito ao nascimento e ao desenvolvimento sadio como derivado do direito fundamental à vida.

## Atenção à Gestante (Art. 8º)

O art. 8º, com redação ampliada por legislações posteriores, garante à gestante atenção humanizada no pré-natal, no parto e no pós-parto. A mulher tem direito a acompanhante durante o trabalho de parto (Lei 11.108/2005). O registro imediato do nascimento é obrigação do estabelecimento de saúde.

## Aleitamento Materno (Art. 9º)

O Poder Público, as instituições e os empregadores devem criar condições para o aleitamento materno. Isso inclui: locais para amamentação em empresas, bancos de leite humano, licença-maternidade adequada.

## Obrigações dos Profissionais de Saúde (Art. 10)

Os estabelecimentos de saúde são obrigados a: manter registro das crianças nascidas; fornecer declaração de nascido vivo; comunicar ao Conselho Tutelar e à autoridade judicial os casos de maus-tratos.

## Notificação Obrigatória (Art. 13)

O art. 13 é um dos mais importantes para profissionais de educação. Estabelece que os casos de **suspeita ou confirmação de maus-tratos** contra crianças ou adolescentes são de **notificação obrigatória** pelos profissionais de saúde, educação e assistência social.

A notificação deve ser feita ao Conselho Tutelar. O profissional que notificar de boa-fé está protegido — a comunicação não configura violação de sigilo profissional. O que configura ilícito é a **omissão**: deixar de notificar casos de maus-tratos é infração administrativa punível.

## Importância para o Professor

O professor, ao identificar sinais de maus-tratos (lesões físicas inexplicadas, comportamento retraído, fome frequente, afirmações da criança), tem dever legal de comunicar ao Conselho Tutelar — mesmo sem certeza, bastando a suspeita fundada."""})

NOVOS.append({"id":"r-eca-05","topico":"eca-05","disciplina":"eca","bloco":"complementares",
"nome":"Lei 13.146/2015 — Estatuto da Pessoa com Deficiência (arts. 27-30)","incidencia":"media",
"versaoCurta":"""# Estatuto da Pessoa com Deficiência — Educação (Arts. 27-30)

## Art. 27 — Direito à educação
- Educação como **direito da pessoa com deficiência** ao longo de toda a vida
- Sistema educacional **inclusivo** em todos os níveis e modalidades
- Objetivo: alcançar máximo desenvolvimento possível de talentos e habilidades físicas, sensoriais, intelectuais e sociais
- De acordo com suas características, interesses e necessidades de aprendizagem

## Art. 28 — Incumbências do Poder Público
- **I**: sistema educacional inclusivo em todos os níveis
- **II**: aprimoramento dos sistemas educacionais para inclusão plena
- **III**: projeto pedagógico que institucionalize atendimento educacional especializado
- **IV**: oferta de educação bilíngue em Libras como primeira língua e português escrito como segunda (surdos)
- **V**: adoção de medidas individualizadas e coletivas para atender necessidades educacionais específicas
- **X**: adoção de práticas pedagógicas inclusivas com capacitação docente
- **XIII**: acesso à educação superior e profissional em igualdade de condições
- **XVII**: oferta de profissionais de apoio escolar

## Art. 28, §1º — Vedação ao sistema privado
- Instituições privadas de ensino não podem cobrar valores adicionais pela inclusão
- Proibido recusar matrícula de pessoa com deficiência

## Art. 30 — Atendimento prioritário
- Processos seletivos devem ser acessíveis (tempo adicional, intérprete, sala adequada)
- Materiais de apoio em formatos acessíveis

## Para a prova
- AEE (Atendimento Educacional Especializado) é complementar à classe regular, não substitutivo
- Recusa de matrícula por deficiência = **crime** (art. 8º, §1º da Lei 7.853/1989, mantido)
- Educação inclusiva ≠ integração — inclusão pressupõe adaptação da escola, não do aluno
- Profissional de apoio escolar: custeado pelo Poder Público""",
"versaoCompleta":"""# Estatuto da Pessoa com Deficiência — Educação (Arts. 27-30)

## A Lei Brasileira de Inclusão

A Lei 13.146/2015, conhecida como Estatuto da Pessoa com Deficiência ou Lei Brasileira de Inclusão (LBI), fundamenta-se na **Convenção sobre os Direitos das Pessoas com Deficiência** da ONU (ratificada pelo Brasil em 2008 com status de emenda constitucional). A LBI adota o **modelo social de deficiência**: a deficiência não está na pessoa, mas na relação entre a pessoa e as **barreiras** impostas pela sociedade.

## Art. 27 — Educação Inclusiva

O art. 27 consagra a educação como direito da pessoa com deficiência ao longo de toda a vida. O sistema educacional deve ser **inclusivo em todos os níveis** — não apenas no Ensino Fundamental, mas também na Educação Infantil, Ensino Médio, EJA, Educação Profissional e Superior.

## Art. 28 — Obrigações do Poder Público

O art. 28 é a espinha dorsal da educação inclusiva na LBI. Dentre os 18 incisos, destacam-se:

**AEE (inciso III)**: o atendimento educacional especializado deve estar institucionalizado no projeto pedagógico da escola. É **complementar e suplementar** ao ensino regular, nunca substitutivo. Ocorre preferencialmente em salas de recursos multifuncionais no contraturno.

**Libras (inciso IV)**: as escolas com alunos surdos devem oferecer educação bilíngue — Libras como primeira língua e português escrito como segunda. O intérprete de Libras é um direito.

**Formação docente (inciso X)**: professores devem receber capacitação inicial e continuada para práticas pedagógicas inclusivas.

**Profissional de apoio (inciso XVII)**: para alunos que necessitam de apoio nas atividades de comunicação, interação social, locomoção e higiene pessoal, o Poder Público deve providenciar profissional de apoio escolar. O custeio é público — não pode ser cobrado dos pais.

## Art. 28, §1º — Sistemas Privados

A proibição de cobranças adicionais por serviços de inclusão nas instituições privadas de ensino é uma das disposições mais polêmicas e importantes da LBI. As escolas particulares não podem:
- Recusar matrícula de pessoa com deficiência
- Cobrar taxas extras pela adaptação curricular ou pelo profissional de apoio

O STF confirmou a constitucionalidade dessas disposições em 2016 (ADI 5357)."""})

todos = dados["resumos"] + [r for r in NOVOS if r["topico"] not in existentes]
dados["resumos"] = todos
dados["versao"] = "2.2.0"
with open(SRC,"w",encoding="utf-8") as f: json.dump(dados,f,ensure_ascii=False,indent=2)
print(f"Batch 2 OK — total: {len(todos)}")
