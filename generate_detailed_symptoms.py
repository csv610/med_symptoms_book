#!/usr/bin/env python3
"""Generate detailed symptom chapters for Medical Symptoms book."""

import os

os.makedirs('/Users/csv610/Projects/MyBooks/MedSymptoms/chapters', exist_ok=True)

# Comprehensive symptom data with detailed content
symptoms_data = [
    {
        'name': 'Abdominal Pain',
        'file_base': 'symptom_abdominal_pain',
        'definition': 'Pain or discomfort anywhere between the chest and groin. Abdominal pain is one of the most common reasons people seek medical attention.',
        'what_is': 'Abdominal pain can be acute (sudden onset) or chronic (lasting longer than three months). The location, character, and timing of the pain often provide clues about its cause. It may be referred pain from other organs or arise directly from abdominal structures such as the gastrointestinal tract, liver, kidneys, or reproductive organs.',
        'common_causes': [
            'Gastroenteritis (stomach flu)',
            'Appendicitis',
            'Gastric ulcers',
            'Irritable bowel syndrome (IBS)',
            'Gallbladder disease (cholecystitis, gallstones)',
            'Kidney stones',
            'Pancreatitis',
            'Inflammatory bowel disease (Crohn\\'s disease, ulcerative colitis)',
            'Ovarian cysts or ectopic pregnancy (in women)',
            'Intestinal obstruction'
        ],
        'associated_conditions': [
            ('Fever with rash', 'Measles, scarlet fever, Rocky Mountain spotted fever'),
            ('Fever with cough', 'Pneumonia, influenza, tuberculosis'),
            ('Fever with abdominal pain', 'Appendicitis, cholecystitis, diverticulitis'),
            ('Fever with stiff neck', 'Meningitis, encephalitis')
        ],
        'when_to_seek': [
            'Severe, sudden abdominal pain',
            'Persistent pain lasting more than 24-48 hours',
            'Accompanied by high fever (>38.5°C or 101.3°F)',
            'Blood in stool or black/tarry stools',
            'Jaundice (yellowing of skin or eyes)',
            'Inability to pass gas or have bowel movements',
            'Pain during pregnancy'
        ],
        'related_symptoms': ['Nausea', 'Vomiting', 'Bloating', 'Diarrhea', 'Constipation', 'Loss of appetite'],
        'assessment': [
            'Detailed history of pain onset, location, character, and radiation',
            'Physical examination including abdominal palpation',
            'Laboratory tests: CBC, CMP, amylase, lipase, urinalysis',
            'Imaging: ultrasound, CT scan, X-ray as indicated',
            'Endoscopy for persistent or unexplained symptoms'
        ],
        'management': [
            'Treating the underlying cause',
            'Antibiotics for bacterial infections',
            'Anti-inflammatory medications',
            'Antacids or proton pump inhibitors for acid-related conditions',
            'Surgical intervention when necessary (e.g., appendectomy)',
            'Dietary modifications for IBS and other functional disorders',
            'Pain management with appropriate analgesics'
        ],
        'pearls': [
            'Children with right lower quadrant pain should be evaluated promptly for appendicitis',
            'Older adults may present with atypical symptoms of serious abdominal pathology',
            'Always consider non-abdominal causes of epigastric pain, such as cardiac ischemia',
            'Pregnant patients require special consideration for both diagnosis and imaging modalities'
        ]
    },
    {
        'name': 'Back Pain',
        'file_base': 'symptom_back_pain',
        'definition': 'Pain anywhere in the back, from the neck to the lower back. Back pain is extremely common and affects millions of people worldwide, being a leading cause of disability and missed work.',
        'what_is': 'Back pain can originate from muscles, nerves, bones, joints, or other structures in the spine. It is typically classified as acute (less than six weeks), subacute (six to twelve weeks), or chronic (more than twelve weeks). Most episodes of low back pain are mechanical in origin, meaning they result from strain, sprain, or degeneration rather than a specific disease process.',
        'common_causes': [
            'Muscle or ligament strain',
            'Herniated or bulging disc',
            'Degenerative disc disease',
            'Spinal stenosis',
            'Osteoarthritis',
            'Scoliosis',
            'Osteoporosis with fracture',
            'Poor posture',
            'Heavy lifting with improper technique',
            'Sitting for prolonged periods'
        ],
        'associated_conditions': [
            ('Fever with back pain', 'Kidney infection, spinal abscess'),
            ('Back pain with numbness in legs', 'Cauda equina syndrome – emergency'),
            ('Back pain after trauma', 'Fracture, spinal injury'),
            ('Unexplained weight loss with back pain', 'Malignancy, infection')
        ],
        'when_to_seek': [
            'Severe pain that does not improve with rest',
            'Loss of bladder or bowel control (cauda equina syndrome)',
            'Numbness in the groin or inner thighs',
            'Fever accompanied by back pain',
            'History of cancer with new back pain',
            'Progressive weakness in the legs',
            'Unexplained weight loss with persistent back pain'
        ],
        'related_symptoms': ['Stiffness', 'Limited range of motion', 'Radiating pain to legs or arms', 'Numbness or tingling', 'Muscle spasms'],
        'assessment': [
            'Clinical history focusing on onset, duration, and aggravating factors',
            'Physical examination including neurological assessment',
            'X-rays if fracture or structural abnormality suspected',
            'MRI for nerve compression or soft tissue evaluation',
            'CT scan for bony detail when MRI is contraindicated',
            'Bone density testing in postmenopausal women or older men'
        ],
        'management': [
            'Rest and activity modification during acute phase',
            'NSAIDs for pain and inflammation',
            'Physical therapy and exercise program',
            'Heat or cold therapy',
            'Epidural steroid injections for radicular pain',
            'Surgical decompression or fusion for severe cases',
            'Cognitive behavioral therapy for chronic pain management'
        ],
        'pearls': [
            'Most cases of uncomplicated low back pain resolve without specific treatment within 4-6 weeks',
            'Avoid prolonged bed rest; maintain activity as tolerated',
            'Red flags include neurological deficits, cauda equina symptoms, and systemic signs of malignancy or infection',
            'Prevention through core strengthening, ergonomic modifications, and proper body mechanics'
        ]
    },
    {
        'name': 'Chest Pain',
        'file_base': 'symptom_chest_pain',
        'definition': 'Discomfort or pain anywhere in the chest area. Chest pain can range from mild to severe and may feel like burning, pressure, squeezing, sharpness, or heaviness. It is a critical symptom requiring careful evaluation due to potentially life-threatening causes.',
        'what_is': 'Chest pain has numerous potential causes spanning cardiac, pulmonary, gastrointestinal, musculoskeletal, and psychological systems. Cardiac causes include myocardial infarction, angina, pericarditis, and aortic dissection. Pulmonary causes include pulmonary embolism, pneumothorax, and pneumonia. Gastrointestinal causes include gastroesophageal reflux disease (GERD), esophageal spasm, and peptic ulcer disease. Musculoskeletal causes include costochondritis and muscle strain. Anxiety and panic disorders also commonly manifest as chest discomfort.',
        'common_causes': [
            'Coronary artery disease / Angina pectoris',
            'Myocardial infarction (heart attack)',
            'Pericarditis',
            'Aortic dissection',
            'Pulmonary embolism',
            'Pneumonia',
            'Pneumothorax',
            'Gastroesophageal reflux disease (GERD)',
            'Esophageal spasm or rupture',
            'Costochondritis (inflammation of rib cartilage)'
        ],
        'associated_conditions': [
            ('Chest pain with shortness of breath', 'Pulmonary embolism, heart failure, pneumothorax'),
            ('Chest pain with sweating or nausea', 'Myocardial infarction'),
            ('Chest pain with cough', 'Pneumonia, pulmonary embolism'),
            ('Chest pain worsened by breathing', 'Pleurisy, pleuritis')
        ],
        'when_to_seek': [
            'Immediate emergency care for: crushing, squeezing, or pressure-like chest pain lasting more than a few minutes, especially with shortness of breath, sweating, nausea, or pain radiating to arm, neck, jaw, or back',
            'Severe tearing chest pain suggesting aortic dissection',
            'Sudden sharp pain with difficulty breathing suggesting pneumothorax',
            'Chest pain with fainting or near-fainting',
            'New or worsening chest pain in individuals with known cardiovascular disease'
        ],
        'related_symptoms': ['Shortness of breath', 'Sweating', 'Nausea', 'Dizziness', 'Palpitations', 'Radiating pain'],
        'assessment': [
            'Immediate assessment of vital signs and clinical stability',
            'Electrocardiogram (ECG/EKG) – urgent in suspected cardiac causes',
            'Cardiac biomarkers (troponin) for myocardial infarction',
            'Chest X-ray to evaluate lung fields and mediastinum',
            'CT angiography for suspected pulmonary embolism or aortic dissection',
            'D-dimer test in appropriate clinical settings',
            'Esophageal pH monitoring for suspected GERD',
            'Stress testing for unstable angina evaluation'
        ],
        'management': [
            'Emergency stabilization of life-threatening conditions',
            'Aspirin and nitroglycerin for suspected cardiac chest pain',
            'Anticoagulation for pulmonary embolism',
            'Proton pump inhibitors for GERD',
            'Beta-blockers and calcium channel blockers for vasospastic angina',
            'Muscle relaxants and NSAIDs for musculoskeletal pain',
            'Anxiolytics and cognitive behavioral therapy for anxiety-related chest pain',
            'Surgical repair when indicated (e.g., aortic dissection, pneumothorax)'
        ],
        'pearls': [
            'Never dismiss chest pain as simply "acid reflux" without ruling out cardiac causes first',
            'Women may present with atypical symptoms of cardiac ischemia (fatigue, nausea, back/jaw pain rather than classic chest pain)',
            'Young patients with benign-appearing chest pain should still be carefully evaluated – costochondritis and anxiety are common but diagnoses of exclusion',
            'Remember to ask about recent travel, oral contraceptive use, or smoking for pulmonary embolism risk assessment'
        ]
    },
    {
        'name': 'Cough',
        'file_base': 'symptom_cough',
        'definition': 'A sudden, often repetitive, hollow-sounding exchange of air that clears the airways. Coughing is a reflex action designed to clear the throat or air passages of mucus or irritants. It is one of the most common presenting complaints in clinical practice.',
        'what_is': 'Coughs are classified as acute (less than three weeks), subacute (three to eight weeks), and chronic (more than eight weeks). They can be dry (non-productive) or wet productive with sputum. The reflex involves irritation of cough receptors in the airways, sending signals via the vagus nerve to the cough center in the brainstem, which then coordinates the expiratory effort.',
        'common_causes': [
            'Upper respiratory infections (common cold, sinusitis)',
            'Acute bronchitis',
            'Asthma',
            'Postnasal drip (upper airway cough syndrome)',
            'Gastroesophageal reflux disease (GERD)',
            'Chronic obstructive pulmonary disease (COPD)',
            'Pneumonia',
            'Medication-induced (ACE inhibitors)',
            'Smoking-related cough',
            'Lung cancer (especially in smokers)'
        ],
        'associated_conditions': [
            ('Cough with wheezing', 'Asthma, COPD'),
            ('Cough with fever and purulent sputum', 'Pneumonia, bronchiectasis'),
            ('Cough with hemoptysis', 'Tuberculosis, lung cancer, pulmonary embolism'),
            ('Cough with dysphagia', 'Esophageal disorders, tracheoesophageal fistula')
        ],
        'when_to_seek': [
            'Cough lasting more than 8 weeks (chronic cough)',
            'Coughing up blood (hemoptysis)',
            'Shortness of breath or wheezing with cough',
            'High fever with productive cough',
            'Unintentional weight loss with chronic cough',
            'Cough interfering significantly with sleep or daily activities',
            'Wheezing or stridor with cough'
        ],
        'related_symptoms': ['Sore throat', 'Runny nose', 'Chest tightness', 'Shortness of breath', 'Fatigue', 'Sputum production'],
        'assessment': [
            'Detailed history on cough characteristics (dry/wet, timing, triggers)',
            'Physical examination including lung auscultation',
            'Chest X-ray to evaluate lungs and mediastinum',
            'Spirometry/pulmonary function tests for asthma or COPD',
            'Sinus CT if chronic rhinosinusitis suspected',
            '24-hour pH monitoring for GERD-related cough',
            'Allergy testing if allergic component suspected',
            'Bronchoscopy when indicated (persistent unexplained cough)'
        ],
        'management': [
            'Treating the underlying cause',
            'Antibiotics for bacterial infections when indicated',
            'Inhaled corticosteroids and bronchodilators for asthma',
            'Lifestyle modifications for GERD (elevate head of bed, avoid trigger foods)',
            'Cough suppressants (dextromethorphan) for symptomatic relief',
            'Expectorants (guaifenesin) for productive cough',
            'Leukotriene receptor antagonists for allergic cough',
            'Switching from ACE inhibitors to alternative antihypertensives if medication-induced',
            'Speech therapy and voice training for chronic cough syndrome'
        ],
        'pearls': [
            'The post-infectious cough may persist for several weeks after viral resolution and is usually self-limiting',
            'ACE inhibitor–induced cough occurs in approximately 5-20% of patients and resolves within weeks of discontinuation',
            'Three common causes account for >85% of chronic cough: upper airway cough syndrome, asthma, and GERD',
            'Children with chronic cough should be evaluated for foreign body aspiration, especially if onset was sudden'
        ]
    },
    {
        'name': 'Dizziness',
        'file_base': 'symptom_dizziness',
        'definition': 'A feeling of lightheadedness, unsteadiness, or vertigo (spinning sensation). Dizziness is a common symptom with many possible causes ranging from benign to life-threatening. Patients describe dizziness in multiple distinct ways that require careful differentiation.',
        'what_is': 'Dizziness encompasses several distinct sensations that require separate consideration: vertigo (a spinning or rotational sensation), presyncope (faintness or impending syncope), disequilibrium (unsteady balance), and non-specific lightheadedness. Each category has different potential etiologies and diagnostic approaches. Vertigo typically indicates peripheral vestibular or central nervous system dysfunction, while presyncope suggests cardiovascular causes.',
        'common_causes': [
            'Benign paroxysmal positional vertigo (BPPV)',
            'Meniere\\'s disease',
            'Vestibular neuritis/labyrinthitis',
            'Orthostatic hypotension',
            'Arrhythmias',
            'Dehydration',
            'Anemia',
            'Medication side effects',
            'Anxiety disorders',
            'Transient ischemic attack (TIA) or stroke'
        ],
        'associated_conditions': [
            ('Dizziness with hearing loss or tinnitus', 'Meniere\\'s disease, acoustic neuroma'),
            ('Dizziness with focal neurologic deficits', 'Stroke, TIA'),
            ('Dizziness upon standing', 'Orthostatic hypotension, dehydration'),
            ('Dizziness with palpitations', 'Arrhythmia, heart block')
        ],
        'when_to_seek': [
            'Sudden onset severe vertigo with headache or neurologic symptoms (possible stroke)',
            'Dizziness associated with chest pain, shortness of breath, or palpitations (cardiac cause)',
            'Recurrent falls or near-falls',
            'Dizziness accompanied by speech difficulties, facial droop, or limb weakness',
            'Head injury followed by dizziness',
            'Progressive or persistent dizziness affecting daily activities'
        ],
        'related_symptoms': ['Nausea', 'Vomiting', 'Balance problems', 'Hearing changes', 'Visual disturbances', 'Headache'],
        'assessment': [
            'Precise characterization of dizziness type (vertigo vs. lightheadedness vs. imbalance)',
            'Vital signs including orthostatic measurements',
            'Neurological examination including cranial nerves, coordination, and gait',
            'Dix-Hallpike maneuver to diagnose BPPV',
            |'Romberg test and finger-nose-finger testing',
            'ECG/cardiac monitoring if arrhythmia suspected',
            'Audiometry if hearing impairment noted',
            'MRI brain if central cause suspected'
        ],
        'management': [
            'Canalith repositioning maneuvers (Epley maneuver) for BPPV',
            'Vestibular rehabilitation therapy for vestibular dysfunction',
            'Fluid replacement and electrolyte correction for dehydration',
            'Medication adjustment if drug-induced',
            'Treatment of underlying cardiovascular conditions',
            'Antivertigo medications (meclizine, promethazine) for acute symptom relief',
            'Cognitive behavioral therapy for anxiety-related dizziness',
            'Fall prevention strategies in elderly patients'
        ],
        'pearls': [
            'BPPV is the most common cause of vertigo and is often precipitated by head position changes',
            'The HINTS exam (Head Impulse, Nystagmus, Test of Skew) helps differentiate central from peripheral vertigo in acute continuous vertigo',
            'Orthostatic hypotension is common in elderly patients taking multiple medications and should be checked with seated, standing, and supine measurements',
            'Psychogenic dizziness often presents as persistent non-specific lightheadedness exacerbated by stress and improved with relaxation'
        ]
    }
]

template = r"""\chapter{{{name}}}

\section*{Definition}
{definition}

\section*{What Is This Symptom?}
{what_is}

\section*{Common Causes}
\begin{{itemize}}
{cause_list}
\end{{itemize}}

\section*{Associated Conditions}
{assoc_list}

\section*{When to Seek Medical Attention}
Seek immediate medical care if:
\begin{{itemize}}
{seek_list}
\end{{itemize}}

\section*{Related Symptoms}
Often occurs with:
\begin{{itemize}}
{rel_list}
\end{{itemize}}

\section*{Assessment and Evaluation}
The evaluation includes:
\begin{{enumerate}}
{eval_list}
\end{{enumerate}}

\section*{Management}
Treatment approaches include:
\begin{{itemize}}
{mgmt_list}
\end{{itemize}}

\section*{Clinical Pearls}
\begin{{pearlbox}}
{pearl_1}
\end{{pearlbox}}

{pearl_2}\clearpage
"""

def format_cause_list(causes):
    return '\n'.join(f'  \\item {c}' for c in causes)

def format_assoc_list(assoc):
    lines = []
    for cond, desc in assoc:
        lines.append(f'  \\item {{\\textbf{{{cond}}}}}: {desc}')
    return '\n'.join(lines)

def format_seeker_list(seek):
    return '\n'.join(f'  \\item {s}' for s in seek)

def format_rel_list(rel):
    return ', '.join(rel)

def format_eval_list(eval_items):
    return '\n'.join(f'  \\item {e}' for e in eval_items)

def format_mgmt_list(mgmt):
    return '\n'.join(f'  \\item {m}' for m in mgmt)

for s in symptoms_data:
    # Build assessment list with corrected formatting
    eval_assessment = [
        'Detailed history on symptom characteristics (onset, duration, triggers, relieving factors)',
        'Physical examination focused on relevant systems',
        'Targeted laboratory testing as indicated by clinical presentation',
        'Imaging studies when structural abnormalities are suspected',
        'Specialized testing (vestibular testing, cardiology workup, etc.) as needed'
    ]
    
    content = template.format(
        name=s['name'],
        definition=s['definition'],
        what_is=s['what_is'],
        cause_list=format_cause_list(s['common_causes']),
        assoc_list=format_assoc_list(s['associated_conditions']),
        seek_list=format_seeker_list(s['when_to_seek']),
        rel_list=format_rel_list(s['related_symptoms']),
        eval_list=format_eval_list(eval_assessment),
        mgmt_list=format_mgmt_list(s['management']),
        pearl_1=f"\\textbf{\\textit{'Clinical Pearl:'}} {s['pearls'][0]}",
        pearl_2=f"\\begin{{pearlbox}}\\textit{{\\textbf{{Note:}}}} {s['pearls'][1]}\\end{{pearlbox}}"
    )
    
    filename = f"/Users/csv610/Projects/MyBooks/MedSymptoms/chapters/{s['file_base']}.tex"
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created: {filename}")

print(f"\nGenerated {len(symptoms_data)} detailed symptom chapters")
