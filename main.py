import ssl
import socket
import time
import json
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Input & Output files
WORKING_SNI_FILE = "working_sni.txt"

# List of JSON files
FILES = {
    "Facebook": "./dns_repo/facebook_data.json",
    "LinkedIn": "./dns_repo/linkedin_data.json",
    "Netflix": "./dns_repo/netflix_data.json",
    "WhatsApp": "./dns_repo/whatsapp_data.json",
    "YouTube": "./dns_repo/youtube_data.json",
    "Zoom": "./dns_repo/zoom_data.json",
    "Garena(gaming)": "./dns_repo/garena_data.json",
    "SteamPowered(gaming)": "./dns_repo/steampowered_data.json",
    # "Dialog(Zero CK)": "./dns_repo/dialog_data.json",
    # "Mobitel(Zero CK)": "./dns_repo/mobitel_data.json",
    # "Slt(Zero CK)": "./dns_repo/slt_data.json",

}


def check_sni(host, port=443, timeout=5):
    """Checks if an SNI is valid by establishing an SSL connection."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=host):
                return True
    except (ssl.SSLError, socket.error):
        return False


def test_latency(host):
    """Measures latency using a TCP connection."""
    try:
        start = time.time()
        socket.create_connection((host, 443), timeout=5).close()
        return round((time.time() - start) * 1000, 2)  # ms
    except socket.error:
        return None


def load_domains_from_json(file_path):
    """Reads JSON file and extracts 'domain' field."""
    with open(file_path, "r") as f:
        data = json.load(f)
        domains = [entry.get("domain").rstrip('.') for entry in data if "domain" in entry]
    return domains


def runCk(file_path, provider_name):
    """Check SNIs and save results."""
    try:
        domains = load_domains_from_json(file_path)
        working_snies = []

        print(Fore.CYAN + f"\n🔍 Checking SNIs for {provider_name}...\n")

        for sni in domains:
            print(Fore.YELLOW + f"Testing: {sni}...", end="\r")
            if check_sni(sni):
                latency = test_latency(sni)
                print(Fore.GREEN + f"[✔] {sni} works! Latency: {latency}ms")
                working_snies.append(f"{sni} - {latency}ms")
            else:
                print(Fore.RED + f"[✘] {sni} failed.")

        if working_snies:
            with open(WORKING_SNI_FILE, "a") as f:
                f.write("\n".join(working_snies) + "\n")
            print(Fore.GREEN + f"\n✅ Results saved in {WORKING_SNI_FILE}")
        else:
            print(Fore.RED + "❌ No working SNIs found.")

    except FileNotFoundError:
        print(Fore.RED + f"❌ Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(Fore.RED + "❌ Error: Invalid JSON format.")


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "="*50)
        print(Fore.YELLOW + "    🔍 SNI Checker Tool - by Dilshan")
        print(Fore.CYAN + "="*50)
        print(Fore.GREEN + "Select the host included in your package:")
        
        # Menu options
        i = 1
        for name in FILES:
            print(f"{i}. {name}")
            i += 1
        print(f"{i}. Check ALL")
        print(f"{i+1}. Exit")
        
        try:
            choice = int(input(Fore.CYAN + "\nEnter your choice: "))
            
            if choice == i+1:
                print(Fore.YELLOW + "👋 Exiting... Goodbye!")
                break
            elif choice == i:
                for provider, path in FILES.items():
                    runCk(path, provider)
            elif 1 <= choice < i:
                provider = list(FILES.keys())[choice-1]
                runCk(FILES[provider], provider)
            else:
                print(Fore.RED + "❌ Invalid choice! Try again.")
            
            input(Fore.CYAN + "\nPress Enter to continue...")
        
        except ValueError:
            print(Fore.RED + "❌ Please enter a valid number.")
            time.sleep(2)


if __name__ == "__main__":
    main()
10