import random
import string

def generate_list(filename, count):
    chars = string.ascii_letters + string.digits
    with open(filename, 'w') as f:
        for _ in range(count):
            # Gagawa ng random password na may 8 characters
            res = ''.join(random.choices(chars, k=8))
            f.write(res + '\n')
    print(f"[+] Tapos na! {count} passwords ang na-save sa {filename}")

generate_list("random_pass.txt", 100)
