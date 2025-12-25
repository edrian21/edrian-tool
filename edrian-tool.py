import os
import sys
import time
import subprocess

# --- COLORS ---
R = "\033[91m" # Red
G = "\033[92m" # Green
Y = "\033[93m" # Yellow
B = "\033[94m" # Blue
P = "\033[95m" # Purple
C = "\033[96m" # Cyan
W = "\033[0m"  # White/Reset

# --- SYSTEM CHECKER ---
def check_dependencies():
    """Tinitiyak na installed ang mga kailangan bago mag-start"""
    dependencies = ['figlet', 'neofetch']
    for pkg in dependencies:
        status = subprocess.getstatusoutput(f"command -v {pkg}")
        if status[0] != 0:
            print(f"{Y}[!] Installing {pkg}...{W}")
            os.system(f"pkg install {pkg} -y > /dev/null 2>&1")

def loading_anim():
    animation = ["|", "/", "-", "\\"]
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write(f"\r{C}[*] Loading {animation[i % len(animation)]}{W}")
        sys.stdout.flush()
    print("\n")

def menu():
    os.system('clear')
    # Rainbow Banner gamit ang Figlet
    os.system('fcolor=$(shuf -i 1-6 -n 1); case $fcolor in 1) c="\\033[91m";; 2) c="\\033[92m";; 3) c="\\033[93m";; 4) c="\\033[94m";; 5) c="\\033[95m";; 6) c="\\033[96m";; esac; echo -e "$c"')
    os.system('figlet -f slant "EDRIAN TOOL"')
    print(f"{W}==========================================")
    print(f"{G}      MASTER EDRIAN'S OFFICIAL TOOLKIT     ")
    print(f"{W}==========================================")
    
    print(f"\n{R}[1] {W}Brute Force Simulator")
    print(f"{Y}[2] {W}Password Strength Checker")
    print(f"{G}[3] {W}Wordlist Generator")
    print(f"{C}[4] {W}Web Traffic Simulator")
    print(f"{B}[5] {W}Data Breach Scanner")
    print(f"{P}[6] {W}Secret Message (Base64)")
    print(f"{R}[7] {W}Update Termux System")
    print(f"{Y}[8] {W}Exit")
    
    choice = input(f"\n{G}[?] Anong utos mo, Master? : {W}")
    
    # INDENTATION FIX: Lahat ng elif ay dapat pantay sa loob ng function
    if choice == '1':
        os.system("termux-vibrate -d 100")
        loading_anim()
        os.system('python ~/mytools/brute.py')
    elif choice == '2':
        loading_anim()
        os.system('python ~/mytools/checker.py')
    elif choice == '3':
        loading_anim()
        os.system('python ~/mytools/generator.py')
    elif choice == '4':
        os.system("termux-tts-speak 'Starting traffic simulation'")
        loading_anim()
        os.system('python ~/mytools/traffic.py')
    elif choice == '5':
        loading_anim()
        os.system('python ~/mytools/breach_check.py')
    elif choice == '6':
        loading_anim()
        os.system('python ~/mytools/secret_msg.py')
    elif choice == '7':
        print(f"\n{Y}[!] Updating System...{W}")
        os.system('pkg update && pkg upgrade -y')
        os.system("termux-tts-speak 'Update finished'")
    elif choice == '8':
        os.system("termux-tts-speak 'Goodbye Master Edrian'")
        print(f"\n{G}Salamat sa paggamit, Master!{W}")
        sys.exit()
    else:
        print(f"\n{R}Maling option! Subukan ulit.{W}")
        time.sleep(1)
        menu()
        
    input(f"\n{C}[Pindutin ang Enter para bumalik sa Menu]{W}")
    menu()

if __name__ == "__main__":
    try:
        check_dependencies()
        menu()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Pinatay ang program.{W}")
        sys.exit()
