import time
import sys
import os
import random

def matrix_effect():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    print("\033[92m") # Ginagawang GREEN ang text
    for _ in range(30):
        line = "".join(random.choices(chars, k=40))
        print(f"  {line}")
        time.sleep(0.03)
    print("\033[0m") # Balik sa normal color

def advanced_brute(target, file_path):
    matrix_effect()
    if not os.path.exists(file_path):
        print(f"Error: {file_path} missing!")
        return

    total_lines = sum(1 for line in open(file_path, 'r'))
    print(f"\n[!] SYSTEM BREACH INITIALIZED")
    print(f"[*] TARGET: {target}")
    print(f"[*] DATABASE: {file_path}")
    print("-" * 40)

    start_time = time.time()
    with open(file_path, 'r') as f:
        for i, line in enumerate(f, 1):
            password = line.strip()
            percent = (i / total_lines) * 100
            bar = '#' * int(percent / 5) + '-' * (20 - int(percent / 5))
            
            sys.stdout.write(f"\r\033[92m[{bar}] {percent:.1f}% | DECRYPTING: {password} \033[0m")
            sys.stdout.flush()
            time.sleep(0.01)

            if password == target:
                end_time = time.time()
                total_time = end_time - start_time
                print(f"\n\n\033[92m[ACCESS GRANTED]\033[0m")
                print(f"[*] Key Found: {password}")
                print(f"[*] Decryption Speed: {i / total_time:.2f} keys/sec")
                return

    print("\n\n[-] ACCESS DENIED: Key not in database.")

# --- RUN ---
target = "YByOphgA" 
advanced_brute(target, "random_pass.txt")
