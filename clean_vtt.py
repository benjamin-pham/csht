import os
import re
import glob

def clean_vtt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    clean_lines = []
    for line in lines:
        line = line.strip()
        if line == 'WEBVTT' or line == '':
            continue
        # Skip UUID lines
        if re.match(r'^[a-f0-9\-]{36}/\d+-\d+$', line):
            continue
        # Skip timestamp lines
        if '-->' in line:
            continue
        
        # Remove speaker tags like <v Name> and </v>
        line = re.sub(r'<v [^>]+>', '', line)
        line = re.sub(r'</v>', '', line)
        
        if line:
            clean_lines.append(line)
            
    # Combine lines, adding space if needed
    text = ' '.join(clean_lines)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    
    out_path = filepath + '.txt'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Cleaned {filepath} -> {out_path} ({len(text)} chars)")

for file in glob.glob('./Transcript/*/*.vtt'):
    clean_vtt(file)
