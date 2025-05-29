import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Rectangle, Ellipse

# ── Datos ─────────────────────────────────────────────
upper = [
    ("Personas", ["Inducción informal", "Sin tutor", "Supervisión débil"]),
    ("Máquinas", ["PMS sin alerta VIP", "Key encoder sin validación"]),
    ("Entorno", ["Hotel lleno", "Sin política de upgrade"]),
]
lower = [
    ("Materiales", ["Tarjetas similares", "Señalética confusa"]),
    ("Métodos", ["No POE check-in", "Sin checklist VIP"]),
    ("Mediciones", ["Sin KPI errores", "Reclamos sin análisis"]),
]

# ── Figura ────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(18, 9))
ax.axis("off")

spine_y = 0.5
# Espina principal (flecha apuntando a la izquierda)
arrow = FancyArrow(
    0.05,
    spine_y,
    0.82,
    0,
    width=0.012,
    head_width=0.06,
    head_length=0.03,
    color="black",
    length_includes_head=True,
)
ax.add_patch(arrow)

# Efecto / Problema
effect = "Servicio Deficiente\n(Hab. fumador / llaves erróneas)"
ellipse = Ellipse(
    (0.93, spine_y),
    width=0.18,
    height=0.15,
    edgecolor="black",
    facecolor="none",
    lw=1.8,
)
ax.add_patch(ellipse)
ax.text(0.93, spine_y, effect, ha="center", va="center", fontsize=13, fontweight="bold")

# ── Parámetros visuales ───────────────────────────────
anchors = [0.70, 0.50, 0.30]  # puntos de unión de las ramas
dx, dy = 0.12, 0.12  # desplazamiento de la rama principal
sub_len = 0.05  # longitud de sub-causa horizontal
rect_w, rect_h = 0.09, 0.045  # tamaño de la caja


def draw_branch(anchor_x, direction, category, causes):
    end_x = anchor_x - dx  # ↖ / ↙ (hacia la izquierda)
    end_y = spine_y + direction * dy
    # Rama principal
    ax.plot([anchor_x, end_x], [spine_y, end_y], lw=2, color="black")
    # Caja de la categoría
    rect_x = end_x - 0.04
    rect_y = end_y
    box = Rectangle(
        (rect_x - rect_w / 2, rect_y - rect_h / 2),
        rect_w,
        rect_h,
        edgecolor="black",
        facecolor="white",
        lw=1.5,
    )
    ax.add_patch(box)
    ax.text(
        rect_x,
        rect_y,
        category,
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
    )
    # Sub-causas
    n = len(causes)
    for i, cause in enumerate(causes):
        t = (i + 1) / (n + 1)
        x_p = anchor_x - t * dx
        y_p = spine_y + direction * t * dy
        ax.plot([x_p, x_p - sub_len], [y_p, y_p], lw=1.2, color="black")
        ax.text(x_p - sub_len - 0.005, y_p, cause, ha="right", va="center", fontsize=9)


# Dibujar todas las ramas
for idx, x in enumerate(anchors):
    cat_up, subs_up = upper[idx]
    cat_dn, subs_dn = lower[idx]
    draw_branch(x, 1, cat_up, subs_up)
    draw_branch(x, -1, cat_dn, subs_dn)

plt.tight_layout()
plt.savefig("ishikawa_fishbone_left.png", dpi=300, bbox_inches="tight")
plt.show()
