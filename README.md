\# Olist Analytics



Dashboard de performance de vendas do marketplace Olist.



\## Contexto

Projeto de análise de dados para responder perguntas estratégicas sobre o negócio.



\## Perguntas de Negócio

\- Quais categorias de produto mais vendem?

\- Qual o tempo médio de entrega e como isso impacta a nota do cliente?

\- Qual a sazonalidade das vendas?

\- Quais estados têm melhor performance?



\## Estrutura do Projeto



```

olist-analytics/

├── data/

│   └── raw/              # Dados brutos da Olist (CSVs)

├── notebooks/            # Jupyter Notebooks

├── src/                  # Módulos Python

├── assets/               # Imagens e prints

├── .gitignore

└── README.md

```



\## Stack Tecnológica



| Ferramenta | Propósito |

|------------|-----------|

| Python 3.10+ | Linguagem principal |

| Pandas, NumPy | Manipulação de dados |

| Matplotlib, Seaborn, Plotly | Visualização |

| Streamlit | Dashboard interativo |

| Power BI | Dashboard corporativo |

| Docker | Containerização |

| GitHub Actions | CI/CD |



\## Como Rodar



```bash

\# Clone

git clone https://github.com/mateusfers/olist-analytics.git

cd olist-analytics



\# Ambiente virtual

python -m venv venv

venv\\Scripts\\activate



\# Dependências

pip install pandas numpy matplotlib seaborn plotly streamlit jupyter



\# Dados: baixe da Olist e coloque em data/raw/

```



\## Entregáveis



\- \[x] Setup inicial

\- \[x] Dados baixados

\- \[ ] Análise exploratória

\- \[ ] Dashboard Streamlit

\- \[ ] Dashboard Power BI

\- \[ ] Docker

\- \[ ] CI/CD



\## Status



Em desenvolvimento.

