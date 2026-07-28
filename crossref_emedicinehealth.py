import re

# All eMedicineHealth entries (symptoms and signs list)
emed_entries = """
Abdominal Pain in Adults
Abdominal Pain in Children
Abscess
Abscessed Tooth
Acetaminophen (Tylenol) Poisoning
Achilles Tendon Rupture
Acid Reflux Disease (GERD)
Acromegaly
Acute Angle-Closure Glaucoma
Acute Bronchitis
Acute Flaccid Myelitis (AFM)
Acute Kidney Failure
Acute Respiratory Distress Syndrome
Addiction
Adenomyosis Uterus
Adenovirus
ADHD in Adults
ADHD in Teens
Adhesions, General and After Surgery
Adrenocortical Carcinoma
Adult Acute Lymphoblastic Leukemia (ALL)
Adult Acute Myeloid Leukemia (AML)
Adult Glaucoma Suspect
Adult Non-Hodgkin Lymphoma
Adult Primary Liver Cancer
Alcohol Intoxication
Alcoholism
Allergic Reaction
Allergy: Insect Sting
Allergy: Poison Ivy, Oak, and Sumac
Alzheimer Disease
Amebiasis (Entamoeba histolytica Infection)
Amenorrhea
Amyotrophic Lateral Sclerosis (ALS)
Anal Abscess
Anal Fissure
Anal Itching
Anatomy Involved in Crohn Disease
Anemia
Aneurysm (Brain)
Angina Pectoris
Angle Recession Glaucoma
Animal Bites
Ankle Fracture
Ankle Sprain
Ankylosing Spondylitis
Anorexia Nervosa
Anthrax
Antibiotics
Anxiety
Aortic Aneurysm
Appendicitis
Arch Pain
Arthritis
Ascariasis
Ascites
Asperger Syndrome
Aspirin Poisoning
Asthma
Asthma in Children
Asthma in Pregnancy
Astigmatism
Athlete's Foot
Atrial Fibrillation
Atrial Flutter
Attention Deficit Hyperactivity Disorder
Autism
Avascular Necrosis
Back Pain Health
Bacterial Pneumonia
Bacterial Vaginosis
Bad Breath (Halitosis)
Barbiturate Abuse
Barotrauma/Decompression Sickness
Bartholin Cyst
Battery Ingestion
Bedbugs
Bedwetting
Bee and Wasp Stings
Bell Palsy
Benign Positional Vertigo
Benzodiazepine Abuse
Binge Eating Disorder
Biological Warfare
Bipolar Disorder Health
Bird Flu
Black Eye
Black Widow Spider Bite
Bladder Cancer
Bladder Control Problems
Bladder Infection in Adults
Blastomycosis
Blood Clot in the Legs
Blood Clots
Blood in the Urine (Hematuria)
Bocavirus
Boil vs Pimple
Boils
Bone Cancer
Bone Fracture (Broken Bone)
Bone Spurs
Borderline Personality Disorder
Botulism
Bowel Obstruction Early Signs and Causes
Boxer's Fracture
Brain Cancer
Brain Infection
Brain Lesions (Lesions on the Brain)
Breast Cancer
Breast Infection
Breast Lumps and Pain
Broken Arm
Broken Collarbone
Broken Elbow
Broken Finger
Broken Foot
Broken Hand
Broken Jaw
Broken Leg
Broken Nose
Broken or Knocked-out Teeth
Broken Shoulder Blade
Broken Toe
Bronchial Adenoma
Bronchiectasis
Bronchitis
Brucellosis
Bruises
Bulimia
Bunions
Bursitis
Cancer of the Esophagus
Cancer of the Mouth and Throat
Cancer of the Small Intestine
Cancer of the Testicle
Cancer Symptoms
Cancer-Related Post-traumatic Stress
Candidiasis (Yeast Infection)
Canker Sores
Carbon Monoxide Poisoning
Carcinoid Lung Tumor
Cardiomyopathy
Carpal Tunnel Syndrome
Carpal Tunnel vs Arthritis
Cat Scratch Disease
Cataracts
Catfish Sting
Cauda Equina Syndrome
Celiac Sprue
Cellulite
Cellulitis
Cerebral Palsy
Cervical Cancer
Cervical Dysplasia
Cervicitis
Chagas Disease (American Trypanosomiasis)
Chalazion (Lump in Eyelid)
Chemical Burns
Chemical Eye Burns
Chemical Pneumonia
Chemical Warfare
Chest Pain Overview
Chickenpox
Chiggers
Chikungunya Virus Infection
Child Abuse
Chlamydia
Chlamydia In Women
Choking
cholecystitis
Cholera
Cholesterol and Children
Chondromalacia Patella
Chronic Fatigue Syndrome
Chronic Kidney Disease
Chronic Obstructive Pulmonary Disease (COPD)
Cirrhosis
Clostridium Difficile (C. difficile, C. diff)
Cluster Headache
Cocaine Abuse
Cognitive Deficits
Cold Hands and Feet
Cold Sores
Colds
Colic
Colitis
Collapsed Lung
Colon Cancer
Colon Polyps
Coma
Concussion
Congestive Heart Failure
Constipation in Adults
Constipation in Children
Contact Dermatitis
Contact Lenses
Corneal Abrasion
Corneal Flash Burns
Corneal Ulcer
Corns and Calluses
Coronary Heart Disease
Coronavirus
Costochondritis
Coughs
Coxsackievirus
Crabs
CRE Infection
Crohn Disease
Croup
Cryptococcosis
Cryptosporidiosis
Cushing Syndrome
Cuts or Lacerations
Cyanide Poisoning
Cyclospora Infection (Cyclosporiasis)
Cyst
Cystic Acne
Cysticercosis
Dandruff
de Quervain's Tenosynovitis
Decompression Syndromes: The Bends
Dehydration in Adults
Dehydration in Children
Dengue Fever
Dental Abscess
Depression Health
Depression Symptoms and Signs
Diabetes (Mellitus, Type 1 and Type 2)
Diabetic Eye Disease
Diabetic Foot Care
Diabetic Ketoacidosis
Diaper Rash
Diarrhea
Diphtheria
Dislocated Ankle (Ankle Dislocation)
Dislocated Hip
Disorders That Disrupt Sleep (Parasomnias)
Diverticulitis vs Ulcerative Colitis UC
Diverticulosis and Diverticulitis
Dizziness
Domestic Violence
Down Syndrome
Drug Allergy
Drug Dependence & Abuse
Drug Overdose
Dry Eye Syndrome
Dry Socket
Dyslexia
Dysphagia (Swallowing Problems)
E. coli: Escherichia coli 0157:H7, E. coli 0157:H7
Ear Pain, Scuba Diving
Earache
Earwax
Ebola Virus Disease (Ebola Hemorrhagic Fever)
Eclampsia
Ectopic Pregnancy
Eczema
Edema
Elbow Dislocation
Elbow Pain
Electric Shock
Electrolytes
Emphysema
Encephalitis
Encephalopathy
Encopresis
Endometrial Cancer
Endometriosis
Enlarged Prostate
Enlarged Spleen (Splenomegaly)
Enterovirus (Non-Polio Enterovirus Infection)
Epiglottitis
Epilepsy
Epstein-Barr Virus Infection
Erythema Nodosum
Esophagitis
Ewing Sarcoma
Exercise-Induced Asthma
Eye Allergies
Eye Floaters
Eye Herpes
Eye Injuries
Eye Pain
Eye Strain
Eyelid Inflammation (Blepharitis)
Facial Fracture
Fainting
Fatigue
Fatty Liver Disease
Female Sexual Problems
Fetal Alcohol Syndrome
Fever in Adults
Fever in Children
Fibromyalgia
Fifth Disease
Finger Dislocation
Finger Infection
Finger Injuries
Finger Sprain
Fish-Handler's Disease
Flatulence (Gas)
Flu in Adults
Flu in Children Health
Folliculitis
Food Allergy
Food Poisoning
Foot Pain
Foreign Body, Ear
Foreign Body, Eye
Foreign Body, Rectum
Foreign Body, Vagina
Foreskin Problems
Frequent Urination
Frostbite
Frozen Shoulder
Gallbladder Pain
Gallstones
Ganglion Cyst
Gangrene
Gastritis
Gastroenteritis
Gastroesophageal Reflux Disease (GERD) FAQs
Gastrointestinal Bleeding
Genital Herpes
Genital Warts
Gestational Diabetes
Giardiasis
Gingivitis
Glaucoma Overview
Gonorrhea
Gout
Group A Strep (GAS) Infection
Group B Strep Infection
Growth Failure in Children
Growth Hormone Deficiency
Guillain-Barre Syndrome
Guinea Worm Disease (Dracunculiasis)
Guttate Psoriasis
Gynecomastia
Hair Loss
Hand Injuries
Hand, Foot, and Mouth Disease
Hantavirus
Hardening of the Arteries
Hashimoto's Disease
Hay Fever
Head Injury
Hearing Loss
Heart Attack
Heart Rhythm Disorders
Heartburn
Heat Cramps
Heat Exhaustion
Heat Rash
Heat Stroke
Heel Spurs
Helicobacter Pylori (H. pylori)
Hematoma
Hemochromatosis (Iron Overload)
Hemophilia
Hemorrhoids
Hepatitis A
Hepatitis B
Hepatitis C
Hernia
Herpangina
Hiatal Hernia
Hiccups
High Blood Pressure
High Blood Sugar (Hyperglycemia)
High Cholesterol
Hip Pain
Histoplasmosis
HIV/AIDS
Hives and Angioedema
Homocysteine
Human Bites
Hypercalcemia (Elevated Calcium Levels)
Hyperhidrosis (Excessive Sweating)
Hyperkalemia
Hyperparathyroidism
Hypersomnia
Hyperthyroidism
Hyperventilation
Hyphema (Bleeding in Eye)
Hyponatremia (Low Sodium)
Hypopharyngeal Cancer
Hypopituitarism in Children
Hypopituitary
Hypothermia
Hypothyroidism
IBD vs IBS
Iliotibial Band Syndrome
Impetigo
Impotence/Erectile Dysfunction
Inability to Urinate
Incontinence
Incontinentia Pigmenti
Indigestion
Indoor Allergens
Inflammation of the Testicle (Orchitis)
Inflammatory Bowel Disease (IBD)
Ingrown Hair
Ingrown Toenails
Insect Bites
Insomnia
Insulin Reaction
Insulin Resistance
Internal Bleeding
Interstitial Cystitis
Interstitial Lung Disease
Iritis
Iron Poisoning
Irritable Bowel Syndrome
Jaundice
Jellyfish Stings
Jock Itch
Joint Pain
Juvenile Rheumatoid Arthritis
Kawasaki Disease
Kidney Cancer Renal Pelvis and Ureter
Kidney Infection
Kidney Stones
Kidney Transplant
Knee Dislocation
Knee Injury
Knee Pain Overview
Labor Signs
Labyrinthitis
Lactose Intolerance
Land Animal Bite
Langerhans Cell Histiocytosis Cancer
Larygeal Cancer
Laryngeal Cancer and Papillomatosis in Children
Laryngitis
Leg Pain
Legionnaires' Disease and Pontiac Fever
Leishmaniasis
Leprosy
Leptospirosis Facts
Leukemia Health
Lice
Life-Threatening Skin Rashes
Lightning Strike
Lip and Oral Cavity Cancer
Listeria monocytogenes Infection
Liver
Liver Cancer
Liver Transplant
Low Blood Pressure
Low Blood Sugar (Hypoglycemia)
Low Potassium
Low Testosterone (Low-T)
Lumbar Disc Disease
Lung Cancer
Lupus (Systemic Lupus Erythematosus) Health
Lyme Disease
Lymphedema
Lymphoma
Macular Degeneration
Mad Cow Disease and Variant Creutzfeldt-Jakob
Malaria
Mallet Finger
Measles
Melanoma
Melioidosis
Meniere Disease
Meningitis in Adults
Meningitis in Children
Meningococcemia
Menopause
Menstrual Pain
Mercury Poisoning
Mesothelioma
Metabolic Syndrome
Migraine Headache
Mild Headache
Miscarriage
Mitral Valve Prolapse
Mittelschmerz
Molluscum Contagiosum
Monkeypox
Mononucleosis
Mortons Neuroma
Motion Sickness
Mountain Sickness
Mouth Wounds and Treatments in Adults and Children
MRSA Infection
Mucormycosis
Multiple Sclerosis
Mumps
Munchausen Syndrome
Muscle Cramps
Muscle Strain
Mycosis Fungoides and Sezary Syndrome
Myeloma
Myxedema Coma
Naegleria fowleri Infection
Nail Injuries
Nail Psoriasis
Narcolepsy
Narcotic Abuse
Nasopharyngeal Cancer in Children
NDM-1
Neck Strain
Necrotizing Fasciitis
Nephrotic Syndrome
Neuroendocrine Carcinoid Tumors in Children
Neuropathic Pain (Nerve Pain)
Neuropathy
Newborn Jaundice
Night Sweats
Night Terrors
Non-Radiographic Axial Spondyloarthritis
Non-Small-Cell Lung Cancer
Normal Pressure Hydrocephalus
Norovirus
Nosebleeds
Nursemaid Elbow
Obesity
Obsessive Compulsive Disorder
Obstructive and Central Sleep Apnea
Occupational Asthma
Ocular Hypertension
Onychomycosis
Opioid Abuse and Addiction
Oral Cancer and Salivary Gland Cancer in Children
Oral Herpes
Oral Thrush
Oropharyngeal Cancer Treatment
Osteoarthritis
Osteopenia
Osteoporosis
Ovarian Cancer
Ovarian Cysts
Overactive Bladder
Paget Disease
Pain After Surgery
Pain During Intercourse
Painful Urination Symptoms and Signs
Palpitations
Pancreatic Cancer
Pancreatitis
PANDAS
Panic Attacks
Paranasal Sinus and Nasal Cavity Cancer
Parkinson's Disease (PD)
Paronychia (Nail Infection)
Pelvic Inflammatory Disease
Penile Cancer Penis Cancer
Peptic Ulcers
Perforated Eardrum
Pericarditis
Periodic Limb Movement Disorder
Periodontal (Gum) Disease
Peripheral Vascular Disease
Peritonsillar Abscess
Pernicious Anemia (Vitamin B-12 Deficiency)
Peyronie's Disease (Curved Penis)
Pheochromocytoma
Phlebitis
Pick Disease
Pilonidal Cyst
Pinched Nerve
Pineal Tumors
Pink Eye (Conjunctivitis)
Pinworms
Piriformis Syndrome
Placenta Previa in Pregnancy
Plague
Plantar Fasciitis Health
Plantar Warts
Plaque Psoriasis
Pleural Effusion
Pleurisy
Pneumonia
Poisoning
Polio
Polycystic Ovarian Syndrome (PCOS)
Polycythemia (High Red Blood Cell Count)
Post-traumatic Stress Disorder (PTSD)
Postpartum Depression
Postpartum Perineal Care
Preeclampsia
Pregnancy Symptoms
Pregnancy, Bleeding
Pregnancy, Round Ligament Pain
Pregnancy, Vomiting
Premenstrual Dysphoric Disorder (PMDD)
Premenstrual Syndrome (PMS)
Presbyopia (Age-Related Farsightedness)
Pressure Sores
Primary Biliary Cirrhosis
Primary Insomnia
Primary Open-Angle Glaucoma
Primary Sclerosing Cholangitis
Proctitis
Prolapsed Bladder
Prolapsed Uterus
Prostate Cancer
Prostate Infections
Psoriasis
Psoriatic Arthritis
Pulled Hamstring
Pulmonary Edema
Pulmonary Embolism
Pulmonary Hypertension
Puncture Wound
Pustular Psoriasis
Rabies
Rash
Raynaud Phenomenon
Rectal Bleeding
Rectal Cancer
Rectal Pain
Rectal Prolapse
REM Sleep Behavior Disorder
Renal Artery Stenosis
Renal Cell Cancer
Repetitive Motion Injuries
Respiratory Syncytial Virus (RSV) Infection
Restless Legs Syndrome (RLS)
Retinal Detachment
Retinoblastoma Eye Cancer
Rhabdomyolysis
Rheumatic Fever
Rheumatoid Arthritis
Ricin
Ringworm on Body
Ringworm on Scalp
Rocky Mountain Spotted Fever
Root Canal
Rosacea Health
Roseola
Rotator Cuff Injury
Rotavirus
Ruptured Tendon
Salmonella
Sarcoidosis
Scabies
Scarlet Fever
Schizophrenia Health
School Refusal
Sciatica
Scoliosis
Seasonal Depression (SAD)
Seizures and Fever
Seizures Emergencies
Seizures in Children
Separation Anxiety
Sepsis (Blood Infection)
Septic Shock
Severe Acute Respiratory Syndrome (SARS)
Severe Allergic Reaction (Anaphylactic Shock)
Sexually Transmitted Diseases
Shaken Baby Syndrome
Shark Bite
Shigellosis (Shigella Infection)
Shin Splints
Shingles
Shock
Short Stature in Children
Shoulder Dislocation
Shoulder Separation
Sick Building Syndrome
Sickle Cell Crisis
Sinus Headache
Sinus Infection
Sjogren Syndrome
Skier's Thumb
Skin Cancer
Skin Rashes in Children
Skin Tags
Sleep and Sleep Disorders in Children
Sleep Disorders and Aging
Sleep Disorders in Women
Sleepwalking
Slipped Disk
Small Intestinal Bacterial Overgrowth
Small-Cell Lung Cancer
Smallpox
Smoke Inhalation
Snakebite
Snoring
Solitary Pulmonary Nodule
Sore Throat
Spider Bite: Brown Recluse Spider Bite
Spina Bifida
Spinal Stenosis
Splinters
Spondylolisthesis
Spondylosis
Sporotrichosis
Sprained Wrist
Sprains and Strains
Staphylococcus
Starfish and Crown of Thorns Puncture Wounds
STDs in Men (Sexually Transmitted Diseases in Men)
Stingray Injury
Stomach Cancer
Stool Color Changes
Strep Throat
Stress Fracture
Stress Health
Stretch Marks
Stroke
Sty
Subconjunctival Hemorrhage (Bleeding in Eye)
Substance Abuse
Subungual Hematoma (Bleeding Under Nail)
Sudden Cardiac Arrest
Sunburn
Supraventricular Tachycardia
Swallowed Object
Swimmer's Ear
Swine Flu
Swollen Lymph Glands
Swollen Testicles Causes, Symptoms and Signs
Symptoms and Signs Shaking Hands Hand Tremors
Syphilis
Systemic Scleroderma
Tailbone (Coccyx) Injury
Teething
Temporomandibular Joint (TMJ) Syndrome
Tendinitis Health
Tennis Elbow
Tension Headache
Testicle Infection (Epididymitis)
Testicular Pain
Testicular Torsion
Tetanus
Tetralogy of Fallot
Thermal (Heat or Fire) Burns
Threatened Miscarriage
Thrombocytopenia (Low Platelet Count)
Thymoma and Thymic Carcinoma in Children
Thyroid Cancer
Thyroid Nodules
Thyroid Problems
Thyroid Storm
Tic Douloureux
Ticks
Tinea Versicolor
Tinnitus
Tonsillitis
Toothache
Torn ACL
Torn or Detached Nail
Torticollis
Tourette's Syndrome
Toxic Shock Syndrome
Toxoplasmosis
Transient Ischemic Attack (Mini-Stroke)
Traveler's Diarrhea
Tremors
Trichomoniasis
Trigeminal Neuralgia (Facial Nerve Pain)
Trigger Finger (Stenosing Flexor Tenosynovitis)
Trisomy 18 (Edwards Syndrome)
Tuberculosis
Type 2 Diabetes
Typhoid Fever (Enteric Fever)
Typhus
Ulcerative Colitis
Upper Respiratory Infection
Urethral Cancer
Urethritis in Men
Urinary Tract Infection (UTI)
Urologic Dysfunction After Menopause
Uterine Cancer Sarcoma
Uterine Fibroids
Vaginal Bleeding
Vaginal Cancer
Vaginal Discharge
Vaginal Infections
Vaginal Prolapse
Vaginal Yeast Infections
Varicose Veins
Vasculitis
Ventricular Septal Defect
Vertebral Compression Fracture
Vertigo
Viral Pneumonia
Vitiligo
Vomiting and Nausea
Warts
Wegener Granulomatosis
West Nile Virus
Whiplash
Whooping Cough (Pertussis)
Wound Care
Wrist Injury
Wrist Pain Symptoms, Signs, and Causes
Yeast Infection and Bacterial Vaginosis Symptoms
Yeast Infection Diaper Rash
Yeast Infection Skin Rash
Yellow Fever
Zika Virus
""".strip().split('\n')

# Clean up entries
emed_clean = [e.strip() for e in emed_entries if e.strip()]

# Read existing symptoms
with open('/tmp/existing_symptoms.txt') as f:
    existing = [line.strip().lower() for line in f if line.strip()]

def normalize(name):
    """Normalize a symptom name for comparison"""
    n = name.lower().strip()
    # Remove parentheticals
    n = re.sub(r'\([^)]*\)', '', n)
    # Remove common suffixes
    n = re.sub(r'\s+health$', '', n)
    n = re.sub(r'\s+overview$', '', n)
    n = re.sub(r'\s+symptoms and signs$', '', n)
    n = re.sub(r'\s+symptoms$', '', n)
    n = re.sub(r'\s+in adults$', '', n)
    n = re.sub(r'\s+in children$', '', n)
    n = re.sub(r'^(symptoms and signs of\s+)', '', n)
    n = n.strip()
    return n

def matches_existing(name, existing):
    name_lower = name.lower().strip()
    norm = normalize(name)
    
    # Direct match
    if name_lower in existing:
        return True
    
    # Normalized match
    for e in existing:
        if norm == e:
            return True
        if norm in e or e in norm:
            return True
    
    return False

# Core symptoms/signs (things a patient would experience)
# vs. conditions/diseases (medical diagnoses)
symptom_keywords = [
    'pain', 'ache', 'bleeding', 'swelling', 'numbness', 'tingling',
    'fatigue', 'fever', 'cough', 'rash', 'nausea', 'vomiting',
    'dizziness', 'headache', 'seizure', 'paralysis', 'weakness',
    'weight', 'loss of', 'difficulty', 'inability', 'frequency',
    'urgency', 'discharge', 'itching', 'burning', 'cramp',
    'bloating', 'constipation', 'diarrhea', 'indigestion',
    'palpitations', 'vertigo', 'tinnitus', 'edema', 'anemia',
    'jaundice', 'cyanosis', 'pallor', 'flush', 'sweating',
    'chill', 'insomnia', 'hypersomnia', 'hiccups',
    'flatulence', 'heartburn', 'dysphagia', 'hemorrhage',
    'hematoma', 'infection', 'inflammation'
]

def is_symptom_like(name):
    """Determine if an entry is more symptom-like vs disease-like"""
    name_l = name.lower()
    
    # Conditions/diseases (not symptoms)
    disease_indicators = [
        'cancer', 'tumor', 'carcinoma', 'sarcoma', 'leukemia', 'lymphoma',
        'disease', 'syndrome', 'disorder', 'infection', 'virus',
        'bacteria', 'fungal', 'poisoning', 'overdose', 'abuse',
        'fracture', 'dislocation', 'sprain', 'strain', 'rupture',
        'surgery', 'transplant', 'treatment', 'therapy',
        'vaccine', 'allergy', 'asthma', 'diabetes', 'arthritis',
        'cirrhosis', 'hepatitis', 'meningitis', 'pneumonia',
        'bronchitis', 'colitis', 'diverticulitis', 'pancreatitis',
        'appendicitis', 'cholecystitis', 'dermatitis',
        'osteoporosis', 'osteopenia', 'glaucoma', 'cataract',
        'aneurysm', 'embolism', 'stenosis', 'sclerosis',
        'fibromyalgia', 'lupus', 'HIV', 'AIDS', 'malaria',
        'tuberculosis', 'syphilis', 'gonorrhea', 'chlamydia',
        'herpes', 'warts', 'migraine', 'epilepsy', 'parkinson',
        'alzheimer', 'dementia', 'schizophrenia', 'depression',
        'anxiety', 'OCD', 'PTSD', 'bipolar', 'autism', 'ADHD',
        'obesity', 'cholesterol', 'hypertension', 'hypotension',
        'thyroid', 'menopause', 'pregnancy', 'endometriosis',
        'fibroids', 'cysts', 'polyps', 'hemorrhoids', 'hernia',
        'ulcer', 'GERD', 'IBS', 'IBD', 'Crohn', 'celiac',
        'kidney stones', 'gallstones', 'gout', 'osteoporosis',
        'scoliosis', 'stenosis', 'spondylosis', 'tendinitis',
        'bursitis', 'fasciitis', 'plantar', 'carpal tunnel',
        'pink eye', 'stye', 'chalazion', 'cataract'
    ]
    
    for d in disease_indicators:
        if d in name_l:
            return False
    
    return True

# Find new entries
new_entries = []
for e in emed_clean:
    if not matches_existing(e, existing):
        new_entries.append(e)

print(f"Total eMedicineHealth entries: {len(emed_clean)}")
print(f"Existing symptoms: {len(existing)}")
print(f"New (not in existing): {len(new_entries)}")
print()

# Separate symptom-like from disease-like
symptom_new = [e for e in new_entries if is_symptom_like(e)]
disease_new = [e for e in new_entries if not is_symptom_like(e)]

print("=== POTENTIAL NEW SYMPTOMS (symptom-like) ===")
for s in sorted(symptom_new):
    print(f"  {s}")

print()
print(f"\n=== DISEASES/CONDITIONS (not symptoms) ===")
for s in sorted(disease_new):
    print(f"  {s}")
print()
print(f"\nSymptom-like new: {len(symptom_new)}")
print(f"Disease-like new: {len(disease_new)}")
