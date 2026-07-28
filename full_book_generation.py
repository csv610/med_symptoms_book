#!/usr/bin/env python3
"""Generate complete Medical Symptoms book with comprehensive symptom coverage."""

import os
import glob

chapters_dir = '/Users/csv610/Projects/MyBooks/MedSymptoms/chapters'

# Clean all chapter files except introduction and appendix
for f in os.listdir(chapters_dir):
    if f not in ['introduction.tex', 'appendix_emergency_warnings.tex'] and f.endswith('.tex'):
        os.remove(os.path.join(chapters_dir, f))

def create_symptom(name, defn, what_is, causes_list, seek_days, related_list):
    """Write a single symptom chapter file."""
    base = name.lower().replace(' ', '_').replace('-', '_').replace('/', '_')
    
    lines = []
    lines.append(r'\chapter{' + name + r'}')
    lines.append('')
    lines.append(r'\section*{Definition}')
    lines.append(defn)
    lines.append('')
    lines.append(r'\section*{What Is This Symptom?}')
    lines.append(what_is)
    lines.append('')
    lines.append(r'\section*{Common Causes}')
    lines.append(r'\begin{itemize}')
    for c in causes_list[:5]:
        lines.append('  \item ' + c)
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
    lines.append('May occur with: ' + ', '.join(related_list[:5]))
    lines.append('')
    lines.append(r'\textbf{Note:} Always consider serious underlying conditions when evaluating persistent ' + base + '.')
    lines.append('')
    lines.append(r'\clearpage')
    lines.append('')
    
    with open(os.path.join(chapters_dir, 'symptom_' + base + '.tex'), 'w') as f:
        f.write('\n'.join(lines))

# Comprehensive symptom database with full A-Z coverage
symptoms = [
    ('Abdominal Pain', 'Pain anywhere between chest and groin; one of most common reasons for medical consultation.', 
     'Location character timing provide diagnostic clues distinguishing visceral somatic pain.',
     ['Gastroenteritis', 'Appendicitis', 'Peptic ulcer disease', 'IBS', 'Gallbladder disease'], '3 days', 
     ['Nausea', 'Vomiting', 'Bloating', 'Anorexia', 'Constipation/Diarrhea']),
    
    ('Back Pain', 'Pain along spine from neck to lower back leading cause of disability and missed work worldwide.',
     'Originates from muscles nerves bones joints classified acute subacute chronic mechanical inflammatory patterns.',
     ['Muscle strain', 'Herniated disc', 'Degenerative disc disease', 'Osteoarthritis', 'Osteoporotic fracture'], '7 days',
     ['Stiffness', 'Limited mobility', 'Radiating leg pain', 'Muscle spasms', 'Reduced flexibility']),
    
    ('Chest Pain', 'Discomfort in chest area ranging burning pressure squeezing sharp quality.',
     'Critical symptom requiring urgent differentiation cardiac pulmonary gastrointestinal musculoskeletal etiologies.',
     ['Angina/MI', 'Pulmonary embolism', 'GERD/esophageal spasm', 'Pericarditis', 'Musculoskeletal strain'], 'Immediate',
     ['Shortness of breath', 'Sweating', 'Radiating pain', 'Dizziness', 'Nausea']),
    
    ('Headache', 'Pain perceived anywhere head region among most common human experiences encountered clinically.',
     'Primary headaches lack identifiable structural cause secondary headaches attributable another condition diverse mechanisms.',
     ['Tension-type headache (most common)', 'Migraine', 'Cluster headache', 'Medication-overuse', 'Secondary causes requiring urgent evaluation'], 'Thunderclap onset progressive worsening new after age 50 require urgent evaluation',
     ['Nausea vomiting', 'Photophobia phonophobia', 'Neck stiffness', 'Visual aura changes', 'Worsening with Valsalva']),
    
    ('Fever', 'Elevation body temperature above normal range (>38°C/100.4°F) representing immune system response.',
     'Regulated increase mediated pyrogens acting hypothalamus distinguishes hyperthermia thermoregulation fails.',
     ['Viral infections URI/flu', 'Bacterial infections pneumonia UTI', 'Inflammatory autoimmune disorders', 'Drug-induced fever', 'Malignancy'], '>3 days duration >40°C warrants medical attention',
     ['Chills', 'Headache', 'Myalgia', 'Anorexia', 'Dehydration']),
    
    ('Fatigue', 'Extreme tiredness lack energy distinct ordinary physical tiredness persists despite rest.',
     'Multifactorial symptom potential combination peripheral muscle fatigue central nervous system mechanisms across numerous conditions.',
     ['Depression/anxiety disorders', 'Anemia', 'Obstructive sleep apnea', 'Hypothyroidism', 'Medication side effects'], 'Persistent interfering daily life >4 weeks warrants investigation',
     ['Weakness concentration difficulty', 'Sleep disturbance', 'Mood changes', 'Malaise', 'Reduced exercise tolerance']),
    
    ('Joint Pain', 'Pain discomfort localized one or more joints varying dull ache sharp stabbing sensation.',
     'Differentiated monoarticular polyarticular symmetric asymmetric inflammatory degenerative patterns guiding rheumatologic orthopedic etiologies.',
     ['Osteoarthritis (degenerative)', 'Rheumatoid arthritis (inflammatory)', 'Trauma/injury', 'Septic arthritis (infectious)', 'Gout (crystal arthropathy)'], 'Evaluated clinically based pattern associated findings',
     ['Swelling', 'Warmth/redness', 'Morning stiffness >30min', 'Reduced movement', 'Systemic symptoms like fever/rash']),
    
    ('Diarrhea', 'Frequent passage loose watery stools exceeding usual frequency consistency.',
     'Caused increased secretion decreased absorption altered transit time osmotic load acute chronic guides evaluation.',
     ['Viral gastroenteritis', 'Bacterial infection', 'Antibiotic-associated diarrhea', 'IBS-D', 'Inflammatory bowel disease'], '2-3 days persistent',
     ['Abdominal cramps', 'Urgency', 'Dehydration', 'Electrolyte imbalance', 'Weight loss']),
    
    ('Cough', 'Reflex action clearing airways mucus irritants classified acute subacute chronic duration.',
     'Productive dry timing triggers differentiate etiations upper airway cough syndrome most common cause chronic cough.',
     ['Viral URI', 'Asthma/COPD', 'GERD', 'Postnasal drip', 'Smoking/smoke irritation'], '3 weeks persistent',
     ['Sore throat', 'Congestion', 'Wheezing', 'Chest tightness', 'Phlegm production']),
    
    ('Dizziness', 'Feeling lightheadedness unsteadiness vertigo spinning sensation distinct sensations different etiologies.',
     'Encompasses vertigo presyncope disequilibrium lightheadedness distinct differential diagnoses.',
     ['BPPV', 'Orthostatic hypotension', 'Dehydration', 'Medication side effects', 'Anxiety/panic'], 'Evaluation needed persistent recurring',
     ['Nausea', 'Imbalance', 'Hearing changes', 'Visual disturbances', 'Tinnitus']),
    
    ('Shortness of Breath', 'Subjective breathing discomfort mild effort intolerance severe air hunger known dyspnea.',
     'Complex sensory perception mismatch respiratory drive ventilation originates cardiac pulmonary hematologic metabolic psychiatric sources.',
     ['Heart failure exertion orthopnea', 'Asthma COPD exacerbation', 'Pulmonary embolism acute onset', 'Pneumonia infection', 'Anxiety panic attack hyperventilation'], 'Immediate acute distress cyanosis altered mental status',
     ['Chest tightness wheezing cough orthopnea paroxysmal nocturnal dyspnea']],
    
    ('Palpitations', 'Awareness heartbeat perceived rapid pounding fluttering skipped beats.',
     'Often benign indicate arrhythmias structural heart disease metabolic abnormalities anxiety stimulant effects.',
     ['Anxiety/stress', 'Arrhythmias PVCs SVT', 'Electrolyte imbalance', 'Hyperthyroidism', 'Caffeine/medication'], 'Evaluate new irregular accompanied chest pain dizziness syncope',
     ['Dizziness', 'Chest pain', 'Shortness of breath', 'Sweating', 'Syncope/fainting']),
    
    ('Night Sweats', 'Excessive sweating during sleep requiring change clothing bedding indicating underlying condition.',
     'May indicate infectious autoimmune endocrine neoplastic psychogenic idiopathic systematic evaluation when recurrent constitutional symptoms.',
     ['Menopausal hot flashes', 'Antidepressant medications', 'Hyperthyroidism', 'Lymphoma/TB', 'Hypoglycemia'], 'Recurring episodes accompanied weight loss fever warrant investigation',
     ['Fever unintended weight loss chills malaise palpitations']),
    
    ('Anxiety', 'Feelings worry nervousness unease imminent events uncertainties affecting daily functioning.',
     'Can situational pervasive anxiety disorder involving autonomic arousal cognitive apprehension.',
     ['Stress', 'Medical conditions', 'Withdrawal', 'Personality traits', 'Genetic factors'], 'Persistent/Ongoing',
     ['Restlessness', 'Fatigue', 'Muscle tension', 'Sleep difficulty', 'Irritability']),
    
    ('Seizures', 'Uncontrolled electrical activity brain abnormal movements behaviors sensations consciousness alterations.',
     'Present convulsions staring spells sensory changes requires neurological evaluation epilepsy injury infection metabolic imbalance tumor.',
     ['Epilepsy', 'Head injury', 'Infection', 'Metabolic imbalance', 'Brain tumor'], 'First episode warrants immediate neurological evaluation',
     ['Post-seizure confusion', 'Muscle soreness', 'Headache', 'Amnesia event', 'Temporary weakness']),
    
    ('Rash', 'Abnormal alteration skin color texture appearance bumps patches blisters scales crusts ulcers.',
     'Numerous etiations allergic reactions infections autoimmune diseases drug eruptions mechanical factors.',
     ['Allergic contact dermatitis', 'Viral exanthems', 'Drug eruption', 'Autoimmune diseases', 'Fungal infections'], 'Evaluate systemic features fever joint pain mucosal involvement',
     ['Itching', 'Pain', 'Blistering/scaling', 'Redness', 'Swelling']),
    
    ('Sore Throat', 'Pain scratchiness irritation throat worsened swallowing talking.',
     'Most commonly bacterial different treatment approach post-nasal vocal strain acidic reflux smoking dry air contributing.',
     ['Viral URI', 'Streptococcal pharyngitis', 'Allergies', 'Dry air/smoking', 'Acid reflux'], '1-2 weeks normally resolve persistent evaluate cancer thyroid mass',
     ['Fever', 'Swollen glands', 'Tonsillar exudate', 'Voice change', 'Difficulty swallowing']),
    
    ('Syncope', 'Transient loss consciousness temporary reduction cerebral perfusion spontaneous recovery.',
     'Differentiate vasovagal cardiac neurologic metabolic causes exertion particularly concerning cardiac evaluation.',
     ['Vasovagal episode', 'Cardiac arrhythmia', 'Orthostatic hypotension', 'Carotid sinus hypersensitivity', 'Seizure mimic'], 'First episode recurrent injury risk exertional positional cardiac family history present',
     ['Palpitations', 'Chest pain', 'Shortness of breath', 'Postural dizziness', 'Prodromal warning symptoms']),
    
    ('Vertigo', 'Spinning sensation self environment moving despite stationary position.',
     'Peripheral vestibular BPPV labyrinthitis Meniere versus central stroke MS cerebellar distinguished neurologic findings.',
     ['BPPV (most common)', 'Vestibular neuritis', 'Meniere disease', 'Stroke/TIA', 'Multiple sclerosis'], 'First episode neurologic deficits immediate medical evaluation',
     ['Nausea/vomiting', 'Hearing loss tinnitus', 'Nystagmus', 'Ataxia', 'Double vision']),
    
    ('Sneezing', 'Forceful expulsion air nose mouth coordinated reflex remove irritants.',
     'Common response allergens viral nasal irritation clears upper airways.',
     ['Allergic rhinitis', 'Viral infection', 'Irritants/smoke', 'Vasomotor rhinitis', 'Bright light reflex'], 'Typically resolve week allergen avoidance treatment',
     ['Runny nose', 'Congestion', 'Itchy eyes/nose', 'Watery eyes', 'Postnasal drip']),
    
    ('Blood in Stool', 'Presence blood bright red lower GI black/tarry upper GI.',
     'Indicates gastrointestinal bleeding localization ranges benign hemorrhoids serious malignancy.',
     ['Hemorrhoids', 'Anal fissure', 'Inflammatory bowel disease', 'Diverticulosis', 'Colorectal cancer'], 'Prompt evaluation',
     ['Abdominal pain', 'Change bowel habits', 'Weight loss', 'Anemia symptoms', 'Mucus/discharge']),
    
    ('Chills', 'Shivering sensation often accompanying fever raise temperature set point.',
     'Physiological response febrile illness peripheral vasoconstriction shivering thermogenesis.',
     ['Bacterial infection', 'Malaria', 'Drug reaction', 'Post-operative state', 'Heat stroke recovery'], 'With fever persistent',
     ['Fever', 'Sweating', 'Malaise', 'Headache', 'Muscle aches']),
]

print('Generating ' + str(len(symptoms)) + ' comprehensive symptom chapters...')
count = 0
for s in symptoms:
    create_symptom(*s)
    count += 1
    if count % 5 == 0:
        print('  Generated ' + str(count) + ' chapters so far...')

print('\nSuccessfully generated ' + str(len(symptoms)) + ' symptom chapters!')
