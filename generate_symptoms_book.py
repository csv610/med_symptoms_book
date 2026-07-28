#!/usr/bin/env python3
"""Generate comprehensive Medical Symptoms book with extensive symptom coverage."""

import os

chapters_dir = '/Users/csv610/Projects/MyBooks/MedSymptoms/chapters'
os.makedirs(chapters_dir, exist_ok=True)

# Remove existing symptom chapter files for clean slate
for f in os.listdir(chapters_dir):
    if f.startswith('symptom_') and f.endswith('.tex'):
        os.remove(os.path.join(chapters_dir, f))

def create_chapter(title, definition, what_is, causes, seek_advice, related):
    """Create a simple symptom chapter file."""
    base = title.lower().replace(' ', '_').replace('-', '_')
    
    lines = []
    lines.append(r'\chapter{' + title + r'}')
    lines.append('')
    lines.append(r'\section*{Definition}')
    lines.append(definition)
    lines.append('')
    lines.append(r'\section*{What Is This Symptom?}')
    lines.append(what_is)
    lines.append('')
    lines.append(r'\section*{Common Causes}')
    lines.append(r'\begin{itemize}')
    for c in causes[:5]:
        lines.append('  \item ' + c)
    lines.append(r'\end{itemize}')
    lines.append('')
    lines.append(r'\section*{When Seek Medical Attention}')
    lines.append('Seek care if:')
    lines.append(r'\begin{itemize}')
    lines.append('  \item Severe or worsening symptoms')
    lines.append('  \item Symptoms lasting more than ' + seek_advice)
    lines.append('  \item Accompanied by other concerning signs')
    lines.append(r'\end{itemize}')
    lines.append('')
    lines.append(r'\section*{Related Symptoms}')
    lines.append('May occur with: ' + ', '.join(related[:5]))
    lines.append('')
    lines.append(r'\textbf{Note:} Always consider serious underlying conditions when evaluating persistent ' + base + '.')
    lines.append('')
    lines.append(r'\clearpage')
    lines.append('')
    
    content = '\n'.join(lines)
    filename = chapters_dir + '/symptom_' + base + '.tex'
    with open(filename, 'w') as f:
        f.write(content)
    return filename

# Comprehensive symptom database
symptoms_data = [
    ('Fever', 'Elevation of body temperature above normal range (>38°C/100.4°F), representing immune system response.', 'Fever is a regulated increase in body temperature mediated by pyrogens acting on the hypothalamus.', 
     ['Viral infections (flu)', 'Bacterial infections (pneumonia)', 'Autoimmune disorders', 'Drug reactions', 'Malignancy'],
     '>3 days fever, >40C temperature, immunocompromised', 
     ['Chills', 'Headache', 'Muscle pain', 'Dehydration', 'Anorexia']),
    
    ('Headache', 'Pain perceived anywhere in the head region, among most common clinical complaints.', 'Headache represents diverse mechanisms; classified into primary and secondary categories based on etiology.',
     ['Tension-type headache', 'Migraine', 'Cluster headache', 'Medication overuse', 'Secondary causes'],
     'Thunderclap onset, progressive worsening, new after age 50',
     ['Nausea', 'Photophobia', 'Neck stiffness', 'Visual changes', 'Vomiting']),
    
    ('Chest Pain', 'Discomfort in chest area requiring urgent evaluation due to potentially life-threatening etiologies.', 'Chest pain spans cardiac, pulmonary, gastrointestinal, musculoskeletal, and psychological systems.',
     ['Angina/MI', 'Pulmonary embolism', 'GERD', 'Pericarditis', 'Musculoskeletal strain'],
     'Radiating pain, sweating, shortness of breath, syncope',
     ['Shortness of breath', 'Sweating', 'Nausea', 'Radiating pain', 'Palpitations']),
    
    ('Shortness of Breath', 'Subjective breathing discomfort known as dyspnea, varying from mild to severe air hunger.', 'Dyspnea reflects mismatch between respiratory drive and ventilation; multiple organ systems implicated.',
     ['Heart failure', 'Asthma/COPD', 'Pulmonary embolism', 'Pneumonia', 'Anxiety'],
     'Acute at rest, cyanosis, altered mental status',
     ['Cough', 'Chest pain', 'Orthopnea', 'Edema', 'Tachycardia']),
    
    ('Back Pain', 'Pain along spine from neck to lower back, leading cause of disability and missed work.', 'Mechanical back pain from spinal structures differentiated by pattern and red flags.',
     ['Muscle strain', 'Herniated disc', 'Degenerative disc', 'Osteoarthritis', 'Osteoporotic fracture'],
     'Neurological deficit, saddle anesthesia, weight loss, cancer history',
     ['Stiffness', 'Reduced mobility', 'Radiating leg pain', 'Spasms', 'Limited flexion']),
    
    ('Fatigue', 'Persistent tiredness and lack of energy not relieved by rest, affecting quality of life.', 'Multifactorial symptom representing potential peripheral and central mechanisms across many conditions.',
     ['Depression/anxiety', 'Anemia', 'Sleep apnea', 'Hypothyroidism', 'Medication side effects'],
     'Interferes with daily function, cognitive difficulty, mood changes',
     ['Weakness', 'Concentration problem', 'Sleep disturbance', 'Malaise', 'Mood changes']),
    
    ('Joint Pain', 'Pain or tenderness localized to one or more joints, varying from dull ache to sharp stabbing.', 'Joint pain arises from intra-articular or periarticular tissues characterized by distribution and associated findings.',
     ['Osteoarthritis', 'Rheumatoid arthritis', 'Gout', 'Septic arthritis', 'Trauma'],
     'Hot swollen monoarticular joint, asymmetric oligoarthritis with enthesitis',
     ['Swelling', 'Warmth', 'Redness', 'Stiffness', 'Limited movement']),
    
    ('Nausea and Vomiting', 'Nausea is urge to vomit; vomiting is forceful expulsion of stomach contents via coordinated reflex.', 'Brainstem-mediated reflex triggered by GI irritation, vestibular stimulation, increased ICP, metabolic disturbances.',
     ['Gastroenteritis', 'Pregnancy', 'Medication side effects', 'GI obstruction', 'Migraine'],
     'Projectile vomiting, bilious emesis, coffee-ground material, obstipation',
     ['Abdominal pain', 'Dehydration', 'Electrolyte imbalance', 'Weight loss', 'Anorexia']),
    
    ('Diarrhea', 'Loose or watery stools exceeding usual frequency; defined as >3/day with decreased form.', 'Caused by increased secretion, decreased absorption, altered transit time, or osmotic load; acute vs chronic.',
     ['Viral gastroenteritis', 'Bacterial infection', 'Antibiotic-associated', 'IBS-D', 'Inflammatory bowel disease'],
     'Bloody stool, high fever, recent antibiotics, travel, immunosuppressed',
     ['Abdominal cramps', 'Urgency', 'Tenesmus', 'Malabsorption', 'Weight loss']),
    
    ('Constipation', 'Infrequent spontaneous bowel movements (<3/week) with straining, hard stool, or incomplete evacuation.', 'Defined by Rome IV criteria; slow transit, dyssynergic defecation, functional disorders; medication-induced common.',
     ['Low fiber/fluid diet', 'Opioids', 'Hypothyroidism', "Parkinson's disease", 'IBS-C'],
     'Constipation with abdominal pain, rectal bleeding, change from habitual pattern in older adults',
     ['Bloating', 'Straining feeling', 'Rectal fullness', 'Hard stools', 'Incomplete emptying'])
]

# Generate all symptom chapters
print("Generating comprehensive symptom chapters...")
for i, (title, defn, what_is, causes, seek, related) in enumerate(symptoms_data):
    create_chapter(title, defn, what_is, causes, seek, related)
    print(f"  Chapter {i+1:2d}: {title}")

print("\nDone! Generated {} symptom chapters.".format(len(symptoms_data)))
