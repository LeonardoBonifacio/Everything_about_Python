from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = ("TVM", "Trocar válvula do Motor")
    TROCAR_OLEO = ("TO", "Trocar óleo")
    BALANCEAMENTO = ("B", "Balanceamento")