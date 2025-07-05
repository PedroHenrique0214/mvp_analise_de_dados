# 🏥 Análise de Hospitais e Leitos no Brasil (2016–2025)
Este projeto de MVP da pós-graduação em Ciência e Análise de Dados tem como objetivo analisar a evolução da quantidade de hospitais e leitos no Brasil ao longo do tempo, com foco no impacto da pandemia de COVID-19. A análise considera dados de 2016 a 2025, obtidos do portal de dados do Governo Federal.

## 🎯 Objetivos
📊 Analisar a evolução da quantidade de hospitais e leitos no Brasil ao longo dos anos.

🦠 Avaliar o impacto da pandemia na infraestrutura hospitalar brasileira.

🌍 Verificar se houve diferenças no comportamento entre as regiões e estados do país.

🏥 Comparar a evolução entre hospitais públicos e privados/filantrópicos.

📈 Utilizar algoritmos de machine learning para mostrar que é possível prever a tendência futura da quantidade de hospitais.

📦 Fonte dos Dados
Os dados utilizados foram extraídos do portal dados.gov.br, especificamente da base Leitos e Estabelecimentos de Saúde (CNES), disponíveis no formato .xml de 2016 até 2025.

### 🧠 Metodologia
Extração e Tratamento de Dados:

Download automatizado dos arquivos XML. (Baixei esses dados e subi para o Git Hub para não correr o risco de mudarem o link)

Padronização das colunas, tipos de dados e nomes.

Agrupamentos por data, região, estado e tipo de gestão.

Análise Exploratória:

Evolução mensal do número de hospitais e leitos.

Comparações regionais e por tipo de hospital (público, privado, filantrópico).

Destaque para períodos pré, durante e pós-pandemia.

Modelagem Preditiva:

Modelagem de série temporal com o algoritmo XGBRegressor (XGBoost).

Utilização de features lag e média móvel para previsão.

Avaliação com métricas como RMSE e MAE.

## 🧪 Resultados
Observou-se um aumento significativo no número de leitos durante o auge da pandemia, especialmente em UTIs.

Após o pico da COVID-19, houve uma leve retração na expansão hospitalar.

Hospitais públicos foram os mais impactados na ampliação da capacidade.

Diferenças regionais indicam que o investimento em infraestrutura de saúde não foi uniforme.

A predição com o modelo XGBoost apresentou bons resultados mesmo com um conjunto de dados limitado, mostrando que é possível utilizar machine learning para apoiar decisões no planejamento de saúde.

## ✅ Conclusão
O projeto demonstrou que, mesmo com dados públicos e acessíveis, é possível realizar uma análise robusta e gerar insights relevantes para políticas públicas e planejamento estratégico. A utilização de técnicas de aprendizado de máquina para prever tendências de infraestrutura hospitalar revelou-se promissora, especialmente se for combinada com um maior número de variáveis e um histórico mais amplo de dados.

Com aprimoramentos adicionais, esse tipo de análise pode servir como ferramenta de apoio à gestão pública de saúde, auxiliando na alocação de recursos e antecipação de demandas.

## 🔧 Tecnologias Utilizadas
Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost)

Jupyter Notebook

Git e GitHub

Dados do SUS

VS Code
