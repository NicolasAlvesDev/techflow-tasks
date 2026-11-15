"""Gera os diagramas UML (casos de uso e classes) em PNG usando matplotlib.

Uso: python docs/uml/generate_uml.py
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Ellipse, Rectangle, FancyArrowPatch  # noqa: E402

OUT = os.path.dirname(os.path.abspath(__file__))
BLUE = "#0b3d91"


def use_case_diagram():
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.set_xlim(0, 100)
    ax.set_ylim(-3, 70)
    ax.axis("off")
    ax.add_patch(Rectangle((25, 1), 50, 66, fill=False, lw=1.5, edgecolor=BLUE))
    ax.text(50, 64, "Sistema TechFlow Tasks", ha="center", fontsize=12, weight="bold", color=BLUE)

    cases = {
        "Criar tarefa": (50, 54, False),
        "Visualizar quadro Kanban": (50, 44, False),
        "Atualizar status da tarefa": (50, 34, False),
        "Excluir tarefa": (50, 24, False),
        "Definir prioridade\n(mudança CR-001)": (50, 14, True),
        "Consultar métricas\nde desempenho (CR-001)": (50, 6, True),
    }
    pos = {}
    for name, (x, y, new) in cases.items():
        ax.add_patch(Ellipse((x, y), 34, 7.5, facecolor="#fde9c9" if new else "#e3ecfb",
                             edgecolor=BLUE, lw=1.2))
        ax.text(x, y, name, ha="center", va="center", fontsize=9)
        pos[name] = (x, y)

    def actor(x, y, label):
        ax.add_patch(plt.Circle((x, y + 8), 2, fill=False, lw=1.5))
        ax.plot([x, x], [y + 6, y], color="k", lw=1.5)
        ax.plot([x - 3, x + 3], [y + 4.5, y + 4.5], color="k", lw=1.5)
        ax.plot([x, x - 3], [y, y - 4], color="k", lw=1.5)
        ax.plot([x, x + 3], [y, y - 4], color="k", lw=1.5)
        ax.text(x, y - 7, label, ha="center", fontsize=10, weight="bold")
        return (x, y + 4)

    member = actor(10, 38, "Membro da equipe")
    manager = actor(90, 38, "Gestor de projeto")

    def link(a, name):
        x, y = pos[name]
        side = -17 if a[0] < 50 else 17
        ax.plot([a[0], x + side], [a[1], y], color="#444", lw=1)

    for n in ["Criar tarefa", "Visualizar quadro Kanban", "Atualizar status da tarefa"]:
        link(member, n)
    for n in ["Visualizar quadro Kanban", "Excluir tarefa", "Definir prioridade\n(mudança CR-001)",
              "Consultar métricas\nde desempenho (CR-001)", "Criar tarefa"]:
        link(manager, n)
    ax.text(50, -1.8, "Laranja = funcionalidades adicionadas pela mudança de escopo", ha="center",
            fontsize=8, style="italic")
    ax.set_title("Diagrama de Casos de Uso", fontsize=13, weight="bold")
    fig.savefig(os.path.join(OUT, "casos_de_uso.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)


def class_box(ax, x, y, w, title, attrs, methods, stereotype=None):
    line = 2.6
    h = 5 + line * (len(attrs) + len(methods)) + 2
    ax.add_patch(Rectangle((x, y - h), w, h, facecolor="#fff", edgecolor=BLUE, lw=1.5))
    head = 5 if stereotype is None else 6.5
    ax.add_patch(Rectangle((x, y - head), w, head, facecolor="#e3ecfb", edgecolor=BLUE, lw=1.5))
    if stereotype:
        ax.text(x + w / 2, y - 2, stereotype, ha="center", va="center", fontsize=8, style="italic")
        ax.text(x + w / 2, y - 4.5, title, ha="center", va="center", fontsize=10, weight="bold")
    else:
        ax.text(x + w / 2, y - head / 2, title, ha="center", va="center", fontsize=10, weight="bold")
    cy = y - head - 1.6
    for a in attrs:
        ax.text(x + 1, cy, a, fontsize=8, va="center", family="monospace")
        cy -= line
    sep = cy + line / 2 + 0.2
    ax.plot([x, x + w], [sep, sep], color=BLUE, lw=1)
    cy -= 0.2
    for m in methods:
        ax.text(x + 1, cy, m, fontsize=8, va="center", family="monospace")
        cy -= line
    return (x, y, w, h)


def arrow(ax, p1, p2, text="", style="-|>", dashed=False):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=14, color="#333",
                                 lw=1.2, linestyle="--" if dashed else "-"))
    if text:
        ax.text((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + 1.2, text, ha="center", fontsize=8)


def class_diagram():
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 80)
    ax.axis("off")

    class_box(ax, 3, 76, 34, "TaskApi (Flask)",
              ["- repo: TaskRepository"],
              ["+ create_app(repo)", "+ list_tasks()", "+ create_task()", "+ get_task(id)",
               "+ update_task(id)", "+ delete_task(id)", "+ stats()  [CR-001]"],
              "<<controller>>")
    class_box(ax, 45, 76, 36, "TaskRepository",
              ["- _tasks: dict[int, Task]", "- _next_id: int"],
              ["+ create(title, desc, status, prio)", "+ get(id): Task", "+ list(): list[Task]",
               "+ update(id, **fields): Task", "+ delete(id): bool", "+ stats(): dict  [CR-001]"])
    class_box(ax, 45, 30, 36, "Task",
              ["+ id: int", "+ title: str", "+ description: str", "+ status: str",
               "+ priority: str  [CR-001]"],
              ["+ to_dict(): dict"])
    class_box(ax, 88, 76, 20, "validators",
              ["STATUSES", "PRIORITIES [CR-001]"],
              ["validate_title()", "validate_status()", "validate_priority()"],
              "<<module>>")
    class_box(ax, 88, 38, 20, "ValidationError",
              [], ["(herda de ValueError)"], "<<exception>>")

    arrow(ax, (37, 62), (45, 62), "usa", "-|>", dashed=True)
    arrow(ax, (63, 48), (63, 30), "", "-")
    ax.text(64.5, 39, "1 contém 0..*", fontsize=8)
    arrow(ax, (81, 66), (88, 66), "usa", "-|>", dashed=True)
    arrow(ax, (98, 56), (98, 38), "lança", "-|>", dashed=True)
    ax.set_title("Diagrama de Classes", fontsize=13, weight="bold")
    fig.savefig(os.path.join(OUT, "classes.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    use_case_diagram()
    class_diagram()
    print("Diagramas gerados em", OUT)
