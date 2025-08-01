import time
import requests 
import re 
import os        




#hibanas Doxxer


#Logo
print(r"""
                                         .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-. \\
                |    |:::||             //'///                    `.\\
                |    |:::||            //  ||'                      `|
        hibana  /    |:::|/        _,-//\\  ||
               /`    |:::|`-,__,-'`  |/  \\ ||
             /`  |   |'' ||           \\   |||
           /`    \\   |   ||            |  /||
         |`       |  |   |)            \\ | ||
        |          \\ |   /      ,.__    \\| ||
        /           `         /`    `\\   | ||
       |                     /        \\  / ||
       |                     |        | /  ||
       /         /           |        `(`  ||
      /          .           /          )  ||
     |            \\          |     ________||
    /             |          /     `-------.|
   |\\            /          |              ||
   \\/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \\              ||
  ///\\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             || 
 `\\\\` /`                    |             // 
     |`                     \\            ||  
    /                        |           //  
  /`                          \\         //   
/`                            |        ||    
`-.___,-.      .-.        ___,'        (/    
         `---'`   `'----'`
""")

#Funcion


def explanation():
    time.sleep(2)
    print("Welcome to the Hibana Doxxer!")
    time.sleep(2)
    print("This tool is designed to gather information about a target.")
    time.sleep(2)
    print("\033[31mPlease use responsibly and respect privacy laws.\033[0m")



def advanced_password_generator():
    # Ordner erstellen
    os.makedirs("password_lists", exist_ok=True)

    name = input("Vorname: ").strip()
    nachname = input("Nachname: ").strip()
    alter = input("Alter (optional): ").strip()
    favword = input("Lieblingswort / Nickname (optional): ").strip()
    favnum = input("Lieblingszahl (optional): ").strip()

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
        mapping = str.maketrans({  # Leetspeak Mapping
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

    # Speicherpfad mit Vor- und Nachname
    filename = f"{name}_{nachname}_password_list.txt"
    output_file = os.path.join("password_lists", filename)

    with open(output_file, "w", encoding="utf-8") as f:
        for pw in sorted(combos):
            f.write(pw + "\n")

    print(f"\n[+] {len(combos)} Passwörter generiert und gespeichert unter '{output_file}'\n")   # Passwörter generiert und gespeichert






# Email Generator Funktion

def email_generator():
    name = input("Vorname: ").strip().lower()
    nachname = input("Nachname: ").strip().lower()
    alter = input("Alter (optional): ").strip()
    domain_choice = input("Domain wählen [1] gmail.com [2] icloud.com: ").strip()  # Auswahl der Domain

    if domain_choice == "1":
        domain = "@gmail.com"
    elif domain_choice == "2":
        domain = "@icloud.com"
    else:
        print("Ungültige Auswahl.")
        return

    geburtsjahr = ""
    if alter.isdigit():
        geburtsjahr = str(2025 - int(alter))

    kombis = set([     # Basis-Kombinationen
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

    print("\n[+] Generierte mögliche E-Mail-Adressen:")
    for mail in email_list:
        print(mail)
    print(f"\n[+] Insgesamt {len(email_list)} mögliche Adressen generiert.\n")



def check_instagram(username):   #Instagram
    url = f"https://www.instagram.com/{username}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return False, None
        
        match = re.search(r"<title>(.*?)</title>", response.text)
        if match:
            title = match.group(1)
            # Instagram zeigt im Titel "Page Not Found" wenn nicht existent
            if "Page Not Found" in title:
                return False, None
            if username.lower() in title.lower():
                return True, url
            else:
                return False, None
        return False, None
    except requests.RequestException:
        return None, None



def check_steam(username):     #Steam
    url = f"https://steamcommunity.com/id/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}   # User-Agent setzen, um Blockierungen zu vermeiden
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return False, None
        
        # Typischer Fehlertext bei nicht vorhandenem Profil
        if "The specified profile could not be found" in response.text or "Error" in response.text:
            return False, None
        return True, url
    except requests.RequestException:
        return None, None



def check_soundcloud(username):       #SoundCloud
    url = f"https://soundcloud.com/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 404:
            return False, None
        
        # SoundCloud zeigt oft 200, aber wenn das Profil nicht existiert, steht "Page Not Found"
        if "Page Not Found" in response.text or "The page you were looking for doesn’t exist" in response.text:
            return False, None
        
        return True, url
    except requests.RequestException:
        return None, None



def user_lookup():    # Benutzerabfrage
    username = input("Enter the username to look up: ")
    print(f"\nGathering information for user: {username}")
    time.sleep(1)

    services = [
    ("instagram", check_instagram),
    ("steam", check_steam),
    ("soundcloud", check_soundcloud),
]

    for name, func in services:
        found, url = func(username)
        if found:
            print(f"({name}) {url}")
        elif found is False:
            # Nur anzeigen, wenn es definitiv nicht existiert -> nichts ausgeben
            pass
        else:
            # found == None (Fehler bei Anfrage)
            print(f"({name}) (-)")
        time.sleep(1)

def webhook_spam():   #Webhook Spam
    print("\n--- Webhook Spam ---")
    webhook_url = input("Enter the Discord Webhook URL: ").strip()
    message = input("Enter the message to spam: ").strip()
    count = input("How many messages do you want to send? (Enter a number): ").strip()

    try:
        count = int(count)
    except ValueError:
        print("Invalid number, defaulting to 10 messages.")
        count = 10

    print(f"Sending {count} messages to the webhook...")
    for i in range(count):
        data = {"content": message}
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print(f"Message {i+1}/{count} sent successfully.")
            else:
                print(f"Failed to send message {i+1}. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error sending message {i+1}: {e}")

        time.sleep(0.5)  # 1 Sekunde Pause zwischen Nachrichten, um Spam-Blockierungen zu vermeiden

    print("Finished sending messages.")



# Main Menu und Funktionsaufruf

def main_menu():
    explanation()
    while True:
        print("\nMain Menu:")    #funktionen
        print("1. User Lookup")     
        print("2. Webhook Spam")
        print("3. Email Generator")
        print("4. Advanced Password List Generator")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_lookup()
        elif choice == '2':
            webhook_spam()
        elif choice == '3':
            email_generator()
        elif choice == '4':
            advanced_password_generator()
        elif choice == '5':
            print("Exiting the Hibanas Doxxer. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
