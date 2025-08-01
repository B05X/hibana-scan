import time
import requests 
import re 
import os
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Hibanas Doxxer - Enhanced Version
def print_banner():
    print(Fore.CYAN + r"""
    ██░ ██  ██▓ ▄▄▄▄    ▄▄▄       ███▄    █  ▄▄▄      
▓██░ ██▒▓██▒▓█████▄ ▒████▄     ██ ▀█   █ ▒████▄    
▒██▀▀██░▒██▒▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  
░▓█ ░██ ░██░▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ 
░▓█▒░██▓░██░░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒
 ▒ ░░▒░▒░▓  ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░
 ▒ ░▒░ ░ ▒ ░▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░
 ░  ░░ ░ ▒ ░ ░    ░   ░   ▒      ░   ░ ░   ░   ▒   
 ░  ░  ░ ░   ░            ░  ░         ░       ░  ░
                  ░                               
    """)
    print(Fore.YELLOW + "=" * 60)
    print(Fore.MAGENTA + "HIBANA'S OSINT TOOLKIT".center(60))
    print(Fore.YELLOW + "=" * 60)
    print(Fore.WHITE + "Version 2.0 | Developed by Hibana | Use Responsibly".center(60))
    print(Fore.RED + "=" * 60 + "\n")

def explanation():
    print(Fore.GREEN + "\n[+] Welcome to Hibana's OSINT Toolkit!")
    time.sleep(1)
    print(Fore.YELLOW + "[~] This tool provides various information gathering utilities")
    time.sleep(1)
    print(Fore.RED + "[!] WARNING: Use this tool responsibly and legally")
    time.sleep(1)
    print(Fore.CYAN + "[*] Always respect privacy laws and terms of service\n")
    time.sleep(1)

def print_section_header(title):
    print(Fore.YELLOW + "\n" + "=" * 60)
    print(Fore.MAGENTA + f"[ {title.upper()} ]".center(60))
    print(Fore.YELLOW + "=" * 60)

def advanced_password_generator():
    print_section_header("Advanced Password Generator")
    print(Fore.CYAN + "\nThis will create a customized password list based on personal information")
    
    # Create directory if it doesn't exist
    os.makedirs("password_lists", exist_ok=True)

    print(Fore.GREEN + "\n[+] Please provide the following information:")
    name = input(Fore.WHITE + "First Name: ").strip()
    nachname = input(Fore.WHITE + "Last Name: ").strip()
    alter = input(Fore.WHITE + "Age (optional): ").strip()
    favword = input(Fore.WHITE + "Favorite Word/Nickname (optional): ").strip()
    favnum = input(Fore.WHITE + "Favorite Number (optional): ").strip()

    # Processing the input
    parts = [name, nachname]
    if favword:
        parts.append(favword)

    numbers = []
    if alter.isdigit():
        geburtsjahr = str(2025 - int(alter))
        numbers.extend([alter, geburtsjahr])
    if favnum.isdigit():
        numbers.append(favnum)

    symbols = ["!", "?", "@", "_", ".", "$"]

    def leetspeak(word):
        mapping = str.maketrans({
            'a': '@', 'A': '@',
            'e': '3', 'E': '3',
            'i': '1', 'I': '1',
            'o': '0', 'O': '0',
            's': '$', 'S': '$'
        })
        return word.translate(mapping)

    combos = set()

    for part in parts:
        base_variants = {part.lower(), part.upper(), part.capitalize(), leetspeak(part)}
        for var in base_variants:
            combos.add(var)
            for num in numbers:
                combos.add(f"{var}{num}")
                combos.add(f"{num}{var}")
            for sym in symbols:
                combos.add(f"{var}{sym}")
                combos.add(f"{sym}{var}")

    for p1 in parts:
        for p2 in parts:
            if p1 != p2:
                combined = p1 + p2
                variants = {combined.lower(), combined.upper(), combined.capitalize(), leetspeak(combined)}
                for var in variants:
                    combos.add(var)
                    for num in numbers:
                        combos.add(f"{var}{num}")
                        combos.add(f"{num}{var}")
                    for sym in symbols:
                        combos.add(f"{var}{sym}")
                        combos.add(f"{sym}{var}")

    # Save to file
    filename = f"{name}_{nachname}_password_list.txt"
    output_file = os.path.join("password_lists", filename)

    with open(output_file, "w", encoding="utf-8") as f:
        for pw in sorted(combos):
            f.write(pw + "\n")

    print(Fore.GREEN + f"\n[+] Successfully generated {len(combos)} passwords")
    print(Fore.CYAN + f"[*] Saved to: {output_file}\n")

def email_generator():
    print_section_header("Email Generator")
    print(Fore.CYAN + "\nThis generates possible email addresses based on personal information")
    
    name = input(Fore.WHITE + "\nFirst Name: ").strip().lower()
    nachname = input(Fore.WHITE + "Last Name: ").strip().lower()
    alter = input(Fore.WHITE + "Age (optional): ").strip()
    
    print(Fore.CYAN + "\n[+] Select email domain:")
    print(Fore.WHITE + "1. gmail.com")
    print(Fore.WHITE + "2. icloud.com")
    domain_choice = input(Fore.WHITE + "Your choice (1-2): ").strip()

    if domain_choice == "1":
        domain = "@gmail.com"
    elif domain_choice == "2":
        domain = "@icloud.com"
    else:
        print(Fore.RED + "[!] Invalid choice, defaulting to gmail.com")
        domain = "@gmail.com"

    geburtsjahr = ""
    if alter.isdigit():
        geburtsjahr = str(2025 - int(alter))

    kombis = set([
        f"{name}{nachname}",
        f"{name}.{nachname}",
        f"{name}_{nachname}",
        f"{name[0]}{nachname}",
        f"{name[0]}.{nachname}",
        f"{nachname}{name}",
        f"{nachname}.{name}",
        f"{name}{nachname[0]}",
        f"{name}.{nachname[0]}",
    ])

    if alter.isdigit():
        for base in list(kombis):
            kombis.add(f"{base}{alter}")
            kombis.add(f"{base}{geburtsjahr}")
            kombis.add(f"{alter}{base}")

    kombis.add(f"{name[0]}{nachname[0]}")
    kombis.add(f"{name[0]}_{nachname[0]}")

    for num in range(1, 100):
        kombis.add(f"{name}{num}")
        kombis.add(f"{nachname}{num}")

    email_list = sorted({f"{k}{domain}" for k in kombis})

    print(Fore.GREEN + f"\n[+] Generated {len(email_list)} possible email addresses:")
    for mail in email_list:
        print(Fore.WHITE + mail)
    print(Fore.CYAN + "\n[*] Tip: Try these with password recovery options\n")

def check_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return False, None
        
        match = re.search(r"<title>(.*?)</title>", response.text)
        if match:
            title = match.group(1)
            if "Page Not Found" in title:
                return False, None
            if username.lower() in title.lower():
                return True, url
            else:
                return False, None
        return False, None
    except requests.RequestException:
        return None, None

def check_steam(username):
    url = f"https://steamcommunity.com/id/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return False, None
        
        if "The specified profile could not be found" in response.text or "Error" in response.text:
            return False, None
        return True, url
    except requests.RequestException:
        return None, None

def check_soundcloud(username):
    url = f"https://soundcloud.com/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 404:
            return False, None
        
        if "Page Not Found" in response.text or "The page you were looking for doesn't exist" in response.text:
            return False, None
        
        return True, url
    except requests.RequestException:
        return None, None

def user_lookup():
    print_section_header("Username Lookup")
    username = input(Fore.WHITE + "\nEnter the username to search: ")
    print(Fore.CYAN + f"\n[~] Searching for {username} across platforms...\n")
    time.sleep(1)

    services = [
        ("Instagram", check_instagram),
        ("Steam", check_steam),
        ("SoundCloud", check_soundcloud),
    ]

    results = []
    for name, func in services:
        found, url = func(username)
        if found:
            print(Fore.GREEN + f"[+] {name}: Found - {url}")
            results.append((name, url))
        elif found is False:
            print(Fore.RED + f"[-] {name}: Not found")
        else:
            print(Fore.YELLOW + f"[?] {name}: Could not verify (connection error)")

    if not any(found for found, _ in services):
        print(Fore.RED + "\n[!] No accounts found with this username")

def webhook_spam():
    print_section_header("Webhook Spammer")
    print(Fore.RED + "\nWARNING: Use of this tool may violate Discord's Terms of Service")
    print(Fore.RED + "Use at your own risk!\n")
    
    webhook_url = input(Fore.WHITE + "Enter Discord Webhook URL: ").strip()
    message = input(Fore.WHITE + "Message to send: ").strip()
    count = input(Fore.WHITE + "Number of messages (default 10): ").strip()

    try:
        count = int(count) if count else 10
    except ValueError:
        print(Fore.RED + "[!] Invalid number, using default (10)")
        count = 10

    print(Fore.CYAN + f"\n[~] Preparing to send {count} messages...")
    time.sleep(1)

    for i in range(count):
        data = {"content": message}
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print(Fore.GREEN + f"[+] Message {i+1}/{count} sent")
            else:
                print(Fore.RED + f"[!] Failed to send message {i+1} (Status: {response.status_code})")
        except requests.RequestException as e:
            print(Fore.RED + f"[!] Error sending message {i+1}: {str(e)}")

        time.sleep(0.5)

    print(Fore.CYAN + "\n[+] Message sending complete\n")

def main_menu():
    print_banner()
    explanation()
    
    while True:
        print(Fore.YELLOW + "\n" + "=" * 60)
        print(Fore.MAGENTA + "MAIN MENU".center(60))
        print(Fore.YELLOW + "=" * 60)
        print(Fore.CYAN + "1. Username Lookup")
        print(Fore.CYAN + "2. Webhook Spammer")
        print(Fore.CYAN + "3. Email Generator")
        print(Fore.CYAN + "4. Advanced Password Generator")
        print(Fore.RED + "5. Exit")
        print(Fore.YELLOW + "=" * 60)

        choice = input(Fore.WHITE + "\nSelect an option (1-5): ").strip()

        if choice == '1':
            user_lookup()
        elif choice == '2':
            webhook_spam()
        elif choice == '3':
            email_generator()
        elif choice == '4':
            advanced_password_generator()
        elif choice == '5':
            print(Fore.CYAN + "\n[+] Thank you for using Hibana's OSINT Toolkit")
            print(Fore.YELLOW + "[~] Remember to use these tools responsibly!")
            break
        else:
            print(Fore.RED + "[!] Invalid choice, please try again")

        input(Fore.CYAN + "\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main_menu()
