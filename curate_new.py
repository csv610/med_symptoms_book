# Curated list of genuinely new symptoms from eMedicineHealth
# These are symptoms/signs (not conditions/diseases) not already in our 178 chapters

NEW_SYMPTOMS = [
    "Amenorrhea",
    "Anal Itching",
    "Anemia",
    "Ascites",
    "Bedwetting",
    "Blood in Urine",
    "Boils",
    "Bruises",
    "Bunions",
    "Canker Sores",
    "Cellulite",
    "Cognitive Deficits",
    "Coma",
    "Concussion",
    "Corns and Calluses",
    "Cyst",
    "Dandruff",
    "Dysphagia",
    "Earwax",
    "Edema",
    "Enlarged Spleen",
    "Eye Floaters",
    "Fainting",
    "Flatulence",
    "Frequent Urination",
    "Frostbite",
    "Gastrointestinal Bleeding",
    "Gynecomastia",
    "Heat Cramps",
    "Heat Exhaustion",
    "Heat Stroke",
    "Hematoma",
    "High Blood Sugar",
    "Hives",
    "Hyperhidrosis",
    "Hyphema",
    "Hypothermia",
    "Inability to Urinate",
    "Indigestion",
    "Ingrown Hair",
    "Ingrown Toenail",
    "Internal Bleeding",
    "Low Blood Sugar",
    "Lymphedema",
    "Mittelschmerz",
    "Nail Psoriasis",
    "Narcolepsy",
    "Night Terrors",
    "Overactive Bladder",
    "Pain After Surgery",
    "Pinched Nerve",
    "Pleurisy",
    "Pressure Sores",
    "Prolapsed Bladder",
    "Rectal Prolapse",
    "Scabies",
    "Shin Splints",
    "Shock",
    "Skin Tags",
    "Splinters",
    "Stool Color Changes",
    "Stretch Marks",
    "Sty",
    "Subconjunctival Hemorrhage",
    "Subungual Hematoma",
    "Sunburn",
    "Swollen Lymph Glands",
    "Tailbone Pain",
    "Teething",
    "Testicular Pain",
    "Testicular Swelling",
    "Vaginal Bleeding",
    "Vaginal Prolapse",
    "Vomiting and Nausea",
]

# Remove entries we already have (double-check)
ALREADY_EXIST = {
    "eye floaters",  # we have "floaters"
    "menstrual pain",  # we have "menstrual cramps" - close enough
    "hyperventilation",  # we have it
    "nosebleeds",  # we have "nosebleed"
    "tremors",  # we have "hand tremor"
    "vomiting and nausea",  # we have "vomiting" 
}

# Also remove things that overlap with already existing chapters via different names
EXISTING_CHAPTER_NAMES = """
symptom_amenorrhea
symptom_anal_itching
symptom_anemia
symptom_ascites
symptom_bedwetting
symptom_blood_in_urine
symptom_boils
symptom_bruises
symptom_bunions
symptom_canker_sores
symptom_cellulite
symptom_cognitive_deficits
symptom_coma
symptom_concussion
symptom_corns_and_calluses
symptom_cyst
symptom_dandruff
symptom_dysphagia
symptom_earwax
symptom_edema
symptom_enlarged_spleen
symptom_eye_floaters
symptom_fainting
symptom_flatulence
symptom_frequent_urination
symptom_frostbite
symptom_gastrointestinal_bleeding
symptom_gynecomastia
symptom_heat_cramps
symptom_heat_exhaustion
symptom_heat_stroke
symptom_hematoma
symptom_high_blood_sugar
symptom_hives
symptom_hyperhidrosis
symptom_hyphema
symptom_hypothermia
symptom_inability_to_urinate
symptom_indigestion
symptom_ingrown_hair
symptom_ingrown_toenail
symptom_internal_bleeding
symptom_low_blood_sugar
symptom_lymphedema
symptom_mittelschmerz
symptom_nail_psoriasis
symptom_narcolepsy
symptom_night_terrors
symptom_overactive_bladder
symptom_pain_after_surgery
symptom_pinched_nerve
symptom_pleurisy
symptom_pressure_sores
symptom_prolapsed_bladder
symptom_rectal_prolapse
symptom_scabies
symptom_shin_splints
symptom_shock
symptom_skin_tags
symptom_splinters
symptom_stool_color_changes
symptom_stretch_marks
symptom_sty
symptom_subconjunctival_hemorrhage
symptom_subungual_hematoma
symptom_sunburn
symptom_swollen_lymph_glands
symptom_tailbone_pain
symptom_teething
symptom_testicular_pain
symptom_testicular_swelling
symptom_vaginal_bleeding
symptom_vaginal_prolapse
""".strip().split('\n')

print(f"Curated new symptoms: {len(NEW_SYMPTOMS)}")
print(f"Potential new chapter files: {len(EXISTING_CHAPTER_NAMES)}")

# Check for existing files
import os, glob
existing_files = set()
for fname in EXISTING_CHAPTER_NAMES:
    fpath = f"chapters/{fname}.tex"
    if os.path.exists(fpath):
        existing_files.add(fname)
        print(f"  EXISTS: {fname}.tex")

print(f"\nAlready exist: {len(existing_files)}")
print(f"Net new: {len(EXISTING_CHAPTER_NAMES) - len(existing_files)}")
