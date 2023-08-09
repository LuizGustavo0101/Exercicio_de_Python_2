def menor_palavra(lista_palavras):
    return min(lista_palavras, key=len)
    
def maior_palavra(lista_palavras):
    return max(lista_palavras, key=len)

palavras = ["python", "programacao", "codigo", "linguagem", "ai"]
menor = menor_palavra(palavras)
maior = maior_palavra(palavras)
print("Menor palavra:", menor, "\nMaior palavra:", maior)