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
