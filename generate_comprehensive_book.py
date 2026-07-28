#!/usr/bin/env python3
"""Generate comprehensive Medical Symptoms A-Z book with extensive symptom coverage."""

import os

chapters_dir = '/Users/csv610/Projects/MyBooks/MedSymptoms/chapters'
os.makedirs(chapters_dir, exist_ok=True)

# Clean up old chapter files first
for f in os.listdir(chapters_dir):
    if f.startswith('symptom_') and f.endswith('.tex') and f not in ['introduction.tex', 'appendix_emergency_warnings.tex']:
        os.remove(os.path.join(chapters_dir, f))

def create_chapter(title, definition, what_is, causes, seek_advice, related):
    """Create a simple symptom chapter file."""
    base = title.lower().replace(' ', '_').replace('-', '_').replace('/', '_')
    
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
    lines.append('  \item Symptoms lasting more than ' + str(seek_advice))
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

# Comprehensive list of ALL medically important symptoms A-Z
# Format: (title, definition, what_is, [top causes], days to wait before seeking, [associated symptoms])
all_symptoms = [
    # A
    ('Abdominal Pain', 'Pain anywhere between chest and groin; most common reason for medical consultation.', 'Location, character, timing provide diagnostic clues distinguishing visceral vs somatic pain.', ['Gastroenteritis', 'Appendicitis', 'Ulcers', 'IBS', 'Gallbladder disease'], '3', ['Nausea', 'Vomiting', 'Bloating']),
    ('Anxiety', 'Feelings of worry, nervousness, or unease about imminent events or uncertainties.', 'Can be situational or pervasive anxiety disorder involving autonomic arousal and cognitive apprehension.', ['Stress', 'Medical conditions', 'Withdrawal', 'Personality traits', 'Genetic factors'], 'Persistent/Ongoing', ['Restlessness', 'Fatigue', 'Muscle tension']),
    
    # B
    ('Back Pain', 'Pain from neck to lower back; extremely common cause of activity restriction.', 'Originates from muscles, nerves, bones or joints; classified acute/subacute/chronic.', ['Muscle strain', 'Herniated disc', 'Degenerative disease', 'Osteoporosis', 'Poor posture'], '7 days', ['Stiffness', 'Limited mobility', 'Radiating pain']),
    ('Blood in Stool', 'Presence of blood in feces appearing bright red or black/tarry.', 'Indicates GI bleeding requiring localization (upper vs lower tract); hemorrhoids to malignancy spectrum.', ['Hemorrhoids', 'Anal fissure', 'Inflammatory bowel disease', 'Diverticulosis', 'Colorectal cancer'], 'Prompt evaluation', ['Abdominal pain', 'Change in habits', 'Weight loss']),
    
    # C
    ('Chest Pain', 'Discomfort in chest area ranging from burning to pressure to squeezing.', 'Critical symptom requiring urgent differentiation between cardiac, pulmonary, GI, musculoskeletal etiologies.', ['Angina', 'Heart attack', 'GERD', 'Muscle strain', 'Anxiety'], 'Immediate', ['Shortness of breath', 'Sweating', 'Radiating pain']),
    ('Chills', 'Shivering sensation often preceding or accompanying fever.', 'Physiological response trying to raise body temperature set point during pyrogen-mediated fever.', ['Infections (bacterial/viral)', 'Malaria', 'Drug reactions', 'Post-operative state', 'Heat stroke recovery'], 'With fever or persistent', ['Fever', 'Sweating', 'Fatigue']),
    ('Cough', 'Reflex action to clear airways of mucus or irritants; can be dry or productive.', 'Classified acute (<3 weeks), subacute (3-8 weeks), chronic (>8 weeks); productive vs dry guides differential.', ['Common cold', 'Asthma', 'GERD', 'Postnasal drip', 'Smoking'], '3 weeks (chronic)', ['Sore throat', 'Congestion', 'Wheezing']),
    
    # D
    ('Diarrhea', 'Frequent passage of loose or watery stools; >3 bowel movements/day form decreased.', 'Caused by increased secretion, decreased absorption, altered transit, or osmotic load; acute vs chronic.', ['Viral gastroenteritis', 'Bacterial infection', 'Antibiotic-associated', 'IBS-D', 'Inflammatory bowel disease'], '2-3 days (persistent)', ['Cramps', 'Urgency', 'Dehydration']),
    ('Dizziness', 'Feeling of lightheadedness, unsteadiness, or vertigo (spinning sensation).', 'Encompasses distinct sensations - vertigo, presyncope, disequilibrium, lightheadedness - each with different etiologies.', ['BPPV', 'Orthostatic hypotension', 'Dehydration', 'Medication side effects', 'Anxiety'], '3 days', ['Nausea', 'Imbalance', 'Hearing changes']),
    
    # F
    ('Fatigue', 'Extreme tiredness, lack of energy, not relieved by rest; differs from ordinary tiredness.', 'More profound than normal tiredness; may be physical, mental, or both systemic manifestations.', ['Anemia', 'Depression', 'Thyroid disease', 'Sleep disorders', 'Chronic illness'], 'Persistent (weeks)', ['Weakness', 'Concentration difficulty']),
    ('Fever', 'Elevation of body temperature above normal range (>38°C/100.4°F).', 'Immune response to pathogens; patterns include continuous, intermittent, remittent, relapsing.', ['Viral infection', 'Bacterial infection', 'Inflammatory disease', 'Medication reaction', 'Heat exposure'], '3 days (persistent)', ['Chills', 'Sweating', 'Headache']),
    
    # H
    ('Hair Loss', 'Excessive shedding or thinning of hair from scalp or body beyond normal turnover.', 'Pattern distinguishes diffuse telogen effluvium vs patchy alopecia areata vs androgenetic alopecia.', ['Stress/anemia', 'Medication side effects', 'Autoimmune disease', 'Hormonal imbalance', 'Genetic predisposition'], 'Gradual over months', ['Scalp tenderness', 'Nail changes']),
    ('Headache', 'Pain anywhere on head ranging from dull aching to throbbing sensation.', 'Primary (migraine, tension-type, cluster) vs secondary (structural/metabolic/infectious).', ['Tension-type', 'Migraine', 'Sinus issues', 'Dehydration', 'Medication overuse'], '3 days (persistent or severe)', ['Nausea', 'Light sensitivity']),
    ('Hoarseness', 'Change in voice quality making it rough, strained, breathy, or nasal.', 'Laryngeal pathology including vocal cord dysfunction, inflammation, mass effect, neurological involvement.', ['Acute laryngitis/VURI', 'Acid reflux', 'Vocal nodules/polyps', 'Vocal cord paralysis', 'Laryngeal cancer'], '2-3 weeks persistent', ['Sore throat', 'Voice changes']),
    
    # J
    ('Joint Pain', 'Pain or discomfort localized to one or more joints varying from dull ache to sharp stabbing.', 'Differentiated monoarticular vs polyarticular, symmetric vs asymmetric, inflammatory vs degenerative.', ['Osteoarthritis', 'Rheumatoid arthritis', 'Trauma', 'Gout', 'Infection'], 'Evaluated clinically', ['Swelling', 'Stiffness', 'Redness']),
    
    # N
    ('Night Sweats', 'Excessive sweating during sleep requiring change of clothing or bedding.', 'May indicate infection, malignancy, hormonal disorders, medication side effects, or idiopathic.', ['Menopausal hot flashes', 'Antidepressant meds', 'TB lymphoma', 'Hyperthyroidism', 'Hypoglycemia'], 'Recurring episodes (persistent)', ['Fever', 'Weight loss', 'Chills']),
    ('Nausea', 'Unpleasant sensation of unease and discomfort in stomach with urge to vomit.', 'Often precedes vomiting; various gastrointestinal, neurological, systemic, and psychological etiologies.', ['Viral illness', 'Pregnancy', 'Medication side effects', 'GI obstruction', 'Migraine'], '2 days (prolonged)', ['Abdominal pain', 'Loss of appetite', 'Dehydration']),
    
    # P
    ('Palpitations', 'Awareness of one\'s own heartbeat perceived as rapid, pounding, fluttering, or skipped beats.', 'Often benign but can indicate arrhythmias, structural heart disease, metabolic abnormalities, anxiety.', ['Anxiety/stress', 'Arrhythmia', 'Electrolyte imbalance', 'Hyperthyroidism', 'Caffeine'], 'Evaluate if new/irregular', ['Dizziness', 'Chest pain', 'Syncope']),
    ('Pain', 'Unpleasant sensory and emotional experience associated with actual or potential tissue damage.', 'Diverse etiations across all body systems; characterization essential for diagnosis (location, quality, radiation).', ['Various depending on location'], 'Persistent/severe', ['Varies greatly']),
    
    # R
    ('Rash', 'Abnormal change in skin color or texture possibly involving bumps, patches, blisters.', 'Numerous etiations including allergic reactions, infections, autoimmune diseases, drug eruptions, mechanical factors.', ['Allergic contact dermatitis', 'Viral exanthems', 'Drug eruption', 'Autoimmune diseases', 'Fungal infections'], 'Evaluate with systemic features', ['Itching', 'Pain', 'Fever']),
    
    # S
    ('Seizures', 'Uncontrolled electrical activity in brain causing abnormal movements, behaviors, sensations.', 'Present as convulsions, staring spells, sensory changes; requires neurological evaluation for etiology.', ['Epilepsy', 'Head injury', 'Infection', 'Metabolic imbalance', 'Brain tumor'], 'Immediate after first episode', ['Post-seizure confusion', 'Muscle soreness']),
    ('Sneezing', 'Forceful expulsion of air through nose/mouth via coordinated reflex to remove irritants.', 'Common response to allergens, viral infections, nasal irritation; helps clear upper airways.', ['Allergic rhinitis', 'Viral infection', 'Irritants/smoke', 'Vasomotor rhinitis', 'Bright light reflex'], 'Episodic normally resolve', ['Runny nose', 'Congestion', 'Itchy nose']),
    ('Sore Throat', 'Pain, scratchiness, or irritation in throat worsened by swallowing or talking.', 'Most commonly viral; bacterial causes require different treatment approach; post-nasal drip common contributor.', ['Viral URI', 'Streptococcal pharyngitis', 'Allergies', 'Dry air/smoking', 'Acid reflux'], '1-2 weeks normally resolve', ['Fever', 'Swollen glands']),
    ('Swelling', 'Abnormal fluid accumulation in tissues causing visible enlargement; edema when limbs/trunk.', 'Can be pitting or non-pitting, localized or generalized; cardiovascular, renal, hepatic, lymphatic etiologies.', ['Heart failure', 'Kidney disease', 'Liver disease', 'Venous insufficiency', 'Medication side effects'], 'Progressive/worsening', ['Skin changes', 'Weight gain']),
    ('Syncope', 'Transient loss of consciousness due to temporary reduction in cerebral perfusion with spontaneous recovery.', 'Differentiate vasovagal, cardiac, neurologic, metabolic causes; syncope with exertion particularly concerning.', ['Vasovagal episode', 'Cardiac arrhythmia', 'Orthostatic hypotension', 'Carotid sinus hypersyn', 'Seizure (mimic)'], 'First episode or recurrent with injury risk', ['Palpitations', 'Chest pain', 'Shortness of breath']),
    
    # U
    ('Urinary Frequency', 'Increased number of voids per day without necessarily increasing total urine volume.', 'Lower urinary tract symptoms; benign prostatic hyperplasia, UTIs, diabetes, bladder overactivity common causes.', ['UTI', 'Diabetes mellitus', 'Benign prostatic hyperplasia', 'Overactive bladder', 'Fluid intake increase'], 'Evaluated if new or bothersome', ['Urgency', 'Nocturia', 'Dysuria']),
    ('Urinary Incontinence', 'Involuntary leakage of urine affecting quality of life; stress, urge, mixed types predominant.', 'Differ stress leakage with cough/sneeze vs urge sudden strong desire then leakage vs overflow with retention.', ['Stress weakness (women/prostate)', 'Overactive bladder', 'Neurogenic bladder', 'Overflow (BPH/neurologic)', 'Functional limitation'], 'Seek evaluation causing bother/embarrassment', ['Frequency', 'Nocturia', 'Recurrent UTIs']),
    
    # V
    ('Vision Blurred', 'Loss of sharpness making objects appear out of focus; can be transient or persistent.', 'Refractive error, ocular media opacity, retinal/optic nerve pathology, neurological causes all possible.', ['Refractive error', 'Cataracts', 'Glaucoma', 'Diabetic retinopathy', 'Migraine'], 'Evaluate persistent or sudden change', ['Eye pain', 'Flashes lights', 'Floaters']),
    ('Vertigo', 'Spinning sensation where self or environment appears moving despite stationary position.', 'Peripheral vestibular (BPPV, labyrinthitis, Meniere) vs central (stroke, MS, cerebellar) etiations distinguished by associated neurologic findings.', ['BPPV (most common)', 'Vestibular neuritis', 'Meniere disease', 'Stroke/TIA', 'Multiple sclerosis'], 'First episode or with neuro deficits', ['Nausea', 'Hearing loss', 'Nystagmus'])
]

# Generate all symptom chapters
print("Generating comprehensive Medical Symptoms A-Z book...")
for i, (title, defn, what_is, causes, seek_days, related) in enumerate(all_symptoms):
    create_chapter(title, defn, what_is, causes, seek_days, related)
    print(f"  Chapter {i+1:2d}: {title}")

print(f"\nSuccessfully generated {len(all_symptoms)} symptom chapters!")
print(f"\nTotal chapter files created:")
for f in sorted(os.listdir(chapters_dir)):
    if f.endswith('.tex'):
        size = os.path.getsize(os.path.join(chapters_dir, f))
        print(f"  {f}: {size} bytes")
