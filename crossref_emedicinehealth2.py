import re, sys

# Read existing symptoms
with open('/tmp/existing_symptoms.txt') as f:
    existing = [line.strip().lower() for line in f if line.strip()]

# Hardcoded list of eMedicineHealth symptom-like entries
# (pre-filtered to remove obvious diseases/conditions)
emed_symptoms = [
    "Abscess",
    "Abscessed Tooth",
    "Allergic Reaction",
    "Amenorrhea",
    "Anal Itching",
    "Anemia",
    "Animal Bites",
    "Ascites",
    "Bedwetting",
    "Bladder Control Problems",
    "Blood in the Urine (Hematuria)",
    "Boils",
    "Bruises",
    "Bunions",
    "Canker Sores",
    "Cellulite",
    "Cognitive Deficits",
    "Cold Hands and Feet",
    "Coma",
    "Concussion",
    "Corns and Calluses",
    "Cyst",
    "Dandruff",
    "Dysphagia (Swallowing Problems)",
    "Earwax",
    "Edema",
    "Enlarged Prostate",
    "Enlarged Spleen (Splenomegaly)",
    "Eye Allergies",
    "Eye Floaters",
    "Eyelid Inflammation (Blepharitis)",
    "Fainting",
    "Female Sexual Problems",
    "Flatulence (Gas)",
    "Foreign Body, Ear",
    "Foreign Body, Eye",
    "Foreign Body, Rectum",
    "Foreign Body, Vagina",
    "Frequent Urination",
    "Frostbite",
    "Ganglion Cyst",
    "Gastrointestinal Bleeding",
    "Gynecomastia",
    "Hair Loss",
    "Head Injury",
    "Hearing Loss",
    "Heat Cramps",
    "Heat Exhaustion",
    "Heat Rash",
    "Heat Stroke",
    "Hematoma",
    "High Blood Sugar (Hyperglycemia)",
    "Hives and Angioedema",
    "Hyperhidrosis (Excessive Sweating)",
    "Hyperventilation",
    "Hyphema (Bleeding in Eye)",
    "Hypothermia",
    "Inability to Urinate",
    "Indigestion",
    "Ingrown Hair",
    "Ingrown Toenails",
    "Insect Bites",
    "Internal Bleeding",
    "Jock Itch",
    "Knee Injury",
    "Labor Signs",
    "Laryngitis",
    "Low Blood Sugar (Hypoglycemia)",
    "Lymphedema",
    "Menstrual Pain",
    "Mittelschmerz",
    "Motion Sickness",
    "Muscle Cramps",
    "Nail Injuries",
    "Nail Psoriasis",
    "Narcolepsy",
    "Night Terrors",
    "Nosebleeds",
    "Overactive Bladder",
    "Pain After Surgery",
    "Pain During Intercourse",
    "Painful Urination Symptoms and Signs",
    "Palpitations",
    "Pinched Nerve",
    "Pleurisy",
    "Pressure Sores",
    "Prolapsed Bladder",
    "Prolapsed Uterus",
    "Rectal Bleeding",
    "Rectal Pain",
    "Rectal Prolapse",
    "Scabies",
    "Sciatica",
    "Shin Splints",
    "Shock",
    "Skin Tags",
    "Snoring",
    "Sore Throat",
    "Splinters",
    "Stool Color Changes",
    "Stress Health",
    "Stretch Marks",
    "Sty",
    "Subconjunctival Hemorrhage (Bleeding in Eye)",
    "Subungual Hematoma (Bleeding Under Nail)",
    "Sunburn",
    "Swollen Lymph Glands",
    "Swollen Testicles Causes, Symptoms and Signs",
    "Tailbone (Coccyx) Injury",
    "Teething",
    "Testicular Pain",
    "Testicular Swelling",
    "Tinnitus",
    "Toothache",
    "Torn or Detached Nail",
    "Tremors",
    "Vaginal Bleeding",
    "Vaginal Discharge",
    "Vaginal Prolapse",
    "Vertigo",
    "Vomiting and Nausea",
    "Wound Care",
    "Wrist Injury",
]

def normalize(name):
    n = name.lower().strip()
    n = re.sub(r'\([^)]*\)', '', n)
    # Common suffixes
    for suffix in [' health', ' overview', ' symptoms and signs', ' causes, symptoms and signs',
                   ' in adults', ' in children', '(gas)', ' symptoms']:
        n = re.sub(re.escape(suffix) + '$', '', n)
    n = re.sub(r'\s+and\s+', ' ', n)
    n = n.strip()
    return n

# Check each
print("=== eMedicineHealth symptom entries vs existing chapters ===\n")
new_symptoms = []
for s in sorted(emed_symptoms):
    s_lower = s.lower().strip()
    s_norm = normalize(s)
    
    matched = False
    match_reason = ""
    
    for e in existing:
        e_norm = e  # already lowercased
        if s_lower == e_norm:
            matched = True
            match_reason = f"EXACT: {e}"
            break
        if s_norm == e_norm:
            matched = True
            match_reason = f"NORM: {e}"
            break
        # Check if any word overlap
        s_words = set(s_norm.split())
        e_words = set(e_norm.split())
        common = s_words & e_words
        if len(common) >= 3 and len(common) >= min(len(s_words), len(e_words)) * 0.7:
            matched = True
            match_reason = f"WORDS: {e} (common: {common})"
            break
    
    if matched:
        print(f"  HAS: {s:50s} -> {match_reason}")
    else:
        print(f"  NEW: {s:50s}")
        new_symptoms.append(s)

print(f"\n\n=== NOVEL SYMPTOMS ({len(new_symptoms)}) ===")
for s in sorted(new_symptoms):
    # Generate file name
    fname = 'symptom_' + s.lower().replace(' ', '_').replace(',', '').replace('-', '_').replace("'", '').replace('/', '_').replace('(', '').replace(')', '').replace('__', '_').strip('_')
    print(f"  {fname}.tex")
