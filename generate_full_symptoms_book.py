#!/usr/bin/env python3
"""Generate comprehensive Medical Symptoms A-Z book with extensive symptom coverage."""

import os
import glob

chapters_dir = '/Users/csv610/Projects/MyBooks/MedSymptoms/chapters'
os.makedirs(chapters_dir, exist_ok=True)

# Clean all existing chapter files except introduction and appendix
for f in os.listdir(chapters_dir):
    if f not in ['introduction.tex', 'appendix_emergency_warnings.tex'] and f.endswith('.tex'):
        os.remove(os.path.join(chapters_dir, f))

def create_chapter(title, definition, what_is, causes, seek_days, related):
    """Create a simple symptom chapter file."""
    base = title.lower().replace(' ', '_').replace('-', '_').replace('/', '_')
    
    lines = []
    lines.append('\\chapter{' + title + r'}')
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
        lines.append('  \\item ' + c)
    lines.append(r'\end{itemize}')
    lines.append('')
    lines.append(r'\section*{When Seek Medical Attention}')
    lines.append('Seek care if:')
    lines.append(r'\begin{itemize}')
    lines.append('  \item Severe or worsening symptoms')
    lines.append('  \item Symptoms lasting more than ' + str(seek_days))
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

# Comprehensive list of medically important symptoms organized alphabetically
symptom_data = [
    ('Abdominal Pain', 'Pain anywhere between chest and groin; one of most common reasons for medical consultation.', 'Location, character, timing provide diagnostic clues distinguishing visceral vs somatic pain.', 
     ['Gastroenteritis', 'Appendicitis', 'Peptic ulcer disease', 'IBS', 'Gallbladder disease'], '3 days', ['Nausea', 'Vomiting', 'Bloating']),
    ('Anxiety', 'Feelings of worry, nervousness, or unease about imminent events or uncertainties affecting daily functioning.', 'Can be situational or pervasive anxiety disorder involving autonomic arousal and cognitive apprehension.', 
     ['Stress', 'Medical conditions', 'Withdrawal', 'Personality traits', 'Genetic factors'], 'Persistent/Ongoing', ['Restlessness', 'Fatigue', 'Muscle tension']),
    ('Back Pain', 'Pain along spine from neck to lower back leading cause of disability and missed work worldwide.', 'Originates from muscles, nerves, bones or joints; classified acute/subacute/chronic with mechanical vs inflammatory patterns.', 
     ['Muscle strain', 'Herniated disc', 'Degenerative disc disease', 'Osteoarthritis', 'Osteoporotic fracture'], '7 days', ['Stiffness', 'Limited mobility', 'Radiating leg pain']),
    ('Blood in Stool', 'Presence of blood appearing bright red (lower GI) or black/tarry (upper GI).', 'Indicates gastrointestinal bleeding requiring localization; ranges from benign hemorrhoids to serious malignancy.', 
     ['Hemorrhoids', 'Anal fissure', 'Inflammatory bowel disease', 'Diverticulosis', 'Colorectal cancer'], 'Prompt evaluation', ['Abdominal pain', 'Change in bowel habits', 'Weight loss']),
    ('Chest Pain', 'Discomfort in chest area ranging from burning, pressure, squeezing, sharp quality.', 'Critical symptom requiring urgent differentiation between cardiac, pulmonary, gastrointestinal, musculoskeletal etiologies.', 
     ['Angina/MI', 'Pulmonary embolism', 'GERD/esophageal spasm', 'Pericarditis', 'Musculoskeletal strain'], 'Immediate', ['Shortness of breath', 'Sweating', 'Radiating pain']),
    ('Chills', 'Shivering sensation often accompanying fever as body tries to raise temperature set point.', 'Physiological response during febrile illness characterized by peripheral vasoconstriction and shivering thermogenesis.', 
     ['Bacterial infection', 'Malaria', 'Drug reaction', 'Post-operative state', 'Heat stroke recovery'], 'With fever or persistent', ['Fever', 'Sweating', 'Malaise']),
    ('Cough', 'Reflex action clearing airways of mucus or irritants; classified acute, subacute, chronic by duration.', 'Productive vs dry, timing, triggers help differentiate etiations; upper airway cough syndrome most common cause of chronic cough.', 
     ['Viral URI', 'Asthma/COPD', 'GERD', 'Postnasal drip', 'Smoking/smoke irritation'], '3 weeks (persistent)', ['Sore throat', 'Congestion', 'Wheezing']),
    ('Diarrhea', 'Frequent passage of loose or watery stools exceeding usual frequency and consistency.', 'Caused by increased secretion, decreased absorption, altered transit time, or osmotic load; acute vs chronic guides evaluation.', 
     ['Viral gastroenteritis', 'Bacterial infection', 'Antibiotic-associated diarrhea', 'IBS-D', 'Inflammatory bowel disease'], '2-3 days (persistent)', ['Abdominal cramps', 'Urgency', 'Dehydration']),
    ('Dizziness', 'Feeling of lightheadedness, unsteadiness, or vertigo (spinning sensation); distinct sensations have different etiations.', 'Encompasses vertigo, presyncope, disequilibrium, lightheadedness - each with distinct differential diagnoses.', 
     ['BPPV', 'Orthostatic hypotension', 'Dehydration', 'Medication side effects', 'Anxiety/panic'], 'Evaluation needed if persistent/recurring', ['Nausea', 'Imbalance', 'Hearing changes']),
    ('Hair Loss', 'Excessive shedding or thinning beyond normal turnover; pattern distinguishes telogen effluvium from alopecia areata from androgenetic.', 'Diffuse vs patchy, gradual vs sudden patterns guide toward nutritional stress/autoimmune/hormonal/mechanical causes.', 
     ['Nutritional deficiencies/stress', 'Medication side effects', 'Autoimmune disease (alopecia areata)', 'Thyroid imbalance', 'Genetic predisposition (androgenetic)'], 'Gradual over months requires evaluation', ['Scalp tenderness', 'Nail changes', 'Thinning pattern']),
    ('Fatigue', 'Extreme tiredness, lack of energy, distinct from ordinary physical tiredness; persists despite rest.', 'Multifactorial symptom representing potential combination of peripheral muscle fatigue and central nervous system mechanisms across numerous conditions.', 
     ['Depression/anxiety disorders', 'Anemia or other hemoglobinopathies', 'Obstructive sleep apnea', 'Hypothyroidism', 'Medication side effects or chronic conditions'], 'Persistent interfering with daily life (>4 weeks) warrants investigation', ['Weakness/concentration difficulty', 'Sleep disturbance', 'Mood changes', 'Malaise']),
    ('Fever', 'Elevation of body temperature above normal range (>38°C/100.4°F) representing immune system response.', 'Regulated increase mediated by pyrogens acting on hypothalamus; distinguishes from hyperthermia where thermoregulation fails.', 
     ['Viral infections (URI/flu)', 'Bacterial infections (pneumonia, UTI)', 'Inflammatory/autoimmune disorders', 'Drug-induced fever', 'Malignancy'], '>3 days duration or >40°C warrants medical attention', ['Chills', 'Headache', 'Myalgia', 'Anorexia', 'Dehydration']),
    ('Headache', 'Pain perceived anywhere in head region among most common human experiences encountered clinically.', 'Primary headaches lack identifiable structural cause; secondary headaches attributable to another condition with diverse mechanisms.', 
     ['Tension-type headache (most common)', 'Migraine', 'Cluster headache', 'Medication-overuse', 'Secondary causes requiring urgent evaluation'], 'Thunderclap onset, progressive worsening, new after age 50 require urgent evaluation', ['Nausea/vomiting', 'Photophobia/phonophobia', 'Neck stiffness', 'Visual aura changes', 'Worsening with Valsalva']),
    ('Hoarseness', 'Change in voice quality making it rough, strained, breathy, or nasal due to laryngeal pathology.', 'Vocal cord dysfunction, inflammation, mass effect, neurological involvement all contribute to altered voice production; vocal abuse common cause.', 
     ['Acute laryngitis/viral URI', 'Acid reflux/laryngopharyngeal reflux', 'Vocal nodules/polyps', 'Vocal cord paralysis', 'Laryngeal carcinoma'], 'Voice change persisting beyond 2-3 weeks warrants ENT evaluation', ['Sore throat', 'Dysphagia', 'Stridor/wheeze', 'Cough', 'Neck mass']),
    ('Joint Pain', 'Pain or discomfort localized to one or more joints varying from dull ache to sharp stabbing sensation.', 'Differentiated monoarticular vs polyarticular, symmetric vs asymmetric, inflammatory vs degenerative patterns guiding toward rheumatologic or orthopedic etiologies.', 
     ['Osteoarthritis (degenerative)', 'Rheumatoid arthritis (inflammatory)', 'Trauma/injury', 'Septic arthritis (infectious)', 'Gout (crystal arthropathy)'], 'Evaluated clinically based on pattern and associated findings including swelling, warmth, erythema, reduced ROM', ['Swelling', 'Warmth/redness', 'Morning stiffness >30min', 'Reduced movement', 'Systemic symptoms like fever/rash']),
    ('Muscle Pain', 'Muscular discomfort ranging from soreness to sharp pain potentially arising from strain, inflammation, metabolic derangement, or medication effects.', 'Differentiate myopathic (proximal weakness, elevated CK) from neuropathic (radicular distribution), systemic causes (thyroid, electrolytes, statins).', 
     ['Exertional strain/sports injury', 'Viral illness (myalgia)', 'Electrolyte imbalances', 'Medication side effects (statins)', 'Inflammatory myopathy (polymyositis)'], 'Evaluated clinically based on distribution associated weakness patterns severity progression', ['Weakness', 'Swelling tenderness cramps fever if infectious/inflammatory systemic malaise']),
    ('Night Sweats', 'Excessive sweating during sleep requiring change of clothing or bedding often indicating underlying medical condition.', 'May indicate infectious autoimmune endocrine neoplastic medication psychogenic or idiopathic etiations requiring systematic evaluation when recurrent associated constitutional symptoms.', 
     ['Menopausal hot flashes most common benign antidepressant medications antipyretics withdrawal states tuberculosis lymphoma hyperthyroidism insulinoma pheochromocytoma malignancies drug reactions'], 'Recurring episodes especially if accompanied by weight loss fever chills warrant medical investigation prompting screening for infection autoimmune neoplastic etiations hormonal disturbances medication review ', ['Fever unintended weight loss chills malaise palpitations anxiety tremor insomnia sleep disturbance'])
]

# Generate all chapters
print('Generating comprehensive Medical Symptoms A-Z book...')
for i, (title, definition, what_is, causes, seek_days, related) in enumerate(symptom_data):
    create_chapter(title, definition, what_is, causes, seek_days, related)
    print(f'  Chapter {i+1:2d}: {title}')

print(f'\nSuccessfully generated {len(symptom_data)} symptom chapters!')
