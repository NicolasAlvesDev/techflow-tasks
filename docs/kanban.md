# Quadro Kanban (GitHub Projects)

Este arquivo é o **espelho em texto** do quadro criado na aba **Projects** do GitHub
(template *Board*), com as colunas **To Do** (A Fazer), **In Progress** (Em Progresso) e
**Done** (Concluído). Crie os cards abaixo como *issues* e adicione-os ao Project.

## Estado final (após a mudança de escopo)

### To Do (A Fazer)
| # | Card | Descrição |
|---|------|-----------|
| 11 | Persistir tarefas em banco de dados | Trocar o armazenamento em memória por SQLite |
| 12 | Autenticação de usuários | Login simples para o gestor (backlog futuro) |

### In Progress (Em Progresso)
| # | Card | Descrição |
|---|------|-----------|
| 10 | Gravar vídeo pitch e capturar prints | Entregável final da disciplina |

### Done (Concluído)
| # | Card | Descrição |
|---|------|-----------|
| 1 | Estruturar repositório | Diretórios `src`, `tests`, `docs`, `.github` |
| 2 | Escrever README | Objetivo, escopo, metodologia e execução |
| 3 | Validar entradas | Título e status obrigatórios/válidos |
| 4 | Implementar CRUD de tarefas | Repositório em memória |
| 5 | Expor API REST | Endpoints `/api/tasks` |
| 6 | Criar interface web Kanban | Página com três colunas |
| 7 | Configurar CI | GitHub Actions com flake8 e pytest |
| 8 | Modelar UML | Casos de uso e classes |
| 9 | **[CR-001] Prioridade e métricas** | Card criado na mudança de escopo |

## Gestão da mudança (CR-001)

- **Antes:** card 9 não existia; o quadro tinha 8 cards e o escopo era apenas CRUD.
- **Depois:** o cliente pediu priorização de tarefas críticas e monitoramento de desempenho;
  foi criado o card 9, **priorizado acima do backlog**, com commit `feat: adiciona prioridade ...`.
- Regra de WIP: no máximo 2 cards em *In Progress* ao mesmo tempo.
