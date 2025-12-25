import os
import time

url = input("\n[?] Enter URL (ex: https://tiktok.com/@user): ")
count = int(input("[?] How many visits?: "))

for i in range(1, count + 1):
    os.system(f"curl -s -L {url} > /dev/null")
    print(f"[{i}] Request sent...")
    time.sleep(2)
print("\n[+] Done.")
