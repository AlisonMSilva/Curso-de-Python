# cores.py

# =========================
# RESET
# =========================
RESET = "\033[m"

# =========================
# ESTILOS
# =========================
NORMAL = "\033[0m"
NEGRITO = "\033[1m"
SUBLINHADO = "\033[4m"
INVERTIDO = "\033[7m"

# =========================
# CORES DO TEXTO
# =========================
PRETO = "\033[30m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
ROXO = "\033[35m"
CIANO = "\033[36m"
BRANCO = "\033[37m"

# =========================
# CORES DE FUNDO
# =========================
FUNDO_PRETO = "\033[40m"
FUNDO_VERMELHO = "\033[41m"
FUNDO_VERDE = "\033[42m"
FUNDO_AMARELO = "\033[43m"
FUNDO_AZUL = "\033[44m"
FUNDO_ROXO = "\033[45m"
FUNDO_CIANO = "\033[46m"
FUNDO_BRANCO = "\033[47m"

# =========================
# COMBINAÇÕES PRONTAS
# =========================
SUCESSO = "\033[1;32m"      # Verde em negrito
ERRO = "\033[1;31m"         # Vermelho em negrito
AVISO = "\033[1;33m"        # Amarelo em negrito
INFO = "\033[1;34m"         # Azul em negrito
DESTAQUE = "\033[7;37;40m"  # Branco invertido

# =========================
# FUNÇÃO AUXILIAR
# =========================
def colorir(texto: str, cor: str) -> str:
    """
    Retorna o texto colorido e já faz o reset automaticamente.

    Exemplo:
        print(colorir("Olá", VERDE))
    """
    return f"{cor}{texto}{RESET}"