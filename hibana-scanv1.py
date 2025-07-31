import time
import requests 
import re   




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





def main_menu():  # Hauptmenü
    explanation()
    while True:
        print("\nMain Menu:")
        print("1. User Lookup")
        print("2. Webhook Spam")   # Neue Option
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_lookup()
        elif choice == '2':
            webhook_spam()      # Funktion aufrufen
        elif choice == '3':
            print("Exiting the Hibanas Doxxer. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()

