# Game Ranking

Aplicação Django para descobrir jogos: ver os mais avaliados do mês, buscar por título, filtrar por gênero, avaliar, comentar e manter uma lista pessoal de jogos jogados.

> 🌐 Em produção: **https://game-ranking-app-ehfhd4gnhvgtatfq.brazilsouth-01.azurewebsites.net/**

## Sumário

- [O que o site faz](#o-que-o-site-faz)
- [Estrutura das páginas](#estrutura-das-páginas)
- [Como rodar localmente](#como-rodar-localmente)
- [Testes](#testes)
- [Deploy (Azure)](#deploy-azure)
- [Integrantes](#integrantes)
- [Histórico de entregas](#histórico-de-entregas)
  - [Entrega 1](#entrega-1)
  - [Entrega 2](#entrega-2)
  - [Entrega 3](#entrega-3)
  - [Entrega 4](#entrega-4)

## O que o site faz

- Página inicial com top 3 do mês, 10 jogos aleatórios e gêneros clicáveis
- Top 20 do mês em página dedicada
- Busca de jogos por título
- Página de detalhes com sinopse, trailer (iframe), gêneros e site oficial
- Cadastro, login e logout
- Avaliação por estrelas (1–5) e comentário, com edição posterior
- Marcar/desmarcar jogo como "jogado"
- Perfil do usuário com suas avaliações, comentários e jogos jogados

## Estrutura das páginas

| Rota | O que mostra |
|---|---|
| `/` | Home com ranking, jogos aleatórios e gêneros |
| `/buscar/` | Busca de jogos |
| `/ranking/` | Top 20 do mês |
| `/genero/<id>/` | Jogos de um gênero |
| `/jogo/<id>/` | Detalhe do jogo (trailer, avaliação, comentários) |
| `/jogo/<id>/jogado/` | POST que adiciona/remove o jogo da lista de jogados |
| `/accounts/register/` | Cadastro |
| `/accounts/login/` | Login |
| `/accounts/profile/` | Perfil com avaliações, comentários e jogos jogados |

## Como rodar localmente

Detalhes completos em [CONTRIBUTING.md](./CONTRIBUTING.md). Resumo:

```bash
python -m venv .venv
# ative o venv (PowerShell: .venv\Scripts\Activate.ps1 | bash: source .venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abra http://127.0.0.1:8000/.

## Testes

### Django (unit / integração)

```bash
python manage.py test
```

### Cypress (E2E)

Em um terminal, suba o servidor Django (passo acima). Em outro:

```bash
npm install        # apenas na primeira vez
npm run cypress:open    # modo interativo
npm run cypress:run     # modo headless
```

Para rodar contra o site no ar (cria dados reais no banco de produção — use com cuidado):

```bash
npm run cypress:run:prod
```

## Deploy (Azure)

A aplicação é publicada automaticamente em **Azure App Service** via GitHub Actions a cada push para `main`. A pipeline em `.github/workflows/django.yml` tem três jobs encadeados:

1. **`test`** — `python manage.py test`
2. **`cypress`** — sobe `runserver` em sqlite isolado, faz seed mínimo de jogos demo e roda `npm run cypress:run` contra todos os specs E2E
3. **`deploy`** — só roda em push para `main`, depende de `test` E `cypress` passarem, faz `collectstatic` e publica via `azure/webapps-deploy@v3` para o App Service `game-ranking-app`

Na boot da Azure, `startup.sh` aplica migrações, garante o superuser (se as envs `DJANGO_SUPERUSER_*` estiverem definidas) e sobe o `gunicorn`.

Variáveis de ambiente esperadas no Azure App Service (configurar via portal → Configuration → Application settings):

- `SECRET_KEY` — chave secreta do Django (gere uma forte; não reutilize a de dev)
- `DEBUG=False`
- `DATABASE_URL` — string de conexão Postgres
- `ALLOWED_HOSTS` — hostname do App Service
- `CSRF_TRUSTED_ORIGINS` — origem(ns) HTTPS do App Service
- `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD` — opcional, só se quiser auto-criar/atualizar um admin no boot

## Integrantes

- Arthur de Almeida Oliveira
- Arthur Filipe Silva dos Reis
- Gabriel Gondim Malta
- Gabriel Mendes Cavalcanti
- Guilherme Silva Guimarães
- Helio de Moraes Rego Neto
- Matheus Assis de Souza Jacome

## Histórico de entregas

### Entrega 1

- Figma: https://www.figma.com/board/fm0wB9xITXtjeqBeBZYJjj/Sem-t%C3%ADtulo?node-id=0-1&t=9dShIyt3maLOlE0m-1
- Histórias do projeto: https://docs.google.com/document/d/1koSvhLiN-m2yipQsbQeLWTG0vbIIWovv3-FDx5r-KnA/edit?tab=t.0
- Prints do Jira: <img width="1918" height="953" alt="backlog" src="https://github.com/user-attachments/assets/b871f751-84ef-4883-9c39-430a3f953a3b" /> <img width="1920" height="952" alt="sprint" src="https://github.com/user-attachments/assets/0c30683d-836b-4962-a348-e28497bdae3c" />
- Screencast: https://www.youtube.com/watch?v=V_xk95SDth4

### Entrega 2

- Site deploy (histórico — substituído na Entrega 3): https://game-ranking.onrender.com/
- Prints do Jira: <img width="1693" height="341" alt="backlog-e2" src="https://github.com/user-attachments/assets/47e204a0-f367-4e75-911e-a5b0042cf65b" /> <img width="1920" height="998" alt="sprint-e2" src="https://github.com/user-attachments/assets/3b19fc64-7c8f-4570-87fe-de9596b16722" />
- Screencast: https://youtu.be/iYjTGXvBgdk
- Relatório de pair programming:

Durante a prática de pair programming, as duplas alternaram os papéis de driver e navigator, mantendo comunicação constante, revisando o código continuamente e dividindo tarefas de forma lógica para garantir produtividade. Como resultado, houve redução de erros, maior clareza nas soluções, aprendizado mútuo, melhoria na qualidade do código e desenvolvimento de habilidades de comunicação e trabalho em equipe. Apesar de desafios como adaptação ao ritmo do parceiro, divergências de ideias e maior tempo na tomada de decisões, esses foram superados com diálogo e colaboração, tornando a prática eficaz tanto tecnicamente quanto no fortalecimento de competências interpessoais essenciais na área de tecnologia.

### Entrega 3

- Site deploy: https://game-ranking-app-ehfhd4gnhvgtatfq.brazilsouth-01.azurewebsites.net/
- Prints do Jira: <img width="1920" height="704" alt="jira-e3-a" src="https://github.com/user-attachments/assets/c8be4d97-6563-4d7d-970b-bf2f43b976e4" /> <img width="1920" height="997" alt="jira-e3-b" src="https://github.com/user-attachments/assets/0d5ab91e-05fb-4fa6-9956-b9ed476e58f9" />
- Screencast (histórias): https://youtu.be/BfQr5rz33Ek
- Screencast (testes): https://youtu.be/XJjphy9XEuso
- Bugtracker: <img width="1920" height="998" alt="bugtracker" src="https://github.com/user-attachments/assets/48df8e3b-2061-4aeb-bf5b-66bca9a5a7e4" />
- Relatório de pair programming:

Após um período de continuidade na prática de pair programming, foi possível observar uma evolução significativa na dinâmica das duplas, com maior sincronização entre driver e navigator e redução das divergências iniciais. A comunicação tornou-se mais objetiva e eficiente, permitindo decisões mais rápidas e um fluxo de trabalho mais natural. Além disso, houve aumento na confiança entre os participantes, refletindo em maior autonomia e produtividade. Os erros continuaram sendo minimizados e a qualidade do código manteve-se elevada, evidenciando que a prática constante contribui não apenas para o aprimoramento técnico, mas também para o fortalecimento do trabalho em equipe e adaptação a diferentes estilos de pensamento.

### Entrega 4

- Site em produção: https://game-ranking-app-ehfhd4gnhvgtatfq.brazilsouth-01.azurewebsites.net/
- Screencast das histórias finais (com URL visível durante todo o vídeo): _<adicionar link YouTube>_
- Screencast dos testes E2E (execução do `npm run cypress:run`): _<adicionar link YouTube>_
- Screencast do CI/CD (build + testes + deploy automatizado): _<adicionar link YouTube>_
- Sprint 04 no Jira (prints do quadro e do backlog): _<adicionar imagens>_
- Issue/bug tracker (GitHub Issues): https://github.com/CC-2025-2-CESAR/Game-Ranking/issues
<img width="1920" height="1003" alt="image" src="https://github.com/user-attachments/assets/1f2408cc-1c84-4e91-ab82-e4cf16e24d41" />

- Guia de contribuição: [CONTRIBUTING.md](./CONTRIBUTING.md)

#### Histórias entregues nesta sprint

- **Lista de jogos jogados** — botão "Marcar como jogado" / "Remover dos jogos jogados" na página de detalhes, lista no perfil. Modelo `PlayedGame` em `games/models.py`, view `toggle_played` em `games/views.py`, rota `/jogo/<id>/jogado/`, seção "Jogos jogados" em `templates/accounts/profile.html`, spec E2E em `cypress/e2e/07-played.cy.js`.

#### Atualização sobre pair programming

Na Entrega 4 a prática de pair programming foi mantida com rodízio mais ágil entre driver e navigator: o tempo médio em cada papel caiu, permitindo que mais membros tocassem nas partes mais sensíveis do projeto (pipeline CI/CD, modelo `PlayedGame`, configuração da Azure). A maior maturidade do time também permitiu sessões assíncronas — duas pessoas alinhavam por chamada de voz e revisavam em PR no GitHub, sem precisar estar lado a lado o tempo todo. O efeito foi um ciclo de revisão mais curto e menos retrabalho na pipeline de deploy.
