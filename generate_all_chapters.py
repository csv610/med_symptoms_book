#!/usr/bin/env python3
"""Generate symptom chapters - simple direct writing."""

import os

os.makedirs('/Users/csv610/Projects/MyBooks/MedSymptoms/chapters', exist_ok=True)

def write_chapter(name, definition, what_is, causes, days, related):
    """Write a single symptom chapter file."""
    # Create filename from name (lowercase, spaces replaced with underscores)
    base_name = name.lower().replace(' ', '_')
    
    lines = []
    lines.append(r'\chapter{' + name + r'}')
    lines.append('')
    lines.append(r'\section*{Definition}')
    lines.append(definition)
    lines.append('')
    lines.append(r'\section*{What Is This Symptom?}')
    lines.append(what_is)
    lines.append('')
    lines.append(r'\section*{Common Causes}')
    lines.append(r'\begin{itemize}')
    for cause in causes[:5]:  # Max 5 causes
        lines.append(r'  \item ' + cause)
    lines.append(r'\end{itemize}')
    lines.append('')
    lines.append(r'\section*{When Seek Medical Attention}')
    lines.append(r'Seek care if:')
    lines.append(r'\begin{itemize}')
    lines.append(r'  \item Severe or worsening symptoms')
    lines.append(r'  \item Symptoms lasting more than ' + days)
    lines.append(r'  \item Accompanied by other concerning signs')
    lines.append(r'\end{itemize}')
    lines.append('')
    lines.append(r'\section*{Related Symptoms}')
    lines.append(r'May occur with: ' + related)
    lines.append('')
    lines.append(r'\textbf{Note:} Always consider serious underlying conditions when evaluating persistent ' + name.lower() + '.')
    lines.append('')
    lines.append(r'\clearpage')
    lines.append('')
    
    content = '\n'.join(lines)
    filename = '/Users/csv610/Projects/MyBooks/MedSymptoms/chapters/symptom_' + base_name + '.tex'
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created: {filename}")

# Define all symptoms
symptoms = [
    ("Abdominal Pain",
     "Pain or discomfort anywhere between the chest and groin.",
     "Abdominal pain can be acute or chronic. Location and character provide clues about cause.",
     ["Gastroenteritis", "Appendicitis", "Ulcers", "IBS", "Gallbladder disease"],
     "3",
     "Nausea, vomiting, bloating"),
    ("Back Pain",
     "Pain anywhere from neck to lower back.",
     "Back pain originates from muscles, nerves, bones, or joints in spine.",
     ["Muscle strain", "Herniated disc", "Degenerative disease", "Osteoporosis", "Poor posture"],
     "7",
     "Stiffness, limited mobility, radiating pain"),
    ("Chest Pain",
     "Discomfort in chest area, may feel like burning, pressure, or squeezing.",
     "Requires careful evaluation - cardiac, pulmonary, GI, or musculoskeletal causes.",
     ["Angina", "Heart attack", "GERD", "Muscle strain", "Anxiety"],
     "Immediate",
     "Shortness of breath, sweating, nausea"),
    ("Cough",
     "Reflex action to clear airways of mucus or irritants.",
     "Dry or productive; classified as acute, subacute, or chronic.",
     ["Cold", "Asthma", "GERD", "Postnasal drip", "Smoking"],
     "3",
     "Sore throat, congestion, wheezing"),
    ("Dizziness",
     "Feeling of lightheadedness, unsteadiness, or vertigo (spinning).",
     "Encompasses vertigo, presyncope, disequilibrium, lightheadedness.",
     ["BPPV", "Orthostatic hypotension", "Dehydration", "Medication side effects", "Anxiety"],
     "3",
     "Nausea, imbalance, hearing changes"),
    ("Fatigue",
     "Extreme tiredness, lack of energy, not relieved by rest.",
     "More profound than normal tiredness; may be physical, mental, or both.",
     ["Anemia", "Depression", "Thyroid disease", "Sleep disorders", "Chronic illness"],
     "7",
     "Weakness, concentration difficulties, sleep problems"),
    ("Headache",
     "Pain on head ranging from dull aching to throbbing.",
     "Primary (migraine, tension-type) or secondary causes.",
     ["Tension", "Migraine", "Sinus issues", "Dehydration", "Medication overuse"],
     "3",
     "Nausea, light sensitivity, neck stiffness"),
    ("Nausea and Vomiting",
     "Nausea is urge to vomit; vomiting is expulsion of stomach contents.",
     "Frequently together; GI, neurological, pregnancy, medications cause them.",
     ["Viral illness", "Pregnancy", "Medication side effects", "GI obstruction", "Migraine"],
     "2",
     "Abdominal pain, loss of appetite, dehydration"),
    ("Shortness of Breath",
     "Difficulty breathing or sensation of not getting enough air (dyspnea).",
     "Acute or chronic; cardiac, pulmonary, hematologic, neuromuscular issues possible.",
     ["Heart failure", "Asthma", "COPD", "Pulmonary embolism", "Anxiety"],
     "Immediate",
     "Chest pain, coughing, palpitations, swelling"),
    ("Fever",
     "Elevation of body temperature above normal range.",
     "Immune response to pathogens; continuous, intermittent, remittent patterns.",
     ["Viral infection", "Bacterial infection", "Inflammatory disease", "Medication reaction", "Heat exposure"],
     "3",
     "Chills, sweating, headache, muscle aches"),
    ("Confusion",
     "Altered awareness, difficulty thinking clearly.",
     "Mild disorientation to severe delirium; often indicates serious condition.",
     ["Infection", "Metabolic disturbance", "Medication effect", "Head injury", "Stroke"],
     "Immediate",
     "Memory loss, agitation, lethargy"),
    ("Memory Loss",
     "Inability to recall information or events previously stored.",
     "Distinction between normal forgetting and pathological impairment; progressive forms suggest neurodegeneration.",
     ["Normal aging", "Alzheimers disease", "Depression", "Medication side effects", "Thyroid disorder"],
     "Persistent",
     "Getting lost easily, repeating questions, difficulty with tasks"),
    ("Seizures",
     "Uncontrolled electrical activity in brain causing abnormal movements.",
     "Convulsions, staring spells, sensory changes; requires neurological eval.",
     ["Epilepsy", "Head injury", "Infection", "Metabolic imbalance", "Tumor"],
     "Immediate",
     "Loss of awareness, post-seizure confusion, muscle soreness"),
    ("Joint Pain",
     "Pain or discomfort in one or more joints.",
     "Affects any joint; associated with arthritis, injury, systemic diseases.",
     ["Arthritis", "Injury", "Overuse", "Gout", "Infection"],
     "3",
     "Swelling, stiffness, redness, decreased range of motion"),
]

for s in symptoms:
    write_chapter(*s)

print("\nAll chapters generated successfully!")
