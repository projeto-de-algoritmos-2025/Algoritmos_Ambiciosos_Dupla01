import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from terminal.papagaio_visual import (
    mostrar_papagaio_falando, 
    cabecalho_projeto, 
    limpar_tela
)

from nucleo.huffman import (
    construir_arvore_huffman,
    gerar_codigos_huffman,
    codificar_texto,
    calcular_estatisticas
)


def mostrar_menu_principal():
    print("O que você gostaria de fazer?")
    print()
    print("1  Ensinar texto para o papagaio")
    print("2  Carregar texto de arquivo")
    print("3  Ver demonstração")
    print("4  Sair")
    print()


def obter_escolha_usuario():
    try:
        escolha = input("Digite sua escolha (1-4): ").strip()
        return escolha
    except KeyboardInterrupt:
        print("\n")
        mostrar_papagaio_falando("Tchau! Até logo! 🦜", "feliz")
        sys.exit(0)


def processar_escolha(escolha):
    if escolha == "1":
        ensinar_texto_papagaio()
        
    elif escolha == "2":
        mostrar_papagaio_falando("Em breve vou ler arquivos!", "pensando")
        input("\nPressione Enter para continuar...")
        
    elif escolha == "3":
        mostrar_demonstracao()
        
    elif escolha == "4":
        mostrar_papagaio_falando("Obrigado por usar o Tradutor do Papagaio! 🦜", "feliz")
        return False
        
    else:
        mostrar_papagaio_falando("Hmm... não entendi essa opção!", "pensando")
        input("\nPressione Enter para tentar novamente...")
    
    return True


def ensinar_texto_papagaio():
    limpar_tela()
    cabecalho_projeto()
    
    mostrar_papagaio_falando("Qual texto você quer me ensinar?", "normal")
    texto = input("\nDigite o texto: ")

    if not texto:
        mostrar_papagaio_falando("Você não digitou nada!", "pensando")
        input("\nPressione Enter para voltar ao menu...")
        return

    arvore = construir_arvore_huffman(texto)
    codigos = gerar_codigos_huffman(arvore)
    texto_codificado = codificar_texto(texto, codigos)
    stats = calcular_estatisticas(texto, texto_codificado, codigos)

    limpar_tela()
    cabecalho_projeto()
    
    mostrar_papagaio_falando("Aprendi um novo texto! Veja como eu o comprimi:", "feliz")
    print()
    
    print("-" * 40)
    print("Estatísticas da Compressão de Huffman")
    print("-" * 40)
    
    print("\n1. Frequência dos Caracteres:")
    for char, freq in sorted(stats["frequencias"].items()):
        print(f"   '{char}': {freq} vez(es)")
        
    print("\n2. Códigos de Huffman Gerados:")
    for char, codigo in sorted(stats["codigos"].items()):
        print(f"   '{char}': {codigo}")
        
    print("\n3. Resultados da Compressão:")
    print(f"   Tamanho original: {stats['bits_originais']} bits")
    print(f"   Tamanho comprimido: {stats['bits_comprimidos']} bits")
    print(f"   Taxa de compressão: {stats['taxa_compressao']:.2f}%")
    
    print("\n4. Texto Codificado:")
    print(f"   {texto_codificado}")
    print("-" * 40)
    
    input("\nPressione Enter para voltar ao menu...")


def mostrar_demonstracao():
    limpar_tela()
    cabecalho_projeto()
    
    print("Demonstração do Algoritmo de Huffman")
    print("-" * 40)
    print()
    
    mostrar_papagaio_falando("Vou mostrar como funciono!", "feliz")
    print()
    
    print("Exemplo: 'hello world'")
    print("Frequências:")
    print("   'l': 3 vezes")
    print("   'o': 2 vezes") 
    print("   'h', 'e', ' ', 'w', 'r', 'd': 1 vez cada")
    print()
    
    mostrar_papagaio_falando("Letras mais comuns = códigos menores!", "normal")
    print()
    
    print("Códigos de exemplo:")
    print("   'l': 0")
    print("   'o': 10") 
    print("   'h': 110")
    print("   etc...")
    print()
    
    mostrar_papagaio_falando("Isso é algoritmo ambicioso em ação!", "feliz")
    
    input("\nPressione Enter para voltar ao menu...")


def executar_interface():
    continuar = True
    
    while continuar:
        limpar_tela()
        cabecalho_projeto()
        
        mostrar_papagaio_falando("Olá! Sou o Papagaio Huffy!", "normal")
        print()
        
        mostrar_menu_principal()
        escolha = obter_escolha_usuario()
        
        print()
        continuar = processar_escolha(escolha)
    
    print("\nObrigado por usar o Tradutor do Papagaio!")