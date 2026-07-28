import re

with open('medical_symptoms.tex', 'r') as f:
    content = f.read()

# Fix all include statements to use correct filenames that actually exist
fixes = [
    ('symptom_nauea', 'symptom_nausea'),  # fix the typo
]

for old, new in fixes:
    content = content.replace(old, new)

with open('medical_symptoms.tex', 'w') as f:
    f.write(content)

print("Fixed include statements")

# Verify all included files now exist
pattern = r'\\include{([^}]+)}'
matches = re.findall(pattern, content)
for inc in matches:
    basename = inc.split('/')[-1] if '/' in inc else inc
    filepath = 'chapters/' + basename + '.tex'
    status = 'OK' if os.path.exists(filepath) else 'MISSING'
    print(f'{basename}: {status}')

