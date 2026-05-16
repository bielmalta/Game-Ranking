# Contribuindo com o Game Ranking

Este guia explica como montar o ambiente, rodar a aplicação localmente, executar os testes e abrir contribuições. Foi escrito para quem está chegando agora no projeto, então não pula etapas.

## Pré-requisitos

- **Python 3.13** (a pipeline usa essa versão; testar localmente em outras pode funcionar mas não é garantido)
- **Node.js 20+** (necessário para rodar os testes E2E com Cypress)
- **Git**
- **Um editor de código** (VS Code, PyCharm, qualquer um serve)
- Sistema operacional: já foi rodado em Windows, macOS e Ubuntu

## Passo a passo

### 1. Clonar o repositório

```bash
git clone https://github.com/CC-2025-2-CESAR/Game-Ranking.git
cd Game-Ranking
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
```

Ativar:

- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
- **macOS/Linux:** `source .venv/bin/activate`

### 3. Instalar dependências Python

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz com no mínimo:

```env
SECRET_KEY=algumacoisa-aleatoria-para-dev
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000
```

Em dev você não precisa de `DATABASE_URL` — o projeto cai para `sqlite:///db.sqlite3` automaticamente.

### 5. Rodar as migrações

```bash
python manage.py migrate
```

### 6. (Opcional) Criar um superusuário

Para acessar o admin em `/admin/` e cadastrar jogos:

```bash
python manage.py createsuperuser
```

### 7. Subir o servidor

```bash
python manage.py runserver
```

Abra http://127.0.0.1:8000/ no navegador.

## Rodar os testes

### Testes Django (unitários/integração)

```bash
python manage.py test
```

### Testes E2E (Cypress)

Em um terminal, suba o servidor (passo 7 acima). Em outro terminal:

```bash
npm install     # apenas na primeira vez
npm run cypress:open    # modo interativo (UI)
npm run cypress:run     # modo headless (gera vídeo em cypress/videos/)
```

Os specs ficam em `cypress/e2e/`. Os comandos auxiliares estão em `cypress/support/commands.js`.

Para rodar contra o site no ar (cuidado — cria dados reais no Postgres de produção):

```bash
npm run cypress:run:prod
```

## Fluxo de contribuição

1. **Crie uma branch nova a partir de `main`** com prefixo coerente:
   - `feat/<descricao>` para novas funcionalidades
   - `fix/<descricao>` para correções de bug
   - `chore/<descricao>` para configurações, deps, infra
   - `ci/<descricao>` para mudanças em pipeline
   - `docs/<descricao>` para README, guias, etc.
2. **Commits frequentes** (no mínimo semanais, conforme regra do projeto). Cada commit deve representar uma unidade lógica — não junte 5 mudanças não relacionadas em um único commit.
3. **Mensagens de commit** em inglês ou português, começando com verbo no imperativo. Exemplos:
   - `Add played games list feature`
   - `Fix CSRF error on rating form`
   - `Update Azure deployment URL`
4. **Antes de abrir a PR**, rode localmente:
   - `python manage.py test`
   - `npm run cypress:run` (com o servidor local rodando)
   - `python manage.py collectstatic --noinput --dry-run` quando mexer em CSS, imagens, favicon ou outros arquivos estáticos
5. **Abra a PR contra `main`** com:
   - Título curto e descritivo
   - Resumo do que mudou e por quê
   - Checklist de testes que você rodou
6. **Aguarde o CI passar** (jobs `test`, `cypress`, e `deploy` no caso de merge).

## Estrutura do projeto

```
Game-Ranking/
├── Game_Ranking/         # configurações Django (settings, urls, wsgi)
├── accounts/             # app de usuários (login, cadastro, perfil)
├── games/                # app principal (Game, Genre, PlayedGame, ranking, busca)
│   └── static/games/img/ # logo, favicon e imagens estáticas do app
├── reviews/              # app de avaliações e comentários
├── templates/            # templates HTML organizados por app
├── cypress/              # testes E2E
│   ├── e2e/              # specs
│   ├── support/          # comandos customizados (createTestUser, etc.)
│   └── fixtures/
├── .github/workflows/    # pipelines CI/CD (Django + Cypress + deploy Azure)
├── manage.py
└── requirements.txt
```

## Restrições do projeto

Esse projeto é uma atividade prática de FDS e segue duas regras técnicas:

- **Sem generic views** (`ListView`, `DetailView`, etc.) — usar views como função.
- **Sem `django.forms` para a lógica de novas histórias** — ler dados de `request.POST` direto. As views existentes em `reviews/views.py` são bons modelos.

## Padrões úteis

- Para arquivos estáticos novos, use nomes descritivos e salve em `games/static/games/img/` quando forem assets visuais do site.
- Para trailers do YouTube, cadastre a URL normal (`watch?v=...`, `youtu.be/...` ou `/embed/...`); o modelo converte automaticamente para iframe.
- Para capas de jogos, prefira preencher `cover_url` como fallback quando também houver upload local. Assim a página não quebra se o arquivo do storage não existir.
- Para correções de bug, adicione pelo menos um teste que reproduza o problema antes ou junto da correção.

## Dúvidas?

Abrir uma issue no repositório ou falar com o time no Slack da turma.
