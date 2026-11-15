"""Validação de entradas do sistema (regras de negócio simples)."""

# Status possíveis de uma tarefa = colunas do quadro Kanban
STATUSES = ("todo", "doing", "done")

TITLE_MAX_LENGTH = 100


class ValidationError(ValueError):
    """Erro lançado quando uma entrada não respeita as regras."""


def validate_title(title):
    """Valida e normaliza o título: obrigatório, texto, até 100 caracteres."""
    if not isinstance(title, str) or not title.strip():
        raise ValidationError("O título é obrigatório.")
    title = title.strip()
    if len(title) > TITLE_MAX_LENGTH:
        raise ValidationError(f"O título deve ter até {TITLE_MAX_LENGTH} caracteres.")
    return title


def validate_status(status):
    """Valida o status: deve ser um dos valores de STATUSES."""
    if status not in STATUSES:
        raise ValidationError(f"Status inválido. Use um destes: {', '.join(STATUSES)}.")
    return status
