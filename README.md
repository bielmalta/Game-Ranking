# Game Ranking

Projeto feito em Django para buscar jogos, ver detalhes, avaliar, comentar e acompanhar os títulos que estão em destaque no mês.

## O que o site faz

- mostrar uma página inicial com o top 3 dos jogos mais avaliados do mês
- exibir um botão para acessar o top 20 completo
- mostrar 10 jogos aleatórios na página principal
- listar gêneros clicáveis para o usuário navegar pelos jogos
- permitir busca de jogos em uma página separada
- abrir a página de detalhes de cada jogo
- criar conta com nome de usuário e senha
- entrar e sair da conta
- avaliar jogos
- comentar em jogos
- ver o perfil do usuário com avaliações, comentários e lista de jogos jogados
- marcar e desmarcar um jogo como jogado a partir da página de detalhes

## Estrutura das páginas

- `/` : página principal com ranking, jogos aleatórios e gêneros
- `/buscar/` : página de busca de jogos
- `/ranking/` : top 20 dos jogos mais avaliados do mês
- `/genero/<id>/` : lista de jogos de um gênero
- `/jogo/<id>/` : página de detalhes de um jogo

## Como rodar no computador

1. Crie e ative o ambiente virtual.
2. Instale os pacotes:

```bash
pip install -r requirements.txt
```

3. Rode as migrações:

```bash
python manage.py migrate
```

4. Inicie o projeto:

```bash
python manage.py runserver
```

5. Abra no navegador:

```text
http://127.0.0.1:8000/
```

## Testes E2E (Cypress)

Os testes ponta a ponta usam [Cypress](https://www.cypress.io/) e ficam em `cypress/e2e/`.

1. Em um terminal, suba o servidor Django:

```bash
python manage.py migrate
python manage.py runserver
```

2. Em outro terminal, instale as dependências de teste (apenas na primeira vez):

```bash
npm install
```

3. Rode os testes em modo interativo (abre a UI do Cypress):

```bash
npm run cypress:open
```

Ou em modo headless (gera vídeo em `cypress/videos/`):

```bash
npm run cypress:run
```

Os testes assumem que o servidor está em `http://127.0.0.1:8000` e que o banco tem ao menos um jogo cadastrado (o `db.sqlite3` do repositório já atende).

### Rodar contra o servidor publicado (Azure)

Os mesmos specs podem rodar contra o site no ar — não precisa subir o Django local. Os scripts já têm a `baseUrl` de produção apontando para a Azure:

```bash
npm run cypress:run:prod    # headless, gera vídeo em cypress/videos/
npm run cypress:open:prod   # modo interativo
```

Por baixo dos panos é só um `cypress run --config baseUrl=...`. Para apontar pra qualquer outra URL (staging, etc.), dá pra usar a env `CYPRESS_BASE_URL`:

```bash
CYPRESS_BASE_URL=https://outro-deploy.example.com npm run cypress:run
```

> ⚠️ **Atenção:** rodar contra produção cria usuários, avaliações e comentários reais no banco. Cada execução adiciona um usuário com nome `e2e_user_<timestamp>` e deixa avaliações/comentários nos jogos visitados pelos testes. Use só pra validar uma entrega; pro dia a dia, prefira o servidor local.

## Como foi colocado no Render

O projeto foi publicado no Render usando a criação manual do serviço web.

No Render, usamos:

- o arquivo `build.sh`
- o comando para iniciar o projeto com `gunicorn`
- um banco PostgreSQL já existente na conta

Também foram preenchidas no painel do Render estas variáveis:

- `DATABASE_URL`
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DJANGO_SUPERUSER_USERNAME`
- `DJANGO_SUPERUSER_EMAIL`
- `DJANGO_SUPERUSER_PASSWORD`

## Integrantes

- Arthur de Almeida Oliveira
- Arthur Filipe Silva dos Reis
- Gabriel Gondim Malta
- Gabriel Mendes Cavalcanti
- Guilherme Silva Guimarães
- Helio de Moraes Rego Neto
- Matheus Assis de Souza Jacome

## Entrega 1

- Figma: https://www.figma.com/board/fm0wB9xITXtjeqBeBZYJjj/Sem-t%C3%ADtulo?node-id=0-1&t=9dShIyt3maLOlE0m-1
- Histórias do projeto: https://docs.google.com/document/d/1koSvhLiN-m2yipQsbQeLWTG0vbIIWovv3-FDx5r-KnA/edit?tab=t.0
- Prints do Jira: <img width="1918" height="953" alt="backlog" src="https://github.com/user-attachments/assets/b871f751-84ef-4883-9c39-430a3f953a3b" />
                  <img width="1920" height="952" alt="sprint" src="https://github.com/user-attachments/assets/0c30683d-836b-4962-a348-e28497bdae3c" />


- Screencast: https://www.youtube.com/watch?v=V_xk95SDth4

## Entrega 2

- Site deploy(DESATUALIZADO, novo link na entrega 3): https://game-ranking.onrender.com/
- Prints do Jira: <img width="1693" height="341" alt="erawerawraw" src="https://github.com/user-attachments/assets/47e204a0-f367-4e75-911e-a5b0042cf65b" />
<img width="1920" height="998" alt="image" src="https://github.com/user-attachments/assets/3b19fc64-7c8f-4570-87fe-de9596b16722" />


- Screencast: https://youtu.be/iYjTGXvBgdk
- Relatório de pair programming: 

Durante a prática de pair programming, as duplas alternaram os papéis de driver e navigator, mantendo comunicação constante, revisando o código continuamente e dividindo tarefas de forma lógica para garantir produtividade. Como resultado, houve redução de erros, maior clareza nas soluções, aprendizado mútuo, melhoria na qualidade do código e desenvolvimento de habilidades de comunicação e trabalho em equipe. Apesar de desafios como adaptação ao ritmo do parceiro, divergências de ideias e maior tempo na tomada de decisões, esses foram superados com diálogo e colaboração, tornando a prática eficaz tanto tecnicamente quanto no fortalecimento de competências interpessoais essenciais na área de tecnologia.
Durante a prática de pair programming, as duplas alternaram os papéis de driver e navigator, mantendo comunicação constante, revisando o código continuamente e dividindo tarefas de forma lógica para garantir produtividade. Como resultado, houve redução de erros, maior clareza nas soluções, aprendizado mútuo, melhoria na qualidade do código e desenvolvimento de habilidades de comunicação e trabalho em equipe. Apesar de desafios como adaptação ao ritmo do parceiro, divergências de ideias e maior tempo na tomada de decisões, esses foram superados com diálogo e colaboração, tornando a prática eficaz tanto tecnicamente quanto no fortalecimento de competências interpessoais essenciais na área de tecnologia.
## Entrega 3
- Site deploy: https://game-ranking-app-ehfhd4gnhvgtatfq.brazilsouth-01.azurewebsites.net/ 
- Prints do jira:<img width="1920" height="704" alt="image" src="https://github.com/user-attachments/assets/c8be4d97-6563-4d7d-970b-bf2f43b976e4" />
<img width="1920" height="997" alt="image" src="https://github.com/user-attachments/assets/0d5ab91e-05fb-4fa6-9956-b9ed476e58f9" />


- screencast (histórias): [youtube.com/watch?v=8Kbwe1w_Krs&feature=youtu.be](https://youtu.be/BfQr5rz33Ek)
- screencast (Testes): https://youtu.be/XJjphy9XEuso
- Bugtracker:<img width="1920" height="998" alt="bugtrackerprint1" src="https://github.com/user-attachments/assets/48df8e3b-2061-4aeb-bf5b-66bca9a5a7e4" />

- Relatório de pair programming:
Após um período de continuidade na prática de pair programming, foi possível observar uma evolução significativa na dinâmica das duplas, com maior sincronização entre driver e navigator e redução das divergências iniciais. A comunicação tornou-se mais objetiva e eficiente, permitindo decisões mais rápidas e um fluxo de trabalho mais natural. Além disso, houve aumento na confiança entre os participantes, refletindo em maior autonomia e produtividade. Os erros continuaram sendo minimizados e a qualidade do código manteve-se elevada, evidenciando que a prática constante contribui não apenas para o aprimoramento técnico, mas também para o fortalecimento do trabalho em equipe e adaptação a diferentes estilos de pensamento.

## Entrega 4

- Site em produção: https://game-ranking-app-ehfhd4gnhvgtatfq.brazilsouth-01.azurewebsites.net/
- Screencast das histórias finais (com URL visível durante todo o vídeo): _<adicionar link YouTube>_
- Screencast dos testes E2E (execução do `npm run cypress:run`): _<adicionar link YouTube>_
- Screencast do CI/CD (build + testes + deploy automatizado): _<adicionar link YouTube>_
- Sprint 04 no Jira (prints do quadro e do backlog): _<adicionar imagens>_
- Issue/bug tracker (GitHub Issues): https://github.com/CC-2025-2-CESAR/Game-Ranking/issues
- Guia de contribuição: [CONTRIBUTING.md](./CONTRIBUTING.md)

### Histórias entregues nesta sprint

- **Lista de jogos jogados**: usuário pode marcar/desmarcar um jogo como jogado a partir da página de detalhes; a lista aparece no perfil. Implementada pelo modelo `PlayedGame` em `games/models.py`, view `toggle_played` em `games/views.py`, rota `/jogo/<id>/jogado/` e nova seção "Jogos jogados" em `templates/accounts/profile.html`. Teste E2E em `cypress/e2e/07-played.cy.js`.

### CI/CD

A pipeline (`.github/workflows/django.yml`) tem três jobs encadeados:

1. **`test`** — `python manage.py test` (testes unitários/integração Django).
2. **`cypress`** — sobe `runserver` em sqlite isolado, faz seed de jogos demo e executa `npm run cypress:run` contra todos os specs em `cypress/e2e/`.
3. **`deploy`** — só roda em push para `main`, depende de `test` E `cypress` passarem, faz `collectstatic` e publica para a Azure Web App `game-ranking-app`.

### Atualização sobre pair programming

Na Entrega 4 a prática de pair programming foi mantida com rodízio mais ágil entre driver e navigator: o tempo médio em cada papel caiu, permitindo que mais membros tocassem nas partes mais sensíveis do projeto (pipeline CI/CD, modelo `PlayedGame`, configuração da Azure). A maior maturidade do time também permitiu sessões assíncronas — duas pessoas alinhavam por chamada de voz e revisavam em PR no GitHub, sem precisar estar lado a lado o tempo todo. O efeito foi um ciclo de revisão mais curto e menos retrabalho na pipeline de deploy.
