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
- ver o perfil do usuário

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

- Site deploy: https://game-ranking.onrender.com/
- Prints do Jira: <img width="1920" height="948" alt="2image" src="https://github.com/user-attachments/assets/3311cfad-5c0e-4bf4-ab2d-5f1037d5d148" />
                  <img width="1761" height="916" alt="sprint2" src="https://github.com/user-attachments/assets/53430806-ad34-4a9d-915c-a2f255f6fbcd" />

- Screencast: https://youtu.be/iYjTGXvBgdk
- Relatório de pair programming: 

Durante a prática de pair programming, as duplas alternaram os papéis de driver e navigator, mantendo comunicação constante, revisando o código continuamente e dividindo tarefas de forma lógica para garantir produtividade. Como resultado, houve redução de erros, maior clareza nas soluções, aprendizado mútuo, melhoria na qualidade do código e desenvolvimento de habilidades de comunicação e trabalho em equipe. Apesar de desafios como adaptação ao ritmo do parceiro, divergências de ideias e maior tempo na tomada de decisões, esses foram superados com diálogo e colaboração, tornando a prática eficaz tanto tecnicamente quanto no fortalecimento de competências interpessoais essenciais na área de tecnologia.
Durante a prática de pair programming, as duplas alternaram os papéis de driver e navigator, mantendo comunicação constante, revisando o código continuamente e dividindo tarefas de forma lógica para garantir produtividade. Como resultado, houve redução de erros, maior clareza nas soluções, aprendizado mútuo, melhoria na qualidade do código e desenvolvimento de habilidades de comunicação e trabalho em equipe. Apesar de desafios como adaptação ao ritmo do parceiro, divergências de ideias e maior tempo na tomada de decisões, esses foram superados com diálogo e colaboração, tornando a prática eficaz tanto tecnicamente quanto no fortalecimento de competências interpessoais essenciais na área de tecnologia.
## Entrega 3
-Prints do jira:
-screencast (histórias):
-screencast (CI/CD):
-screencast (Testes):
- Relatório de pair programming:
Após um período de continuidade na prática de pair programming, foi possível observar uma evolução significativa na dinâmica das duplas, com maior sincronização entre driver e navigator e redução das divergências iniciais. A comunicação tornou-se mais objetiva e eficiente, permitindo decisões mais rápidas e um fluxo de trabalho mais natural. Além disso, houve aumento na confiança entre os participantes, refletindo em maior autonomia e produtividade. Os erros continuaram sendo minimizados e a qualidade do código manteve-se elevada, evidenciando que a prática constante contribui não apenas para o aprimoramento técnico, mas também para o fortalecimento do trabalho em equipe e adaptação a diferentes estilos de pensamento.


