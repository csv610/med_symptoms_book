import os, re

def get_sections_for_symptom(title, fname):
    title_lower = title.lower()
    is_pain = 'pain' in title_lower
    is_resp = any(w in title_lower for w in ['cough', 'sneez', 'wheez', 'shortness', 'breath', 'nasal', 'runny', 'congestion', 'sore throat', 'hoarse', 'catarrh', 'nosebleed', 'haemoptysis', 'snore'])
    is_gi = any(w in title_lower for w in ['nausea', 'vomit', 'diarrhea', 'constip', 'bloat', 'heartburn', 'abdominal', 'loss of appetite', 'blood in stool', 'bowel', 'motion sickness', 'sickness', 'burp'])
    is_neuro = any(w in title_lower for w in ['headache', 'dizzi', 'syncope', 'vertigo', 'seizure', 'tremor', 'numb', 'tingl', 'facial droop', 'facial numb', 'memory', 'confus', 'delirium', 'stroke', 'disorient', 'brain fog'])
    is_psych = any(w in title_lower for w in ['anxiety', 'depression', 'insomnia', 'mood', 'delusion', 'hallucin', 'addiction', 'withdrawal'])
    is_skin = any(w in title_lower for w in ['rash', 'itch', 'hair loss', 'heat rash', 'chronic wound', 'dry skin'])
    is_ent = any(w in title_lower for w in ['ear', 'tinnitus', 'ringing', 'fluid from ear', 'hearing', 'smell', 'anosmia'])
    is_eye = any(w in title_lower for w in ['eye', 'vision', 'dry eye', 'eyelid', 'double vision', 'twitch'])
    is_cardio = any(w in title_lower for w in ['palpitation', 'tachycardia', 'heart murmur', 'chest tightness', 'chest pain'])
    is_uro = any(w in title_lower for w in ['urinary', 'hematuria', 'kidney', 'blood in urine'])
    is_repro = any(w in title_lower for w in ['vaginal', 'period', 'bleeding between', 'heavy period', 'irregular period', 'penis', 'testicle', 'painful sex', 'pelvic', 'blood in semen', 'morning sick', 'hot flush', 'pregnancy', 'breast', 'erectile', 'nipple'])
    is_muscle = any(w in title_lower for w in ['muscle cramp', 'muscle pain', 'calf', 'leg pain', 'joint', 'sciatica', 'back pain', 'heel', 'hip', 'knee', 'shoulder', 'wrist'])
    is_fever = 'fever' in title_lower or 'chills' in title_lower or 'sweat' in title_lower
    is_oral = any(w in title_lower for w in ['bad breath', 'dry mouth', 'toothache', 'gum', 'hiccup', 'ulcer', 'thrush', 'cold sore', 'drool', 'taste'])
    is_misc = any(w in title_lower for w in ['fatigue', 'malaise', 'weakness', 'weight loss', 'swelling', 'jaundice', 'choking', 'black eye', 'lump', 'nerve pain', 'pain', 'dehydration', 'cold hands', 'raynaud'])

    self_care = []
    diagnostic = []
    treatment = []

    if is_pain:
        self_care = [
            "Rest the affected area and avoid activities that aggravate the pain.",
            "Apply ice packs for 15-20 minutes at a time during the first 48 hours, then switch to heat if preferred.",
            "Over-the-counter analgesics such as acetaminophen or ibuprofen may provide relief (follow label instructions).",
            "Gentle stretching or movement within pain tolerance helps prevent stiffness.",
            "Seek medical evaluation if pain persists beyond 7 days despite self-care measures."
        ]
        diagnostic = [
            "A focused history assesses onset, location, quality, severity, duration, radiation, aggravating/relieving factors, and prior treatments.",
            "Physical examination includes inspection for swelling/deformity, palpation for tenderness point, range-of-motion testing, and neurovascular assessment.",
            "Imaging (X-ray, ultrasound, MRI, CT) may be indicated based on suspected etiology and red flag findings.",
            "Laboratory studies (CBC, CRP, ESR) help evaluate for inflammatory or infectious causes."
        ]
        treatment = [
            "First-line management includes activity modification, physical therapy, and analgesics (NSAIDs or acetaminophen).",
            "Specific diagnoses may require targeted therapy: antibiotics for infection, corticosteroids for inflammation, surgery for structural pathology.",
            "Referral to a specialist (orthopedics, rheumatology, pain medicine) is indicated for refractory cases or complex diagnoses.",
            "Multimodal approaches combining medication, manual therapy, exercise, and behavioral strategies yield best outcomes for chronic pain."
        ]
    elif is_resp:
        self_care = [
            "Maintain adequate hydration with water, warm tea, or broth to thin secretions.",
            "Use a humidifier or steam inhalation to soothe irritated airways and loosen mucus.",
            "Rest and avoid exposure to smoke, dust, and other respiratory irritants.",
            "Over-the-counter remedies such as saline nasal spray, cough drops, or honey (for adults) may provide symptomatic relief.",
            "Monitor for warning signs including high fever, difficulty breathing, chest pain, or worsening symptoms."
        ]
        diagnostic = [
            "History focuses on onset, duration, character of symptoms (productive vs dry cough, nasal discharge color), fever pattern, and exposure history.",
            "Physical examination includes vital signs, lung auscultation, nasal inspection, and oropharyngeal examination.",
            "Targeted testing may include rapid antigen/ PCR for respiratory viruses, chest X-ray, pulse oximetry, and sputum culture.",
            "Allergy testing or pulmonary function tests are reserved for chronic or recurrent cases."
        ]
        treatment = [
            "Symptomatic management includes antitussives, expectorants, decongestants, antihistamines, and saline irrigation as appropriate.",
            "Bacterial infections require appropriate antibiotic therapy based on suspected pathogen and local resistance patterns.",
            "Inhaled bronchodilators or corticosteroids are used for reactive airway disease or asthma exacerbations.",
            "Referral to pulmonology or ENT is indicated for chronic, recurrent, or treatment-refractory cases."
        ]
    elif is_gi:
        self_care = [
            "Maintain hydration with clear fluids (water, oral rehydration solutions, clear broths) in small, frequent amounts.",
            "Eat bland, easy-to-digest foods (bananas, rice, applesauce, toast) and avoid fatty, spicy, or dairy-heavy meals during recovery.",
            "Rest the digestive system by eating smaller meals more frequently rather than large meals.",
            "Over-the-counter remedies may help: antacids for heartburn, loperamide for diarrhea, fiber supplements for constipation.",
            "Seek medical attention if symptoms persist beyond 48 hours, or if accompanied by severe pain, fever, or bloody stools."
        ]
        diagnostic = [
            "History covers onset, duration, stool frequency/character, associated symptoms (pain, fever, nausea), dietary triggers, and travel history.",
            "Physical examination includes abdominal auscultation, palpation for tenderness/masses, and assessment of hydration status.",
            "Stool studies (culture, ova/parasites, occult blood, fecal calprotectin) help identify infectious or inflammatory causes.",
            "Endoscopy or colonoscopy is indicated for chronic symptoms, unexplained weight loss, or concerning features."
        ]
        treatment = [
            "Supportive care with hydration and dietary modification is first-line for most acute gastrointestinal symptoms.",
            "Probiotics may help restore gut flora balance after infectious diarrhea or antibiotic use.",
            "Specific pharmacotherapy depends on diagnosis: antiemetics for vomiting, antispasmodics for cramping, antibiotics for bacterial infection.",
            "Chronic conditions (IBS, IBD, GERD) require specialist management with tailored medical and lifestyle interventions."
        ]
    elif is_neuro:
        self_care = [
            "Ensure a safe environment to prevent injury during episodes (remove hazards, avoid driving or operating machinery).",
            "Keep a symptom diary documenting triggers, duration, frequency, and associated features.",
            "Practice stress reduction techniques (deep breathing, meditation, adequate sleep) as stress often exacerbates neurological symptoms.",
            "Avoid alcohol, caffeine, and recreational drugs which can worsen many neurological conditions.",
            "Seek immediate evaluation for sudden-onset, severe, or progressive neurological symptoms."
        ]
        diagnostic = [
            "Detailed neurological history includes onset pattern, progression, triggers, associated symptoms, and functional impact.",
            "Comprehensive neurological examination assesses mental status, cranial nerves, motor/sensory function, reflexes, coordination, and gait.",
            "Neuroimaging (CT, MRI) is often indicated to evaluate for structural, vascular, or demyelinating causes.",
            "Specialized testing (EEG for seizures, nerve conduction studies for neuropathy, lumbar puncture for meningitis) is guided by clinical suspicion."
        ]
        treatment = [
            "Treatment is directed at the underlying cause identified through diagnostic evaluation.",
            "Symptomatic pharmacotherapy may include analgesics, anticonvulsants, antidepressants, or disease-modifying agents as appropriate.",
            "Physical, occupational, and speech therapy play important roles in functional recovery and rehabilitation.",
            "Referral to neurology is indicated for unexplained, progressive, or treatment-refractory neurological symptoms."
        ]
    elif is_psych:
        self_care = [
            "Establish a consistent daily routine with regular sleep, meals, and physical activity to support mental health stability.",
            "Practice stress management techniques including mindfulness, deep breathing exercises, and progressive muscle relaxation.",
            "Maintain social connections and avoid isolation by reaching out to trusted friends, family, or support groups.",
            "Avoid alcohol, caffeine, and recreational drugs which can destabilize mood and exacerbate psychiatric symptoms.",
            "If experiencing suicidal thoughts or crisis, contact emergency services or a crisis helpline immediately."
        ]
        diagnostic = [
            "Comprehensive psychiatric assessment includes history of present illness, past psychiatric history, substance use, medical history, and collateral information from family.",
            "Standardized screening tools (GAD-7, PHQ-9, PCL-5) help quantify symptom severity and track treatment response.",
            "Medical evaluation (thyroid function, basic metabolic panel, CBC, toxicology screen) rules out organic causes of psychiatric symptoms.",
            "Risk assessment for self-harm, suicide, and danger to others is an essential component of every psychiatric evaluation."
        ]
        treatment = [
            "Psychotherapy (CBT, DBT, interpersonal therapy) is a first-line treatment for most psychiatric disorders.",
            "Pharmacotherapy with antidepressants, anxiolytics, mood stabilizers, or antipsychotics is tailored to the specific diagnosis and individual patient factors.",
            "Combined treatment (medication plus psychotherapy) generally yields superior outcomes compared to either modality alone.",
            "Referral to psychiatry is indicated for severe symptoms, treatment resistance, suicidal ideation, or diagnostic uncertainty."
        ]
    elif is_skin:
        self_care = [
            "Keep the affected area clean and dry; wash gently with mild, fragrance-free soap and lukewarm water.",
            "Avoid scratching — use cool compresses, calamine lotion, or OTC hydrocortisone cream to relieve itching.",
            "Apply moisturizer regularly to maintain skin barrier integrity, especially after bathing.",
            "Identify and avoid potential triggers (irritants, allergens, excessive heat, tight clothing).",
            "Seek medical evaluation if the rash spreads rapidly, develops blisters, shows signs of infection (pus, increasing redness, warmth), or is accompanied by fever."
        ]
        diagnostic = [
            "History includes onset, location, progression, associated symptoms (itching, pain, fever), exposure to triggers, and prior skin conditions.",
            "Physical examination assesses morphology (macules, papules, vesicles, etc.), distribution, and extent of skin involvement.",
            "Diagnostic tests may include skin scraping for fungal examination, patch testing for allergic contact dermatitis, or biopsy for suspicious lesions.",
            "Laboratory studies (CBC, ESR, autoimmune serologies) are obtained when systemic disease is suspected."
        ]
        treatment = [
            "Topical therapies (corticosteroids, antifungals, antibiotics, emollients) are first-line for most localized skin conditions.",
            "Systemic therapy (oral antihistamines, antibiotics, antifungals, or immunosuppressants) is reserved for extensive or refractory cases.",
            "Phototherapy or biologic agents may be indicated for chronic inflammatory skin diseases (psoriasis, eczema).",
            "Referral to dermatology is appropriate for uncertain diagnoses, treatment failure, or skin lesions suspicious for malignancy."
        ]
    elif is_ent:
        self_care = [
            "Avoid inserting objects into the ear canal; use a warm compress externally for comfort.",
            "For tinnitus, reduce exposure to loud noises, limit caffeine and alcohol, and use background sound masking.",
            "Keep the ear dry during bathing or swimming to prevent worsening of ear infections.",
            "Over-the-counter pain relievers (acetaminophen, ibuprofen) may help with ear discomfort.",
            "Seek evaluation if symptoms persist beyond 2-3 days, or if accompanied by hearing loss, fever, or discharge."
        ]
        diagnostic = [
            "History includes onset, character of symptoms (pain, discharge type, hearing changes), preceding illness, and trauma.",
            "Otoscopic examination evaluates the external canal, tympanic membrane integrity, and presence of effusion or discharge.",
            "Hearing assessment (tuning fork tests, audiometry) determines type and degree of hearing loss if present.",
            "Imaging (CT temporal bone) is reserved for complicated infections, cholesteatoma, or suspected structural pathology."
        ]
        treatment = [
            "External ear infections require topical antibiotic/antifungal drops and keeping the ear dry.",
            "Middle ear infections may be managed with observation, oral antibiotics, or analgesics depending on severity and patient age.",
            "Chronic tinnitus management includes sound therapy, cognitive behavioral therapy, and addressing underlying hearing loss.",
            "ENT referral is indicated for recurrent infections, hearing loss, cholesteatoma, or refractory tinnitus."
        ]
    elif is_eye:
        self_care = [
            "Rest the eyes using the 20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds.",
            "Apply artificial tears or lubricating eye drops for dryness — avoid drops that claim to 'get the red out' which can cause rebound redness.",
            "Use a warm compress for blepharitis or styes; use a cold compress for allergic conjunctivitis or swelling.",
            "Remove contact lenses immediately and switch to glasses if eye irritation develops.",
            "Seek urgent evaluation for eye pain, vision changes, light sensitivity, or chemical exposure."
        ]
        diagnostic = [
            "History covers onset, duration, visual changes, pain character, discharge, contact lens use, and trauma.",
            "Visual acuity testing and slit-lamp examination are essential components of the eye evaluation.",
            "Fluorescein staining identifies corneal abrasions or ulcers; tonometry measures intraocular pressure.",
            "Fundoscopic examination evaluates the retina, optic disc, and vasculature for pathology."
        ]
        treatment = [
            "Infectious conjunctivitis is treated with appropriate topical antibiotics (bacterial) or antihistamines (allergic).",
            "Dry eye disease management includes artificial tears, punctal plugs, topical cyclosporine, and lifestyle modifications.",
            "Corneal abrasions heal with antibiotic ointment and pressure patching; deep ulcers require ophthalmology referral.",
            "Sudden vision loss, retinal detachment, or acute angle-closure glaucoma are ophthalmologic emergencies requiring immediate specialist care."
        ]
    elif is_cardio:
        self_care = [
            "Monitor symptoms including frequency, duration, triggers, and associated features; keep a symptom log.",
            "Avoid stimulants (caffeine, nicotine, decongestants, energy drinks) which can exacerbate palpitations and tachycardia.",
            "Practice relaxation techniques and stress reduction to minimize sympathetic activation.",
            "Maintain adequate hydration and electrolyte balance, especially during illness or exercise.",
            "Seek immediate evaluation for chest pain, shortness of breath, fainting, or palpitations with dizziness."
        ]
        diagnostic = [
            "History characterizes the symptom (quality, onset, duration, triggers, relieving factors) and assesses cardiac risk factors.",
            "Physical examination includes vital signs, cardiac auscultation (rate, rhythm, murmurs), lung exam, and peripheral edema assessment.",
            "Diagnostic testing includes ECG, ambulatory cardiac monitoring (Holter or event monitor), echocardiogram, and stress testing.",
            "Laboratory studies (troponin, BNP, electrolytes, thyroid function) help identify acute or contributing pathology."
        ]
        treatment = [
            "Benign palpitations require reassurance and trigger avoidance; persistent symptoms may benefit from beta-blockers.",
            "Arrhythmias are treated based on type: rate control, rhythm control, anticoagulation, or ablation procedures.",
            "Heart murmurs require echocardiographic evaluation; management depends on the specific valvular lesion and severity.",
            "Cardiology referral is indicated for concerning symptoms, abnormal ECG findings, or newly discovered murmurs."
        ]
    elif is_uro:
        self_care = [
            "Drink adequate water throughout the day unless fluid restriction is medically indicated.",
            "Avoid bladder irritants including caffeine, alcohol, acidic foods, and artificial sweeteners.",
            "Practice good hygiene and urinate promptly when the urge arises to prevent urinary stasis.",
            "Apply a heating pad to the lower abdomen or back for comfort during urinary discomfort.",
            "Seek medical attention for fever, flank pain, visible blood in urine, or difficulty urinating."
        ]
        diagnostic = [
            "History covers urinary symptoms (frequency, urgency, dysuria, hesitancy, stream changes), fever, and flank pain.",
            "Urinalysis with microscopy and culture is the first-line diagnostic test for urinary symptoms.",
            "Imaging (renal ultrasound, CT urogram) evaluates for stones, obstruction, structural abnormalities, or masses.",
            "Urodynamic studies or cystoscopy may be indicated for complex or refractory voiding dysfunction."
        ]
        treatment = [
            "Urinary tract infections are treated with targeted antibiotics based on culture sensitivity results.",
            "Nephrolithiasis management includes hydration, analgesics, medical expulsive therapy, or urologic intervention for large stones.",
            "Voiding dysfunction may respond to behavioral modification, pelvic floor therapy, or pharmacotherapy.",
            "Urology referral is indicated for recurrent infections, hematuria, obstructive symptoms, or suspected malignancy."
        ]
    elif is_repro:
        self_care = [
            "Track symptoms including cycle dates, flow characteristics, and associated pain using a diary or app.",
            "Apply a heating pad to the lower abdomen for menstrual cramp relief.",
            "Practice good genital hygiene and avoid douching or scented products which can disrupt normal flora.",
            "Over-the-counter pain relievers (ibuprofen, naproxen) are effective for menstrual pain and can reduce heavy bleeding.",
            "Seek evaluation for abnormal bleeding, pelvic pain, unusual discharge, or breast changes."
        ]
        diagnostic = [
            "History includes menstrual history, sexual activity, contraceptive use, pregnancy status, and associated symptoms.",
            "Pelvic examination (speculum and bimanual) assesses the cervix, uterus, and adnexa for tenderness, masses, or discharge.",
            "Pregnancy testing is essential for any reproductive-age woman with abnormal bleeding or pelvic symptoms.",
            "Ultrasound (transabdominal or transvaginal) evaluates the endometrium, myometrium, ovaries, and adnexal structures."
        ]
        treatment = [
            "Hormonal contraceptives (oral, injectable, intrauterine) are first-line treatment for many menstrual disorders.",
            "NSAIDs reduce prostaglandin-mediated pain and bleeding in dysmenorrhea and menorrhagia.",
            "Specific diagnoses require targeted therapy: antibiotics for pelvic infection, endometrial ablation for refractory bleeding, surgery for fibroids or endometriosis.",
            "Referral to gynecology is indicated for complex cases, infertility, or suspected malignancy."
        ]
    elif is_muscle:
        self_care = [
            "Apply the RICE protocol: Rest, Ice (15-20 min every 2-3 hours), Compression with elastic bandage, Elevation above heart level.",
            "Gradual return to activity with gentle stretching once acute pain subsides.",
            "Over-the-counter anti-inflammatory medications (ibuprofen, naproxen) can reduce pain and swelling.",
            "Avoid activities that worsen symptoms until healing is well underway.",
            "Seek evaluation for severe pain, inability to bear weight, joint deformity, or symptoms lasting beyond 2 weeks."
        ]
        diagnostic = [
            "History focuses on mechanism of injury, onset (acute vs insidious), location, aggravating/relieving factors, and prior episodes.",
            "Physical examination includes inspection (swelling, bruising, deformity), palpation, range-of-motion, and strength testing.",
            "Imaging (X-ray for fracture, ultrasound for tendon/ligament injury, MRI for soft tissue detail) guides diagnosis.",
            "Functional assessment evaluates ability to perform daily activities and sports-specific movements."
        ]
        treatment = [
            "Acute injuries benefit from RICE, activity modification, and gradual rehabilitation exercises.",
            "Physical therapy is central to recovery, focusing on range-of-motion, strengthening, and proprioceptive training.",
            "Corticosteroid injections may be considered for significant inflammatory conditions (tendinitis, bursitis).",
            "Orthopedic referral is indicated for complete tears, fractures, joint instability, or failure of conservative therapy for 6-8 weeks."
        ]
    elif is_fever:
        self_care = [
            "Rest and maintain adequate hydration with water, clear fluids, or oral rehydration solutions.",
            "Use acetaminophen or ibuprofen to reduce fever and body aches (follow label dosing instructions).",
            "Dress lightly and keep the room at a comfortable temperature — avoid bundling excessively.",
            "Monitor temperature at regular intervals and track other symptoms to identify worsening trends.",
            "Seek medical attention for fever above 40\textdegree{}C (104\textdegree{}F), fever lasting more than 3 days, or fever with stiff neck, severe headache, rash, or difficulty breathing."
        ]
        diagnostic = [
            "History includes fever duration, pattern (intermittent, remittent, continuous), associated symptoms (chills, rigors, sweats), and exposure history.",
            "Vital signs assess fever severity and hemodynamic stability; complete physical examination seeks a source.",
            "Laboratory evaluation includes CBC with differential, blood cultures, urinalysis, inflammatory markers (CRP, ESR), and targeted testing based on exposure history.",
            "Imaging (chest X-ray, abdominal ultrasound, CT) is guided by clinical findings and suspected source."
        ]
        treatment = [
            "Antipyretics (acetaminophen, NSAIDs) provide symptomatic relief but do not treat the underlying cause.",
            "Empiric antibiotics may be indicated for suspected bacterial infection after appropriate cultures are obtained.",
            "Antiviral, antifungal, or antimalarial therapy is directed at specific pathogens based on exposure and testing.",
            "Source control (drainage of abscess, removal of infected device) is essential for focal infections."
        ]
    elif is_oral:
        self_care = [
            "Maintain good oral hygiene: brush twice daily, floss daily, and rinse with warm salt water (1/2 tsp salt in 8 oz water).",
            "Avoid tobacco, alcohol, and spicy or acidic foods that may irritate oral tissues.",
            "Stay hydrated by sipping water throughout the day to combat dry mouth.",
            "Over-the-counter pain relievers and topical oral gels can provide temporary relief for toothache or gum discomfort.",
            "See a dentist promptly for persistent oral symptoms, as early intervention improves outcomes."
        ]
        diagnostic = [
            "History covers onset, character of pain, aggravating/relieving factors, oral hygiene habits, and dental care history.",
            "Oral examination inspects teeth, gums, mucosa, tongue, and oropharynx for caries, inflammation, lesions, or masses.",
            "Dental X-rays (panoramic, periapical) identify caries, abscesses, impactions, and bone pathology.",
            "Referral to a dentist or oral surgeon is appropriate for definitive diagnosis and treatment of dental pathology."
        ]
        treatment = [
            "Dental caries require restorative treatment (fillings, crowns, root canal) by a dentist.",
            "Oral infections (abscess, pericoronitis) may require drainage, antibiotics, and definitive dental treatment.",
            "Dry mouth management includes hydration, sugar-free lozenges, saliva substitutes, and addressing underlying causes.",
            "Regular dental check-ups every 6 months are essential for prevention and early detection of oral pathology."
        ]
    elif is_misc:
        self_care = [
            "Prioritize adequate rest and sleep to support the body's healing and recovery processes.",
            "Maintain a balanced diet with regular meals and stay well-hydrated.",
            "Monitor symptoms and track any changes in severity, frequency, or associated features.",
            "Avoid overexertion and gradually increase activity levels as tolerated.",
            "Seek medical evaluation if symptoms persist, worsen, or interfere significantly with daily function."
        ]
        diagnostic = [
            "Comprehensive history and physical examination guide the diagnostic workup based on the specific symptom presentation.",
            "Laboratory testing (CBC, metabolic panel, inflammatory markers) helps screen for underlying systemic conditions.",
            "Imaging studies are tailored to the suspected anatomic region and pathology.",
            "Referral to appropriate specialists is guided by the differential diagnosis established through initial evaluation."
        ]
        treatment = [
            "Treatment is directed at the underlying cause identified through diagnostic evaluation.",
            "Symptomatic management may include pharmacotherapy, lifestyle modifications, and supportive care.",
            "Multidisciplinary care is often beneficial for complex or chronic symptoms.",
            "Close follow-up ensures treatment effectiveness and allows adjustment of the management plan as needed."
        ]
    else:
        self_care = [
            "Prioritize adequate rest and sleep to support the body's natural healing processes.",
            "Maintain good hydration and a balanced diet to support overall health.",
            "Monitor symptoms and keep a record of any changes or patterns that develop.",
            "Avoid known triggers and avoid self-medicating without professional guidance.",
            "Consult a healthcare professional if symptoms persist, worsen, or cause significant concern."
        ]
        diagnostic = [
            "Comprehensive history and physical examination guide the diagnostic workup based on the specific symptom presentation.",
            "Laboratory testing (CBC, metabolic panel, inflammatory markers) helps screen for underlying systemic conditions.",
            "Imaging studies are tailored to the suspected anatomic region and pathology.",
            "Referral to appropriate specialists is guided by the differential diagnosis established through initial evaluation."
        ]
        treatment = [
            "Treatment is directed at the underlying cause identified through diagnostic evaluation.",
            "Symptomatic management may include pharmacotherapy, lifestyle modifications, and supportive care.",
            "Multidisciplinary care is often beneficial for complex or chronic symptoms.",
            "Close follow-up ensures treatment effectiveness and allows adjustment of the management plan as needed."
        ]

    return self_care, diagnostic, treatment


def add_sections_to_file(fpath):
    with open(fpath, 'r') as f:
        content = f.read()

    # Extract chapter title
    m = re.search(r'\\chapter\{([^}]+)\}', content)
    if not m:
        print(f"  SKIP: No chapter title found in {fpath}")
        return False
    title = m.group(1)

    # Check if sections already exist
    if '\\section*{Self-Care' in content or '\\section*{Diagnostic' in content or '\\section*{Treatment' in content:
        print(f"  SKIP: New sections already present in {fpath}")
        return False

    self_care, diagnostic, treatment = get_sections_for_symptom(title, fpath)

    # Build new sections text
    new_sections = ""

    new_sections += "\\section*{Self-Care / Home Management}\n"
    new_sections += "\\begin{itemize}\n"
    for item in self_care:
        new_sections += f"  \\item {item}\n"
    new_sections += "\\end{itemize}\n\n"

    new_sections += "\\section*{Diagnostic Approach}\n"
    new_sections += "\\begin{itemize}\n"
    for item in diagnostic:
        new_sections += f"  \\item {item}\n"
    new_sections += "\\end{itemize}\n\n"

    new_sections += "\\section*{Treatment / Management Overview}\n"
    new_sections += "\\begin{itemize}\n"
    for item in treatment:
        new_sections += f"  \\item {item}\n"
    new_sections += "\\end{itemize}\n\n"

    # Insert before \clearpage
    if '\\clearpage' in content:
        content = content.replace('\\clearpage', new_sections + '\\clearpage')
    else:
        content += '\n' + new_sections

    with open(fpath, 'w') as f:
        f.write(content)

    print(f"  Updated: {fpath} -- {title}")
    return True


def main():
    chapters_dir = '/Users/csv610/Projects/MyBooks/MedSymptoms/chapters'
    files = sorted([f for f in os.listdir(chapters_dir) if f.startswith('symptom_') and f.endswith('.tex')])
    print(f"Processing {len(files)} symptom chapters...")
    updated = 0
    skipped = 0
    for fname in files:
        fpath = os.path.join(chapters_dir, fname)
        if add_sections_to_file(fpath):
            updated += 1
        else:
            skipped += 1
    print(f"\nDone. Updated: {updated}, Skipped: {skipped}")

if __name__ == '__main__':
    main()
