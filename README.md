# TechFlow Tasks

Sistema web de gerenciamento de tarefas baseado em metodologias ágeis, desenvolvido pela
(fictícia) **TechFlow Solutions** para uma startup de logística.

## Objetivo

Permitir que a equipe acompanhe o fluxo de trabalho em tempo real por meio de um quadro
Kanban, priorize tarefas críticas e monitore o desempenho do time.

## Escopo inicial (v1.0)

- CRUD de tarefas (criar, listar, editar, excluir).
- Quadro Kanban com as colunas **A Fazer**, **Em Progresso** e **Concluído**.
- API REST (`/api/tasks`) e interface web simples.
- Testes automatizados e integração contínua (GitHub Actions).

## Metodologia

Adotamos um modelo **híbrido Scrum + Kanban**:

- **Scrum:** trabalho dividido em sprints curtas, com planejamento e revisão.
- **Kanban:** fluxo visual no GitHub Projects com limite de trabalho em progresso (WIP).
- **Commits semânticos** (`feat:`, `fix:`, `docs:`, `test:`, `ci:`, `chore:`).
- **CI** a cada push: lint (flake8) e testes (pytest).

O quadro Kanban está descrito em [`docs/kanban.md`](docs/kanban.md).

## Estrutura de diretórios

```
src/        código da aplicação (Flask)
tests/      testes automatizados (pytest)
docs/       documentação, quadro Kanban e diagramas UML
.github/    workflow de integração contínua
```

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m src.app                # abre em http://127.0.0.1:5000
```

## Como testar

```bash
pytest -v
flake8 src tests --max-line-length=120
```

## Gestão de mudanças - CR-001 (mudança de escopo)

**Solicitação do cliente:** durante a sprint 2, a startup de logística informou que precisava
*priorizar entregas críticas* e *medir o desempenho da equipe*, algo fora do escopo inicial (só CRUD).

**Decisão:** aceitar a mudança, pois ela atende diretamente ao objetivo do projeto (priorizar tarefas
críticas e monitorar o desempenho), tem baixo custo técnico e baixo risco (campo novo com valor padrão,
sem quebrar a API existente).

**O que mudou:**

- Novo campo `priority` na tarefa (`low`, `medium`, `high`, `critical`; padrão `medium`).
- Novo endpoint `GET /api/stats` com total, tarefas por status, taxa de conclusão e críticas abertas.
- Interface web exibe a prioridade e permite escolhê-la ao criar a tarefa.
- Kanban: criado o card **[CR-001] Prioridade e métricas**, priorizado no topo; o item "Autenticação"
  foi mantido no backlog (To Do).
- Testes automatizados novos cobrem a prioridade e as métricas.

**Impacto:** +1 sprint-dia de esforço; nenhum endpoint existente foi alterado de forma incompatível.
