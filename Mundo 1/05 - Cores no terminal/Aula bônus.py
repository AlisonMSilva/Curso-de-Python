# \033[style; text; background 'm'
print("\n")

# Stilo da fonte
print(
  "Texto normal\n" 
  f"\033[1mTexto em negrito\033[m"
  "\n"
  )


# Cor do texto
print(
  "Texto com cor padrão\n"
  f"\033[32mTexto com cor ANSI\033[m"
)

# Cor do Background
print(
  "Background padrão\n"
  f"\033[46mBackround Ciano \033[m"
  "\n"
)

# Combinanação
print("\033[9;30;47mOlá Mundo!\033[m")