#!/usr/bin/env python3
"""Generate missing symptom chapters from healthdirect.gov.au list."""
import os

chapters_dir = '/Users/csv610/Projects/MyBooks/MedSymptoms/chapters'

def create_chapter(title, definition, pathophysiology, causes, seek_advice, related, short_name=None):
    if short_name:
        base = short_name
    else:
        # Clean name: remove parenthesized text and normalize
        clean = title.split('(')[0].strip().rstrip()
        base = clean.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace(',', '').rstrip('_')
    
    lines = []
    lines.append('\\chapter{' + title + '}')
    lines.append('')
    lines.append('\\section*{Definition}')
    lines.append(definition)
    lines.append('')
    lines.append('\\section*{Pathophysiology}')
    lines.append(pathophysiology)
    lines.append('')
    lines.append('\\section*{Etiology}')
    lines.append('\\begin{itemize}')
    for c in causes:
        lines.append('  \\item ' + c)
    lines.append('\\end{itemize}')
    lines.append('')
    lines.append('\\section*{Indications for Evaluation}')
    lines.append('Seek care if:')
    lines.append('\\begin{itemize}')
    lines.append('  \\item Severe or worsening symptoms')
    lines.append('  \\item ' + seek_advice)
    lines.append('  \\item Accompanied by other concerning signs')
    lines.append('\\end{itemize}')
    lines.append('')
    lines.append('\\section*{Related Symptoms}')
    lines.append('May occur with: ' + ', '.join(related))
    lines.append('')
    lines.append('\\textbf{Note:} Always consider serious underlying conditions when evaluating persistent ' + title.lower() + '.')
    lines.append('')
    lines.append('\\section*{Self-Care / Home Management}')
    lines.append('\\begin{itemize}')
    lines.append('  \\item Rest and avoid activities that may aggravate the condition.')
    lines.append('  \\item Maintain adequate hydration and a balanced diet.')
    lines.append('  \\item Over-the-counter remedies may provide symptomatic relief (consult a pharmacist or doctor).')
    lines.append('  \\item Monitor symptoms and seek professional advice if they persist or worsen.')
    lines.append('  \\item Avoid self-medicating with prescription medications without medical guidance.')
    lines.append('\\end{itemize}')
    lines.append('')
    lines.append('\\section*{Diagnostic Approach}')
    lines.append('\\begin{itemize}')
    lines.append('  \\item A thorough history and physical examination are the first steps in evaluation.')
    lines.append('  \\item Laboratory tests (blood work, urinalysis) may be ordered based on clinical suspicion.')
    lines.append('  \\item Imaging studies (X-ray, ultrasound, CT, MRI) may be indicated when structural pathology is suspected.')
    lines.append('  \\item Specialist referral is arranged when the diagnosis remains uncertain or requires specific expertise.')
    lines.append('\\end{itemize}')
    lines.append('')
    lines.append('\\section*{Treatment / Management Overview}')
    lines.append('\\begin{itemize}')
    lines.append('  \\item Treatment targets the underlying cause identified through diagnostic evaluation.')
    lines.append('  \\item Supportive care and symptom management are provided while awaiting definitive therapy.')
    lines.append('  \\item Medications, lifestyle modifications, and physical therapies may be prescribed as appropriate.')
    lines.append('  \\item Follow-up ensures treatment effectiveness and allows timely adjustments to the care plan.')
    lines.append('\\end{itemize}')
    lines.append('')
    lines.append('\\clearpage')
    
    content = '\n'.join(lines)
    filename = chapters_dir + '/symptom_' + base + '.tex'
    with open(filename, 'w') as f:
        f.write(content)
    return filename

# Missing symptoms from healthdirect.gov.au not yet in existing chapters
missing = [
    {
        'title': 'Bloating',
        'definition': 'Abdominal distension, fullness, or tightness sensation caused by excess gas accumulation in the gastrointestinal tract, often accompanied by visible swelling of the abdomen.',
        'pathophysiology': 'Gas accumulation results from swallowed air (aerophagia), bacterial fermentation of undigested food in the colon, or impaired gas transit/evacuation. Visceral hypersensitivity amplifies the perception of normal gas volumes in patients with functional bowel disorders.',
        'causes': [
            'Irritable bowel syndrome (IBS)',
            'Small intestinal bacterial overgrowth (SIBO)',
            'Constipation',
            'Food intolerances (lactose, fructose, gluten)',
            'Swallowing air (aerophagia)',
            'Gastroparesis or delayed gastric emptying',
            'Ovarian pathology (cysts, masses)',
            'Celiac disease',
            'Gastrointestinal obstruction',
            'Ascites from liver disease or malignancy'
        ],
        'seek_advice': 'Persistent bloating lasting more than 2 weeks, bloating with abdominal pain, unexplained weight loss, or changes in bowel habits',
        'related': ['Abdominal pain', 'Flatulence', 'Constipation', 'Diarrhea', 'Nausea']
    },
    {
        'title': 'Earache',
        'definition': 'Pain or discomfort localized to the ear, ranging from dull ache to sharp stabbing sensation, originating from the external, middle, or inner ear structures or referred from adjacent regions.',
        'pathophysiology': 'Ear pain arises from inflammation, infection, pressure changes, or irritation of the auricle, ear canal, tympanic membrane, or middle ear structures. Referred pain occurs via shared innervation with the temporomandibular joint, teeth, sinuses, and pharynx through cranial nerves V, VII, IX, and X.',
        'causes': [
            'Otitis media (middle ear infection)',
            'Otitis externa (swimmer\'s ear)',
            'Eustachian tube dysfunction',
            'Temporomandibular joint (TMJ) disorders',
            'Dental infections or abscesses',
            'Foreign body in ear canal',
            'Earwax impaction',
            'Perforated tympanic membrane',
            'Mastoiditis',
            'Referred pain from tonsillitis or pharyngitis'
        ],
        'seek_advice': 'Severe ear pain, fever, hearing loss, ear discharge, or pain persisting more than 2-3 days',
        'related': ['Hearing loss', 'Fever', 'Ear discharge', 'Dizziness', 'Headache']
    },
    {
        'title': 'Nosebleed (Epistaxis)',
        'definition': 'Bleeding from the nasal cavity, arising from the anterior septum (Kiesselbach plexus, 90%) or posterior nasal cavity (more severe, especially in elderly).',
        'pathophysiology': 'Nasal mucosal vessels are superficial and fragile; anterior epistaxis from Little\'s area (Kiesselbach plexus) where several arteries anastomose. Posterior epistaxis arises from Woodruff plexus in the inferior meatus. Bleeding may be spontaneous or triggered by trauma, dryness, inflammation, or systemic coagulopathy.',
        'causes': [
            'Nasal trauma or picking',
            'Dry air (low humidity, heating, air conditioning)',
            'Allergic rhinitis or sinusitis',
            'Anticoagulant medications (warfarin, aspirin, clopidogrel)',
            'Nasal tumors or polyps',
            'Coagulation disorders (hemophilia, von Willebrand disease)',
            'Hypertension (especially posterior bleeds)',
            'Pregnancy (hormonal vascular changes)',
            'Cocaine use or intranasal medications',
            'Hereditary hemorrhagic telangiectasia (Osler-Weber-Rendu)'
        ],
        'seek_advice': 'Bleeding persisting more than 20 minutes despite direct pressure, recurrent episodes, heavy blood loss, or bleeding on anticoagulation therapy',
        'related': ['Nasal congestion', 'Headache', 'Dizziness', 'Pale skin (anemia)', 'Easy bruising']
    },
    {
        'title': 'Runny Nose (Rhinorrhea)',
        'definition': 'Excessive discharge of nasal mucus from the nostrils, varying in consistency from clear and watery to thick and purulent, reflecting underlying etiology.',
        'pathophysiology': 'Increased nasal secretion from goblet cells and submucosal glands triggered by viral infection, allergic response (IgE-mediated mast cell degranulation), vasomotor instability, or irritation. Clear rhinorrhea suggests allergy or viral etiology; purulent discharge suggests bacterial sinusitis.',
        'causes': [
            'Common cold (viral URI)',
            'Allergic rhinitis (hay fever)',
            'Sinusitis (acute or chronic)',
            'Vasomotor rhinitis',
            'Cold weather or temperature changes',
            'Spicy foods (gustatory rhinitis)',
            'Nasal polyps',
            'Cerebrospinal fluid leak (clear watery unilateral)',
            'Pregnancy rhinitis',
            'Medication-induced (rhinitis medicamentosa from decongestant overuse)'
        ],
        'seek_advice': 'Persistent symptoms beyond 10 days, thick yellow/green discharge with facial pain, fever, bloody discharge, or unilateral clear drainage after head trauma',
        'related': ['Sneezing', 'Nasal congestion', 'Sore throat', 'Cough', 'Itchy eyes']
    },
    {
        'title': 'Bad Breath (Halitosis)',
        'definition': 'Unpleasant odor of the breath, caused primarily by volatile sulfur compounds produced by bacterial metabolism in the oral cavity, and occasionally from systemic conditions.',
        'pathophysiology': 'Anaerobic gram-negative bacteria in the oral biofilm (especially on the posterior tongue dorsum, periodontal pockets, and tonsillar crypts) degrade sulfur-containing amino acids producing hydrogen sulfide, methyl mercaptan, and dimethyl sulfide. Extrinsic sources include sinonasal, respiratory, gastrointestinal, and metabolic causes.',
        'causes': [
            'Poor oral hygiene (tongue coating, food debris)',
            'Periodontal disease (gingivitis, periodontitis)',
            'Tonsillitis or tonsil stones (tonsilloliths)',
            'Dry mouth (xerostomia)',
            'Dental caries or abscesses',
            'Sinusitis or postnasal drip',
            'Gastroesophageal reflux disease (GERD)',
            'Strong foods (garlic, onions, spices)',
            'Smoking or tobacco use',
            'Systemic diseases (diabetes, liver failure, kidney failure)'
        ],
        'seek_advice': 'Persistent halitosis despite good oral hygiene, associated with dental pain, fever, or other systemic symptoms',
        'related': ['Dry mouth', 'Dental pain', 'Postnasal drip', 'Sore throat', 'Acid reflux']
    },
    {
        'title': 'Tinnitus (Ringing in the Ears)',
        'definition': 'Perception of sound in the absence of an external acoustic stimulus, described as ringing, buzzing, hissing, humming, or clicking, which may be unilateral or bilateral, continuous or intermittent.',
        'pathophysiology': 'Abnormal neural activity in the auditory pathway, from cochlear hair cell damage to central auditory cortex reorganization. Subtypes include objective (arising from vascular or muscular sources near the ear) and subjective (much more common, arising from auditory system dysfunction).',
        'causes': [
            'Noise-induced hearing loss',
            'Age-related hearing loss (presbycusis)',
            'Meniere disease',
            'Otosclerosis',
            'Cerumen impaction (earwax)',
            'Ototoxic medications (aspirin, NSAIDs, aminoglycosides, loop diuretics)',
            'Vascular disorders (pulsatile tinnitus — AV malformations, carotid stenosis)',
            'Temporomandibular joint (TMJ) disorders',
            'Head or neck injury',
            'Acoustic neuroma (vestibular schwannoma)'
        ],
        'seek_advice': 'Sudden onset tinnitus, pulsatile tinnitus, tinnitus with hearing loss, dizziness, or focal neurological symptoms',
        'related': ['Hearing loss', 'Vertigo', 'Ear fullness', 'Headache', 'Dizziness']
    },
    {
        'title': 'Brain Fog',
        'definition': 'A subjective sensation of mental clouding or cognitive dysfunction characterized by difficulty concentrating, forgetfulness, slowed thinking, and reduced mental clarity.',
        'pathophysiology': 'Multifactorial disruption of cognitive processing involving neuroinflammation, altered neurotransmitter balance, impaired cerebral blood flow, hormonal dysregulation, and sleep disruption. Often associated with chronic illness, stress, hormonal changes, or medication effects.',
        'causes': [
            'Chronic fatigue syndrome (myalgic encephalomyelitis)',
            'Fibromyalgia',
            'Autoimmune diseases (lupus, multiple sclerosis, Sjogren syndrome)',
            'Thyroid dysfunction (hypothyroidism)',
            'Sleep disorders (insomnia, sleep apnea)',
            'Depression and anxiety',
            'Nutritional deficiencies (B12, vitamin D, iron)',
            'Medication side effects (antihistamines, benzodiazepines, opioids)',
            'Long COVID or post-viral syndrome',
            'Chronic stress or burnout'
        ],
        'seek_advice': 'Persistent cognitive symptoms affecting daily function, progressive worsening, or accompanied by other neurological symptoms',
        'related': ['Fatigue', 'Memory loss', 'Headache', 'Sleep disturbance', 'Irritability']
    },
    {
        'title': 'Jaundice',
        'definition': 'Yellowish discoloration of the skin, sclerae, and mucous membranes due to elevated serum bilirubin levels, clinically detectable when bilirubin exceeds 2-3 mg/dL (34-51 µmol/L).',
        'pathophysiology': 'Bilirubin accumulation results from pre-hepatic (hemolysis, ineffective erythropoiesis), hepatic (impaired hepatocyte uptake, conjugation, or excretion), or post-hepatic (biliary obstruction preventing bilirubin excretion into the gut) causes. Unconjugated (indirect) vs conjugated (direct) hyperbilirubinemia distinguished by laboratory testing guides diagnostic workup.',
        'causes': [
            'Viral hepatitis (A, B, C, E)',
            'Alcoholic liver disease or cirrhosis',
            'Gallstones or bile duct obstruction',
            'Pancreatic cancer (head of pancreas)',
            'Hemolytic anemias (sickle cell, spherocytosis)',
            'Drug-induced liver injury (acetaminophen, statins, isoniazid)',
            'Primary biliary cholangitis',
            'Gilbert syndrome (benign unconjugated hyperbilirubinemia)',
            'Acute fatty liver of pregnancy',
            'Autoimmune hepatitis'
        ],
        'seek_advice': 'Any jaundice requires medical evaluation to identify underlying cause quickly',
        'related': ['Dark urine', 'Pale stools', 'Abdominal pain', 'Nausea', 'Itching (pruritus)']
    },
    {
        'title': 'Shoulder Pain',
        'definition': 'Pain or discomfort localized to the shoulder joint and surrounding structures, arising from the glenohumeral joint, acromioclavicular joint, rotator cuff, or referred from cervical spine or viscera.',
        'pathophysiology': 'The shoulder\'s complex anatomy allows extensive range of motion but predisposes to instability and impingement. Rotator cuff muscles (supraspinatus, infraspinatus, teres minor, subscapularis) stabilize the glenohumeral joint; their dysfunction leads to impingement, tendinopathy, or tears. Referred pain from the diaphragm, gallbladder, or heart may present as shoulder pain via phrenic nerve connections.',
        'causes': [
            'Rotator cuff tendinopathy or tear',
            'Frozen shoulder (adhesive capsulitis)',
            'Shoulder impingement syndrome',
            'Acromioclavicular joint arthritis or separation',
            'Glenohumeral osteoarthritis',
            'Bicipital tendinopathy',
            'Labral tear (SLAP tear)',
            'Cervical radiculopathy (referred from neck)',
            'Fracture (proximal humerus, clavicle)',
            'Referred cardiac pain (left shoulder — angina or MI)'
        ],
        'seek_advice': 'Acute shoulder pain after injury, inability to raise arm, fever, or chest pain radiating to shoulder',
        'related': ['Neck pain', 'Arm weakness', 'Limited range of motion', 'Night pain', 'Arm numbness']
    },
    {
        'title': 'Hip Pain',
        'definition': 'Discomfort localized to the hip joint or surrounding structures (groin, lateral thigh, buttock), arising from intra-articular pathology, periarticular soft tissues, or referred sources.',
        'pathophysiology': 'Hip pain localizes differently based on origin: groin pain typically indicates intra-articular pathology (osteoarthritis, labral tear, AVN); lateral thigh pain suggests trochanteric bursitis; buttock pain may arise from the sacroiliac joint, lumbar spine, or posterior hip structures.',
        'causes': [
            'Hip osteoarthritis (degenerative joint disease)',
            'Trochanteric bursitis',
            'Hip labral tear',
            'Avascular necrosis (AVN) of femoral head',
            'Femoroacetabular impingement (FAI)',
            'Hip fracture (especially in elderly/osteoporotic)',
            'Iliopsoas tendinopathy or bursitis',
            'Referred low back pain or sacroiliac dysfunction',
            'Osteitis pubis',
            'Septic arthritis (urgent, with fever and severe pain)'
        ],
        'seek_advice': 'Severe hip pain after fall or injury, inability to bear weight, fever with hip pain, or groin pain with fever',
        'related': ['Groin pain', 'Limping', 'Stiffness', 'Lower back pain', 'Knee pain']
    },
    {
        'title': 'Knee Pain',
        'definition': 'Pain localized to the knee joint and surrounding structures, one of the most common musculoskeletal complaints affecting mobility and quality of life.',
        'pathophysiology': 'The knee\'s weight-bearing role and complex ligamentous/cartilage structures make it vulnerable to acute injury (ligament tears, meniscal tears) and chronic degenerative changes (osteoarthritis). Anterior knee pain suggests patellofemoral pathology; medial/lateral pain suggests meniscal or collateral ligament involvement; diffuse pain suggests inflammatory arthritis.',
        'causes': [
            'Osteoarthritis (degenerative joint disease)',
            'Meniscal tear',
            'Anterior cruciate ligament (ACL) injury',
            'Patellofemoral pain syndrome',
            'Patellar tendinopathy (jumper\'s knee)',
            'Baker\'s cyst (popliteal cyst)',
            'Rheumatoid arthritis or gout',
            'Iliotibial band syndrome',
            'Prepatellar bursitis (housemaid\'s knee)',
            'Septic arthritis or osteomyelitis'
        ],
        'seek_advice': 'Acute knee injury with inability to bear weight, significant swelling, fever, locking, or instability',
        'related': ['Swelling', 'Stiffness', 'Locking or catching', 'Instability (giving way)', 'Limping']
    },
    {
        'title': 'Leg Pain',
        'definition': 'Pain or discomfort anywhere in the lower extremity from the hip to the foot, arising from musculoskeletal, vascular, neurological, or dermatological sources.',
        'pathophysiology': 'Leg pain mechanisms include nociceptive (musculoskeletal injury, inflammation), neuropathic (nerve compression or damage from disc herniation, peripheral neuropathy), ischemic (peripheral arterial disease, DVT), and referred (hip or spine pathology presenting as thigh or leg pain).',
        'causes': [
            'Peripheral arterial disease (claudication)',
            'Deep vein thrombosis (DVT)',
            'Sciatica or lumbar radiculopathy',
            'Muscle strain or tear (hamstring, quadriceps, calf)',
            'Peripheral neuropathy (diabetic, alcoholic)',
            'Varicose veins or chronic venous insufficiency',
            'Compartment syndrome (acute or chronic)',
            'Shin splints (medial tibial stress syndrome)',
            'Stress fracture',
            'Cellulitis or soft tissue infection'
        ],
        'seek_advice': 'Sudden severe leg pain with swelling and redness (possible DVT), leg pain with chest pain or shortness of breath, or non-healing ulcers',
        'related': ['Swelling', 'Numbness or tingling', 'Skin changes', 'Ulcers', 'Calf tenderness']
    },
    {
        'title': 'Calf Pain',
        'definition': 'Pain localized to the posterior lower leg (gastrocnemius and soleus muscles), ranging from mild soreness to severe debilitating pain.',
        'pathophysiology': 'Calf pain most commonly arises from musculoskeletal strain (gastrocnemius or soleus tears), but critical vascular causes (DVT, compartment syndrome, arterial occlusion) must be excluded. The calf muscles are particularly vulnerable to strain during activities involving sudden push-off (sprinting, jumping).',
        'causes': [
            'Gastrocnemius or soleus strain (tennis leg)',
            'Deep vein thrombosis (DVT)',
            'Muscle contusion or hematoma',
            'Achilles tendinopathy or rupture',
            'Baker\'s cyst rupture (pseudothrombophlebitis)',
            'Peripheral arterial disease (claudication)',
            'Compartment syndrome',
            'Cellulitis or soft tissue infection',
            'Electric contusion (charlie horse)',
            'Ruptured popliteal aneurysm'
        ],
        'seek_advice': 'Sudden severe calf pain with swelling, redness, and warmth (DVT concern), or pain after trauma with inability to bear weight',
        'related': ['Leg swelling', 'Knee pain', 'Ankle pain', 'Numbness or tingling', 'Redness or warmth']
    },
    {
        'title': 'Heel Pain',
        'definition': 'Pain localized to the posterior or inferior aspect of the heel, commonly caused by mechanical stress on the plantar fascia or Achilles tendon insertion.',
        'pathophysiology': 'Plantar fasciitis results from repetitive microtrauma and degeneration of the plantar fascia origin at the medial calcaneal tuberosity. Achilles tendinopathy involves degeneration of the Achilles tendon fibers from overuse, poor footwear, or biomechanical abnormalities. Heel pain is characteristically worse with the first steps in the morning or after prolonged sitting.',
        'causes': [
            'Plantar fasciitis (most common cause)',
            'Achilles tendinopathy or insertional tendinitis',
            'Calcaneal stress fracture',
            'Retrocalcaneal bursitis',
            'Heel spur syndrome',
            'Sever disease (calcaneal apophysitis in children)',
            'Fat pad atrophy (especially in elderly)',
            'Tarsal tunnel syndrome',
            'Gout or pseudogout',
            'Seronegative spondyloarthropathy (ankylosing spondylitis, reactive arthritis)'
        ],
        'seek_advice': 'Severe heel pain with inability to bear weight, fever, redness, or swelling over the heel',
        'related': ['Arch pain', 'Achilles tendon pain', 'Ankle pain', 'Foot numbness', 'Morning stiffness']
    },
    {
        'title': 'Wrist Pain',
        'definition': 'Pain or discomfort localized to the wrist joint and surrounding structures, commonly resulting from overuse, trauma, or inflammatory conditions.',
        'pathophysiology': 'The wrist\'s complex anatomy of eight carpal bones, multiple ligaments, and flexor/extensor tendons makes it susceptible to injury. Pain localizes anatomically: radial side (De Quervain tenosynovitis, scaphoid fracture, thumb arthritis), ulnar side (TFCC tear, extensor carpi ulnaris tendinopathy), dorsal (ganglion cyst, intersection syndrome), volar (carpal tunnel syndrome).',
        'causes': [
            'De Quervain tenosynovitis',
            'Carpal tunnel syndrome',
            'Wrist sprain or fracture (scaphoid, distal radius)',
            'Osteoarthritis or post-traumatic arthritis',
            'Ganglion cyst',
            'Rheumatoid arthritis',
            'Gout or pseudogout',
            'Ligamentous injury (TFCC tear)',
            'Tendinopathy (extensor carpi radialis, flexor carpi ulnaris)',
            'Kienböck disease (avascular necrosis of lunate)'
        ],
        'seek_advice': 'Wrist pain after injury, inability to move the wrist, severe swelling, numbness in fingers, or fever',
        'related': ['Hand numbness', 'Finger pain', 'Swelling', 'Weak grip', 'Snapping sensation']
    },
    {
        'title': 'Kidney Pain',
        'definition': 'Pain originating from the kidneys, typically felt in the flank region (costovertebral angle) between the ribs and hip, often radiating to the lower abdomen or groin.',
        'pathophysiology': 'Kidney pain arises from distention of the renal capsule (stretching from inflammation, obstruction, or mass), ureteral colic (smooth muscle spasm from stone passage), or inflammation of renal parenchyma (pyelonephritis). Unlike musculoskeletal back pain, renal pain is typically constant, not positional, and associated with urinary symptoms.',
        'causes': [
            'Nephrolithiasis (kidney stones)',
            'Pyelonephritis (kidney infection)',
            'Ureteral obstruction',
            'Renal infarction or thrombosis',
            'Polycystic kidney disease',
            'Renal cell carcinoma',
            'Glomerulonephritis',
            'Hydronephrosis',
            'Papillary necrosis',
            'Perinephric abscess'
        ],
        'seek_advice': 'Severe flank pain with fever and chills, inability to urinate, blood in urine, or severe unrelenting pain',
        'related': ['Flank pain', 'Blood in urine (hematuria)', 'Fever', 'Nausea and vomiting', 'Dysuria']
    },
    {
        'title': 'Nerve Pain (Neuropathic Pain)',
        'definition': 'Pain caused by damage or dysfunction of the somatosensory nervous system, characterized by burning, shooting, electric shock-like, or stabbing sensations.',
        'pathophysiology': 'Nerve injury leads to abnormal ectopic discharge from damaged axons, altered ion channel expression, central sensitization in the spinal cord dorsal horn, and reduced descending inhibitory control. Neuroplastic changes in the brain amplify pain perception, making neuropathic pain often chronic and difficult to treat.',
        'causes': [
            'Diabetic peripheral neuropathy',
            'Postherpetic neuralgia (shingles)',
            'Trigeminal neuralgia',
            'Sciatica or lumbar radiculopathy',
            'Carpal tunnel syndrome',
            'Multiple sclerosis',
            'Chemotherapy-induced peripheral neuropathy',
            'HIV-associated neuropathy',
            'Alcohol-related neuropathy',
            'Complex regional pain syndrome (CRPS)'
        ],
        'seek_advice': 'New or progressive burning or shooting pain, pain with weakness, numbness, or changes in bladder/bowel function',
        'related': ['Numbness', 'Tingling', 'Burning sensation', 'Weakness', 'Allodynia (pain to light touch)']
    },
    {
        'title': 'Pelvic Pain',
        'definition': 'Chronic or acute pain localized to the lower abdominal region below the umbilicus, involving reproductive, urinary, gastrointestinal, or musculoskeletal structures.',
        'pathophysiology': 'Pelvic pain in women most commonly arises from gynecological sources (endometriosis, adenomyosis, pelvic inflammatory disease, ovarian cysts) but can originate from gastrointestinal (IBS, diverticulitis), urological (interstitial cystitis), or musculoskeletal (pelvic floor dysfunction) systems. Visceral pain is poorly localized and often referred.',
        'causes': [
            'Endometriosis',
            'Pelvic inflammatory disease (PID)',
            'Ovarian cysts or torsion',
            'Uterine fibroids (leiomyomas)',
            'Adenomyosis',
            'Irritable bowel syndrome (IBS)',
            'Interstitial cystitis (painful bladder syndrome)',
            'Pelvic floor dysfunction',
            'Ectopic pregnancy (emergent)',
            'Chronic prostatitis (in men)'
        ],
        'seek_advice': 'Sudden severe pelvic pain, fever, vaginal bleeding in pregnancy, or pain with dizziness/syncope',
        'related': ['Lower back pain', 'Dysmenorrhea (painful periods)', 'Dyspareunia (painful sex)', 'Urinary frequency', 'Constipation']
    },
    {
        'title': 'Anal Pain',
        'definition': 'Pain or discomfort localized to the anal canal and perianal region, often sharp or throbbing, aggravated by sitting and bowel movements.',
        'pathophysiology': 'The anal canal\'s rich nerve supply (somatic innervation below the dentate line) makes it highly sensitive to pain. Acute anal pain commonly results from anal fissure (tear in the anal mucosa) or thrombosed external hemorrhoid. Chronic pain suggests fissure, fistula, abscess, or levator ani syndrome.',
        'causes': [
            'Anal fissure (acute or chronic)',
            'Thrombosed external hemorrhoid',
            'Perianal abscess',
            'Anal fistula',
            'Proctalgia fugax (brief sudden rectal spasm)',
            'Levator ani syndrome (chronic pelvic floor spasm)',
            'Inflammatory bowel disease (Crohn disease, UC)',
            'Proctitis (infectious or radiation-induced)',
            'Pruritus ani with skin breakdown',
            'Anal malignancy (rare)'
        ],
        'seek_advice': 'Severe anal pain preventing bowel movements, fever, purulent drainage, or bleeding with pain',
        'related': ['Rectal bleeding', 'Constipation', 'Itching', 'Swelling', 'Fever']
    },
    {
        'title': 'Groin Pain or Swelling',
        'definition': 'Pain, discomfort, or visible enlargement in the inguinal or pubic region, arising from musculoskeletal, hernia-related, vascular, or genitourinary causes.',
        'pathophysiology': 'Groin pain in younger patients commonly results from adductor muscle strain (sports hernia or athletic pubalgia). Hernias present with bulging aggravated by increased intra-abdominal pressure. Lymphadenopathy suggests infection or malignancy. Testicular causes (torsion, epididymitis) refer pain to groin via shared innervation.',
        'causes': [
            'Inguinal or femoral hernia',
            'Adductor muscle strain (groin pull)',
            'Lymphadenopathy (inguinal lymph nodes)',
            'Epididymitis or orchitis',
            'Testicular torsion or tumor',
            'Osteitis pubis',
            'Hip joint pathology (labral tear, OA)',
            'Kidney stones (referred pain)',
            'Femoral artery pseudoaneurysm (post-catheterization)',
            'Psoas abscess'
        ],
        'seek_advice': 'Severe groin pain with nausea/vomiting (possible strangulated hernia), testicular pain with swelling, or fever with groin pain',
        'related': ['Hip pain', 'Lower abdominal pain', 'Testicular pain', 'Nausea', 'Lump in groin']
    },
    {
        'title': 'Motion Sickness',
        'definition': 'A syndrome of nausea, dizziness, and autonomic symptoms triggered by real or perceived motion, arising from sensory conflict between visual, vestibular, and proprioceptive inputs.',
        'pathophysiology': 'The sensory conflict theory posits motion sickness occurs when information from the vestibular system (detecting motion) does not match visual and proprioceptive inputs. Autonomic activation via the brainstem vomiting center leads to nausea, pallor, cold sweats, and vomiting. Central habituation reduces symptoms over repeated exposure.',
        'causes': [
            'Car travel (especially winding roads)',
            'Boat or sea travel (sea sickness)',
            'Airplane travel',
            'Virtual reality or video simulations',
            'Amusement park rides',
            'Migraine-associated vertigo',
            'Inner ear disorders (Meniere disease, labyrinthitis)',
            'Pregnancy (first trimester)',
            'Migraine headache',
            'Panic disorder or anxiety'
        ],
        'seek_advice': 'Motion sickness with severe or persistent vomiting causing dehydration, or with neurological symptoms',
        'related': ['Nausea', 'Dizziness', 'Sweating', 'Headache', 'Pallor']
    },
    {
        'title': 'Heavy Periods (Menorrhagia)',
        'definition': 'Excessive or prolonged menstrual bleeding defined as soaking through one or more pads/tampons every hour for several consecutive hours, bleeding lasting more than 7 days, or passing large blood clots.',
        'pathophysiology': 'Menorrhagia results from hormonal imbalance (estrogen-progesterone ratio disruption), uterine structural abnormalities (fibroids, polyps, adenomyosis), coagulation disorders, or endometrial dysfunction. Anovulatory cycles common in perimenopause and adolescence lead to unopposed estrogen stimulation causing thickened endometrium and heavy bleeding.',
        'causes': [
            'Uterine fibroids (leiomyomas)',
            'Hormonal imbalance (anovulation, perimenopause)',
            'Adenomyosis',
            'Endometrial polyps',
            'Coagulation disorders (von Willebrand disease, platelet disorders)',
            'Pelvic inflammatory disease',
            'Endometriosis',
            'Thyroid dysfunction (hypothyroidism)',
            'Intrauterine device (IUD) side effects',
            'Endometrial hyperplasia or malignancy'
        ],
        'seek_advice': 'Profuse bleeding soaking more than 1 pad/tampon per hour, bleeding with dizziness or fatigue, or between-period bleeding',
        'related': ['Fatigue (anemia)', 'Abdominal cramps', 'Irregular periods', 'Back pain', 'Pale skin']
    },
    {
        'title': 'Hot Flushes (Hot Flashes)',
        'definition': 'Sudden episodes of intense heat sensation spreading over the upper body and face, often accompanied by sweating, palpitations, and anxiety, primarily associated with hormonal changes.',
        'pathophysiology': 'Estrogen withdrawal (menopausal transition) alters hypothalamic thermoregulatory set-point, narrowing the thermoneutral zone so minor core temperature elevations trigger heat-loss responses (vasodilation, sweating). Fluctuations in luteinizing hormone and norepinephrine also contribute to vasomotor instability.',
        'causes': [
            'Menopause (natural or surgical)',
            'Perimenopause',
            'Medication side effects (SSRIs, tamoxifen, raloxifene)',
            'Thyroid disorders (hyperthyroidism)',
            'Cancer treatment (chemotherapy, radiation, hormone therapy)',
            'Orchidectomy (in men)',
            'Carcinoid syndrome',
            'Adrenal insufficiency',
            'Alcohol or caffeine triggers',
            'Anxiety or panic disorder'
        ],
        'seek_advice': 'Hot flushes with fever, night sweats with weight loss, or flushes interfering significantly with quality of life',
        'related': ['Night sweats', 'Palpitations', 'Anxiety', 'Sleep disturbance', 'Mood swings']
    },
    {
        'title': 'Mood Swings',
        'definition': 'Rapid or extreme fluctuations in emotional state, shifting between euphoria, irritability, sadness, or anger over short periods without clear precipitants.',
        'pathophysiology': 'Mood regulation involves complex interplay between neurotransmitters (serotonin, dopamine, norepinephrine), hormones (estrogen, progesterone, cortisol), and neural circuits (prefrontal cortex, amygdala, hippocampus). Disruption from hormonal changes, stress, sleep deprivation, or psychiatric conditions produces emotional lability.',
        'causes': [
            'Premenstrual syndrome (PMS) or PMDD',
            'Perimenopause and menopause',
            'Pregnancy and postpartum period',
            'Bipolar disorder',
            'Depression or anxiety disorders',
            'Chronic stress',
            'Sleep deprivation',
            'Substance use or withdrawal',
            'Thyroid disorders (hyperthyroidism)',
            'Medication side effects (corticosteroids, antidepressants)'
        ],
        'seek_advice': 'Mood swings with thoughts of self-harm, significant functional impairment, or accompanying severe depression or mania',
        'related': ['Irritability', 'Fatigue', 'Sleep changes', 'Anxiety', 'Appetite changes']
    },
    {
        'title': 'Chronic Wounds',
        'definition': 'Wounds that fail to proceed through orderly healing stages within 4-6 weeks, including pressure ulcers, venous stasis ulcers, diabetic foot ulcers, and arterial insufficiency ulcers.',
        'pathophysiology': 'Healing failure results from prolonged inflammation, impaired angiogenesis, bacterial biofilm formation, and matrix metalloproteinase imbalance. Underlying causes include ischemia (arterial disease), venous hypertension (venous insufficiency), neuropathy and pressure (diabetes), or prolonged pressure (immobility). Biofilm bacteria evade immune clearance and resist antibiotics.',
        'causes': [
            'Venous insufficiency (venous stasis ulcers)',
            'Peripheral arterial disease (ischemic ulcers)',
            'Diabetes mellitus (diabetic foot ulcers)',
            'Prolonged pressure (pressure ulcers/bedsores)',
            'Chronic infection or osteomyelitis',
            'Vasculitis or autoimmune disease',
            'Malignancy (basal cell carcinoma, squamous cell carcinoma)',
            'Radiation therapy damage',
            'Lymphedema',
            'Pyoderma gangrenosum'
        ],
        'seek_advice': 'Any non-healing wound persisting more than 4 weeks, wound with increasing pain, redness, swelling, or purulent drainage',
        'related': ['Leg swelling', 'Skin discoloration', 'Pain', 'Fever', 'Reduced mobility']
    },
    {
        'title': 'Urinary Retention',
        'definition': 'Inability to partially or completely empty the bladder, classified as acute (sudden and painful) or chronic (gradual onset with less discomfort but significant residual urine volume).',
        'pathophysiology': 'Acute retention typically results from mechanical obstruction (BPH, urethral stricture, stone, clot) or neurological causes (spinal cord injury, post-operative). Chronic retention involves detrusor underactivity or bladder outlet obstruction with compensatory detrusor hypertrophy, leading to high post-void residuals, overflow incontinence, and upper tract damage risk.',
        'causes': [
            'Benign prostatic hyperplasia (BPH) — most common cause in men',
            'Urethral stricture',
            'Medication side effects (anticholinergics, antihistamines, decongestants)',
            'Post-operative (anesthesia, opioids, pelvic surgery)',
            'Neurological conditions (spinal cord injury, multiple sclerosis, diabetic neuropathy)',
            'Severe constipation (fecal impaction)',
            'Bladder stones or tumors',
            'Pelvic organ prolapse (cystocele) in women',
            'Prostate cancer or bladder cancer',
            'Phimosis or paraphimosis'
        ],
        'seek_advice': 'Complete inability to urinate (emergency requiring catheterization), painful distension, or acute retention with fever',
        'related': ['Urinary frequency', 'Hesitancy', 'Weak urinary stream', 'Overflow incontinence', 'Abdominal distension']
    },
    {
        'title': 'Vaginal Dryness',
        'definition': 'Insufficient vaginal lubrication causing discomfort, irritation, and pain during sexual activity or daily activities, most commonly due to decreased estrogen levels.',
        'pathophysiology': 'Estrogen maintains vaginal mucosal thickness, elasticity, and lubrication via cervical and Bartholin gland secretions. Estrogen decline (menopause, breastfeeding, medications) leads to mucosal atrophy, decreased blood flow, reduced secretions, and increased vaginal pH predisposing to infection. Vaginal dryness is symptomatic of the genitourinary syndrome of menopause (GSM).',
        'causes': [
            'Menopause (natural or surgical)',
            'Breastfeeding or postpartum period',
            'Medication effects (antihistamines, antidepressants, chemotherapy, tamoxifen)',
            'Sjogren syndrome (autoimmune)',
            'Radiation therapy to pelvis',
            'Hormonal contraception (some types)',
            'Perimenopause',
            'Oophorectomy (surgical removal of ovaries)',
            'Anxiety or inadequate arousal',
            'Chemotherapy or endocrine therapy for breast cancer'
        ],
        'seek_advice': 'Vaginal dryness with painful intercourse, itching, burning, or recurrent urinary tract infections',
        'related': ['Painful sex (dyspareunia)', 'Vaginal itching', 'Urinary frequency', 'Recurrent UTIs', 'Vaginal irritation']
    },
    {
        'title': 'Tachycardia',
        'definition': 'Resting heart rate exceeding 100 beats per minute, classified by origin (sinus, supraventricular, ventricular), duration (paroxysmal, persistent, permanent), and electrocardiographic characteristics.',
        'pathophysiology': 'Tachycardia mechanisms include increased automaticity (enhanced pacemaker activity), triggered activity (afterdepolarizations), or reentry (abnormal conduction circuit). Sinus tachycardia is a physiologic response to increased demand; pathologic tachyarrhythmias (atrial fibrillation, SVT, VT) require specific diagnosis and management.',
        'causes': [
            'Sinus tachycardia (fever, dehydration, anxiety, exercise)',
            'Atrial fibrillation or atrial flutter',
            'Supraventricular tachycardia (SVT, AVNRT, WPW)',
            'Ventricular tachycardia (VT)',
            'Hyperthyroidism',
            'Anemia',
            'Pulmonary embolism',
            'Heart failure or cardiomyopathy',
            'Electrolyte imbalances',
            'Medication or substance effects (caffeine, alcohol, stimulants, thyroid medication)'
        ],
        'seek_advice': 'Resting tachycardia with chest pain, shortness of breath, syncope, or dizziness (possible cardiac arrhythmia)',
        'related': ['Palpitations', 'Shortness of breath', 'Dizziness', 'Chest pain', 'Fatigue']
    },
    {
        'title': 'Heart Murmur',
        'definition': 'An extra or unusual heart sound heard during auscultation, caused by turbulent blood flow across cardiac valves, septal defects, or vascular structures.',
        'pathophysiology': 'Murmurs result from high-flow across normal valves, forward flow across stenotic valves, backward flow across regurgitant valves, or flow across septal defects. Graded by intensity (I-VI), timing (systolic, diastolic, continuous), configuration (crescendo, decrescendo), and quality (blowing, harsh, rumbling).',
        'causes': [
            'Innocent (functional) murmur — benign, no structural heart disease',
            'Aortic stenosis (degenerative, bicuspid valve)',
            'Aortic regurgitation',
            'Mitral regurgitation (mitral valve prolapse, papillary muscle dysfunction)',
            'Mitral stenosis (typically rheumatic heart disease)',
            'Pulmonic stenosis or regurgitation',
            'Hypertrophic cardiomyopathy (HOCM)',
            'Ventricular septal defect (congenital)',
            'Atrial septal defect (congenital)',
            'Infective endocarditis with valve vegetation'
        ],
        'seek_advice': 'New murmur with chest pain, shortness of breath, syncope, fever (possible endocarditis), or unexplained weight loss',
        'related': ['Shortness of breath', 'Chest pain', 'Palpitations', 'Fatigue', 'Leg swelling']
    },
    {
        'title': 'Loss of Smell (Anosmia)',
        'definition': 'Complete or partial inability to perceive odors, which can be temporary or permanent, congenital or acquired.',
        'pathophysiology': 'Anosmia results from either conductive loss (nasal obstruction preventing odorants from reaching olfactory epithelium — sinusitis, polyps, URI) or sensorineural loss (damage to olfactory neuroepithelium, olfactory nerve, or central pathways). Viral-induced anosmia (including COVID-19) arises from inflammation and damage to sustentacular cells supporting olfactory neurons.',
        'causes': [
            'Viral upper respiratory infection (including COVID-19)',
            'Nasal polyps or chronic rhinosinusitis',
            'Allergic rhinitis',
            'Head trauma with cribriform plate fracture',
            'Aging (presbyosmia)',
            'Smoking or toxic chemical exposure',
            'Neurodegenerative diseases (Parkinson disease, Alzheimer disease)',
            'Nasal tumors or sinus neoplasms',
            'Congenital anosmia (Kallmann syndrome)',
            'Medication side effects (zinc nasal sprays, some antibiotics)'
        ],
        'seek_advice': 'Sudden anosmia after head injury, anosmia with neurological symptoms, or persistent loss of smell beyond 4 weeks',
        'related': ['Loss of taste (ageusia)', 'Nasal congestion', 'Runny nose', 'Headache', 'Neurological symptoms']
    },
    {
        'title': 'Delusions',
        'definition': 'Fixed, false beliefs that persist despite contradictory evidence, inconsistent with the individual\'s cultural or religious background, and representing a disturbance in thought content.',
        'pathophysiology': 'Dysfunction in prefrontal cortex (reality testing and belief evaluation) and limbic system (salience attribution) leads to formation and maintenance of delusional beliefs. Dopamine hyperactivity in mesolimbic pathways contributes to aberrant salience where neutral stimuli acquire false meaning. Delusions are categorized by content: persecutory, grandiose, referential, somatic, erotomanic, and nihilistic.',
        'causes': [
            'Schizophrenia or schizoaffective disorder',
            'Bipolar disorder (manic phase)',
            'Major depressive disorder with psychotic features',
            'Delirium (acute confusional state)',
            'Dementia (Alzheimer, Lewy body)',
            'Substance use or withdrawal (amphetamine, cocaine, alcohol withdrawal)',
            'Medication side effects (corticosteroids, anticholinergics, dopaminergic drugs)',
            'Metabolic or endocrine disorders (thyroid disease, B12 deficiency)',
            'Parkinson disease (medication-induced)',
            'Brain tumors or traumatic brain injury'
        ],
        'seek_advice': 'New-onset delusions, especially with agitation, self-harm risk, or inability to care for oneself (immediate psychiatric evaluation)',
        'related': ['Hallucinations', 'Agitation', 'Confusion', 'Suspiciousness', 'Sleep disturbance']
    },
    {
        'title': 'Hallucinations',
        'definition': 'Perception of sensory experiences (visual, auditory, tactile, olfactory, or gustatory) in the absence of external stimuli, arising from neurological or psychiatric dysfunction.',
        'pathophysiology': 'Hallucinations involve aberrant activation of sensory cortex without corresponding external input. Auditory hallucinations (most common in schizophrenia) arise from misattribution of inner speech to external sources via dysfunction in frontotemporal networks. Visual hallucinations suggest organic pathology (delirium, dementia, seizures, migraine).',
        'causes': [
            'Psychiatric disorders (schizophrenia, schizoaffective disorder, bipolar disorder)',
            'Delirium (especially in elderly or hospitalized patients)',
            'Dementia (Lewy body dementia, Alzheimer disease)',
            'Substance use (LSD, psilocybin, PCP, cannabis)',
            'Alcohol withdrawal (delirium tremens)',
            'Seizures (temporal lobe epilepsy)',
            'Migraine with aura (scintillating scotomas, fortification spectra)',
            'Sensory deprivation (Charles Bonnet syndrome in visually impaired)',
            'Brain tumors or strokes affecting sensory pathways',
            'Metabolic derangements (electrolyte imbalance, hepatic encephalopathy)'
        ],
        'seek_advice': 'New-onset hallucinations with confusion, agitation, head injury, or risk of harm to self or others (emergency evaluation)',
        'related': ['Delusions', 'Confusion', 'Agitation', 'Sleep disturbance', 'Anxiety']
    },
    {
        'title': 'Nasal Congestion (Blocked Nose)',
        'definition': 'Obstruction of nasal airflow due to inflammation, swelling of nasal turbinates, mucus accumulation, or structural abnormalities, causing difficulty breathing through the nose.',
        'pathophysiology': 'Nasal congestion results from vasodilation and engorgement of venous sinusoids in the nasal turbinates triggered by inflammation (allergic, infectious), autonomic dysregulation, or medication effects. Mucosal edema narrows nasal passages while increased secretions further obstruct airflow. Chronic causes include structural abnormalities (deviated septum, nasal polyps) or chronic rhinosinusitis.',
        'causes': [
            'Common cold (viral upper respiratory infection)',
            'Allergic rhinitis (hay fever)',
            'Sinusitis (acute or chronic)',
            'Deviated nasal septum',
            'Nasal polyps',
            'Vasomotor rhinitis',
            'Pregnancy rhinitis',
            'Rhinitis medicamentosa (decongestant spray overuse)',
            'Environmental irritants (smoke, pollution, dry air)',
            'Enlarged adenoids or tonsils (in children)'
        ],
        'seek_advice': 'Nasal congestion with high fever, facial swelling, visual changes, or unilateral congestion with bloody discharge',
        'related': ['Runny nose', 'Sneezing', 'Sinus pressure', 'Headache', 'Reduced sense of smell']
    },
    {
        'title': 'Bleeding Between Periods (Spotting)',
        'definition': 'Vaginal bleeding occurring between regular menstrual periods, ranging from light spotting to heavy flow, and including any bleeding after menopause.',
        'pathophysiology': 'Intermenstrual bleeding arises from hormonal imbalance (anovulation, estrogen breakthrough), uterine pathology (polyps, fibroids, hyperplasia), cervical lesions (polyps, cervicitis, dysplasia), or implantation bleeding in pregnancy. Postmenopausal bleeding always requires evaluation to exclude endometrial cancer.',
        'causes': [
            'Hormonal imbalance (anovulatory cycles, perimenopause)',
            'Uterine fibroids or polyps',
            'Cervical polyps, cervicitis, or ectropion',
            'Endometrial hyperplasia or carcinoma',
            'Hormonal contraception (IUD, pills, implant) breakthrough',
            'Pregnancy complications (ectopic pregnancy, threatened miscarriage)',
            'Infection (pelvic inflammatory disease, sexually transmitted infections)',
            'Thyroid disorders',
            'Coagulation disorders',
            'Cervical or vaginal trauma'
        ],
        'seek_advice': 'Any postmenopausal bleeding, heavy intermenstrual bleeding, or bleeding with pain, fever, or pregnancy concerns',
        'related': ['Abnormal menstrual cycles', 'Pelvic pain', 'Fatigue', 'Heavy periods', 'Vaginal discharge']
    },
    {
        'title': 'Blood in Semen (Hematospermia)',
        'definition': 'Presence of blood in the ejaculate, presenting as pink, red, or brown-tinged semen, most often benign and self-limiting but requiring careful evaluation.',
        'pathophysiology': 'Bleeding typically arises from the prostate (most common), seminal vesicles, vas deferens, or urethra. In men under 40, infection or iatrogenic causes predominate; in men over 40, prostate pathology including malignancy must be excluded. Most cases are idiopathic with spontaneous resolution.',
        'causes': [
            'Seminal vesicle or prostate infection (prostatitis, seminal vesiculitis)',
            'Post-prostate biopsy (most common iatrogenic cause)',
            'Urethral stricture or trauma',
            'Prostate calculi',
            'Sexually transmitted infections',
            'Prostate or seminal vesicle cysts',
            'Hypertension or coagulopathy',
            'Prostate cancer (especially in men over 40)',
            'Testicular or prostate trauma',
            'Schistosomiasis (in endemic areas)'
        ],
        'seek_advice': 'Persistent blood in semen beyond 3-4 weeks, recurrent episodes, or men over 40 with associated urinary symptoms',
        'related': ['Dysuria', 'Urinary frequency', 'Perineal pain', 'Fever', 'Lower back pain']
    },
    {
        'title': 'Haemoptysis (Coughing Up Blood)',
        'definition': 'Expectoration of blood or blood-tinged sputum from the respiratory tract below the larynx, distinguishing it from hematemesis (gastrointestinal) and epistaxis (nasal).',
        'pathophysiology': 'Bleeding originates from bronchial arteries (systemic circulation, 90% of significant hemoptysis) or pulmonary arteries (low pressure, less common but catastrophic). Causes include airway inflammation (bronchitis, bronchiectasis), parenchymal disease (pneumonia, TB, malignancy), vascular disorders (AVM, PE), or bleeding diatheses.',
        'causes': [
            'Acute bronchitis (most common cause)',
            'Bronchiectasis',
            'Tuberculosis',
            'Lung cancer or endobronchial tumor',
            'Pneumonia (including lung abscess)',
            'Pulmonary embolism with infarction',
            'Aspergilloma (fungus ball in pre-existing cavity)',
            'Bronchial adenoma or carcinoid tumor',
            'Pulmonary arteriovenous malformation',
            'Autoimmune disease (Wegener granulomatosis, Goodpasture syndrome)'
        ],
        'seek_advice': 'Any episode of hemoptysis requires medical evaluation; large volume (>100mL) or hemodynamic instability requires emergency care',
        'related': ['Cough', 'Shortness of breath', 'Chest pain', 'Fever', 'Weight loss']
    },
    {
        'title': 'Dry Eye Disease (Dry Eyes)',
        'definition': 'A multifactorial disease of the ocular surface characterized by loss of homeostasis of the tear film, accompanied by ocular discomfort symptoms and visual disturbance.',
        'pathophysiology': 'Tear film instability from either reduced tear production (aqueous-deficient dry eye — Sjogren, age, medications) or excessive tear evaporation (meibomian gland dysfunction leading to lipid layer deficiency). Ocular surface inflammation creates a vicious cycle of tear dysfunction, hyperosmolarity, and epithelial damage.',
        'causes': [
            'Aging (reduced tear production with age)',
            'Meibomian gland dysfunction (most common cause)',
            'Environmental factors (dry climate, AC, wind, screen time)',
            'Contact lens wear',
            'Sjogren syndrome (autoimmune)',
            'Medication side effects (antihistamines, decongestants, diuretics, antidepressants)',
            'Hormonal changes (menopause)',
            'Blepharitis (eyelid inflammation)',
            'Refractive surgery (LASIK)',
            'Systemic diseases (rheumatoid arthritis, lupus, diabetes)'
        ],
        'seek_advice': 'Persistent dry eye symptoms despite artificial tears, eye pain, photophobia, or vision changes',
        'related': ['Eye redness', 'Blurred vision', 'Photophobia', 'Eye fatigue', 'Foreign body sensation']
    },
    {
        'title': 'Eye Discharge',
        'definition': 'Abnormal secretion from the eye ranging from clear and watery to thick, purulent, or mucoid, indicating underlying ocular surface or lacrimal system pathology.',
        'pathophysiology': 'Watery discharge typically accompanies viral conjunctivitis or allergic reaction with increased lacrimation. Purulent (yellow/green) discharge indicates bacterial infection with neutrophil accumulation. Mucoid discharge (stringy, white) suggests allergic conjunctivitis. Chronic discharge may indicate lacrimal duct obstruction or dacryocystitis.',
        'causes': [
            'Conjunctivitis (viral, bacterial, or allergic)',
            'Dacryocystitis (lacrimal sac infection)',
            'Nasolacrimal duct obstruction',
            'Keratitis (corneal infection or inflammation)',
            'Stye (hordeolum) or chalazion',
            'Blepharitis (eyelid margin inflammation)',
            'Entropion or ectropion (eyelid malposition)',
            'Foreign body',
            'Contact lens-related infection',
            'Herpes simplex or herpes zoster ophthalmicus'
        ],
        'seek_advice': 'Eye discharge with vision changes, severe eye pain, photophobia, or in contact lens wearers (risk of corneal ulcer)',
        'related': ['Eye redness', 'Itchy eyes', 'Blurred vision', 'Eye pain', 'Photophobia']
    },
    {
        'title': 'Eye Strain (Asthenopia)',
        'definition': 'Ocular discomfort, fatigue, or pain associated with prolonged visual tasks, eye muscle imbalance, or uncorrected refractive errors.',
        'pathophysiology': 'Prolonged near-work (digital screens, reading) causes sustained contraction of ciliary muscle (accommodation) and medial rectus muscles (convergence), leading to muscle fatigue, reduced blink rate, and ocular surface drying. Accommodative spasm may follow prolonged near-focus, causing transient distance blur.',
        'causes': [
            'Prolonged screen time (computer vision syndrome / digital eye strain)',
            'Uncorrected refractive errors (myopia, hyperopia, astigmatism, presbyopia)',
            'Poor lighting or glare',
            'Decreased blink rate while concentrating',
            'Dry eye disease',
            'Accommodative or convergence insufficiency',
            'Small font sizes or poor screen contrast',
            'Postural issues (looking up vs. down at screens)',
            'Reading in dim light',
            'Eye muscle imbalance'
        ],
        'seek_advice': 'Persistent eye strain despite taking breaks and correcting ergonomics, or eye strain with headaches, double vision, or vision changes',
        'related': ['Headache', 'Blurred vision', 'Dry eyes', 'Neck pain', 'Photophobia']
    },
    {
        'title': 'Facial Droop',
        'definition': 'Unilateral or bilateral weakness of facial muscles resulting in asymmetry of expression, inability to close the eye or raise the eyebrow, and flattening of the nasolabial fold.',
        'pathophysiology': 'Facial droop results from dysfunction of the facial nerve (cranial nerve VII) at any point from its nucleus in the pons to its peripheral branches. Lower motor neuron lesions (Bell palsy, Ramsay Hunt, Lyme) affect entire ipsilateral face; upper motor neuron lesions (stroke, tumor) spare the forehead due to bilateral cortical innervation.',
        'causes': [
            'Bell palsy (idiopathic facial nerve palsy)',
            'Stroke or transient ischemic attack (upper motor neuron)',
            'Ramsay Hunt syndrome (herpes zoster oticus)',
            'Lyme disease (borreliosis)',
            'Brain tumor or metastatic lesion',
            'Traumatic facial nerve injury',
            'Otitis media or mastoiditis',
            'Guillain-Barre syndrome (bilateral facial weakness)',
            'Sarcoidosis (Heerfordt syndrome)',
            'Myasthenia gravis (fatigable weakness)'
        ],
        'seek_advice': 'Sudden facial droop requires immediate medical evaluation to differentiate stroke from Bell palsy (FAST assessment)',
        'related': ['Arm or leg weakness', 'Speech difficulty', 'Ear pain', 'Eye closure difficulty', 'Drooling']
    },
    {
        'title': 'Hiccups (Singultus)',
        'definition': 'Involuntary, spasmodic contractions of the diaphragm followed by sudden glottic closure producing the characteristic "hic" sound, mediated by a reflex arc involving the phrenic nerve and vagus nerve.',
        'pathophysiology': 'The hiccup reflex arc involves afferent fibers (phrenic and vagus nerves, sympathetic chain from T6-T12), central coordinator in the brainstem (medulla, reticular formation), and efferent fibers (phrenic nerve to diaphragm, vagus nerve to glottis). Hiccups lasting >48h (persistent) or >1 month (intractable) require investigation for underlying pathology.',
        'causes': [
            'Gastric distension (overeating, carbonated drinks, swallowing air)',
            'Sudden temperature changes (hot then cold food/drink)',
            'Alcohol consumption',
            'Excitement or emotional stress',
            'Gastroesophageal reflux disease (GERD)',
            'Medication side effects (benzodiazepines, barbiturates, corticosteroids)',
            'Central nervous system disorders (stroke, tumor, multiple sclerosis)',
            'Diaphragmatic irritation (pneumonia, pleurisy, pericarditis)',
            'Metabolic disorders (uremia, diabetes, electrolyte imbalance)',
            'Post-operative (especially abdominal or thoracic surgery)'
        ],
        'seek_advice': 'Hiccups persisting more than 48 hours, hiccups with severe pain, or associated with neurological symptoms',
        'related': ['GERD', 'Abdominal distension', 'Chest discomfort', 'Nausea', 'Fatigue']
    },
    {
        'title': 'Irregular Periods',
        'definition': 'Menstrual cycles that vary significantly from the typical 21-35 day pattern, including absent periods (amenorrhea), infrequent periods (oligomenorrhea), or unpredictable cycle length.',
        'pathophysiology': 'Normal menstruation requires intact hypothalamic-pituitary-ovarian axis with appropriate hormone levels. Disruption at any level causes irregular bleeding: hypothalamic (stress, exercise, weight loss), pituitary (prolactinoma), ovarian (PCOS, perimenopause, premature ovarian failure), uterine (fibroids, polyps), or endocrine (thyroid, adrenal) causes.',
        'causes': [
            'Polycystic ovary syndrome (PCOS)',
            'Perimenopause (transition to menopause)',
            'Thyroid disorders (hyperthyroidism or hypothyroidism)',
            'Hyperprolactinemia',
            'Stress or significant weight changes',
            'Excessive exercise (athletic amenorrhea)',
            'Eating disorders (anorexia nervosa)',
            'Uterine fibroids or polyps',
            'Primary ovarian insufficiency (premature menopause)',
            'Hormonal contraception effects'
        ],
        'seek_advice': 'Missed periods for 3+ cycles, very heavy bleeding, bleeding between periods, or difficulty conceiving',
        'related': ['Heavy bleeding', 'Pelvic pain', 'Weight changes', 'Hair growth changes', 'Acne']
    },
    {
        'title': 'Lump Under Armpit (Axillary Mass)',
        'definition': 'A palpable swelling or mass in the axillary region, most commonly representing enlarged lymph nodes but also arising from breast tissue, skin lesions, or subcutaneous structures.',
        'pathophysiology': 'Axillary lymph nodes drain the upper limb, breast, chest wall, and upper back. Lymphadenopathy results from infection (local or systemic), inflammatory conditions, or malignancy (lymphoma, breast cancer metastasis). Other causes include sebaceous cysts, lipomas, hidradenitis suppurativa, and accessory breast tissue.',
        'causes': [
            'Lymphadenopathy (reactive from infection of arm/hand)',
            'Breast cancer metastasis',
            'Lymphoma or leukemia',
            'Sebaceous cyst or epidermoid cyst',
            'Lipoma (benign fatty tumor)',
            'Hidradenitis suppurativa (inflamed sweat gland)',
            'Cat scratch disease (Bartonella henselae)',
            'Tuberculosis or mycobacterial infection',
            'Sarcoidosis',
            'Vaccination reaction (recent COVID-19, flu, or other vaccine)'
        ],
        'seek_advice': 'Firm, fixed, non-tender lump, progressive enlargement, or lump with fever, night sweats, or unexplained weight loss',
        'related': ['Breast lump', 'Arm swelling', 'Fever', 'Night sweats', 'Weight loss']
    },
    {
        'title': 'Morning Sickness (Nausea Gravidarum)',
        'definition': 'Nausea and vomiting experienced during pregnancy, typically beginning around week 6, peaking around week 9, and resolving by week 14-16, though symptoms may begin earlier or persist longer.',
        'pathophysiology': 'Rising human chorionic gonadotropin (hCG) and estrogen levels during early pregnancy stimulate the brainstem vomiting center. Other contributing factors include enhanced olfactory sensitivity, delayed gastric emptying, and gastroesophageal reflux. Psychological factors and prior history of motion sickness may increase susceptibility.',
        'causes': [
            'Normal pregnancy-related hormonal changes',
            'Elevated hCG levels (more severe in multiple pregnancies or molar pregnancy)',
            'Estrogen surge in first trimester',
            'Enhanced sense of smell',
            'Delayed gastric emptying',
            'Gastroesophageal reflux',
            'Multiparous pregnancy history',
            'Personal or family history of hyperemesis gravidarum',
            'Migraine susceptibility',
            'Psychological factors (stress, anxiety)'
        ],
        'seek_advice': 'Severe vomiting causing dehydration (inability to keep fluids down), weight loss, or ketosis (hyperemesis gravidarum)',
        'related': ['Fatigue', 'Food aversions', 'Weight loss', 'Dehydration', 'Dizziness']
    },
    {
        'title': 'Painful Sex (Dyspareunia)',
        'definition': 'Recurrent or persistent genital pain occurring before, during, or after sexual intercourse, classified as superficial (introital) or deep pelvic pain.',
        'pathophysiology': 'Superficial dyspareunia involves vulvar, vestibular, or vaginal pathology (lack of lubrication, vulvodynia, vaginismus, infection, atrophy). Deep dyspareunia (pelvic pain with thrusting) indicates upper reproductive tract pathology (endometriosis, PID, ovarian cyst, adenomyosis) or non-gynecologic causes (IBS, interstitial cystitis).',
        'causes': [
            'Vaginal dryness (especially menopause or breastfeeding)',
            'Vaginismus (involuntary pelvic floor muscle spasm)',
            'Vulvodynia or vestibulodynia (chronic vulvar pain)',
            'Endometriosis',
            'Pelvic inflammatory disease (PID)',
            'Ovarian cysts',
            'Interstitial cystitis (painful bladder syndrome)',
            'Uterine fibroids or adenomyosis',
            'Irritable bowel syndrome',
            'Postpartum perineal changes or scar tissue'
        ],
        'seek_advice': 'Painful sex with fever, bleeding, discharge, or lasting beyond initial penetration attempts',
        'related': ['Vaginal dryness', 'Pelvic pain', 'Irregular bleeding', 'Urinary symptoms', 'Lower back pain']
    },
    {
        'title': 'Vaginal Irritation and Infection',
        'definition': 'Inflammation of the vaginal mucosa characterized by itching, burning, abnormal discharge, odor, and discomfort, most commonly caused by infectious or irritant triggers.',
        'pathophysiology': 'Vaginal ecosystem disruption alters normal lactobacillus-dominated flora, increasing pH and allowing pathogen overgrowth. Common pathogens: Candida albicans (fungal), Gardnerella vaginalis with other anaerobes (bacterial vaginosis), Trichomonas vaginalis (parasitic). Non-infectious causes include chemical irritants, allergic reactions, and atrophic changes.',
        'causes': [
            'Vulvovaginal candidiasis (yeast infection)',
            'Bacterial vaginosis',
            'Trichomoniasis (sexually transmitted)',
            'Chemical irritants (soaps, douches, detergents, spermicides)',
            'Atrophic vaginitis (menopause-related)',
            'Allergic reactions (latex, lubricants, contraceptive devices)',
            'Poor hygiene or excessive hygiene',
            'Tight non-breathable clothing',
            'Diabetes mellitus (increased glucose promotes yeast)',
            'Antibiotic use disrupting normal flora'
        ],
        'seek_advice': 'Vaginal irritation with abnormal discharge, fever, pelvic pain, or recurrent episodes',
        'related': ['Vaginal discharge', 'Itching', 'Dysuria', 'Painful sex', 'Abnormal odor']
    },
    {
        'title': 'Chest Tightness and Discomfort',
        'definition': 'A subjective sensation of pressure, squeezing, constriction, or fullness in the chest area, distinct from sharp or stabbing chest pain but equally requiring careful evaluation.',
        'pathophysiology': 'Chest tightness may reflect bronchoconstriction (asthma, COPD), esophageal spasm (GERD, motility disorder), anxiety/hyperventilation (muscle tension), or cardiac ischemia (angina presenting as tightness without frank pain). Differentiating cardiac from non-cardiac causes is critical.',
        'causes': [
            'Asthma or reactive airway disease',
            'Gastroesophageal reflux disease (GERD) with esophageal spasm',
            'Anxiety, panic attacks, or hyperventilation syndrome',
            'Angina pectoris or coronary artery disease',
            'Chronic obstructive pulmonary disease (COPD) exacerbation',
            'Costochondritis (chest wall tenderness)',
            'Pulmonary embolism',
            'Pneumonia or pleurisy',
            'Laryngeal or tracheal irritation',
            'Heart failure (especially with orthopnea)'
        ],
        'seek_advice': 'Chest tightness with shortness of breath, radiating pain, sweating, nausea, or lightheadedness (possible cardiac cause — emergency)',
        'related': ['Shortness of breath', 'Wheezing', 'Cough', 'Anxiety', 'Palpitations']
    },
    {
        'title': 'Swollen or Painful Testicle',
        'definition': 'Enlargement, pain, or tenderness of one or both testicles, ranging from mild discomfort to acute severe pain requiring emergency evaluation.',
        'pathophysiology': 'Testicular torsion (spermatic cord twisting) compromises blood flow causing ischemia within 4-6 hours — surgical emergency. Epididymitis results from infection ascending from urethra/bladder. Hydrocele, varicocele, and spermatocele cause painless swelling. Testicular tumors typically present as painless solid mass.',
        'causes': [
            'Testicular torsion (surgical emergency)',
            'Epididymitis (often bacterial or sexually transmitted)',
            'Orchitis (viral — mumps, or bacterial)',
            'Hydrocele (fluid collection around testicle)',
            'Varicocele (dilated scrotal veins)',
            'Spermatocele (epididymal cyst)',
            'Testicular tumor or cancer',
            'Testicular trauma',
            'Inguinal hernia (scrotal extension)',
            'Torsion of appendix testis (small testicular appendage)'
        ],
        'seek_advice': 'Sudden severe testicular pain with nausea/vomiting (possible torsion — immediate emergency), or painless testicular lump',
        'related': ['Groin pain', 'Scrotal swelling', 'Nausea and vomiting', 'Fever', 'Urinary symptoms']
    },
    {
        'title': 'Disorientation',
        'definition': 'Impairment of awareness of time, place, or person, often accompanied by confusion, difficulty concentrating, and inability to perform familiar tasks.',
        'pathophysiology': 'Disorientation results from dysfunction in cortical and subcortical networks supporting orientation and attention. Acute disorientation (delirium) involves global cognitive impairment from metabolic, toxic, infectious, or structural causes. Chronic disorientation (dementia) reflects progressive neurodegenerative damage. The reticular activating system and prefrontal cortex are key affected regions.',
        'causes': [
            'Delirium (metabolic, infectious, medication-induced)',
            'Alzheimer disease and other dementias',
            'Head trauma or traumatic brain injury',
            'Stroke or transient ischemic attack',
            'Seizure (especially complex partial or post-ictal)',
            'Hypoglycemia or hyperglycemia',
            'Electrolyte imbalances',
            'Medication side effects (anticholinergics, benzodiazepines, opioids)',
            'Alcohol intoxication or withdrawal',
            'Severe dehydration or malnutrition'
        ],
        'seek_advice': 'Sudden-onset disorientation (possible stroke, hypoglycemia, or delirium — emergency evaluation)',
        'related': ['Memory loss', 'Confusion', 'Agitation', 'Dizziness', 'Speech difficulty']
    },
    {
        'title': 'Addiction Withdrawal',
        'definition': 'A syndrome of physical and psychological symptoms that occurs when a person stops or reduces use of a substance to which they have developed dependence.',
        'pathophysiology': 'Chronic substance use causes neuroadaptation — the brain compensates for the drug\'s effects by altering neurotransmitter systems (dopamine, GABA, glutamate, norepinephrine, opioid). Abrupt cessation removes the drug effect, unmasking the compensatory changes causing rebound hyperactivity or hypoactivity depending on the substance.',
        'causes': [
            'Alcohol withdrawal (potentially severe — DTs, seizures, death)',
            'Opioid withdrawal (flu-like symptoms, cravings, not life-threatening)',
            'Benzodiazepine withdrawal (prolonged, can cause seizures)',
            'Nicotine withdrawal (cigarettes, vaping)',
            'Stimulant withdrawal (amphetamine, cocaine — fatigue, depression)',
            'Cannabis withdrawal (irritability, insomnia, anxiety)',
            'Antidepressant discontinuation syndrome',
            'Caffeine withdrawal (headache, fatigue, irritability)',
            'Antipsychotic withdrawal',
            'Barbiturate withdrawal (severe, can be life-threatening)'
        ],
        'seek_advice': 'Severe withdrawal symptoms, history of heavy alcohol/benzodiazepine use, suicidal thoughts, or hallucinations',
        'related': ['Anxiety', 'Insomnia', 'Agitation', 'Sweating', 'Palpitations']
    },
    {
        'title': 'Black Eye (Periorbital Ecchymosis)',
        'definition': 'Bruising around the eye caused by blunt trauma to the periorbital region, resulting in blood accumulation in the loose subcutaneous connective tissue of the eyelids.',
        'pathophysiology': 'Blunt force fractures small blood vessels in the periorbital tissues, causing extravasation of blood into the subcutaneous space. The loose eyelid skin allows significant swelling. Blood tracks along tissue planes, often spreading to the cheek and contralateral eye. The classic black-blue-purple-yellow color progression reflects hemoglobin breakdown over 7-14 days.',
        'causes': [
            'Blunt trauma (sports injury, assault, fall)',
            'Nasal fracture with periorbital tracking',
            'Basilar skull fracture (raccoon eyes — bilateral, delayed)',
            'Orbital blowout fracture',
            'Post-surgical (eyelid surgery, rhinoplasty, sinus surgery)',
            'Coagulation disorders or anticoagulant medications',
            'Subgaleal hematoma tracking from scalp injury',
            'Insect bite or allergic reaction (mimics black eye)',
            'Periorbital cellulitis (not traumatic, requires urgent care)',
            'Child abuse (suspicious pattern or mechanism)'
        ],
        'seek_advice': 'Blurry or double vision, eye pain with movement, inability to move the eye, blood in the eye, or trauma from high-velocity object',
        'related': ['Periorbital swelling', 'Vision changes', 'Headache', 'Nasal pain', 'Nausea']
    },
    {
        'title': 'Choking (Airway Obstruction)',
        'definition': 'Partial or complete blockage of the airway by a foreign object, food, or anatomical structure, preventing adequate breathing and requiring immediate intervention.',
        'pathophysiology': 'Foreign body lodges in the pharynx, larynx, or trachea causing mechanical obstruction. Partial obstruction allows some air exchange (coughing, wheezing, stridor). Complete obstruction causes silent distress with inability to cough, speak, or breathe, leading to hypoxia, loss of consciousness, and cardiac arrest within minutes without intervention.',
        'causes': [
            'Food aspiration (meat, nuts, seeds, hot dogs, grapes)',
            'Small objects (coins, marbles, toy parts, buttons)',
            'Inadequate chewing or eating too fast',
            'Alcohol intoxication (impaired swallowing reflex)',
            'Dental issues or poorly fitting dentures',
            'Neurological conditions (dysphagia from stroke, Parkinson, dementia)',
            'Anaphylaxis (laryngeal edema causing airway closure)',
            'Croup or epiglottitis (infectious airway narrowing)',
            'Trauma causing laryngeal fracture or airway compression',
            'Tongue obstruction in unconscious patient'
        ],
        'seek_advice': 'Complete airway obstruction (unable to cough, speak, or breathe) requires immediate emergency response and abdominal thrusts (Heimlich maneuver)',
        'related': ['Shortness of breath', 'Stridor', 'Cough', 'Cyanosis', 'Loss of consciousness']
    },
    {
        'title': 'Fluid from the Ear (Otorrhea)',
        'definition': 'Any discharge from the ear canal, varying in character (clear, bloody, purulent, serous) depending on the underlying pathology of the external ear, middle ear, or mastoid.',
        'pathophysiology': 'Otorrhea results from external ear canal infection (otitis externa), middle ear infection with tympanic membrane perforation (otitis media suppurativa), cholesteatoma with secondary infection, or cerebrospinal fluid leakage from skull base fracture. Purulent discharge suggests bacterial infection; clear fluid suggests CSF leak (halo sign) or serous effusion.',
        'causes': [
            'Acute otitis externa (swimmer\'s ear)',
            'Acute otitis media with tympanic membrane perforation',
            'Chronic suppurative otitis media',
            'Cholesteatoma (keratinizing squamous epithelial cyst)',
            'Foreign body in ear canal with secondary infection',
            'Traumatic tympanic membrane perforation',
            'CSF otorrhea from temporal bone fracture (clear fluid)',
            'Ear canal eczema or seborrheic dermatitis',
            'Furuncle or abscess of ear canal',
            'Post-surgical (after ear tube placement, mastoidectomy)'
        ],
        'seek_advice': 'Ear discharge with severe pain, fever, hearing loss, or head trauma; clear watery discharge after head injury',
        'related': ['Earache', 'Hearing loss', 'Fever', 'Dizziness', 'Ear fullness']
    },
    {
        'title': 'Heat Rash (Miliaria)',
        'definition': 'A skin condition caused by blockage of eccrine sweat ducts during hot, humid weather, leading to sweat retention and superficial inflammation presenting as small red bumps or blisters.',
        'pathophysiology': 'Sweat duct obstruction from keratin plugs, bacteria, or inflammation leads to sweat retention and ductal rupture. Miliaria crystallina (superficial, clear vesicles) involves stratum corneum duct obstruction. Miliaria rubra (prickly heat, red papules) involves deeper epidermal duct rupture with periductal inflammation. Miliaria profunda (deep, flesh-colored papules) involves dermal duct rupture.',
        'causes': [
            'Hot, humid weather (most common)',
            'Excessive sweating (exercise, fever)',
            'Tight or non-breathable clothing',
            'Prolonged bed rest (friction and heat trapping)',
            'Occlusive dressings or ointments',
            'Neonatal (immature sweat ducts in infants)',
            'Fever with profuse sweating',
            'Intense physical activity in heat',
            'Overdressing in warm environments',
            'Tropical climate exposure'
        ],
        'seek_advice': 'Heat rash with fever, signs of heat exhaustion (nausea, dizziness, confusion), or rash with pus drainage suggesting secondary infection',
        'related': ['Itching (pruritus)', 'Red bumps on skin', 'Prickling sensation', 'Heat exhaustion', 'Dehydration']
    },
    {
        'title': 'Penis Irritation (Balanitis)',
        'definition': 'Inflammation or irritation of the glans penis and/or foreskin (balanoposthitis), characterized by redness, swelling, itching, discharge, and discomfort.',
        'pathophysiology': 'Irritation results from infectious (candidal, bacterial, viral, parasitic), inflammatory (lichen sclerosus, contact dermatitis, psoriasis), or traumatic (friction, chemical irritation) causes. Poor hygiene, diabetes, and immunosuppression predispose to infection. Phimosis (tight foreskin) traps secretions increasing irritation risk.',
        'causes': [
            'Candidal infection (yeast — especially in diabetes)',
            'Poor hygiene (smegma accumulation)',
            'Contact dermatitis (soaps, detergents, lubricants, latex condoms)',
            'Bacterial infection (streptococcal, staphylococcal, anaerobic)',
            'Sexually transmitted infections (HSV, gonorrhea, chlamydia, syphilis)',
            'Lichen sclerosus (chronic inflammatory skin condition)',
            'Psoriasis or reactive arthritis',
            'Trauma or friction (vigorous intercourse, masturbation)',
            'Phimosis or Tight foreskin',
            'Allergic reaction (medications, topical creams)'
        ],
        'seek_advice': 'Penis irritation with discharge, fever, difficulty urinating, or inability to retract foreskin (paraphimosis)',
        'related': ['Penile discharge', 'Dysuria', 'Swelling', 'Itching', 'Painful urination']
    },
    {
        'title': 'Penis Swelling and Injury',
        'definition': 'Trauma or swelling involving the penis, ranging from minor contusions to serious injuries including fracture (tunica albuginea rupture), amputation, or strangulation.',
        'pathophysiology': 'Penile fracture occurs when an erect penis is subjected to bending force, causing rupture of the corpus cavernosum tunica albuginea with characteristic popping sound, immediate detumescence, swelling, and ecchymosis. Strangulation (hair tourniquet, constricting bands) causes venous outflow obstruction leading to edema and ischemia. Zipper injuries are common superficial trauma.',
        'causes': [
            'Penile fracture (tunica albuginea rupture during intercourse)',
            'Zipper entrapment injury (common in children)',
            'Hair tourniquet or constricting band (strangulation)',
            'Blunt trauma (sports injury, straddle injury)',
            'Penile amputation (rare, surgical emergency)',
            'Iatrogenic (post-circumcision, catheterization)',
            'Insect sting or bite causing angioedema',
            'Paraphimosis (retracted foreskin cannot be reduced)',
            'Peyronie disease (palpable plaque with curvature)',
            'Balanitis or cellulitis with significant edema'
        ],
        'seek_advice': 'Penile trauma with rapid swelling, inability to urinate, severe pain, blood at urethral meatus, or penile fracture (audible pop during erection)',
        'related': ['Penis pain', 'Blood in urine', 'Difficulty urinating', 'Swelling', 'Bruising']
    },
    {
        'title': 'Toothache (Dental Pain)',
        'definition': 'Pain originating from a tooth or its supporting structures, ranging from mild sensitivity to severe throbbing pain, caused by dental caries, infection, trauma, or dental procedures.',
        'pathophysiology': 'Dental caries (decay) progresses through enamel into dentin, exposing sensitive nerve endings. Pulpitis (inflammation of dental pulp) results from deep decay, trauma, or thermal injury. Periapical abscess forms when pulp infection extends through the apical foramen into surrounding bone. Periodontal abscess arises from gum infection in periodontal pockets.',
        'causes': [
            'Dental caries (tooth decay) — most common cause',
            'Pulpitis (reversible or irreversible)',
            'Periapical abscess (dental abscess)',
            'Periodontal abscess (gum infection)',
            'Cracked tooth syndrome',
            'Dental trauma (fractured or avulsed tooth)',
            'Impacted wisdom teeth (pericoronitis)',
            'Temporomandibular joint (TMJ) disorders (referred pain)',
            'Sinusitis (referred pain to upper teeth)',
            'Dental procedures (recent filling, root canal, extraction)'
        ],
        'seek_advice': 'Severe tooth pain with facial swelling, fever, difficulty swallowing or breathing (possible deep space neck infection), or persistent pain beyond 2 days',
        'related': ['Facial swelling', 'Fever', 'Headache', 'Gum swelling', 'Earache (referred)']
    },
    {
        'title': 'Warning Signs During Pregnancy',
        'definition': 'A set of signs and symptoms during pregnancy that may indicate serious complications requiring urgent medical evaluation, including preeclampsia, placental abruption, preterm labor, or infection.',
        'pathophysiology': 'Pregnancy induces significant physiological changes in the cardiovascular, renal, respiratory, and immune systems. Warning signs reflect pathological decompensation: hypertension and proteinuria indicate preeclampsia (endothelial dysfunction, placental ischemia); vaginal bleeding suggests placental abruption or placenta previa; decreased fetal movement indicates fetal distress; severe abdominal pain may signal placental abruption, uterine rupture, or appendicitis; fever suggests chorioamnionitis or other infection.',
        'causes': [
            'Preeclampsia (hypertension, proteinuria, headache, visual changes, RUQ pain)',
            'Placental abruption (vaginal bleeding, abdominal pain, uterine tenderness)',
            'Placenta previa (painless vaginal bleeding in third trimester)',
            'Preterm labor (regular contractions, pelvic pressure, back pain before 37 weeks)',
            'Chorioamnionitis (fever, uterine tenderness, foul amniotic fluid)',
            'Gestational diabetes complications (polyuria, polydipsia, blurred vision)',
            'Deep vein thrombosis (unilateral leg swelling, pain, warmth)',
            'Pulmonary embolism (sudden shortness of breath, chest pain, hemoptysis)',
            'Miscarriage (vaginal bleeding, cramping in first trimester)',
            'Ectopic pregnancy (sharp abdominal/pelvic pain, shoulder pain, fainting)'
        ],
        'seek_advice': 'Any vaginal bleeding in pregnancy, severe headache with visual changes, sudden swelling of face/hands, decreased fetal movement, rupture of membranes, or signs of preterm labor before 37 weeks',
        'related': ['Abdominal pain', 'Vaginal bleeding', 'Headache', 'Swelling', 'Fever']
    },
    {
        'title': 'Febrile Seizure',
        'definition': 'A seizure occurring in children aged 6 months to 5 years, triggered by fever (temperature above 38\textdegree{}C) in the absence of intracranial infection, metabolic disturbance, or history of afebrile seizures. Simple febrile seizures last less than 15 minutes and are generalized; complex febrile seizures are focal, prolonged, or recurrent within 24 hours.',
        'pathophysiology': 'Fever causes rapid temperature elevation that lowers the seizure threshold in the developing brain through cytokine-mediated effects (IL-1, IL-6) on neuronal excitability and GABAergic inhibition. Genetic susceptibility involving sodium channel and GABA receptor genes increases risk. The immature blood-brain barrier and developing myelination make young children particularly vulnerable. Simple febrile seizures do not cause brain damage.',
        'causes': [
            'Upper respiratory tract infections (otitis media, pharyngitis, tonsillitis)',
            'Viral infections (influenza, adenovirus, RSV, HHV-6 roseola, enterovirus)',
            'Pneumonia or bronchiolitis',
            'Urinary tract infection (especially in young children)',
            'Gastroenteritis',
            'Bacterial infections (pneumonia, occult bacteremia)',
            'Post-immunization fever (MMR, DTaP, pneumococcal, influenza)',
            'Roseola infantum (HHV-6) — classic cause of febrile seizures',
            'Dental abscess or other focal infection',
            'Genetic predisposition (family history of febrile seizures)'
        ],
        'seek_advice': 'First febrile seizure always requires emergency evaluation to exclude meningitis, encephalitis, or electrolyte disturbance; seizure lasting more than 5 minutes, focal seizure, or multiple seizures within 24 hours',
        'related': ['Fever', 'Seizures', 'Loss of consciousness', 'Confusion', 'Shaking']
    },
    {
        'title': 'Burping (Eructation)',
        'definition': 'The involuntary or voluntary expulsion of gas from the upper gastrointestinal tract through the mouth, caused by swallowed air (aerophagia) or intraluminal gas production, often accompanied by abdominal distension and discomfort.',
        'pathophysiology': 'Burping occurs when swallowed air accumulates in the stomach and is expelled via relaxation of the upper esophageal sphincter. Aerophagia (excessive air swallowing) occurs during eating, drinking, chewing gum, smoking, or anxiety. Supragastric belching involves voluntary air aspiration into the esophagus followed by immediate expulsion without gastric involvement. Gastric fermentation from certain foods or bacterial overgrowth can increase intraluminal gas production.',
        'causes': [
            'Aerophagia (eating too quickly, talking while eating, chewing gum, drinking carbonated beverages)',
            'Gastroesophageal reflux disease (GERD)',
            'Functional dyspepsia',
            'Gastroparesis (delayed gastric emptying)',
            'Helicobacter pylori infection',
            'Chronic pancreatitis or pancreatic insufficiency',
            'Celiac disease or lactose intolerance',
            'Small intestinal bacterial overgrowth (SIBO)',
            'Hiatal hernia',
            'Anxiety, stress, or behavioral factors (supragastric belching)'
        ],
        'seek_advice': 'Burping accompanied by severe abdominal pain, vomiting, weight loss, or signs of GI bleeding; inability to pass gas with abdominal distension (possible obstruction)',
        'related': ['Bloating', 'Abdominal pain', 'Heartburn', 'Nausea', 'Indigestion']
    },
    {
        'title': 'Hearing Loss',
        'definition': 'A partial or total inability to hear sound in one or both ears, ranging from mild (difficulty with soft speech) to profound (deafness), classified as conductive (outer/middle ear), sensorineural (inner ear/auditory nerve), or mixed type.',
        'pathophysiology': 'Conductive hearing loss results from obstruction or damage to the external ear canal, tympanic membrane, or ossicular chain impeding sound transmission to the cochlea. Sensorineural hearing loss involves damage to cochlear hair cells, the auditory nerve, or central auditory pathways. Noise exposure causes mechanical damage to hair cells and metabolic exhaustion. Presbycusis (age-related) involves cumulative hair cell loss, stria vascularis atrophy, and central processing decline.',
        'causes': [
            'Presbycusis (age-related hearing loss, most common)',
            'Noise-induced hearing loss (occupational, recreational, acute acoustic trauma)',
            'Otitis media with effusion (glue ear, most common in children)',
            'Otosclerosis (abnormal bone remodeling of stapes)',
            'Cerumen impaction (earwax blockage)',
            'Meniere disease (episodic vertigo, tinnitus, fluctuating hearing)',
            'Ototoxic medications (aminoglycosides, loop diuretics, cisplatin, salicylates)',
            'Sudden sensorineural hearing loss (viral, vascular, autoimmune)',
            'Acoustic neuroma (vestibular schwannoma)',
            'Trauma (temporal bone fracture, barotrauma, perforated TM)'
        ],
        'seek_advice': 'Sudden hearing loss (within 72 hours), hearing loss with vertigo, tinnitus, or ear pain, or hearing loss in one ear only',
        'related': ['Tinnitus', 'Earache', 'Vertigo', 'Ear fullness', 'Balance problems']
    },
    {
        'title': 'Breast Lump',
        'definition': 'A palpable mass, nodule, or thickening in the breast tissue, which may be benign (cyst, fibroadenoma, fibrocystic change) or malignant, requiring systematic evaluation to determine etiology.',
        'pathophysiology': 'Breast lumps arise from proliferation of breast tissue components: epithelial (fibroadenoma, carcinoma), connective tissue (phyllodes tumor), or cystic dilation of ducts (simple cysts). Malignant transformation involves genetic mutations (BRCA1/2, HER2, ER/PR) leading to uncontrolled cellular proliferation, angiogenesis, and potential metastasis. Hormonal influences (estrogen, progesterone) drive growth of many benign and malignant breast lesions.',
        'causes': [
            'Fibroadenoma (most common benign solid breast mass in young women)',
            'Simple breast cyst (fluid-filled sac, common in premenopausal women)',
            'Fibrocystic changes (nodularity, tenderness with menstrual cycle)',
            'Breast cancer (invasive ductal carcinoma most common)',
            'Intraductal papilloma (nipple discharge, often bloody)',
            'Mastitis or breast abscess (infection, often during lactation)',
            'Lipoma or hamartoma (benign fatty tumors)',
            'Fat necrosis (post-traumatic or post-surgical)',
            'Phyllodes tumor (rare, can be benign or malignant)',
            'Gynecomastia (male breast enlargement from hormonal imbalance)'
        ],
        'seek_advice': 'Any new breast lump, particularly in women over 30; lump with skin dimpling, nipple retraction, bloody discharge, or axillary lymphadenopathy',
        'related': ['Breast pain', 'Nipple discharge', 'Axillary lump', 'Skin changes', 'Swelling']
    },
    {
        'title': 'Erectile Dysfunction (Impotence)',
        'definition': 'The persistent inability to achieve or maintain an erection sufficient for satisfactory sexual performance, lasting at least 3 months, with significant distress or interpersonal difficulty.',
        'pathophysiology': 'Erection requires intact neurological, vascular, endocrine, and psychological systems. Nitric oxide released from cavernous nerve terminals and endothelium activates guanylate cyclase, increasing cGMP, causing smooth muscle relaxation and arterial dilation. ED results from disruption at any level: endothelial dysfunction (atherosclerosis, diabetes) impairs NO production; venous leak prevents trapping of blood; neurological damage disrupts signaling; low testosterone reduces libido and erectile function.',
        'causes': [
            'Vascular disease (atherosclerosis, hypertension, diabetes mellitus)',
            'Neurological disorders (spinal cord injury, multiple sclerosis, Parkinson, stroke)',
            'Endocrine causes (hypogonadism, hyperprolactinemia, thyroid disorders)',
            'Psychological factors (anxiety, depression, performance anxiety, stress)',
            'Medications (antidepressants SSRIs, antihypertensives beta-blockers, diuretics, antipsychotics)',
            'Lifestyle factors (smoking, alcohol, obesity, sedentary lifestyle, recreational drugs)',
            'Pelvic surgery or trauma (prostatectomy, cystectomy, pelvic radiation)',
            'Peyronie disease (penile curvature with plaques)',
            'Renal failure or liver cirrhosis',
            'Aging-related decline in testosterone and vascular function'
        ],
        'seek_advice': 'Sudden onset of ED after pelvic trauma or surgery, ED with loss of morning erections (possible hypogonadism), or ED causing significant relationship distress',
        'related': ['Low libido', 'Premature ejaculation', 'Difficulty achieving orgasm', 'Penile curvature', 'Urinary symptoms']
    },
    {
        'title': 'Mouth Ulcers (Aphthous Ulcers)',
        'definition': 'Painful, shallow, round or oval sores on the oral mucosa, typically covered by a yellow-gray fibrinous membrane and surrounded by an erythematous halo, recurring at intervals (minor, major, or herpetiform types).',
        'pathophysiology': 'Aphthous ulcers involve a localized immune-mediated inflammatory response targeting the oral epithelium. T-cell activation, tumor necrosis factor-alpha (TNF-alpha), and other cytokines cause epithelial breakdown. Trigger factors include minor trauma, stress, nutritional deficiencies, food sensitivities, and hormonal changes. Genetic predisposition is strong with positive family history in about 40\% of cases.',
        'causes': [
            'Minor aphthous ulcers (most common, recur every few months)',
            'Major aphthous ulcers (larger, deeper, heal with scarring)',
            'Herpetiform ulcers (multiple clustered small ulcers)',
            'Trauma (biting cheek, sharp tooth, dental appliances, burns)',
            'Nutritional deficiencies (iron, folate, vitamin B12, zinc)',
            'Stress and anxiety (common trigger)',
            'Food sensitivities (chocolate, coffee, strawberries, nuts, cheese, tomatoes)',
            'Hormonal changes (premenstrual period)',
            'Autoimmune conditions (Crohn disease, Behcet disease, celiac disease)',
            'Immunosuppression (HIV, chemotherapy)'
        ],
        'seek_advice': 'Ulcers lasting more than 3 weeks, unusually large or painful ulcers, ulcers accompanied by systemic symptoms (fever, weight loss, rash, joint pain), or difficulty eating/drinking',
        'related': ['Oral pain', 'Difficulty swallowing', 'Bad breath', 'Swollen gums', 'Sore throat']
    },
    {
        'title': 'Oral Thrush (Oropharyngeal Candidiasis)',
        'definition': 'A fungal infection of the oral mucosa caused by overgrowth of Candida species (most commonly Candida albicans), presenting as white, creamy, curd-like plaques on the tongue, buccal mucosa, palate, and oropharynx that can be scraped off revealing erythematous underlying tissue.',
        'pathophysiology': 'Candida albicans is a normal commensal of the oral cavity kept in check by competitive oral flora, saliva, and immune surveillance. Disruption of this balance by antibiotics, corticosteroids, immunosuppression, xerostomia, or denture use allows Candida to proliferate and adhere to epithelial cells, forming hyphae that invade the superficial mucosa and trigger an inflammatory response.',
        'causes': [
            'Antibiotic use (suppression of competing oral bacteria)',
            'Inhaled or systemic corticosteroid use',
            'Immunosuppression (HIV/AIDS, chemotherapy, organ transplantation)',
            'Diabetes mellitus (especially poorly controlled)',
            'Denture use (denture stomatitis)',
            'Xerostomia (dry mouth from medications, Sjogren syndrome, radiation)',
            'Smoking',
            'Infancy (immature immune system)',
            'Iron or folate deficiency',
            'Nutritional deficiencies and general debilitation'
        ],
        'seek_advice': 'White plaques that do not scrape off easily, difficulty swallowing, fever, or thrush in immunocompromised patients or those receiving chemotherapy',
        'related': ['Dry mouth', 'Bad breath', 'Difficulty swallowing', 'Altered taste', 'Sore throat']
    },
    {
        'title': 'Cold Sores (Herpes Labialis)',
        'definition': 'Recurrent, painful, vesicular eruptions on the lips and perioral skin caused by herpes simplex virus (typically HSV-1), characterized by prodromal tingling followed by clustered blisters that crust and heal within 7-14 days.',
        'pathophysiology': 'Primary HSV-1 infection typically occurs in childhood (gingivostomatitis). The virus then establishes lifelong latency in the trigeminal ganglion. Reactivation triggers include UV radiation, fever, stress, immunosuppression, trauma, and hormonal changes. Reactivated virus travels along sensory nerve axons to the skin, causing epithelial cell lysis, vesicle formation, and local inflammation. Healing involves cell-mediated immune clearance.',
        'causes': [
            'HSV-1 reactivation (most common, triggered by UV light, stress, illness)',
            'Fever or viral illness (hence "cold sores")',
            'Ultraviolet radiation (sun exposure, tanning beds)',
            'Physical or emotional stress',
            'Immunosuppression (HIV, chemotherapy, transplant)',
            'Hormonal changes (menstruation)',
            'Facial trauma or dental procedures',
            'Fatigue and sleep deprivation',
            'Cold weather or wind exposure',
            'Close contact with active lesions (autoinoculation or transmission)'
        ],
        'seek_advice': 'Frequent recurrent episodes (more than 6 per year), lesions spreading to eyes, or lesions lasting more than 2 weeks',
        'related': ['Fever', 'Swollen lymph nodes', 'Sore throat', 'Mouth ulcers', 'Facial pain']
    },
    {
        'title': 'Eyelid Bump (Stye and Chalazion)',
        'definition': 'A localized, tender, erythematous nodule on the eyelid margin caused by acute bacterial infection of eyelash follicle (external hordeolum/style) or meibomian gland (internal hordeolum); a chalazion is a chronic, painless, inflammatory granuloma of the meibomian gland.',
        'pathophysiology': 'External styes involve infection of the Zeis or Moll glands (eyelash follicles) by Staphylococcus aureus, causing acute suppurative inflammation. Internal styes infect meibomian glands with similar pathophysiology. Chalazion results from obstruction of the meibomian gland duct without acute infection, leading to lipogranulomatous inflammation with lipid-laden macrophages, giant cells, and a firm, nontender nodule.',
        'causes': [
            'Staphylococcus aureus infection (most common cause of stye)',
            'Poor eyelid hygiene',
            'Blepharitis (chronic eyelid inflammation predisposing to styes)',
            'Contact lens use (improper hygiene)',
            'Rosacea (associated with meibomian gland dysfunction)',
            'Seborrheic dermatitis',
            'Hormonal changes',
            'Stress and fatigue',
            'Use of expired or contaminated eye makeup',
            'Duct obstruction from thickened meibomian secretions (chalazion)'
        ],
        'seek_advice': 'Recurrent styes, lesion not resolving within 2 weeks, vision changes, eyelid swelling spreading to entire eye or face, or fever',
        'related': ['Eyelid swelling', 'Eye redness', 'Eye discharge', 'Eye pain', 'Blepharitis']
    },
    {
        'title': 'Double Vision (Diplopia)',
        'definition': 'The perception of two images of a single object, classified as monocular (persists when one eye is covered, originates from ocular media) or binocular (resolves with covering either eye, originates from ocular misalignment).',
        'pathophysiology': 'Binocular diplopia results from misalignment of the visual axes (strabismus) due to cranial nerve palsy (CN III, IV, VI), neuromuscular junction disorder (myasthenia gravis), restrictive orbitopathy (thyroid eye disease), or brainstem/cerebellar lesions affecting ocular motor control. Monocular diplopia arises from refractive errors, cataract, corneal irregularity, or retinal problems causing light scattering within one eye.',
        'causes': [
            'Cranial nerve palsy (CN III, IV, VI from microvascular disease, aneurysm, trauma, tumor)',
            'Myasthenia gravis (fatigable diplopia, worse with sustained gaze)',
            'Thyroid eye disease (Graves orbitopathy, restrictive myopathy)',
            'Strabismus (childhood squint, decompensating in adulthood)',
            'Multiple sclerosis (demyelinating brainstem lesion)',
            'Stroke or transient ischemic attack (brainstem, cerebellum)',
            'Orbital trauma or fracture',
            'Cataract (monocular diplopia)',
            'Corneal irregularity (dry eye, keratoconus, scar)',
            'Botulism or Guillain-Barre syndrome (Miller Fisher variant)'
        ],
        'seek_advice': 'Sudden-onset diplopia (possible stroke, aneurysm, or brainstem lesion), diplopia with headache, ptosis, or pupil changes',
        'related': ['Headache', 'Ptosis (drooping eyelid)', 'Blurred vision', 'Dizziness', 'Strabismus']
    },
    {
        'title': 'Dehydration',
        'definition': 'A state of negative fluid balance resulting from excessive water loss (through skin, lungs, kidneys, or GI tract) or inadequate intake, leading to intracellular and extracellular volume depletion with potential electrolyte disturbances.',
        'pathophysiology': 'Water loss exceeds intake, causing reduced total body water, increased plasma osmolality, and stimulation of osmoreceptors in the hypothalamus. Antidiuretic hormone (ADH) is released, increasing water reabsorption in renal collecting ducts. Thirst is stimulated. Continued loss without replacement leads to hypovolemia, reduced cardiac output, compensatory tachycardia, vasoconstriction, and eventually hemodynamic instability and shock. Cellular dehydration impairs enzyme function and organ performance.',
        'causes': [
            'Inadequate fluid intake (common in elderly, infants, dementia, during illness)',
            'Vomiting and diarrhea (gastroenteritis most common cause in children)',
            'Excessive sweating (exercise, fever, heat exposure)',
            'Polyuria (diabetes mellitus, diabetes insipidus, diuretic medications)',
            'Blood loss (hemorrhage)',
            'Burns (loss of skin barrier leading to fluid evaporation)',
            'Fever (increased insensible water loss)',
            'Alcohol intake (diuretic effect)',
            'Gastrointestinal losses (NG suction, fistulas, ostomy output)',
            'Reduced thirst sensation in elderly (presbyphagia, cognitive impairment)'
        ],
        'seek_advice': 'Severe dehydration signs: no urine output for 8 hours, lethargy or confusion, rapid heart rate, low blood pressure, sunken eyes, or inability to keep fluids down',
        'related': ['Thirst', 'Dark urine', 'Fatigue', 'Dizziness', 'Dry mouth']
    },
    {
        'title': 'Drooling (Sialorrhea)',
        'definition': 'The unintentional loss of saliva from the mouth, resulting from excessive saliva production (hypersalivation) or impaired oral motor control causing difficulty swallowing saliva, which can lead to skin irritation, aspiration, and social embarrassment.',
        'pathophysiology': 'Saliva is produced by three major paired salivary glands (parotid, submandibular, sublingual) and minor glands, with daily production of 0.5-1.5 L. Drooling occurs due to excess production (rare) or, more commonly, from oropharyngeal dysphagia, impaired lip seal, poor head control, or reduced swallowing frequency. Neurological conditions disrupt the coordinated neuromuscular sequence of saliva clearance.',
        'causes': [
            'Neurological disorders (cerebral palsy, Parkinson disease, ALS, stroke)',
            'Developmental delay (children with poor oral motor control)',
            'Oropharyngeal dysphagia (difficulty swallowing)',
            'Dental problems (teething in infants, ill-fitting dentures)',
            'GERD (increased salivation as compensatory response)',
            'Medications (clozapine, risperidone, cholinesterase inhibitors, ketamine)',
            'Toxins (mercury, organophosphates, arsenic)',
            'Pregnancy (hormonal changes causing hypersalivation)',
            'Mouth breathing (nasal obstruction, enlarged tonsils/adenoids)',
            'Parkinson disease (stooped posture, reduced swallowing frequency, rigidity)'
        ],
        'seek_advice': 'Sudden onset of drooling (possible stroke, especially with facial droop or speech difficulty), drooling with fever and difficulty swallowing (possible epiglottitis or retropharyngeal abscess)',
        'related': ['Dysphagia', 'Speech difficulty', 'Facial droop', 'Bad breath', 'Choking']
    },
    {
        'title': 'Snoring',
        'definition': 'A coarse, harsh breathing sound produced during sleep by vibration of the soft palate, uvula, pharyngeal walls, and tongue base due to partial upper airway obstruction, ranging from benign primary snoring to a marker of obstructive sleep apnea (OSA).',
        'pathophysiology': 'During sleep, reduced muscle tone in the pharyngeal dilator muscles allows the soft palate, uvula, and tongue to collapse partially into the airway. Airflow through the narrowed oropharynx creates negative pressure causing vibration of floppy soft tissue structures. Factors increasing collapse risk include obesity (fat deposition around airway), supine position, alcohol/sedatives (muscle relaxation), and anatomical narrowing (large tonsils, retrognathia, macroglossia).',
        'causes': [
            'Obesity (most common modifiable risk factor)',
            'Supine sleeping position (gravity worsens airway collapse)',
            'Alcohol, sedatives, or muscle relaxants before sleep',
            'Nasal congestion or obstruction (allergies, deviated septum, polyps)',
            'Enlarged tonsils or adenoids (common in children)',
            'Retrognathia or micrognathia (small or recessed jaw)',
            'Macroglossia (large tongue, seen in Down syndrome, acromegaly)',
            'Hypothyroidism (myxedematous changes, obesity, muscle dysfunction)',
            'Menopause (hormonal changes affecting airway muscle tone)',
            'Aging (decreased pharyngeal muscle tone with age)'
        ],
        'seek_advice': 'Loud snoring with witnessed breathing pauses, choking/gasping during sleep, excessive daytime sleepiness, morning headaches, or hypertension (possible sleep apnea)',
        'related': ['Daytime sleepiness', 'Fatigue', 'Morning headache', 'Sleep apnea', 'Restless sleep']
    },
    {
        'title': 'Dry Skin (Xerosis)',
        'definition': 'A common skin condition characterized by rough, scaling, flaking, and sometimes pruritic skin due to reduced water content in the stratum corneum, often exacerbated by cold weather, low humidity, and frequent washing.',
        'pathophysiology': 'Dry skin results from disruption of the skin barrier function, particularly the stratum corneum lipid matrix (ceramides, cholesterol, free fatty acids) that normally retains water. Decreased natural moisturizing factors (amino acids, urea, lactate) and impaired desquamation lead to accumulation of corneocytes on the surface. Environmental factors (low humidity, cold, wind, excessive bathing) accelerate transepidermal water loss. Aging reduces sebaceous and sweat gland activity.',
        'causes': [
            'Cold, dry weather (winter xerosis, most common)',
            'Excessive bathing or hand washing (strips natural oils)',
            'Harsh soaps and detergents (disrupt skin barrier)',
            'Aging (decreased sebum production, thinner skin)',
            'Central heating or air conditioning (low indoor humidity)',
            'Atopic dermatitis (eczema, genetic barrier defect)',
            'Psoriasis (increased epidermal turnover with scaling)',
            'Hypothyroidism (reduced sweating and sebum production)',
            'Diabetes mellitus (dehydration, autonomic dysfunction)',
            'Medications (diuretics, retinoids, antihistamines, statins)'
        ],
        'seek_advice': 'Dry skin with severe itching, signs of infection (increasing redness, warmth, swelling, pus), extensive cracking or fissures, or rash unresponsive to moisturizers',
        'related': ['Itching (pruritus)', 'Rash', 'Skin flaking', 'Erythema', 'Skin fissures']
    },
    {
        'title': 'Eye Twitching (Blepharospasm and Myokymia)',
        'definition': 'Intermittent, involuntary, repetitive contractions of the orbicularis oculi muscle. Benign eyelid myokymia involves fine, rippling twitching of a single eyelid (usually lower), while blepharospasm involves sustained, bilateral, forceful eyelid closure.',
        'pathophysiology': 'Eyelid myokymia results from spontaneous depolarization of motor units in the orbicularis oculi muscle, often triggered by fatigue, stress, or caffeine. The pathophysiology involves increased excitability of the facial nerve nucleus or motor cortex. Blepharospasm is a focal dystonia involving involuntary contraction of the orbicularis oculi due to basal ganglia dysfunction and altered inhibition in the brainstem blink reflex circuits.',
        'causes': [
            'Fatigue and sleep deprivation (most common cause of myokymia)',
            'Stress and anxiety',
            'Caffeine or stimulant intake',
            'Eye strain (prolonged screen time, uncorrected vision)',
            'Dry eyes (ocular surface irritation triggers reflex blinking)',
            'Nutritional deficiencies (magnesium, potassium, calcium)',
            'Alcohol or tobacco use',
            'Benign essential blepharospasm (focal dystonia, typically bilateral)',
            'Hemifacial spasm (unilateral, involving entire side of face, vascular compression of CN VII)',
            'Medications (antipsychotics, antihistamines, SSRIs)'
        ],
        'seek_advice': 'Twitching spreading to other parts of the face, both eyes closing involuntarily, eye redness or discharge, or twitching lasting more than 2 weeks',
        'related': ['Eye strain', 'Dry eyes', 'Facial twitching', 'Blepharospasm', 'Fatigue']
    },
    {
        'title': 'Bad Taste in the Mouth (Dysgeusia)',
        'definition': 'A persistent abnormal or distorted sense of taste, ranging from a metallic, salty, bitter, or sour taste in the mouth without an external stimulus, caused by disorders of the taste buds, olfactory system, or systemic conditions.',
        'pathophysiology': 'Taste is mediated by taste buds on the tongue, palate, pharynx, and epiglottis, innervated by cranial nerves VII (chorda tympani), IX (glossopharyngeal), and X (vagus). Dysgeusia results from damage to taste receptors, alteration of saliva composition, or disruption of central taste pathways. Olfactory dysfunction (as in sinusitis or COVID-19) significantly alters flavor perception. Systemic conditions change saliva composition affecting taste receptor microenvironment.',
        'causes': [
            'Oral infections (gingivitis, periodontitis, oral thrush, sinusitis)',
            'Medications (metronidazole, clarithromycin, ACE inhibitors, metformin, lithium, chemotherapy)',
            'Dental problems (poor oral hygiene, dental caries, abscesses, amalgam fillings)',
            'GERD (regurgitation of acidic stomach contents)',
            'Sjogren syndrome or xerostomia (reduced saliva alters taste)',
            'Neurological disorders (Bell palsy, multiple sclerosis, stroke affecting taste pathways)',
            'COVID-19 infection (taste and smell dysfunction)',
            'Nutritional deficiencies (zinc, vitamin B12, copper)',
            'Smoking and tobacco use',
            'Radiation therapy to head and neck (damage to taste buds and salivary glands)'
        ],
        'seek_advice': 'Persistent bad taste with weight loss, difficulty swallowing, or any neurological symptoms (facial droop, weakness, speech changes)',
        'related': ['Bad breath', 'Dry mouth', 'Loss of taste', 'Oral thrush', 'Sinus pressure']
    },
    {
        'title': 'Nipple Discharge',
        'definition': 'Any fluid that escapes from the nipple, varying in character (milky, serous, purulent, bloody, green/black) and significance from benign physiological discharge to a marker of underlying breast pathology including infection, duct ectasia, papilloma, or malignancy.',
        'pathophysiology': 'Milk production is regulated by prolactin from the anterior pituitary, normally suppressed by dopamine from the hypothalamus. Pathologic discharge arises from spontaneous activation of breast epithelial cells (hyperprolactinemia), ductal inflammation (duct ectasia, periductal mastitis), intraductal growth (papilloma), or malignant cells eroding into ducts. Unilateral, spontaneous, bloody discharge from a single duct raises highest concern for malignancy.',
        'causes': [
            'Physiological discharge (bilateral, milky, expressed only, common in reproductive-age women)',
            'Intraductal papilloma (most common cause of bloody unilateral discharge)',
            'Duct ectasia (benign dilation of mammary ducts, thick green/black discharge)',
            'Mastitis or breast abscess (purulent discharge with pain and erythema)',
            'Hyperprolactinemia (pituitary adenoma, medications, hypothyroidism)',
            'Breast cancer (invasive or DCIS, often unilateral spontaneous bloody discharge)',
            'Pregnancy and lactation (colostrum, milk)',
            'Galactorrhea (medication-induced: antipsychotics, metoclopramide, SSRIs, oral contraceptives)',
            'Breast trauma or surgery',
            'Fibrocystic breast changes'
        ],
        'seek_advice': 'Spontaneous, unilateral, bloody, or clear watery discharge; discharge associated with a palpable breast lump; or persistent discharge requiring pad use',
        'related': ['Breast lump', 'Breast pain', 'Breast swelling', 'Galactorrhea', 'Nipple changes']
    },
    {
        'title': 'Cold Hands and Feet (Raynaud Phenomenon)',
        'definition': 'A vasospastic disorder characterized by episodic digital ischemia triggered by cold or stress, causing well-demarcated color changes (white, blue, red) in the fingers and/or toes, often with numbness, tingling, and pain during rewarming.',
        'pathophysiology': 'Raynaud phenomenon involves exaggerated vasoconstriction of digital arteries and arterioles in response to cold or emotional stress. Primary Raynaud is idiopathic, benign, and associated with hyperactivation of alpha-2 adrenergic receptors on digital vessels. Secondary Raynaud involves underlying pathology (scleroderma, lupus) causing structural vessel damage, intimal hyperplasia, and obliterative microvascular disease, leading to more severe ischemia and potential digital ulceration.',
        'causes': [
            'Primary Raynaud disease (benign, no underlying cause, onset before age 30)',
            'Connective tissue diseases (scleroderma, systemic lupus, mixed connective tissue disease)',
            'Cryoglobulinemia (abnormal cold-precipitating proteins)',
            'Buerger disease (thromboangiitis obliterans, linked to smoking)',
            'Atherosclerosis or peripheral artery disease',
            'Thoracic outlet syndrome (neurovascular compression)',
            'Medications (beta-blockers, ergotamines, chemotherapy bleomycin, cisplatin)',
            'Repetitive vibration injury (hand-arm vibration syndrome from power tools)',
            'Hypothyroidism (reduced metabolic rate, cold intolerance)',
            'Carpal tunnel syndrome (associated with vasomotor symptoms)'
        ],
        'seek_advice': 'Unilateral symptoms, skin ulceration or gangrene, symptoms beginning after age 30, or associated with rash, joint pain, or systemic symptoms',
        'related': ['Numbness', 'Tingling', 'Finger swelling', 'Joint pain', 'Digital ulcers']
    },
]

print(f"Generating {len(missing)} missing symptom chapters...")
generated = []
for s in missing:
    fname = create_chapter(
        s['title'], s['definition'], s['pathophysiology'],
        s['causes'], s['seek_advice'], s['related']
    )
    generated.append(s['title'])
    print(f"  Created: {fname}")

print(f"\nSuccessfully generated {len(generated)} missing symptom chapters!")
print("\nMissing chapters generated:")
for g in generated:
    print(f"  - {g}")
