import re

input_file = "C:\\Users\\pbuko\\Desktop\\ClassDAmp\\ClassDAmplifier\\simulations\\libraries\\TPS54202H_TRANS.LIB" # Podaj ścieżkę do oryginalnej biblioteki
output_file = "poprawiony_model.lib"

with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open(output_file, 'w', encoding='utf-8') as file:
    for line in lines:
        # 1. Zamiana v={...} na v=(...)
        line = re.sub(r'v=\{(.*?)\}', r'v=(\1)', line)
        # 2. Zamiana i={...} na i=(...)
        line = re.sub(r'i=\{(.*?)\}', r'i=(\1)', line)
        # 3. Usuwanie wewnętrznych klamer z zagnieżdżonych warunków, np. {if(...)}
        line = re.sub(r'\{if\(', r'if(', line)
        line = line.replace('})', '))')

        file.write(line)

print("Parsowanie zakończone. Możesz podpiąć nowy plik .lib w LTspice.")