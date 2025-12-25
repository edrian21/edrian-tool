import base64
import os

def crypt_tool():
    print("\033[95m")
    print("--- SECRET MESSAGE ENCRYPTER ---")
    print("\033[0m")
    print("[1] I-Encrypt ang Message (Gawing Secret Code)")
    print("[2] I-Decrypt ang Code (Basahin ang Secret Code)")
    
    choice = input("\n[?] Anong gagawin natin?: ")
    
    if choice == '1':
        msg = input("[>] I-type ang secret message: ")
        encoded = base64.b64encode(msg.encode()).decode()
        print(f"\n\033[92m[SUCCESS] Secret Code: {encoded}\033[0m")
        print("(I-copy ito at i-send sa kaibigan mo!)")
        
    elif choice == '2':
        code = input("[>] I-paste ang Secret Code: ")
        try:
            decoded = base64.b64decode(code.encode()).decode()
            print(f"\n\033[92m[DECRYPTED]: {decoded}\033[0m")
        except:
            print("\n\033[91m[ERROR] Maling code!\033[0m")

if __name__ == "__main__":
    crypt_tool()
