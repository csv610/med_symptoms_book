#!/usr/bin/env python3
"""Generate ALL symptom chapters for Medical Symptoms book."""

import os

os.makedirs('/Users/csv610/Projects/MyBooks/MedSymptoms/chapters', exist_ok=True)

def write_chapter(name, definition, what_is, causes, days, related):
    """Write a single symptom chapter file in LaTeX format."""
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
    for cause in causes[:5]:
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

# Comprehensive list of common medical symptoms
symptoms_data = [
    # General Systemic Symptoms
    ("Abdominal Pain", "Pain or discomfort anywhere between the chest and groin.", "Can be acute or chronic; location and character provide diagnostic clues.", ["Gastroenteritis", "Appendicitis", "Peptic ulcers", "IBS", "Gallbladder disease"], "3 days", "Nausea, vomiting, bloating"),
    ("Back Pain", "Pain anywhere from neck to lower back.", "Originates from muscles, nerves, bones, or joints in spine.", ["Muscle strain", "Herniated disc", "Degenerative disc disease", "Osteoporosis", "Poor posture"], "7 days", "Stiffness, limited mobility, radiating pain"),
    ("Chest Pain", "Discomfort in chest area, may feel like burning, pressure, or squeezing.", "Requires urgent evaluation - cardiac, pulmonary, GI, or musculoskeletal causes.", ["Angina", "Myocardial infarction", "GERD", "Muscle strain", "Anxiety"], "Immediate", "Shortness of breath, sweating"),
    ("Dizziness", "Feeling of lightheadedness, unsteadiness, or vertigo (spinning).", "Encompasses vertigo, presyncope, disequilibrium, and non-specific lightheadedness.", ["BPPV", "Orthostatic hypotension", "Dehydration", "Medication side effects", "Anxiety"], "3 days", "Nausea, imbalance"),
    ("Fatigue", "Extreme tiredness, lack of energy, not relieved by rest.", "More profound than normal tiredness; may be physical, mental, or both systemic.", ["Anemia", "Depression", "Thyroid disease", "Sleep disorders", "Chronic illness"], "Persistent", "Weakness, concentration difficulties"),
    ("Fever", "Elevation of body temperature above normal range (>38°C).", "Immune response to pathogens; patterns include continuous, intermittent, remittent.", ["Viral infection", "Bacterial infection", "Inflammatory disease", "Medication reaction", "Heat exposure"], "3 days", "Chills, sweating, headache"),
    ("Weight Loss", "Unintentional decrease in body weight over time.", "Can result from metabolic, gastrointestinal, psychological, or malignant processes.", ["Hyperthyroidism", "Diabetes mellitus", "Malignancy", "Depression", "Malabsorption"], "Unintentional", "Appetite changes, fatigue"),
    ("Night Sweats", "Excessive sweating during sleep that soaks clothing or bedding.", "May indicate infection, malignancy, hormonal disorders, or medication side effects.", ["Tuberculosis", "Lymphoma", "Menopause", "Medication side effects", "Endocarditis"], "Recurring", "Fever, chills, weight loss"),
    # Neurological Symptoms
    ("Headache", "Pain anywhere on the head ranging from dull aching to throbbing.", "Classified as primary (migraine, tension-type) or secondary causes.", ["Tension-type migraine", "Sinus headaches", "Dehydration", "Medication overuse", "Eye strain"], "3 days", "Nausea, light sensitivity"),
    ("Confusion", "Altered awareness of surroundings with difficulty thinking clearly.", "Ranges from mild disorientation to severe delirium; often indicates serious condition.", ["Infection/metabolic", "Medication effect", "Head injury", "Stroke", "Seizure"], "Immediate", "Memory loss, agitation"),
    ("Memory Loss", "Inability to recall information or events previously stored.", "Distinction between normal forgetting and pathological impairment.", ["Normal aging", "Alzheimer disease", "Depression", "Medication side effects", "Thyroid disorder"], "Persistent", "Getting lost easily"),
    ("Seizures", "Uncontrolled electrical activity in brain causing abnormal movements or sensations.", "Present as convulsions, staring spells, or sensory changes;", ["Epilepsy", "Head injury", "Infection", "Metabolic imbalance", "Brain tumor"], "Immediate", "Loss of awareness"),
    ("Weakness", "Reduced muscle strength affecting one or more limbs or entire body.", "May be focal or generalized; various neuromuscular or systemic causes.", ["Neurological disorder", "Electrolyte imbalance", "Muscle disease", "Anemia", "Cardiovascular"], "Ongoing", "Fatigue, cramps"),
    # Respiratory Symptoms
    ("Cough", "Reflex action to clear airways of mucus or irritants.", "Dry or productive; classified as acute, subacute, or chronic.", ["Upper respiratory infection", "Asthma", "GERD", "Postnasal drip", "Smoking"], "3 weeks", "Sore throat, congestion"),
    ("Shortness of Breath", "Difficulty breathing or sensation of not getting enough air.", "Acute or chronic; may indicate cardiac, pulmonary, or other issues.", ["Heart failure", "Asthma/COPD", "Pulmonary embolism", "Anemia", "Anxiety"], "Immediate", "Chest pain, palpitations"),
    ("Wheezing", "High-pitched whistling sound during breathing, typically on exhalation.", "Indicates narrowed airways; common in asthma but can have many causes.", ["Asthma", "Bronchitis", "Foreign body aspiration", "Heart failure", "Allergy"], "Persistent", "Chest tightness"),
    # Cardiovascular Symptoms
    ("Palpitations", "Awareness of own heartbeat; may feel rapid, pounding, fluttering, or skipped beats.", "Often benign but can indicate arrhythmias or structural heart disease.", ["Anxiety/stress", "Arrhythmia", "Electrolyte imbalance", "Hyperthyroidism", "Caffeine"], "Evaluate needed", "Dizziness, chest pain"),
    ("Swelling (Edema)", "Abnormal accumulation of fluid in body tissues, typically legs/ankles.", "Can be localized or generalized; cardiovascular, renal, hepatic, or inflammatory causes.", ["Heart failure", "Kidney disease", "Liver disease", "Venous insufficiency", "Medication side effects"], "Progressive", "Skin changes"),
    # Gastrointestinal Symptoms
    ("Nausea and Vomiting", "Nausea is urge to vomit; vomiting is forceful expulsion of stomach contents.", "Frequently occur together; numerous GI, neurological, pregnancy, and medication causes.", ["Viral gastroenteritis", "Pregnancy", "Medication side effects", "GI obstruction", "Migraine"], "2 days", "Abdominal pain, dehydration"),
    ("Diarrhea", "Frequent passage of loose or watery stools.", "Can be acute (infectious) or chronic (functional/inflammatory).", ["Viral/bacterial infection", "Food intolerance", "IBS", "Antibiotic-associated", "IBD"], "2-3 days", "Abdominal cramping"),
    ("Constipation", "Infrequent bowel movements or difficult passage of stools.", "Defined as fewer than 3 spontaneous bowel movements per week.", ["Low fiber diet", "Dehydration", "Medication side effects", "Opioid use", "IBS"], "Persistent", "Abdominal bloating"),
    ("Blood in Stool", "Presence of blood in fecal matter, may appear bright red or black/tarry.", "Requires evaluation to determine source (upper vs lower GI tract).", ["Hemorrhoids", "Anal fissure", "Inflammatory bowel disease", "Diverticulosis", "Colorectal cancer"], "Prompt evaluation", "Abdominal pain, change in bowel habits"),
    # Dermatological Symptoms
    ("Rash", "Abnormal change in skin color or texture, may involve bumps, patches, or blisters.", "Numerous causes including allergic reactions, infections, autoimmune diseases, drug eruptions.", ["Allergic contact dermatitis", "Viral infection", "Drug eruption", "Autoimmune disease", "Fungal infection"], "Evaluating", "Itching, pain"),
    ("Itching (Pruritus)", "Sensation that provokes desire to scratch the skin.", "Can be localized or generalized; various dermatological, systemic, and neurological causes.", ["Dry skin", "Allergies", "Liver disease", "Kidney disease", "Psychological factors"], "Persistent", "Skin damage from scratching"),
    ("Hair Loss", "Excessive shedding or thinning of hair from scalp or body.", "Can be diffuse, patchy, or patterned; includes alopecia areata, telogen effluvium.", ["Stress/anemia", "Medication side effects", "Autoimmune disease", "Hormonal imbalance", "Genetic predisposition"], "Gradual/sudden", "Scalp tenderness"),
    # Musculoskeletal Symptoms
    ("Joint Pain", "Pain or discomfort in one or more joints.", "Associated with arthritis, injury, infection, or systemic diseases.", ["Osteoarthritis", "Rheumatoid arthritis", "Injury/fracture", "Gout", "Infection"], "Evaluated", "Swelling, stiffness"),
    ("Muscle Pain (Myalgia)", "Pain, discomfort, or tenderness in skeletal muscles.", "May be due to exertion, injury, infection, medications, or systemic diseases.", ["Overuse/exercise", "Viral infection", "Statins", "Electrolyte imbalance", "Fibromyalgia"], "Variable", "Muscle weakness"),
    ("Joint Stiffness", "Reduced ease and range of motion in joints, often worse in mornings.", "Common in arthritis, injury, or inflammatory conditions.", ["Osteoarthritis", "Rheumatoid arthritis", "Ankylosing spondylitis", "Injury", "Overuse"], "Morning improvement", "Pain, swelling"),
    # Psychiatric/Emotional Symptoms
    ("Anxiety", "Feelings of unease, worry, fear about uncertain events.", "Can be situational or pervasive; anxiety disorders vary widely.", ["Stress", "Medical conditions", "Substance withdrawal", "Personality traits", "Genetic predisposition"], "Persistent", "Restlessness, fatigue"),
    ("Depression", "Persistent sadness, loss of interest or pleasure lasting weeks or more.", "Major depressive disorder involves multiple symptoms affecting daily function.", ["Chemical imbalance", "Life events/genetics", "Medical conditions", "Medication side effects", "Chronic stress"], "Persistent (2+ weeks)", "Sleep/appetite changes"),
    ("Insomnia", "Difficulty falling asleep, staying asleep, or waking too early.", "Can be transient, acute, or chronic; numerous behavioral and medical contributors.", ["Stress/anxiety", "Environmental factors", "Circadian disruption", "Medical conditions", "Medication effects"], "Evaluation needed", "Daytime fatigue"),
    ("Mood Swings", "Rapid or extreme changes in emotional state differing from typical variations.", "Can indicate bipolar disorder, thyroid dysfunction, PMDD, or other conditions.", ["Bipolar disorder", "Thyroid dysfunction", "PMDD", "Stress", "Medication effects"], "Evaluation needed", "Energy/sleep changes"),
    # Other Common Symptoms
    ("Blurred Vision", "Lack of sharpness or clarity in vision, making objects out of focus.", "Can be refractive error, ocular disease, neurological condition, or systemic-related.", ["Refractive error", "Cataracts", "Glaucoma", "Diabetic retinopathy", "Migraine"], "Evaluate promptly", "Eye pain, floaters"),
    ("Sore Throat", "Pain, scratchiness, or irritation in the throat worsened by swallowing.", "Most commonly viral; bacterial causes require different treatment.", ["Viral URI", "Streptococcal pharyngitis", "Allergies", "Dry air/smoking", "Acid reflux"], "1-2 weeks", "Fever, swollen glands"),
    ("Sneezing", "Forceful expulsion of air through nose/mouth to remove irritants.", "Common response to allergens, viral infections, or nasal irritation.", ["Allergic rhinitis", "Viral infection", "Irritants/smoke", "Vasomotor rhinitis", "Bright light reflex"], "Episodic", "Runny nose, congestion"),
    ("Runny Nose", "Excessive nasal discharge, typically clear/watery but can be thick/colored.", "Response to infection, allergy, or environmental irritants.", ["Viral cold/allergies", "Bacterial infection", "Non-allergic rhinitis", "Temperature/humidity", "Spicy food"], "Variable", "Congestion, sneezing"),
    ("Muscle Cramps", "Sudden, involuntary, painful muscle contractions that do not relax.", "Commonly affect legs and feet; caused by dehydration, electrolyte imbalance, overuse, medications.", ["Dehydration", "Electrolyte imbalance", "Overuse/exercise", "Medication side effects", "Peripheral artery disease"], "Episodic", "Muscle soreness"),
    ("Goosebumps", "Small raised bumps on skin from contraction of tiny muscles at hair follicles.", "Evolutionary response to cold or emotion; harmless and temporary.", ["Cold temperature", "Emotional response", "Autonomic stimulation", "Certain drugs", "Rare medical conditions"], "Transient", "Usually none"),
    ("Tingling/Numbness", "Sensation of pins and needles or loss of sensation in body parts.", "Can be temporary (pressure on nerve) or indicative of neurological conditions.", ["Pressure on nerve", "Vitamin B12 deficiency", "Diabetic neuropathy", "Multiple sclerosis", "Carpal tunnel syndrome"], "Persistent/warning", "Muscle weakness")
]

# Write all chapters
for s in symptoms_data:
    write_chapter(*s)

print(f"Generated {len(symptoms_data)} symptom chapters!")

# Create appendix
appendix_content = r'''\chapter{When to Seek Emergency Medical Care}

Seek immediate emergency attention for:

\begin{itemize}
  \item Chest pain with shortness of breath or radiation to arm/jaw
  \item Sudden weakness or numbness in face, arm, or leg (especially one-sided)
  \item Sudden confusion or trouble speaking/understanding
  \item Sudden vision problems in one or both eyes
  \item Sudden difficulty walking, dizziness, or loss of balance
  \item Sudden severe headache ("worst headache of life")
  \item High fever (>40°C) or fever in infants under 3 months
  \item Difficulty breathing at rest
  \item Unconsciousness or altered consciousness
  \item Seizures
  \item Heavy/uncontrollable bleeding
  \item Serious burns or major trauma
  \item Poisoning or overdose
\end{itemize}

These symptoms may indicate life-threatening conditions including heart attack, stroke, sepsis, pulmonary embolism, meningitis. Do not delay seeking professional medical care.

\clearpage
'''

with open('chapters/appendix_emergency_warnings.tex', 'w') as f:
    f.write(appendix_content)
print("Created appendix: emergency_warnings")

print("\nAll chapters generated successfully!")
