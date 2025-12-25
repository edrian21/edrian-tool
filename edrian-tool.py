import os
import sys
import time

# Color Palette (Rainbow)
R = "\033[91m" # Red
G = "\033[92m" # Green
Y = "\033[93m" # Yellow
B = "\033[94m" # Blue
P = "\033[95m" # Purple
C = "\033[96m" # Cyan
W = "\033[0m"  # White/Reset

def loading_anim():
    animation = ["|", "/", "-", "\\"]
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write(f"\r{C}[*] Loading {animation[i % len(animation)]}{W}")
        sys.stdout.flush()
    print("\n")

def menu():
    os.system('clear')
    # Rainbow Header
    print(f"{R}==={Y}==={G}==={C}==={B}==={P}==={R}==={Y}==={G}==={C}==={B}==={P}===")
    print(f"{G}      EDRIAN'S ULTIMATE TOOL V2.0 (PRO)    ")
    print(f"{R}==={Y}==={G}==={C}==={B}==={P}==={R}==={Y}==={G}==={C}==={B}==={P}==={W}")
    
    print(f"\n{R}[1] {W}Brute Force Simulator")
    print(f"{Y}[2] {W}Password Strength Checker")
    print(f"{G}[3] {W}Wordlist Generator")
    print(f"{C}[4] {W}Web Traffic Simulator")
    print(f"{B}[5] {W}Data Breach Scanner")
    print(f"{P}[6] {W}Secret Message Tool")
    print(f"{R}[7] {W}Update Termux System")
    print(f"{Y}[8] {W}Exit")
    
    choice = input(f"\n{G}[?] Master, anong gagawin natin? : {W}")
    
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
        print(f"\n{G}Salamat sa paggamit!{W}")
        sys.exit()
    else:
        print(f"\n{R}Maling option!{W}")
        
    input(f"\n{C}[Pindutin ang Enter]{W}")
    menu()

if __name__ == "__main__":
    menu()
