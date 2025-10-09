import os

def ler_arquivo_texto(caminho_arquivo):
    try:
        if not os.path.exists(caminho_arquivo):
            return False, "Arquivo não encontrado!"
        
        if not os.path.isfile(caminho_arquivo):
            return False, "O caminho não é um arquivo!"
        
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        
        if not conteudo.strip():
            return False, "Arquivo está vazio!"
            
        return True, conteudo
        
    except PermissionError:
        return False, "Sem permissão para ler o arquivo!"
    except UnicodeDecodeError:
        return False, "Arquivo não é um texto válido (problema de codificação)!"
    except Exception as e:
        return False, f"Erro inesperado: {str(e)}"


def listar_arquivos_texto(diretorio="exemplos"):
    try:
        arquivos = []
        for arquivo in os.listdir(diretorio):
            caminho_completo = os.path.join(diretorio, arquivo)
            if os.path.isfile(caminho_completo) and arquivo.lower().endswith('.txt'):
                arquivos.append(arquivo)
        return sorted(arquivos)
    except:
        return []


def obter_tamanho_arquivo(caminho_arquivo):
    try:
        return os.path.getsize(caminho_arquivo)
    except:
        return -1