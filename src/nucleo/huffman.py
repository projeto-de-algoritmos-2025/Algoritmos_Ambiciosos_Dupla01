import heapq
from collections import Counter

class NoHuffman:
    # Nó da árvore de Huffman.
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        #Comparador para a fila de prioridade.
        return self.freq < other.freq

def construir_arvore_huffman(texto):
    # Constrói a árvore de Huffman a partir do texto que o usuário inseriu.
    if not texto:
        return None
    
    freq = Counter(texto)
    fila_prioridade = [NoHuffman(char, f) for char, f in freq.items()]
    heapq.heapify(fila_prioridade)

    while len(fila_prioridade) > 1:
        no_esq = heapq.heappop(fila_prioridade)
        no_dir = heapq.heappop(fila_prioridade)
        no_pai = NoHuffman(None, no_esq.freq + no_dir.freq)
        no_pai.left = no_esq
        no_pai.right = no_dir
        heapq.heappush(fila_prioridade, no_pai)

    return fila_prioridade[0] if fila_prioridade else None

def gerar_codigos_huffman(arvore):
    # Gera os códigos de Huffman a partir da árvore.
    if arvore is None:
        return {}

    codigos = {}
    
    def _percorrer_arvore(no, codigo_atual):
        if no.char is not None:
            codigos[no.char] = codigo_atual
            return
        if no.left:
            _percorrer_arvore(no.left, codigo_atual + "0")
        if no.right:
            _percorrer_arvore(no.right, codigo_atual + "1")

    _percorrer_arvore(arvore, "")
    return codigos

def codificar_texto(texto, codigos):
    # Codifica o texto usando os códigos de Huffman.
    return "".join(codigos[char] for char in texto)

def decodificar_texto(texto_codificado, arvore):
    # Decodifica o texto usando a árvore de Huffman.
    if not texto_codificado or not arvore:
        return ""

    texto_decodificado = []
    no_atual = arvore
    for bit in texto_codificado:
        if bit == '0': no_atual = no_atual.left
        else: no_atual = no_atual.right

        if no_atual.char is not None:
            texto_decodificado.append(no_atual.char)
            no_atual = arvore
            
    return "".join(texto_decodificado)

def calcular_estatisticas(texto_original, texto_codificado, codigos):
    # Calcula as estatísticas de compressão.
    bits_originais = len(texto_original) * 8
    bits_comprimidos = len(texto_codificado)
    
    taxa_compressao = 0
    if bits_originais > 0:
        taxa_compressao = 100 * (1 - (bits_comprimidos / bits_originais))

    return {
        "bits_originais": bits_originais,
        "bits_comprimidos": bits_comprimidos,
        "taxa_compressao": taxa_compressao,
        "frequencias": Counter(texto_original),
        "codigos": codigos
    }
