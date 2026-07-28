with open('generate_missing_symptoms.py') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
in_string = False
fixed = 0

for i, line in enumerate(lines):
    stripped = line.strip()
    
    if not in_string and stripped.startswith("r'") and stripped.endswith(","):
        # Check content after r' and before trailing comma
        inner = stripped[2:-1].strip()
        if "'" not in inner:
            in_string = True
            fixed += 1
            new_lines.append(line.replace("r'", 'r"""', 1).rstrip(',') + '')
            continue
    
    elif in_string:
        if stripped == "',":
            in_string = False
            new_lines.append('"""')
            new_lines.append(line)
            continue
        elif stripped == "'":
            in_string = False
            new_lines.append('"""')
            continue
    
    new_lines.append(line)

result = '\n'.join(new_lines)
with open('generate_missing_symptoms.py', 'w') as f:
    f.write(result)
print(f'Fixed {fixed} strings')
