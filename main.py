import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from terminal.interface_cli import executar_interface  


def main():

    try:
        executar_interface()
    except KeyboardInterrupt:
        print("\n\n🦜 Papagaio saindo... Tchau!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("🦜 O papagaio ficou confuso! Tente novamente.")


if __name__ == "__main__":
    main()