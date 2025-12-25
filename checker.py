import time
import sys

def check_and_crack():
    print("\033[92m")
    print("=== SECURITY & PENETRATION TEST SIMULATOR ===")
    password = input("\033[0m[?] Mag-enter ng password na i-te-test: ")
    
    # --- PART 1: STRENGTH ANALYSIS ---
    print("\n[*] Analyzing security...")
    time.sleep(1)
    
    score = 0
    if len(password) >= 8: score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    
    if score == 1: status = "\033[91mWEAK\033[0m"
    elif score == 2: status = "\033[93mMEDIUM\033[0m"
    else: status = "\033[92mSTRONG\033[0m"
    
    print(f"[!] Security Level: {status}")
    print("-" * 45)

    # --- PART 2: BRUTE FORCE ATTEMPT ---
    wordlist = ["123456", "admin", "password", "qwerty", "Edrian321", "welcome", "P@ssword123"]
    
    print(f"[*] Simulating Brute Force using common wordlist...")
    time.sleep(1)
    
    found = False
    for attempt, word in enumerate(wordlist, 1):
        sys.stdout.write(f"\r[Attempt {attempt}] Testing: {word}      ")
        sys.stdout.flush()
        time.sleep(0.3)
        
        if word == password:
            print(f"\n\n\033[91m[CRACKED!]\033[0m Password found in wordlist.")
            print(f"[*] Aralin: Huwag gumamit ng common passwords!")
            found = True
            break
            
    if not found:
        print(f"\n\n\033[92m[SECURE]\033[0m Password not found in common wordlist.")
        print("[*] Aralin: Mas mahirap i-crack ang password na wala sa dictionary.")

# Run the program
check_and_crack()
