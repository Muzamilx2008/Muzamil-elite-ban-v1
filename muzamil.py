import os
import time
import smtplib
import ssl
from email.message import EmailMessage
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Initialize colorama and dotenv
init(autoreset=True)
load_dotenv()

perm_file = "perm_ban.txt"
temp_file = "temp_ban.txt"

sender_email = os.getenv('GMAIL_ADDRESS')
password = os.getenv('GMAIL_PASSWORD')

support_emails = [
    "support@whatsapp.com",
    "abuse@support.whatsapp.com",
    "privacy@support.whatsapp.com",
    "terms@support.whatsapp.com",
    "accessibility@support.whatsapp.com"
]


def banner():
    # Use ANSI color codes directly (Termux supports these natively)
    print("\033[31m\n===[ MR DEV â€” SHADOW BAN CORE ]===\033[0m")
    print("""
\033[91m
â–ˆâ–ˆâ–ˆâ•—   â–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—   â–ˆâ–ˆâ•—
â–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—   â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘
â–ˆâ–ˆâ•”â–ˆâ–ˆâ–ˆâ–ˆâ•”â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘
â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â•šâ•â•â•â•â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ•— â–ˆâ–ˆâ•”â•
â–ˆâ–ˆâ•‘ â•šâ•â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘   â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘ â•šâ–ˆâ–ˆâ–ˆâ–ˆâ•”â• 
â•šâ•â•     â•šâ•â•â•šâ•â•  â•šâ•â•    â•šâ•â•â•â•â•â• â•šâ•â•â•â•â•â•â•  â•šâ•â•â•â•  

         â˜ ï¸  MR DEV â€” THE MUZAMIL KING â˜ ï¸
             âš”ï¸  Silent. Swift. Fatal. âš”ï¸

         "The system has no mercy for the wicked..."
\033[0m
""")
 
def is_banned(number):
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            if number in f.read():
                return "permanent"
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            for line in f:
                if line.startswith(number + ","):
                    unban_time = int(line.strip().split(",")[1])
                    if time.time() < unban_time:
                        return "temporary"
    return None

def simulate_reports(number, total):
    # mr dev is the best....
    print(f"\n{Fore.LIGHTBLACK_EX}ðŸ©¸ {Fore.RED}Shadow Sequence Engaged â€” Queued:{Fore.WHITE} {total} {Fore.RED}vectors for {Fore.WHITE}{number}")
    time.sleep(0.35)
    for i in range(1, total + 1):
        print(f"{Fore.RED}â˜ ï¸  [{i:03d}/{total}]  Emitting dark packet â†’ {Fore.WHITE}{number}")
        time.sleep(0.05)
    print(f"\n{Fore.GREEN}âœ…  Operation complete. {Fore.WHITE}{total} vectors deployed on {number}.")
    print(f"{Fore.LIGHTBLACK_EX}â€” Crafted & executed by MR DEV ðŸ•·ï¸{Style.RESET_ALL}")
def save_perm_ban(number):
    with open(perm_file, "a") as f:
        f.write(number + "\n")

def save_temp_ban(number, duration):
    unban_time = int(time.time() + duration)
    with open(temp_file, "a") as f:
        f.write(f"{number},{unban_time}\n")

def check_temp_expiry():
    if not os.path.exists(temp_file):
        return
    with open(temp_file, "r") as f:
        lines = f.readlines()

    active = []
    for line in lines:
        try:
            number, unban_time = line.strip().split(",")
        except ValueError:
            continue
        if time.time() < int(unban_time):
            active.append(line)
        else:
            print(f"{Fore.RED}ðŸ©¸  Shadow Seal Lifted â€” {Fore.WHITE}{number} {Fore.LIGHTBLACK_EX}has returned from the void...")

    with open(temp_file, "w") as f:
        f.writelines(active)

    print(f"{Fore.LIGHTBLACK_EX}â€” Orchestrated by MR DEV âš”ï¸{Style.RESET_ALL}")
    
def ban_permanent():
    number = input(f"{Fore.RED}ðŸ  Enter target soul ðŸ”¥ {Fore.WHITE}: ").strip()
    if is_banned(number):
        print(f"{Fore.RED}â˜ ï¸  {number} is already bound in darkness ({is_banned(number)} ban active).")
        return

    confirm = input(f"{Fore.LIGHTRED_EX}âš ï¸  Once marked, the soul cannot return. Proceed with eternal ban on {number}? (y/n): ").strip().lower()
    if confirm != 'y':
        print(f"{Fore.LIGHTBLACK_EX}ðŸ•¯ï¸  Ritual aborted â€” the void remains silent.")
        return

    try:
        reports = int(input(f"{Fore.MAGENTA}ðŸ”¢  Input the number of dark strikes to deploy: {Fore.WHITE}"))
    except ValueError:
        print(f"{Fore.RED}âŒ  Invalid symbol. Only numbers of pain accepted.")
        return

    simulate_reports(number, reports)
    save_perm_ban(number)

    print(f"\n{Fore.RED}ðŸš«  The number {number} has been cast into eternal oblivion.")
    print(f"{Fore.LIGHTBLACK_EX}ðŸ©¸  Whisper sent to the shadow networkâ€¦ awaiting confirmation.")

    # mr dev is the best lol.....
    reason = "This Number Have Been Stealing and scamming People On WhatsApp, destroying people WhatsApp account, sending negative Text, spamming virus, Sending nudes to different people on WhatsApp please He his Going against the Community guidelines please disable the account from using WhatsApp He hacked My Number and start using it to scam people Online And he his very dangerous Sending Different videos and pictures especially Nudes or sex stuff, please i beg of you WhatsApp support team work together and disable this number from Violating WhatsApp please, He is a Fraud, scammer,Thief, Sending spam messages, text viruses, And many of all negative attitude Please disable the account permanently from using WhatsApp account again he will continue doing so if you guy's didn't take action on time. Thank you"
    

    send_report_email(number, reason, reports)
    print(f"\n{Fore.LIGHTBLACK_EX}ðŸ•·ï¸  Execution completed. Power channeled by {Fore.RED}MR DEV â€” The Architect of Shadows.")
    
def ban_temporary():
    #  prompt
    number = input("ðŸ’€ Enter the Shadow Target Number ðŸŽ¯: ").strip()
    if is_banned(number):
        print(f"{Fore.RED}â˜ ï¸  {number} is already marked in the dark registry.")
        return

    confirm = input(f"âš ï¸  Do you wish to unleash temporary lockdown on {number}? (Y/N): ").strip().lower()
    if confirm != 'y':
        print(f"{Fore.LIGHTBLACK_EX}âŒ  Operation aborted. Target remains active in the shadows.")
        return

    try:
        minutes = int(input("â³ Enter Ban Duration in minutes (how long the darkness lasts): "))
        reports = int(input("ðŸ”¢ Enter number of shadow strikes to deploy: "))
    except ValueError:
        print(f"{Fore.RED}âŒ  Invalid input. Only numbers for the ritual.")
        return

    # effect 
    print(f"\n{Fore.LIGHTBLACK_EX}{'â”€'*60}")
    print(f"{Fore.MAGENTA}â˜ ï¸  Initiating shadow protocol â€” Target: {Fore.WHITE}{number} {Fore.MAGENTA}Â· Duration: {minutes}m Â· Strikes: {reports}")
    print(f"{Fore.LIGHTBLACK_EX}{'â”€'*60}\n")

    simulate_reports(number, reports)
    save_temp_ban(number, minutes * 60)

    # Success style 
    print(f"\n{Fore.RED}ðŸ©¸  {Fore.WHITE}{number} has been cloaked in shadow for {minutes} minutes.")
    print(f"{Fore.GREEN}âœ”ï¸  Shadow registry updated successfully.")
    print(f"{Fore.LIGHTBLACK_EX}â€” Operation executed by MR DEV (Shadow Ban Tool) ðŸ•·ï¸\n")

    # mr dev is the best
    reason = f"This Number will be disabled for some {minutes} minutes because he has been stealing and scamming people on WhatsApp, destroying people's WhatsApp accounts, sending negative texts, spamming viruses, and sending nudes to different people on WhatsApp. He is going against the community guidelines â€” please disable the account. He hacked my number and started using it to scam people online, and he is very dangerous, sending inappropriate videos and pictures. I beg the WhatsApp support team to work together and disable this number for violating WhatsApp's rules. He is a fraud, scammer, thief, and spammer. Please disable the account permanently before he continues doing so. Thank you."

    send_report_email(number, reason, reports)
    print(f"\n{Fore.LIGHTBLACK_EX}ðŸ•·ï¸  Execution completed. Power channeled by {Fore.RED}MR DEV â€” The Architect of Shadows.")
    
def unban_permanent():
    number = input(f"{Fore.RED}ðŸ©¸ Enter number to unban from PERMANENT ban: ").strip()
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            lines = f.readlines()
        with open(perm_file, "w") as f:
            for line in lines:
                if line.strip() != number:
                    f.write(line)
        print(f"{Fore.MAGENTA}ðŸ’€ {number} has been freed from eternal darkness.")
    else:
        print(f"{Fore.YELLOW}âš ï¸ No permanent ban records found.")

def unban_temporary():
    number = input(f"{Fore.RED}ðŸ©¸ ð—¦ð—µð—®ð—±ð—¼ð˜„ ð—¿ð—²ð—®ð—½ð—²ð—¿ whispers: ð—³ð—¿ð—¼ð—º TEMP ban , ð—°ð—¹ð—®ð—¶ð—º ð˜ð—µð—² ð—°ð—µð—®ð—¼ð˜ð—¶ð—° ð—»ð˜‚ð—ºð—¯ð—²ð—¿: ").strip()
    
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            lines = f.readlines()
        # mr dev is the best
        new_lines = [line for line in lines if not line.startswith(number + ",")]
        with open(temp_file, "w") as f:
            f.writelines(new_lines)
        print(f"{Fore.MAGENTA}ðŸ’€ {number} ð—µð—®ð˜€ ð—¯ð—²ð—²ð—» ð—¿ð—¶ð—½ð—½ð—²ð—± ð—³ð—¿ð—¼ð—º ð˜ð—²ð—ºð—½ð—¼ð—¿ð—®ð—¿ð˜† ð—½ð—®ð—¶ð—»!")
    else:
        print(f"{Fore.YELLOW}âš ï¸ ð—¡ð—¼ ð—²ð˜ð—µð—²ð—¿ð—²ð—®ð—¹ ð—¹ð—¶ð˜€ð˜ ð—³ð—¼ð˜‚ð—»ð—±. ð—¡ð˜‚ð—ºð—¯ð—²ð—¿ {number} ð—°ð—®ð—»ð—»ð—¼ð˜ ð—¯ð—² ð—¿ð—²ð—¹ð—²ð—®ð˜€ð—²ð—±.")
        
def send_report_email(target_number, reason, count):
    context = ssl.create_default_context()
    for i in range(count):
        msg = EmailMessage()
        msg['Subject'] = f"Report of WhatsApp Account (Attempt {i+1})"
        msg['From'] = sender_email
        msg['To'] = ", ".join(support_emails)
        msg.set_content(f"""Hello WhatsApp Support,

I would like to report the following WhatsApp number:

ðŸ“± Number: {target_number}
ðŸ“ Reason: {reason}

please take action immediately 
Thank you.
""")
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg)
            print(f"âœ… ð—•ð—®ð—» ð—¿ð—²ð—¾ð˜‚ð—²ð˜€ð˜ {i+1}/{count} ð˜€ð—²ð—»ð˜ ð˜ð—¼ ð—ªð—µð—®ð˜ð˜€ð—”ð—½ð—½")
        except Exception as e:
            print(f"âŒ ð—•ð—®ð—» ð—³ð—®ð—¶ð—¹ð—²ð—± {i+1} ð—³ð—®ð—¶ð—¹ð—²ð—±: {e}")
            break
            
def view_banned():
    print(f"\n{Fore.RED}ðŸš« ð—£ð—˜ð—¥ð— ð—”ð—¡ð—˜ð—¡ð—§ ð—•ð—”ð—¡ð—¦:")
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            print(f.read().strip() or "None")
    else:
        print("ð—¡ð—¼ð—»ð—²")

    print(f"\n{Fore.MAGENTA}â³ ð—§ð—˜ð— ð—£ð—¢ð—¥ð—”ð—¥ð—¬ ð—•ð—”ð—¡ð—¦:")
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            for line in f:
                number, unban_time = line.strip().split(",")
                remaining = int(unban_time) - int(time.time())
                if remaining > 0:
                    mins = remaining // 60
                    print(f"{number} â€” {mins} min left")
    else:
        print("ð—¡ð—¼ð—»ð—²")

# Mr Dev is the best take am play first
while True:
    check_temp_expiry()
    banner()

    print(f"{Fore.RED}{'â•'*70}")
    print(f"{Fore.LIGHTBLACK_EX}ðŸ©¸ {Fore.RED}M R   D E V   â€“   E V I L   O P S   C O N S O L E  ðŸ©¸")
    print(f"{Fore.RED}{'â•'*70}")
    print(f"{Fore.LIGHTBLACK_EX}ðŸ’»  Access Level: {Fore.RED}ROOT ADMIN     {Fore.LIGHTBLACK_EX}â”‚  Status: {Fore.RED}ONLINE âš¡")
    print(f"{Fore.RED}{'â”€'*70}\n")

    print(f"{Fore.RED}1ï¸âƒ£   ðŸ’€  PERMANENT BAN        {Fore.LIGHTBLACK_EX}:: Erase target permanently")
    print(f"{Fore.RED}2ï¸âƒ£   ðŸ”¥  TEMPORARY BAN        {Fore.LIGHTBLACK_EX}:: Lock target temporarily")
    print(f"{Fore.LIGHTBLACK_EX}3ï¸âƒ£   ðŸ§¹  REMOVE PERM BAN      {Fore.LIGHTBLACK_EX}:: Reverse eternal restriction")
    print(f"{Fore.LIGHTBLACK_EX}4ï¸âƒ£   ðŸ•’  REMOVE TEMP BAN      {Fore.LIGHTBLACK_EX}:: Restore temporary subject")
    print(f"{Fore.WHITE}5ï¸âƒ£   ðŸ‘ï¸   VIEW BAN RECORDS     {Fore.LIGHTBLACK_EX}:: Access encrypted logs")
    print(f"{Fore.LIGHTBLACK_EX}6ï¸âƒ£   ðŸšª  EXIT CONSOLE         {Fore.LIGHTBLACK_EX}:: Shutdown operation\n")

    print(f"{Fore.RED}{'â”€'*70}")
    choice = input(f"{Fore.RED}ðŸ•·ï¸  INPUT COMMAND [1â€“6]: {Fore.WHITE}").strip()
    print(f"{Fore.RED}{'â”€'*70}\n")

    if choice == "1":
        print(f"{Fore.RED}ðŸ’£  Deploying PERMANENT ban protocol...\n")
        time.sleep(0.6)
        ban_permanent()

    elif choice == "2":
        print(f"{Fore.RED}â³  Activating TEMPORARY restriction module...\n")
        time.sleep(0.6)
        ban_temporary()

    elif choice == "3":
        print(f"{Fore.LIGHTBLACK_EX}ðŸ”“  Releasing PERMANENT lockdown...\n")
        time.sleep(0.6)
        unban_permanent()

    elif choice == "4":
        print(f"{Fore.LIGHTBLACK_EX}ðŸ•’  Lifting TEMPORARY isolation...\n")
        time.sleep(0.6)
        unban_temporary()

    elif choice == "5":
        print(f"{Fore.WHITE}ðŸ“œ  Scanning ban registry archives...\n")
        time.sleep(0.6)
        view_banned()

    elif choice == "6":
        print(f"{Fore.RED}\nðŸ©¸  SYSTEM OVERRIDE INITIATED...")
        time.sleep(1)
        print(f"{Fore.LIGHTBLACK_EX}ðŸ’€  Closing all secure channels...")
        time.sleep(1)
        print(f"{Fore.RED}âš¡  CORE OFFLINE. Until next hunt, Mr Dev.\n")
        print(f"{Fore.LIGHTBLACK_EX}{'â•'*70}")
        break

    else:
        print(f"{Fore.RED}âŒ  Invalid command detected. Try again, Operator.\n")

    time.sleep(1.4)
