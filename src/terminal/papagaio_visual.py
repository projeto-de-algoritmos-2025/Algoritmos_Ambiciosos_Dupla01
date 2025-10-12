try:
    from colorama import init, Fore, Style
    init()  # Inicializa colorama para Windows
    CORES_DISPONIVEL = True
except ImportError:
    CORES_DISPONIVEL = False


def papagaio_normal():
    if CORES_DISPONIVEL:
        return (f"    {Fore.RED}..-..{Style.RESET_ALL}\n"
                f"   {Fore.GREEN}/{Style.RESET_ALL}o {Fore.YELLOW}v{Style.RESET_ALL} o{Fore.GREEN}\\{Style.RESET_ALL}\n"
                f"  {Fore.GREEN}( /   \\ ){Style.RESET_ALL}\n"
                f" {Fore.YELLOW}====w=w==={Style.RESET_ALL}{Fore.CYAN}< {Style.RESET_ALL}")
    else:
        return """    ..-..
   /o v o\\
  ( /   \\ )
 ====w=w===< """


def papagaio_pensando():
    if CORES_DISPONIVEL:
        return (f"    {Fore.RED}..-..{Style.RESET_ALL}\n"
                f"   {Fore.GREEN}/{Style.RESET_ALL}? {Fore.YELLOW}v{Style.RESET_ALL} ?{Fore.GREEN}\\{Style.RESET_ALL}\n"
                f"  {Fore.GREEN}( /   \\ ){Style.RESET_ALL}\n"
                f" {Fore.YELLOW}====w=w==={Style.RESET_ALL}{Fore.BLUE}< {Style.RESET_ALL}")
    else:
        return """    ..-..
   /? v ?\\
  ( /   \\ )
 ====w=w===< """


def papagaio_feliz():
    if CORES_DISPONIVEL:
        return (f"    {Fore.RED}..-..{Style.RESET_ALL}\n"
                f"   {Fore.GREEN}/{Style.RESET_ALL}^ {Fore.YELLOW}v{Style.RESET_ALL} ^{Fore.GREEN}\\{Style.RESET_ALL}\n"
                f"  {Fore.GREEN}( /   \\ ){Style.RESET_ALL}\n"
                f" {Fore.YELLOW}====w=w==={Style.RESET_ALL}{Fore.GREEN}< {Style.RESET_ALL}")
    else:
        return """    ..-..
   /^ v ^\\
  ( /   \\ )
 ====w=w===< """


def mostrar_papagaio_falando(texto, estado="normal"):
    if estado == "pensando":
        ascii_art = papagaio_pensando()
    elif estado == "feliz":
        ascii_art = papagaio_feliz()
    else:
        ascii_art = papagaio_normal()
    
    print(ascii_art + f'"{texto}"') 
    if CORES_DISPONIVEL:
        print(f"        {Fore.YELLOW}|_|{Style.RESET_ALL}")
    else:
        print("        |_|")


def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def cabecalho_projeto():
    if CORES_DISPONIVEL:
        print(f"{Fore.CYAN}🦜 Tradutor do Papagaio - Algoritmo de Huffman{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    else:
        print("🦜 Tradutor do Papagaio - Algoritmo de Huffman")
        print("=" * 50)
    print()
