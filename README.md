# Projeto_Analise_Jogos_Steam

Este projeto realiza uma análise exploratória dos dados contidos no arquivo todos_os_jogos.csv, utilizando a biblioteca Pandas para tratamento de dados e as bibliotecas Matplotlib e Seaborn para visualização gráfica. O objetivo é entender melhor o comportamento do mercado de jogos digitais ao longo dos anos, com foco em lançamentos, desenvolvedoras, gêneros, plataformas e publicadoras.

Dados Utilizados
O arquivo todos_os_jogos.csv contém informações sobre jogos digitais, incluindo:
Nome do jogo
Data de lançamento
Desenvolvedor
Publicadora
Gêneros
Categorias
Plataformas
Os dados foram tratados para extrair o ano de lançamento e permitir agregações por diferentes colunas.

Gráficos e Insights
1. Número de jogos únicos lançados por ano
Identifica a evolução do mercado de jogos ao longo do tempo.

Observa-se um crescimento até a última década, com possível queda recente (pode refletir mudança de modelos de distribuição ou dados incompletos para anos recentes).

2. Top 15 desenvolvedoras com mais jogos únicos
Lista os estúdios mais ativos em volume de lançamentos.

Útil para identificar players dominantes no mercado.

3. Top 15 categorias com mais jogos únicos
Mostra quais categorias de jogos são mais frequentes (ex: Indie, Multiplayer, Aventura).

Ajuda a mapear as preferências dos desenvolvedores e jogadores.

4. Top 15 gêneros com mais jogos únicos
Identifica os gêneros mais comuns como Ação, RPG, Estratégia etc.

5. Jogos por ano e desenvolvedora (top 5)
Permite visualizar a produção anual das principais desenvolvedoras.

Ajuda a entender a constância e evolução do portfólio das empresas.

6. Jogos por ano e publicadora (top desenvolvedores)
Analisa quais publicadoras mais lançaram jogos ao longo do tempo, considerando os principais desenvolvedores.

7. Jogos por ano e gêneros (top desenvolvedores)
Verifica os gêneros preferidos pelas desenvolvedoras mais ativas em cada ano.

8. Jogos por ano e plataformas (top desenvolvedores)
Identifica as plataformas mais visadas (PC, Xbox, PS, Switch) por grandes estúdios.

9. Desenvolvedoras x Gêneros (top 5 gêneros)
Gráfico empilhado mostrando a diversificação (ou especialização) de cada desenvolvedora em diferentes gêneros.

10. Desenvolvedoras x Plataformas (top 5 plataformas)
Mostra se as desenvolvedoras são multiplataforma ou especializadas.

11. Publicadoras x Gêneros (top 5 gêneros)
Verifica quais gêneros são mais publicados por grandes distribuidoras.

12. Publicadoras x Plataformas (top 5 plataformas)
Indica o foco estratégico de publicação de acordo com as plataformas mais populares.

Conclusões
O mercado de jogos tem mostrado crescimento expressivo, com forte presença de estúdios grandes e independentes.
Algumas desenvolvedoras se destacam por seu alto volume de lançamentos e diversificação.
Gêneros como Ação e Indie são recorrentes, enquanto plataformas como PC e consoles lideram.
A análise cruzada permite mapear estratégias específicas de empresas (como foco em certo gênero ou plataforma).

Tecnologias e Bibliotecas Utilizadas
Python
Pandas
Matplotlib
Seaborn

