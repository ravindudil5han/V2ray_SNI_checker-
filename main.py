import ssl
import socket
import time
import json

# Input & Output files
HOST_FILE = "./dns_repo/facebook_data.json"
WORKING_SNI_FILE = "working_sni.txt"


def check_sni(host, port=443, timeout=5):
    """
    Checks if an SNI is valid by establishing an SSL connection.
    Returns True if the server responds correctly.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                return True
    except (ssl.SSLError, socket.error):
        return False


def test_latency(host):
    """
    Measures latency using a TCP connection.
    """
    try:
        start = time.time()
        socket.create_connection((host, 443), timeout=5).close()
        return round((time.time() - start) * 1000, 2)  # Convert to ms
    except socket.error:
        return None


def load_domains_from_json(file_path):
    """
    Reads JSON file and extracts the 'domain' field from each object.
    Returns a list of domains.
    """
    with open(file_path, "r") as f:
        data = json.load(f)
        domains = [entry.get("domain").rstrip('.') for entry in data if "domain" in entry]
    return domains


def main():
    try:
        domains = load_domains_from_json(HOST_FILE)
        working_snies = []

        for sni in domains:
            print(f"Testing SNI: {sni}...")
            if check_sni(sni):
                latency = test_latency(sni)
                print(f"[✔] {sni} works! Latency: {latency}ms")
                working_snies.append(f"{sni} - {latency}ms")
            else:
                print(f"[✘] {sni} failed.")

        # Save working SNIs
        with open(WORKING_SNI_FILE, "w") as f:
            f.write("\n".join(working_snies))

        print(f"\n✅ Working SNIs saved to {WORKING_SNI_FILE}")

    except FileNotFoundError:
        print(f"❌ Error: {HOST_FILE} not found.")
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON format in host.json")


if __name__ == "__main__":
    main()
