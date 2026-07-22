def ringkas_nilai(data):
    nilai_valid = []
    
for nilai in data:
    if isinstance(nilai, (int, float)):
        if 0 <= nilai <= 100:
            nilai_valid.append(nilai)
    if nilai == str(nilai):
        try:
            nilai_float = float(nilai)
            if 0 <= nilai_float <= 100:
                nilai_valid.append(nilai_float)
        except ValueError:
            continue