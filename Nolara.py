import random
import sys
import time

# color code
PINK = "\033[38;5;201m"
PINK_BG = "\033[48;5;201m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"


def get_timestamp():
    return time.strftime("%H:%M:%S")


def print_ascii_header(target_count):
    ascii_art = f"""{PINK}{BOLD}
 ███╗   ██╗ ██████╗ ██╗      █████╗ ██████╗ █████╗ 
 ████╗  ██║██╔═══██╗██║     ██╔══██╗██╔══██╗██╔══██╗
 ██╔██╗ ██║██║   ██║██║     ███████║██████╔╝███████║
 ██║╚██╗██║██║   ██║██║     ██╔══██║██╔══██╗██╔══██║
 ██║ ╚████║╚██████╔╝███████╗██║  ██║██║  ██║██║  ██║
 ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝{RESET}
    """
    print(ascii_art)
    print(
        f"{PINK}{BOLD}    HATERS EXTERMINATOR v4.0 (MASS OVERKILL - {target_count} TARGETS){RESET}\n"
    )


def generate_fake_ip():
    return f"{random.randint(10, 190)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"


def generate_fake_phone():
    country_codes = ["+1", "+44", "+49", "+33", "+31", "+41", "+34", "+46"]
    cc = random.choice(country_codes)
    num = "".join([str(random.randint(0, 9)) for _ in range(9)])
    return f"{cc} {num[:3]} {num[3:6]} {num[6:]}"


def build_target_list(count=500):
    prefixes = [
        "Wipe",
        "Destroy",
        "Expose",
        "NoMore",
        "Crush",
        "Slain",
        "Fuck",
        "Rage",
        "Stop",
        "Hate",
        "Toxic",
        "Ban",
        "_Anti",
        "xX_",
    ]
    suffixes = [
        "NullSec1337",
        "NullSecGang666",
        "NullSecDevs",
        "NullSecArmy_V2",
        "NullSecNet007",
        "NullSec_Official",
        "NullSecOps",
        "NullSec_X",
        "NullSecNet88",
    ]
    locations = [
    "Zurich, CH",
    "Geneva, CH",
    "Basel, CH",
    "Bern, CH",
    "Lausanne, CH",

    "Stockholm, SE",
    "Gothenburg, SE",
    "Malmo, SE",

    "Brussels, BE",
    "Antwerp, BE",
    "Ghent, BE",

    "Copenhagen, DK",
    "Aarhus, DK",
    "Odense, DK",

    "Oslo, NO",
    "Bergen, NO",
    "Trondheim, NO",
    "Stavanger, NO",

    "Helsinki, FI",
    "Turku, FI",
    "Tampere, FI",

    "Tallinn, EE",
    "Tartu, EE",

    "Riga, LV",

    "Vilnius, LT",
    "Kaunas, LT",

    "Paris, FR",
    "Lyon, FR",
    "Marseille, FR",
    "Nice, FR",
    "Bordeaux, FR",
    "Toulouse, FR",
    "Lille, FR",
    "Strasbourg, FR",
    "Nantes, FR",

    "Vienna, AT",
    "Salzburg, AT",
    "Graz, AT",
    "Linz, AT",

    "London, UK",
    "Manchester, UK",
    "Birmingham, UK",
    "Liverpool, UK",
    "Leeds, UK",
    "Glasgow, UK",
    "Edinburgh, UK",
    "Bristol, UK",
    "Cardiff, UK",
    "Belfast, UK",

    "Dublin, IE",
    "Cork, IE",
    "Galway, IE",

    "Amsterdam, NL",
    "Rotterdam, NL",
    "The Hague, NL",
    "Utrecht, NL",
    "Eindhoven, NL",

    "Berlin, DE",
    "Munich, DE",
    "Hamburg, DE",
    "Frankfurt, DE",
    "Cologne, DE",
    "Stuttgart, DE",
    "Dusseldorf, DE",
    "Leipzig, DE",
    "Dresden, DE",
    "Nuremberg, DE",
    "Bremen, DE",
    "Hanover, DE",

    "Madrid, ES",
    "Barcelona, ES",
    "Valencia, ES",
    "Seville, ES",
    "Malaga, ES",
    "Bilbao, ES",
    "Zaragoza, ES",
    "Palma, ES",

    "Lisbon, PT",
    "Porto, PT",
    "Braga, PT",
    "Coimbra, PT",

    "Rome, IT",
    "Milan, IT",
    "Naples, IT",
    "Turin, IT",
    "Bologna, IT",
    "Florence, IT",
    "Venice, IT",
    "Verona, IT",
    "Genoa, IT",
    "Palermo, IT",
    "Catania, IT",

    "Warsaw, PL",
    "Krakow, PL",
    "Wroclaw, PL",
    "Poznan, PL",
    "Gdansk, PL",
    "Lodz, PL",
    "Szczecin, PL",

    "Prague, CZ",
    "Brno, CZ",
    "Ostrava, CZ",

    "Bratislava, SK",
    "Kosice, SK",

    "Budapest, HU",
    "Debrecen, HU",
    "Szeged, HU",

    "Ljubljana, SI",
    "Maribor, SI",

    "Zagreb, HR",
    "Split, HR",
    "Rijeka, HR",
    "Dubrovnik, HR",

    "Belgrade, RS",
    "Novi Sad, RS",

    "Sarajevo, BA",
    "Banja Luka, BA",

    "Podgorica, ME",

    "Skopje, MK",

    "Tirana, AL",

    "Bucharest, RO",
    "Cluj-Napoca, RO",
    "Timisoara, RO",
    "Iasi, RO",

    "Sofia, BG",
    "Plovdiv, BG",
    "Varna, BG",

    "Athens, GR",
    "Thessaloniki, GR",
    "Patras, GR",

    "Chisinau, MD",

    "Kyiv, UA",
    "Lviv, UA",
    "Odesa, UA",

    "Istanbul, TR",
    "Ankara, TR",
    "Izmir, TR",
    "Antalya, TR",

    "Reykjavik, IS",

    "Luxembourg, LU",

    "Valletta, MT",

    "Nicosia, CY",
]

    targets = []
    for i in range(1, count + 1):
        name = f"{random.choice(prefixes)}{random.choice(suffixes)}"
        ip = generate_fake_ip()
        loc = random.choice(locations)
        phone = generate_fake_phone()
        targets.append(
            {
                "id": f"{i:03d}",
                "name": name,
                "ip": ip,
                "location": loc,
                "phone": phone,
            }
        )
    return targets


def render_pink_progress(label, duration=0.8, width=30):
    sys.stdout.write(
        f"{WHITE}[{get_timestamp()}] {CYAN}[*] {label} ...{RESET}\n"
    )

    steps = 20
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        filled_len = int(width * i // steps)
        bar = " " * filled_len
        empty = " " * (width - filled_len)

        sys.stdout.write(
            f"\r   {GRAY}└─ {PINK_BG}{bar}{RESET}{GRAY}{empty}{RESET} {WHITE}{BOLD}{percent}%{RESET}"
        )
        sys.stdout.flush()
        time.sleep(duration / steps)
    print("\n")


def stream_hex_buffer(lines=30):
    """Generates the red memory address hex stream matching Image 1."""
    print(
        f"{WHITE}[{get_timestamp()}] {CYAN}[*] Streaming raw exfiltrated memory hex buffer ...{RESET}"
    )
    phrases = [
        "ANTI_NULLSEC_EXPOSED..",
        "HATERS_EXTERMINATED..",
        "PASSWORDS_STOLEN..",
        "SYSTEM_DOXED..",
        "MASS_LEAK_SUCCESS..",
        "NO_LARP_WINNING..",
        "DARKWEB_DUMP..",
    ]

    base_addr = 0x00A26694
    for _ in range(lines):
        addr_str = f"0x{base_addr:08X}"
        hex_bytes = " ".join([f"{random.randint(0, 255):02X}" for _ in range(8)])
        tag = random.choice(phrases)

        print(
            f"{RED}{BOLD}{addr_str}{RESET}  {WHITE}{hex_bytes}{RESET}  {GRAY}| ..{tag}.. |{RESET}"
        )
        base_addr += 0x1000
        time.sleep(0.03) #hex scrolling speed
    print()


def run_full_simulation():
    TARGET_COUNT = 500
    print_ascii_header(TARGET_COUNT)
    time.sleep(0.3)

    # 1. Network Initialization
    print(
        f"{WHITE}[{get_timestamp()}] {CYAN}[*] Initializing Command & Control (C2) Network ...{RESET}"
    )
    time.sleep(1)
    print(
        f"{WHITE}[{get_timestamp()}] {CYAN}[*] Establishing encrypted 5-hop Tor circuit ...{RESET}"
    )

    nodes = [
        ("185.220.101.5", "Exit: DE"),
        ("45.66.35.12", "Middle: NL"),
        ("192.42.116.16", "Guard: SE"),
    ]
    for ip, loc in nodes:
        print(
            f"   {GRAY}└─ [TOR CIRCUIT] Node linked: {ip:<16} ({loc}){RESET}"
        )
        time.sleep(1.0)

    print()
    print(
        f"{WHITE}[{get_timestamp()}] {CYAN}[*] Scanning global targets ... Located ALL {TARGET_COUNT} entities.{RESET}"
    )
    time.sleep(3.0)

    # Build target
    targets = build_target_list(TARGET_COUNT)

    # 2. Fast target scrolling simulation
    for t in targets:
        line = f"{RED}{BOLD}[TARGET {t['id']}/{TARGET_COUNT}]{RESET} {WHITE}{t['name']:<30}{RESET} {GRAY}{t['ip']:<18}{RESET} {WHITE}Ports: 22, 80, 443, 8080{RESET}"
        print(line)
        time.sleep(0.02)

    print(
        f"\n{WHITE}[{get_timestamp()}] {CYAN}[+] All {TARGET_COUNT} target profiles fully indexed into attack queue.{RESET}\n"
    )
    time.sleep(0.5)

    # hacking simulation
    render_pink_progress("COMPROMISING TARGET FIREWALLS", duration=10.0) #fake time waiting for effect
    render_pink_progress(
        "Executing Zero-Day Exploit Payload (CVE-2026-9918)", duration=10.0 #fake time waiting for effect
    )
    render_pink_progress(
        "Bruteforcing SSH Root Credentials via Botnet & hashcat", duration=2.0
    )

    print(
        f"{WHITE}[{get_timestamp()}] {CYAN}[+] AUTHENTICATION BYPASSED:Sudo root access granted on {TARGET_COUNT} targets!{RESET}\n"
    )
    time.sleep(2.0)

    # 4. hex buffer stream
    render_pink_progress(
        "Compressing & Encrypting Massive Loot Package (AES-256-GCM)",
        duration=1.0,
    )
    stream_hex_buffer(lines=500) # hex

    # dox report generation
    print(
        f"{WHITE}[{get_timestamp()}] {CYAN}[*] GENERATING AUTOMATED DOX REPORTS FOR ALL {TARGET_COUNT} TARGETS ...{RESET}"
    )
    time.sleep(10) # simulate report generation time

    for t in targets:
        dox_line = (
            f"{CYAN}{BOLD}[DOX GENERATED]{RESET} {WHITE}#{t['id']}{RESET} | "
            f"User: {WHITE}{t['name']:<28}{RESET} | "
            f"IP: {GRAY}{t['ip']:<15}{RESET} | "
            f"Loc: {WHITE}{t['location']:<16}{RESET} | "
            f"Phone: {WHITE}{t['phone']}{RESET}"
        )
        print(dox_line)
        time.sleep(0.015)

    print(
        f"\n{PINK}{BOLD}[+] DOX GENERATION COMPLETE. ALL {TARGET_COUNT} PROFILES EXPORTED.{RESET}\n"
    )


if __name__ == "__main__":
    run_full_simulation()
