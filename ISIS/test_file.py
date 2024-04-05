import os

# Name des Makefiles
MAKEFILE = "D:/Projects/ISIS/Makefile"

# Verzeichnis, in dem die Zielfiles gespeichert werden sollen
OUTPUT_DIR = "D:/Projects/ISIS/makefile_targets"

# Erstellen des Ausgabeverzeichnisses, wenn es nicht existiert
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(MAKEFILE, 'r') as fh:
    lines = fh.readlines()
    last_line = len(lines)
    current_line = 0

# Lesen des Makefiles
with open(MAKEFILE, 'r') as fh:
    target_name = ""
    target_content = ""
    
    while current_line < last_line:
        for line in fh:
            current_line += 1
            line = line.strip()

            # Überprüfe, ob ".o" in der Zeile vorhanden ist
            if ".o" in line and not "$(CXX)" in line:
                # Speichern des vorherigen Ziels in eine Datei, falls vorhanden
                if target_name:
                    with open(os.path.join(OUTPUT_DIR, target_name + ".d"), 'w') as output_fh:
                        output_fh.write(target_content)
                # Neues Ziel für eine .o-Datei gefunden
                target_name = line.split(':')[0]
                target_content = line + '\n'
            elif not line:
                # Leerzeile gefunden
                if target_name:
                    # Wenn ein Ziel vorhanden ist, füge die Leerzeile hinzu
                    target_content += '\n'
            elif target_name:
                # Fortsetzung des aktuellen Ziels
                target_content += line + '\n'
            

        # Schließen der letzten Ziel-Datei, falls vorhanden
        if target_name:
            with open(os.path.join(OUTPUT_DIR, target_name + ".d"), 'w') as output_fh:
                output_fh.write(target_content)
 