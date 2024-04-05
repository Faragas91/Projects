import os

# Name des Makefiles
MAKEFILE = "D:/Projects/ISIS/Makefile"

# Verzeichnis, in dem die Zielfiles gespeichert werden sollen
OUTPUT_DIR = "D:/Projects/ISIS/makefile_targets"

# Erstellen des Ausgabeverzeichnisses, wenn es nicht existiert
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(MAKEFILE, 'r') as fh:
    lines = fh.readlines()
    target_name = ""
    target_content = ""
    processing_target = True
    
    # Goes throw every line 
    for line in lines:
        line = line.strip()

        # When the processing is Stoped but the Row contains "./" and ".o" given, the process continues
        if line.startswith("./") and ".o" in line and processing_target == False:
            processing_target = True

        # The progress starts
        if line.startswith("./") and ".o" in line and processing_target == True:
            # Catch the Name from the arget
            target_name = line.split(':')[0]
            
            # Create the .d File from target
            with open(os.path.join(OUTPUT_DIR, target_name + ".d"), 'w') as output_fh:
                output_fh.write(target_content)
            
        
        # Stoped the processing when the row is empty
        if target_name and not line:
            processing_target = False
        
        # Only necessary files are added  
        elif ".cpp" in line or ".hpp" in line or ".o" in line:
            target_content += line + '\n'

        # Close the last target file, if available
        if target_name and processing_target == False and not line:
            with open(os.path.join(OUTPUT_DIR, target_name + ".d"), 'w') as output_fh:
                output_fh.write(target_content)
                target_name = ""
                target_content = ""
