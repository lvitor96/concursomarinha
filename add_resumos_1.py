#!/usr/bin/env python3
"""Batch 1: df-01, df-02, df-03, le-02 to le-05"""
import json, pathlib
BASE = pathlib.Path(__file__).parent
SRC  = BASE / "data" / "resumos.json"
with open(SRC) as f: dados = json.load(f)
existentes = {r["topico"] for r in dados["resumos"]}
NOVOS = []

NOVOS.append({"id":"r-df-01","topico":"df-01","disciplina":"realidade-df","bloco":"basicos",
"nome":"História e geografia do Distrito Federal","incidencia":"media",
"versaoCurta":"""# História e Geografia do DF

## Fundação e histórico
- **21 de abril de 1960**: inauguração de Brasília como nova capital federal
- **JK** (Juscelino Kubitschek): presidente que viabilizou a construção
- **Lúcio Costa** (urbanismo) + **Oscar Niemeyer** (arquitetura) + **Burle Marx** (paisagismo)
- **NOVACAP**: empresa criada para construir a cidade (1956)
- Patrimônio Mundial pela UNESCO desde **1987** (urbanismo modernista)
- **GDF** criado pela Lei nº 3.751/1960; DF não é município nem estado

## Localização e relevo
- Planalto Central brasileiro, **altitude média 1.000-1.200 m**
- Bioma **Cerrado** — maior biodiversidade de savana tropical do mundo
- Bacia hidrográfica: **Lago Paranoá** (artificial, represado no Paranoá)
- Divisas: estado de **Goiás** (a norte, sul e oeste) e **Minas Gerais** (a leste — fragmento)

## Regiões Administrativas (RAs)
- 35 RAs atualmente (criadas progressivamente desde 1960)
- **Plano Piloto** = RA I (núcleo original)
- Primeiras cidades-satélites: **Taguatinga** (1958), **Sobradinho** e **Gama** (1960)

## Para a prova
- Distância Brasília-Rio: ≈ 1.150 km; Brasília-São Paulo: ≈ 1.010 km
- DF é a **única unidade federativa** sem municípios — dividida em RAs
- A construção de Brasília fez parte do Plano de Metas ("50 anos em 5")
- Setor cultural: CCBB, Museu Nacional Honestino Guimarães (Niemeyer)""",
"versaoCompleta":"""# História e Geografia do Distrito Federal

## Antecedentes Históricos

A transferência da capital federal para o interior do Brasil foi prevista desde a Constituição de 1891, que designou uma área no Planalto Central. A **Missão Cruls (1892)** demarcou o chamado "Quadrilátero Cruls", que orientou a escolha do sítio definitivo. A Constituição de 1946 retomou o compromisso, e JK transformou a promessa em realidade.

## Construção e Inauguração (1956-1960)

Juscelino Kubitschek criou a **NOVACAP** em 1956 para coordenar as obras. O projeto urbanístico de **Lúcio Costa** (Plano Piloto) foi escolhido por concurso — o traçado em forma de avião ou cruz combina os dois eixos: Monumental (L-O) e Rodoviário (N-S). **Oscar Niemeyer** projetou os edifícios governamentais: Palácio do Planalto, Congresso Nacional, Supremo Tribunal Federal, Catedral e Palácio da Alvorada. **Roberto Burle Marx** criou o paisagismo.

A inauguração ocorreu em **21 de abril de 1960**. Em **1987**, a UNESCO reconheceu o Conjunto Urbanístico de Brasília como Patrimônio Cultural da Humanidade, valorizado pelo planejamento urbano modernista único.

## Estatuto Político e Administrativo

O Distrito Federal não é estado nem município — é uma unidade federativa *sui generis*. A **Lei Orgânica do DF (1993)** e a CF/88 (art. 32) vedam a divisão do DF em municípios. É governado pelo **Governador do DF** e pela **Câmara Legislativa**. As **35 Regiões Administrativas** são circunscrições administrativas, não municípios.

## Geografia e Bioma

Situado no Planalto Central, o DF ocupa 5.779,99 km². O relevo é de chapadas e vales suaves, altitude média de 1.000-1.200 m. O bioma **Cerrado** cobre grande parte do território, com vegetação de savana e alta biodiversidade endêmica. O **Lago Paranoá**, criado artificialmente, é fundamental para o microclima local.

## Cidades-Satélites e Expansão

As cidades-satélites surgiram durante a construção para abrigar trabalhadores (candangos). **Taguatinga** (1958) é a mais antiga RA autônoma. Seguiram-se Sobradinho, Gama, Ceilândia (1971 — maior RA em população), Samambaia, entre outras."""})

NOVOS.append({"id":"r-df-02","topico":"df-02","disciplina":"realidade-df","bloco":"basicos",
"nome":"Aspectos sociais, culturais, econômicos e políticos do DF","incidencia":"media",
"versaoCurta":"""# Aspectos do DF

## Economia
- **Maior PIB per capita** do Brasil (puxado pelo funcionalismo público)
- Base econômica: **serviço público federal e distrital** (~50% do PIB)
- Setor terciário dominante; parques tecnológicos e indústria incipiente
- **IBGE 2023**: ≈ 3,1 milhões de habitantes

## Educação
- **SEDF** (Secretaria de Estado de Educação do DF): rede pública distrital
- Única UF com sistema próprio de educação profissional: **CEP-EMB, CEMAB** etc.
- Altas taxas de acesso ao ensino superior (concentração de universidades)
- **UnB** (Universidade de Brasília): única universidade federal do DF

## Cultura
- **Patrimônio da Humanidade** (UNESCO 1987): conjunto urbanístico modernista
- Concentração de museus, teatros e centros culturais (escala nacional)
- **Festival Internacional de Cinema de Brasília**, **FIAC**, Festival de Teatro
- Multiculturalidade: migrantes de todos os estados compõem a identidade local

## Política
- Estrutura: **Governador** + **Câmara Legislativa** (24 deputados distritais)
- CF/88, art. 32: DF tem competências estaduais E municipais
- Segurança pública: peculiaridade — **Polícia Civil e Militar do DF** são custeadas pela União
- DF tem representação no Congresso: **3 senadores** e deputados federais

## Para a prova
- DF tem as melhores médias do IDEB/SAEB entre as UFs (historicamente)
- Ceilândia é a RA mais populosa
- IDH alto (≈ 0,824) — melhor do Brasil
- Peculiaridade fiscal: DF não recebe FPM (Fundo de Participação dos Municípios)""",
"versaoCompleta":"""# Aspectos Sociais, Culturais, Econômicos e Políticos do DF

## Perfil Econômico

O Distrito Federal possui o **maior PIB per capita do Brasil**, mas isso se deve à concentração de funcionários públicos federais e distritais bem remunerados, não à produção industrial. O setor de serviços responde por mais de 90% da atividade econômica. A presença de embaixadas, organismos internacionais e ministérios atrai fluxo financeiro significativo.

O **comércio e o turismo** (administrativo e cultural) complementam a base econômica. O DF não é autossuficiente em produção primária — importa alimentos das cidades do Entorno.

## Perfil Social

Com cerca de 3,1 milhões de habitantes (IBGE 2023), o DF tem alta densidade relativa para sua área (5.779 km²). O **IDH é o mais alto do Brasil** (≈ 0,824), mas esconde desigualdades entre o Plano Piloto e as RAs periféricas como Estrutural e Itapoã.

A **SEDF** gerencia uma rede com mais de 600 escolas públicas. Os índices de analfabetismo são baixos, mas a segregação espacial reflete-se no acesso à educação de qualidade.

## Cultura e Identidade

Brasília é uma cidade de migrantes — os "candangos" originais vieram de todo o Brasil, especialmente do Nordeste. Essa diversidade criou uma identidade cultural híbrida e cosmopolita.

O acervo cultural inclui: Museu Nacional Honestino Guimarães (Niemeyer), CCBB Brasília, Teatro Nacional Cláudio Santoro, Espaço Cultural Renato Russo e dezenas de galerias. O festival **Bananada** (rock alternativo) e eventos de música erudita convivem na mesma cidade.

## Estrutura Política

Diferentemente dos estados, o DF acumula competências estaduais e municipais (CF/88, art. 32). A **Câmara Legislativa** (24 deputados distritais) exerce funções de assembleia estadual e câmara municipal. As **Regiões Administrativas** são geridas por administradores nomeados, sem eleição própria.

A peculiaridade mais importante para concursos: as **Polícias Civil e Militar do DF** são organizadas e custeadas pela União (art. 21, XIV, CF/88), embora operem no território distrital sob supervisão do Governador."""})

NOVOS.append({"id":"r-df-03","topico":"df-03","disciplina":"realidade-df","bloco":"basicos",
"nome":"RIDE — Região Integrada de Desenvolvimento","incidencia":"baixa",
"versaoCurta":"""# RIDE-DF

## O que é a RIDE
- **Região Integrada de Desenvolvimento do Distrito Federal e Entorno**
- Criada pela **LC nº 94/1998** e regulamentada pelo **Decreto nº 7.469/2011**
- Área metropolitana funcional do DF integrada com municípios de GO e MG

## Composição
- **Distrito Federal** + municípios do **Goiás** e de **Minas Gerais** do entorno
- Municípios goianos incluídos: Águas Lindas, Planaltina-GO, Luziânia, Valparaíso, Novo Gama, entre outros (~22 municípios de GO)
- Municípios mineiros: Unaí, Buritis, Cabeceira Grande
- Total original: 22 municípios + DF; ampliado por decreto subsequente

## Finalidade
- Articular ações do Poder Público federal e dos entes subnacionais
- Promover desenvolvimento integrado nas áreas de: infraestrutura, saúde, educação, segurança pública, transportes, habitação e saneamento
- Reduzir desigualdades entre o DF (rico) e o Entorno (pobre)

## Governança
- **COARIDE**: Conselho Administrativo da RIDE — coordena ações
- Presidido pelo **Ministério do Desenvolvimento Regional**
- Participam representantes da União, do DF e dos municípios

## Para a prova
- Base legal: LC 94/1998
- RIDE não é região metropolitana clássica — não tem governo próprio
- O Entorno recebe serviços de saúde e educação do DF (fluxo de pendulares)
- "Cidades dormitório": moradores trabalham no DF e dormem no Entorno
- Questões costumam cobrar: base legal, composição, finalidade e COARIDE""",
"versaoCompleta":"""# RIDE-DF — Região Integrada de Desenvolvimento do DF e Entorno

## Contexto e Criação

A expansão urbana de Brasília extrapolou os limites do Distrito Federal ainda nas décadas de 1970 e 1980. A expulsão de moradores do Plano Piloto e a migração contínua criaram um **aglomerado urbano que não se limita ao DF**: cidades goianas como Luziânia, Planaltina-GO, Formosa e Águas Lindas tornaram-se extensões funcionais da metrópole.

A **Lei Complementar nº 94, de 19 de fevereiro de 1998**, criou formalmente a RIDE-DF. O **Decreto nº 7.469/2011** a regulamentou e expandiu sua composição.

## Composição Atual

A RIDE-DF abrange o Distrito Federal e municípios dos estados de Goiás e Minas Gerais. Os municípios goianos incluem: Abadiânia, Água Fria de Goiás, Águas Lindas de Goiás, Alexânia, Cabeceiras, Cidade Ocidental, Cocalzinho de Goiás, Corumbá de Goiás, Cristalina, Formosa, Luziânia, Mimoso de Goiás, Novo Gama, Padre Bernardo, Pirenópolis, Planaltina-GO, Santo Antônio do Descoberto, Valparaíso de Goiás e Vila Boa. Os municípios mineiros são: Buritis, Cabeceira Grande e Unaí.

## Objetivos da RIDE

A RIDE foi criada para articular ações de governo nas áreas de:
- Infraestrutura (rodovias, saneamento básico)
- Serviços de saúde de alta e média complexidade
- Educação e formação profissional
- Segurança pública
- Habitação e urbanização
- Transportes coletivos metropolitanos

O problema central é a assimetria: o DF concentra empregos, serviços e renda, enquanto os municípios do Entorno sediam trabalhadores que dependem dos serviços do DF.

## Governança

O **COARIDE** (Conselho Administrativo da RIDE) é o órgão deliberativo, presidido pelo ministério competente (Desenvolvimento Regional). Reúne representantes da União, do GDF e das prefeituras. As deliberações dependem de convênios entre os entes — a RIDE não tem personalidade jurídica própria nem orçamento autônomo.

## Impacto na Educação

A demanda por escolas públicas no Entorno é reprimida; muitos jovens estudam em escolas do DF, especialmente nos CEPs (Centros de Ensino Profissional). A questão dos **estudantes pendulares** é recorrente nas políticas educacionais da SEDF."""})

# ── CC Legislação ────────────────────────────────────────────

NOVOS.append({"id":"r-le-02","topico":"le-02","disciplina":"legislacao-educacional","bloco":"complementares",
"nome":"LDB — Composição dos níveis escolares (arts. 21-38)","incidencia":"alta",
"versaoCurta":"""# LDB — Níveis e Etapas da Educação (Arts. 21-38)

## Estrutura da educação nacional (art. 21)
- **I — Educação Básica**: Educação Infantil + Ensino Fundamental + Ensino Médio
- **II — Educação Superior**

## Educação Infantil (arts. 29-31)
- Finalidade: desenvolvimento integral da criança até 5 anos e 11 meses
- **Creche**: 0 a 3 anos | **Pré-escola**: 4 a 5 anos
- Avaliação: mediante acompanhamento e registro, **sem promoção ou retenção**
- Carga horária mínima: **800h/ano**, **4h diárias** (parcial) ou 7h (integral)

## Ensino Fundamental (arts. 32-34)
- **9 anos** de duração; obrigatório e gratuito; matrícula a partir dos 6 anos
- Objetivos: leitura/escrita, cálculo, compreensão do ambiente, fortalecimento dos vínculos
- Carga horária mínima: **800h/ano** em pelo menos **200 dias** letivos
- Anos iniciais (1º-5º) e anos finais (6º-9º)

## Ensino Médio (arts. 35-36)
- **3 anos** de duração mínima; etapa final da Educação Básica
- Carga horária mínima: **1.400h** (Novo EM — Lei 13.415/2017)
- **Itinerários formativos**: linguagens; matemática; ciências da natureza; ciências humanas; formação técnica e profissional
- Base comum: **BNCC** (1.800h máximo)

## Para a prova
- Educação Infantil: **SEM reprovação**, SEM nota — apenas relatórios
- Ensino Fundamental: **6 anos completos** para matrícula no 1º ano
- Art. 23: organização em séries anuais, períodos semestrais, ciclos ou grupos não-seriados
- Jornada integral: progressiva; art. 34 prevê tempo integral como objetivo""",
"versaoCompleta":"""# LDB — Níveis e Etapas da Educação (Arts. 21-38)

## Estrutura Geral

O art. 21 da LDB (Lei 9.394/1996) estabelece dois grandes níveis: **Educação Básica** (composta por Educação Infantil, Ensino Fundamental e Ensino Médio) e **Educação Superior**. A Educação Básica é o foco das provas da SEDF.

## Educação Infantil (Arts. 29-31)

A Educação Infantil é a primeira etapa da Educação Básica. Sua finalidade é o desenvolvimento integral da criança em seus aspectos físico, psicológico, intelectual e social, complementando a ação da família e da comunidade (art. 29).

Organiza-se em: **creche** (0 a 3 anos) e **pré-escola** (4 e 5 anos). A obrigatoriedade de matrícula na pré-escola foi estabelecida pela EC 59/2009.

A avaliação na Educação Infantil far-se-á mediante **acompanhamento e registro do desenvolvimento das crianças, sem o objetivo de promoção, mesmo para o acesso ao Ensino Fundamental** (art. 31, I). Carga horária mínima: 800 horas anuais, em no mínimo 200 dias letivos.

## Ensino Fundamental (Arts. 32-34)

Com duração de **9 anos**, obrigatório e gratuito, com início a partir dos 6 anos de idade (art. 32). Objetivos: leitura, escrita e cálculo; compreensão do ambiente natural e social; fortalecimento dos vínculos de família e dos laços de solidariedade humana.

O art. 23 permite organização flexível: séries anuais, períodos semestrais, ciclos, grupos não-seriados — com progressão regular ou não.

Carga horária: **800 horas/ano** em **200 dias letivos** mínimos.

## Ensino Médio (Arts. 35-38)

Etapa final da Educação Básica, com duração mínima de 3 anos. A **Lei 13.415/2017** (Novo Ensino Médio) reformulou sua estrutura, estabelecendo:
- Carga horária total progressiva até **1.400 horas**
- **BNCC** como base curricular comum
- **Itinerários formativos** escolhidos pelo estudante: linguagens e suas tecnologias; matemática e suas tecnologias; ciências da natureza e suas tecnologias; ciências humanas e sociais aplicadas; formação técnica e profissional

O art. 36-A ao 36-D (incluídos por legislação posterior) tratam da educação profissional integrada ao Ensino Médio."""})

NOVOS.append({"id":"r-le-03","topico":"le-03","disciplina":"legislacao-educacional","bloco":"complementares",
"nome":"LDB — Princípios e fins da educação (arts. 1-3)","incidencia":"alta",
"versaoCurta":"""# LDB — Princípios e Fins (Arts. 1-3)

## Art. 1º — Abrangência da educação
- Educação abrange processos formativos na **vida familiar**, **convivência humana**, **trabalho**, **instituições de ensino e pesquisa**, **movimentos sociais e organizações**, **manifestações culturais**
- §1º: Lei disciplina apenas a educação escolar
- §2º: educação escolar deve vincular-se ao **mundo do trabalho e à prática social**

## Art. 2º — Finalidade da educação
- **Dever da família e do Estado**
- Inspirada nos **princípios de liberdade** e nos **ideais de solidariedade humana**
- Finalidade: **pleno desenvolvimento do educando**, preparo para **exercício da cidadania** e **qualificação para o trabalho**

## Art. 3º — Princípios (11 incisos)
1. Igualdade de condições para o acesso e permanência na escola
2. Liberdade de aprender, ensinar, pesquisar e divulgar a cultura
3. Pluralismo de ideias e concepções pedagógicas
4. Respeito à liberdade e apreço à tolerância
5. Coexistência de instituições públicas e privadas de ensino
6. Gratuidade do ensino público em estabelecimentos oficiais
7. **Valorização do profissional da educação escolar**
8. Gestão democrática do ensino público
9. Garantia de padrão de qualidade
10. Valorização da experiência extraescolar
11. Vinculação entre educação escolar, trabalho e práticas sociais
12. Consideração com a diversidade étnico-racial *(incluído pela Lei 12.796/2013)*
13. Garantia do direito à educação e à aprendizagem ao longo da vida

## Para a prova
- Art. 2º: tríade — pleno desenvolvimento, cidadania, trabalho
- Art. 3º: saber todos os 13 incisos; VII (valorização do profissional) é muito cobrado
- Gestão democrática: princípio que fundamenta PPP, Conselho Escolar
- "Dever da família e do Estado" — família vem antes de Estado na LDB""",
"versaoCompleta":"""# LDB — Princípios e Fins da Educação (Arts. 1-3)

## Art. 1º — Conceito Ampliado de Educação

A LDB adota um conceito amplo de educação, que vai além da escola. O art. 1º reconhece que os processos formativos se desenvolvem em múltiplos espaços: na vida familiar, na convivência humana, no trabalho, nas instituições de ensino e pesquisa, nos movimentos sociais e organizações da sociedade civil, e nas manifestações culturais.

O §2º é particularmente importante: estabelece que a educação escolar deve **vincular-se ao mundo do trabalho e à prática social**. Esse dispositivo fundamenta as propostas de integração curricular e de pedagogia crítica.

## Art. 2º — Dever e Finalidade

A educação é dever da **família** e do **Estado** — nessa ordem. Essa precedência da família reflete a tradição constitucional (CF/88, art. 205) e tem implicações para questões sobre responsabilidade educacional.

A educação é **inspirada nos princípios de liberdade e nos ideais de solidariedade humana**. A finalidade é tripla:
1. **Pleno desenvolvimento do educando** — dimensão pessoal e integral
2. **Preparo para o exercício da cidadania** — dimensão política e social
3. **Qualificação para o trabalho** — dimensão produtiva

## Art. 3º — Princípios do Ensino

Os princípios são a base valorativa de toda a legislação educacional. Os 13 incisos cobrem desde igualdade de acesso (I) até a garantia da aprendizagem ao longo da vida (XIII).

Princípios mais cobrados em concurso:
- **Inciso VII**: valorização do profissional da educação escolar — base para planos de carreira e piso salarial
- **Inciso VIII**: gestão democrática do ensino público — fundamenta conselhos escolares e PPP participativo
- **Inciso IX**: garantia de padrão de qualidade — base para avaliações em larga escala (SAEB, IDEB)
- **Inciso XI**: vinculação entre educação escolar, trabalho e práticas sociais — reitera o art. 1º, §2º

A inclusão do **inciso XII** (diversidade étnico-racial) pela Lei 12.796/2013 demonstra a evolução da LDB para incorporar demandas da educação para as relações étnico-raciais (Lei 10.639/2003)."""})

NOVOS.append({"id":"r-le-04","topico":"le-04","disciplina":"legislacao-educacional","bloco":"complementares",
"nome":"LDB — Direito à educação e dever de educar (arts. 4-7)","incidencia":"alta",
"versaoCurta":"""# LDB — Direito à Educação (Arts. 4-7)

## Art. 4º — Dever do Estado (o mais cobrado!)
O Estado deve garantir:
- **I**: Educação Básica obrigatória e gratuita dos **4 aos 17 anos** (EC 59/2009)
- **II**: Educação Infantil gratuita às crianças de até 5 anos
- **III**: Atendimento ao educando na Educação Básica pública por meio de: transporte, alimentação, material didático-escolar e assistência à saúde
- **IV**: Acesso público e gratuito aos ensinos fundamental e médio para todos os que não os concluíram na idade própria
- **V**: Acesso aos níveis mais elevados do ensino, da pesquisa e da criação artística, segundo a capacidade de cada um
- **VIII**: Atendimento ao educando com deficiência, TGD e altas habilidades
- **X**: Vaga na escola pública de Educação Infantil ou Ensino Fundamental mais próxima da residência *(cobrado!)*

## Art. 5º — Exigibilidade
- Direito é exigível judicialmente: pais podem acionar o **Ministério Público**
- Censo escolar anual identificará crianças fora da escola

## Art. 6º — Obrigatoriedade dos pais
- Dever dos pais ou responsáveis: **efetuar a matrícula** das crianças na Educação Básica a partir dos 4 anos

## Art. 7º — Ensino privado
- Livre à iniciativa privada com: cumprimento das normas gerais + autorização do poder público + capacidade de autofinanciamento

## Para a prova
- "4 a 17 anos" é pós-EC 59/2009 (antes era 6-14)
- Art. 4º, X: escola mais próxima da residência — questão recorrente
- Art. 6º: pais obrigados a matricular a partir dos **4 anos**
- Ensino privado: 3 requisitos do art. 7º""",
"versaoCompleta":"""# LDB — Direito à Educação e Dever de Educar (Arts. 4-7)

## Art. 4º — O Dever do Estado

O art. 4º é o mais extenso e cobrado dessa seção. Ele especifica como o Estado cumpre seu dever constitucional de garantir educação a todos.

O inciso I foi profundamente alterado pela **Emenda Constitucional 59/2009**: a obrigatoriedade escolar, que antes era do Ensino Fundamental (6 a 14 anos), foi ampliada para **toda a Educação Básica dos 4 aos 17 anos**. Isso incluiu a pré-escola (4-5 anos) e o Ensino Médio na obrigatoriedade.

O inciso III estabelece que o atendimento ao educando na Educação Básica pública inclui, além da instrução, serviços de **suporte à permanência**: transporte escolar, alimentação, material didático e assistência à saúde. Esses serviços não são opcionais — são obrigações do Estado.

O inciso VIII garante atendimento especializado para **educandos com deficiência, transtornos globais do desenvolvimento e altas habilidades/superdotação**, preferencialmente na rede regular.

O inciso X — vaga na **escola pública mais próxima da residência** — é muito cobrado. Implica que o Estado não pode designar arbitrariamente uma escola distante quando houver vaga próxima.

## Art. 5º — Exigibilidade Judicial

O art. 5º transforma o direito à educação em direito subjetivo público: qualquer cidadão, grupo de cidadãos, associação comunitária ou organização sindical pode acionar o **Poder Público** e o **Ministério Público** para exigi-lo. O MP tem legitimidade para agir de ofício. Esse dispositivo tem sido usado para garantir vagas em creches por via judicial.

O censo escolar anual (atribuição do INEP) deve identificar crianças fora da escola para que o Estado tome as providências necessárias.

## Art. 6º — Obrigatoriedade Familiar

O dever de **efetuar a matrícula** é dos pais ou responsáveis. A partir dos **4 anos** (pré-escola), a matrícula é obrigatória. O descumprimento pode acarretar responsabilização, inclusive com comunicação ao Conselho Tutelar.

## Art. 7º — Ensino Privado

O ensino é livre à iniciativa privada, desde que atenda: cumprimento das normas gerais de educação nacional; autorização e avaliação de qualidade pelo Poder Público; e capacidade de autofinanciamento (não dependência de verbas públicas como condição de existência, salvo parcerias regulamentadas)."""})

NOVOS.append({"id":"r-le-05","topico":"le-05","disciplina":"legislacao-educacional","bloco":"complementares",
"nome":"Constituição Federal — arts. 205-217 (Educação, Cultura, Desporto)","incidencia":"alta",
"versaoCurta":"""# CF/88 — Educação, Cultura e Desporto (Arts. 205-217)

## Art. 205 — Educação: direito e dever
- Direito de todos, dever do **Estado e da família**
- Promovida e incentivada com a colaboração da sociedade
- Visando: pleno desenvolvimento da pessoa, preparo para cidadania, qualificação para trabalho

## Art. 206 — Princípios do ensino (8 incisos)
- I — Igualdade de condições de acesso e permanência
- II — Liberdade de aprender, ensinar, pesquisar e divulgar
- III — Pluralismo de ideias e concepções pedagógicas
- IV — Gratuidade do ensino público
- V — Valorização dos profissionais da educação *(piso salarial garantido)*
- VI — Gestão democrática do ensino público
- VII — Garantia de padrão de qualidade
- VIII — Piso salarial profissional nacional (EC 53/2006)

## Art. 208 — Deveres do Estado
- I: Educação Básica obrigatória e gratuita dos **4 aos 17 anos**
- II: Progressiva universalização do Ensino Médio gratuito
- IV: Atendimento em creche e pré-escola para crianças de **0 a 5 anos**
- V: Acesso aos níveis mais elevados segundo capacidade
- VII: Atendimento ao educando com deficiência, preferencialmente na rede regular

## Art. 212 — Vinculação de recursos
- **União: mínimo 18%** da receita líquida de impostos
- **Estados e DF: mínimo 25%**
- **Municípios: mínimo 25%**

## Arts. 215-217 — Cultura e Desporto
- Art. 215: Estado garante pleno exercício dos direitos culturais
- Art. 216: Patrimônio cultural — bens materiais e imateriais
- Art. 217: Desporto como direito; recursos para desporto educacional prioritariamente

## Para a prova
- Art. 206, VIII: piso salarial nacional do professor (base do PSPN)
- Art. 212: percentuais de vinculação (18% União, 25% demais)
- Direito à educação: **subjetivo público** — exigível judicialmente""",
"versaoCompleta":"""# CF/88 — Educação, Cultura e Desporto (Arts. 205-217)

## Art. 205 — O Direito à Educação

A CF/88 consagra a educação como **direito social** (art. 6º) e, na seção específica (art. 205), define-a como direito de todos e dever do Estado e da família. A tríade finalística — desenvolvimento da pessoa, cidadania, trabalho — espelha-se no art. 2º da LDB.

## Art. 206 — Princípios do Ensino

Os oito princípios do art. 206 estruturam toda a legislação educacional. Destacam-se:

O inciso **V** (valorização dos profissionais da educação) foi o fundamento constitucional para a Lei 11.738/2008, que criou o **PSPN (Piso Salarial Profissional Nacional)** do magistério.

O inciso **VI** (gestão democrática) impõe que o ensino público seja administrado com participação da comunidade — base para Conselhos Escolares, eleição de diretores e construção coletiva do PPP.

O inciso **VIII** foi inserido pela EC 53/2006 e garantiu o piso salarial nacional como direito constitucional, não apenas legal.

## Art. 207 — Autonomia Universitária

As universidades gozam de autonomia didático-científica, administrativa e de gestão financeira e patrimonial. Obedecerão ao princípio de **indissociabilidade entre ensino, pesquisa e extensão**.

## Art. 208 — Deveres Específicos do Estado

O art. 208 detalha como o Estado cumpre o dever do art. 205. O §1º transforma o acesso ao Ensino Fundamental (e, após EC 59/2009, toda a Educação Básica obrigatória dos 4-17 anos) em **direito público subjetivo** — o que significa que pode ser exigido judicialmente pelo indivíduo.

O inciso IV garante atendimento em creche e pré-escola para crianças de **0 a 5 anos** — fundamento constitucional para políticas de Educação Infantil.

## Art. 212 — Vinculação Orçamentária

A CF institui percentuais mínimos de investimento em manutenção e desenvolvimento do ensino:
- **União**: nunca menos que **18%** da receita líquida de impostos
- **Estados, DF e Municípios**: nunca menos que **25%**

Esses percentuais são vinculados — não podem ser desviados para outras finalidades. O FUNDEB (EC 108/2020) é o principal mecanismo de redistribuição desses recursos.

## Arts. 215-217 — Cultura e Desporto

O art. 215 garante o pleno exercício dos direitos culturais e acesso às fontes da cultura nacional. O art. 216 define o **patrimônio cultural brasileiro** como bens materiais e imateriais que remetem à identidade, ação e memória dos grupos formadores da sociedade brasileira — tombamento, registro, vigilância e desapropriação são formas de proteção.

O art. 217 reconhece o desporto como direito e prioriza os recursos para o **desporto educacional**, antes do de rendimento e de participação."""})

todos = dados["resumos"] + [r for r in NOVOS if r["topico"] not in existentes]
dados["resumos"] = todos
dados["versao"] = "2.1.0"
with open(SRC,"w",encoding="utf-8") as f: json.dump(dados,f,ensure_ascii=False,indent=2)
print(f"Batch 1 OK — total: {len(todos)}")
