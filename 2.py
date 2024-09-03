texto = "Esta é uma string de exemplo para verificar a quantidade de letras A ou a."

texto_minusculo = texto.lower()
quantidade_a = texto_minusculo.count('a')

if quantidade_a > 0:
    print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
else:
    print("A letra 'a' não foi encontrada na string.")
