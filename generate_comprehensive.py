#!/usr/bin/env python3
"""Generate comprehensive Medical Symptoms book with extensive symptom coverage."""

import os
import re

os.makedirs('/Users/csv610/Projects/MyBooks/MedSymptoms/chapters', exist_ok=True)

def create_detailed_symptom(name, category, defn, what_is, pathoph, clinical_feat, diff_diag, causes, serious_causes, assoc_symptoms, when_to_seek, workup, management, pearls, refs):
    """Create a detailed symptom chapter with full clinical content."""
    
    # Clean filename
    base = name.lower().replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '').replace('-', '_')
    
    lines = []
    lines.append(r'\chapter{' + name + r'}')
    lines.append('')
    
    if category:
        lines.append(r'\textbf{' + category + r'}\par')
        lines.append('')
    
    sections = {
        'Definition': defn,
        'What Is This Symptom?': what_is,
        'Pathophysiology': pathoph,
        'Clinical Features': clinical_feat,
        'Differential Diagnosis': diff_diag,
        'Common Causes': causes[0] if isinstance(causes, list) else causes,
        'Serious/Emergency Causes': serious_causes[0] if isinstance(serious_causes, list) else serious_causes,
        'Associated Symptoms': ', '.join(assoc_symptoms[:5]) if isinstance(assoc_symptoms, list) else assoc_symptoms,
        'When to Seek Immediate Medical Attention': when_to_seek,
        'Diagnostic Approach': workup,
        'Workup': workup,
        'Management Principles': management,
        'Clinical Pearls': pearls,
        'References': refs,
    }
    
    section_order = [
        'Definition', 'What Is This Symptom?', 'Pathophysiology', 'Clinical Features', 
        'Differential Diagnosis', 'Common Causes', 'Serious/Emergency Causes', 
        'Associated Symptoms', 'When to Seek Immediate Medical Attention', 
        'Diagnostic Approach', 'Workup', 'Management Principles', 'Clinical Pearls', 'References'
    ]
    
    for section_name in section_order:
        if section_name in sections:
            content = sections[section_name]
            if isinstance(content, list):
                content = '\n'.join(['  \\item ' + c for c in content[:8]])
            lines.append('\\section*{' + section_name + r'}')
            lines.append(content)
        lines.append('')
    
    # Add clinical pearl as boxed note if available
    if pearls and isinstance(pearsels, str):
        lines.append('\\begin{pearlbox}')
        lines.append(pearsls)
        lines.append('\\end{pearlbox}')
        lines.append('')
    
    lines.append('\\clearpage')
    lines.append('')
    
    content = '\n'.join(lines)
    filepath = '/Users/csv610/Projects/MyBooks/MedSymptoms/chapters/symptom_' + base + '.tex'
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath

# Use simplified content generation to avoid escaping complexity
symptom_sets = {
    'Fever': ('General Systemic', 'Elevation of body temperature above normal range (>38C or 100.4F), representing immune system response.', 'Fever is a regulated increase in body temperature mediated by pyrogens acting on the hypothalamic thermoregulatory center.', 'Pyrogens (exogenous from pathogens, endogenous from cytokines like IL-1, IL-6, TNF-alpha) reset hypothalamic set point; vasodilation in skin increases heat loss; shivering generates heat until new set point reached.', 'Acute onset suggests infection/inflammation; pattern may differentiate (continuous in typhoid, intermittent in malaria, relapsing in Hodgkin\'s); associated symptoms localize etiology.', 'Infectious (viral, bacterial, fungal, parasitic), Inflammatory/autoimmune (RA, SLE), Malignancy (lymphoma, renal cell carcinoma), Drug fever, Thyroid storm, Heat stroke, Embolic events.', 'Viral URI/flu, Bacterial pneumonia, UTI, Appendicitis, Influenza, Gastroenteritis', 'Sepsis, Meningitis, Endocarditis, Pyelonephritis, Abdominal abscess, Osteomyelitis', 'Chills, headache, myalgias, anorexia, dehydration', 'High fever (>40C/Celsius), prolonged fever (>3 days), immunocompromised state, neurologic symptoms, rash non-blanching', 'CBC with diff, CMP, blood cultures, urinalysis, CXR as indicated; consider inflammatory markers (ESR, CRP), blood cultures prior to antibiotics in febrile neutropenia', 'Antipyretics (acetaminophen, NSAIDs), hydration, treat underlying cause; consider admission for high-risk patients', 'Always determine etiology before treating fever alone; fever in infants under 3 months requires complete septic workup; antipyretics improve comfort but do not alter disease course.', '\\begin{enumerate}\n  \\item Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett\\'s Principles and Practice of Infectious Diseases.\n  \\item CDC Guidelines for Fever Management.\n  \\item UpToDate.com: Evaluation of fever in adults.\n\\end{enumerate}'},
    
    'Headache': ('Neurological', 'Pain perceived anywhere in the head region among most common human experiences encountered clinically.', 'Primary headaches lack identifiable structural cause; secondary headaches attributable to another condition.', 'Diverse mechanisms: vascular dilation/trigeminovascular system activation (migraine), muscle tension/pericranial myofascial pain (tension-type), cranial nerve irritation/vascular compression (cluster).', 'Character location timing triggers prodrome aura postdrome associated features photophobia phonophobia vertigo nausea vomiting neck stiffness focal neurologic deficits help categorize.', 'Migraine without aura, Migraine with aura, Tension-type headache, Cluster headache, Medication-overuse headache, Secondary causes (SAH, tumor, meningitis, glaucoma, temporal arteritis)', 'Tension-type (stress-related, bilateral band-like), Migraine (unilateral pulsating moderate-severe, 4-72 hrs, with nausea/light/noise sensitivity), Cluster (severe orbital/temporal unilateral, autonomic features, episodic pattern)', 'Subarachnoid hemorrhage (thunderclap onset), Meningitis (fever+nuchal rigidity), Temporal arteritis (>50yo with jaw claudication), Brain tumor (progressive morning exacerbation), Glaucoma (eye pain+vision changes)', 'Headache with neck stiffness+photophobia, Thunderclap onset, New/worse pattern >50yo, Headache with neurologic deficit, Immunosuppressed patient with headache', 'Headache evaluation: History focusing on onset, character, location, duration, aggravating/alleviating factors, associated symptoms, past history; Physical exam including neurologic assessment, fundoscopy, temporal artery palpation; If red flags present: urgent CT head (noncontrast) then MRI/MRA, lumbar puncture for suspected SAH/meningitis, ESR/CRP for temporal arteritis suspicion', 'CT head noncontrast emergently for thunderclap/subacute onset red flag headache; MRI brain with contrast for progressive headache, suspected mass lesion; LP for suspected meningitis/SAH if CT negative; Temporal artery biopsy if giant cell arteritis suspected', 'Analgesics for acute episodes (NSAIDs, triptans for migraine, ergotamines); Preventive therapy for frequent migraines (beta-blockers, topiramate, CGRP mAbs); Manage underlying conditions (infection, hypertension, tumor); Avoid medication overuse', 'Thunderclap headache requires immediate exclusion of subarachnoid hemorrhage; Temporal arteritis with visual symptoms constitutes ophthalmologic emergency requiring urgent high-dose steroids; Progressive worsening headache warrants neuroimaging regardless of age.', '\\begin{enumerate}\n  \\item Silberstein SD. Migraine and Other Headaches.\n  \\item Headache Classification Committee of the International Headache Society (IHS) The International Classification of Headache Disorders, 3rd edition.\n  \\item UpToDate.com: Evaluation of adult with headache.\n\\end{enumerate>'},
}

for name, (category, defn, what_is, pathoph, clinical_feat, diff_diag, causes, serious_causes, assoc_symptoms, when_to_seek, workup, management, pearls, refs) in symptom_sets.items():
    create_detailed_symptom(name, category, defn, what_is, pathoph, clinical_feat, diff_diag, causes, serious_causes, assoc_symptoms, when_to_seek, workup, management, pearls, refs)
    print(f"Created: {name}")

print("\nCreated initial symptom chapters successfully!")
