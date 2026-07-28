#!/usr/bin/env python3
"""Generate missing symptom chapters from Mayo Clinic cross-reference."""
import os

chapters_dir = '/Users/csv610/Projects/MyBooks/MedSymptoms/chapters'

def create_chapter(title, definition, pathophysiology, causes, seek_advice, related, short_name=None):
    if short_name:
        base = short_name
    else:
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
    lines.append('\\textbf{Note:} Always consider serious underlying conditions when evaluating persistent ' + title.lower().split(' (')[0] + '.')
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
    print(f'Created: {filename}')
    return base

missing = [
    {
        'title': 'Ankle Pain',
        'definition': 'Pain or discomfort localized to the ankle joint and surrounding structures, including the medial and lateral malleoli, talocrural joint, and supporting ligaments and tendons.',
        'pathophysiology': 'Ankle pain most commonly results from ligamentous injury (ankle sprain) involving the lateral ligament complex (anterior talofibular, calcaneofibular, posterior talofibular). The ankle\'s weight-bearing role and its reliance on ligamentous stability make it vulnerable to inversion injuries. Chronic pain may arise from post-traumatic arthritis, tendinopathy (peroneal, Achilles, posterior tibial), or osteochondral defects of the talar dome.',
        'causes': [
            'Acute ankle sprain (lateral, medial, or syndesmotic)',
            'Ankle fracture (malleolar, bimalleolar, trimalleolar)',
            'Achilles tendinopathy or rupture',
            'Peroneal tendinopathy or subluxation',
            'Posterior tibial tendinopathy',
            'Osteochondritis dissecans of the talus',
            'Ankle osteoarthritis (post-traumatic)',
            'Gout or pseudogout',
            'Cellulitis or septic arthritis',
            'Tarsal coalition (congenital, presenting in adolescence)'
        ],
        'seek_advice': 'Inability to bear weight after injury, severe swelling or deformity, fever with ankle pain, or chronic pain lasting more than 6 weeks',
        'related': ['Foot pain', 'Leg pain', 'Swelling', 'Bruising', 'Instability']
    },
    {
        'title': 'Arm Pain',
        'definition': 'Pain or discomfort anywhere in the upper extremity from the shoulder to the hand, arising from musculoskeletal, vascular, neurological, or referred sources.',
        'pathophysiology': 'Arm pain mechanisms include nociceptive (musculoskeletal strain, fracture, arthritis), neuropathic (cervical radiculopathy, peripheral nerve entrapment), ischemic (peripheral arterial disease, thoracic outlet syndrome), and referred (cardiac ischemia presenting as left arm pain). The brachial plexus distribution and shared cervical nerve roots mean arm pain frequently originates from the neck.',
        'causes': [
            'Cervical radiculopathy (herniated disc, foraminal stenosis)',
            'Rotator cuff tendinopathy or tear',
            'Fracture (humerus, radius, ulna)',
            'Lateral epicondylitis (tennis elbow)',
            'Medial epicondylitis (golfer\'s elbow)',
            'Carpal tunnel syndrome',
            'Thoracic outlet syndrome',
            'Bursitis (olecranon, subacromial)',
            'Referred cardiac pain (left arm — angina or MI)',
            'Peripheral neuropathy (diabetic, alcoholic)'
        ],
        'seek_advice': 'Arm pain with chest pain, shortness of breath, or diaphoresis (possible cardiac), acute severe pain after injury, or arm pain with weakness or numbness',
        'related': ['Shoulder pain', 'Neck pain', 'Hand numbness', 'Weakness', 'Swelling']
    },
    {
        'title': 'Bent Penis (Peyronie Disease)',
        'definition': 'Acquired curvature of the erect penis caused by fibrous plaque formation in the tunica albuginea of the corpora cavernosa, often associated with pain and erectile dysfunction.',
        'pathophysiology': 'Peyronie disease results from repetitive microvascular trauma or buckling injury to the erect penis, triggering an abnormal wound-healing response. Fibrin deposition leads to chronic inflammation, dysregulated collagen production, and plaque formation in the tunica albuginea. The inelastic plaque prevents uniform expansion of the tunica during erection, causing curvature toward the side of the plaque.',
        'causes': [
            'Peyronie disease (idiopathic, most common)',
            'Penile trauma or fracture during intercourse',
            'Dupuytren contracture (associated condition)',
            'Genetic predisposition (family history)',
            'Connective tissue disorders',
            'Diabetes mellitus',
            'Autoimmune conditions',
            'Radiation therapy to the pelvis'
        ],
        'seek_advice': 'Sudden onset of penile curvature with severe pain, inability to have intercourse, or associated erectile dysfunction',
        'related': ['Erectile dysfunction', 'Penile pain', 'Penile shortening', 'Dupuytren contracture', 'Penile plaque']
    },
    {
        'title': 'Bleeding After Vaginal Sex (Postcoital Bleeding)',
        'definition': 'Vaginal bleeding or spotting occurring after sexual intercourse, ranging from light spotting to heavier flow, originating from the cervix, vagina, or uterus.',
        'pathophysiology': 'Postcoital bleeding most commonly arises from cervical pathology: cervicitis (infectious or inflammatory), cervical ectropion (exposure of columnar epithelium on the ectocervix), cervical polyps, or cervical dysplasia/neoplasia. Vaginal atrophy (especially postmenopausal) and vaginal lacerations from insufficient lubrication or trauma may also cause bleeding. Uterine sources include endometrial polyps, fibroids, or pregnancy-related conditions.',
        'causes': [
            'Cervicitis (chlamydia, gonorrhea, trichomonas, HSV)',
            'Cervical ectropion (ectopy)',
            'Cervical or endometrial polyps',
            'Cervical dysplasia or carcinoma',
            'Vaginal atrophy (genitourinary syndrome of menopause)',
            'Insufficient lubrication',
            'Vaginal or cervical trauma/laceration',
            'Endometritis or pelvic inflammatory disease',
            'Pregnancy (cervical friability)',
            'Coagulation disorders or anticoagulant therapy'
        ],
        'seek_advice': 'Persistent or heavy postcoital bleeding, pain during intercourse, abnormal Pap smear history, or postmenopausal bleeding',
        'related': ['Vaginal bleeding between periods', 'Pelvic pain', 'Vaginal discharge', 'Painful sex', 'Abnormal Pap smear']
    },
    {
        'title': 'Bleeding During Pregnancy',
        'definition': 'Any vaginal bleeding occurring during pregnancy, which requires immediate evaluation to exclude potentially life-threatening causes for both mother and fetus.',
        'pathophysiology': 'First-trimester bleeding (most common) results from implantation bleeding, threatened miscarriage, or ectopic pregnancy. Second- and third-trimester bleeding raises concern for placenta previa (placenta covering the cervical os), placental abruption (premature separation of the placenta from the uterine wall), or vasa previa (fetal vessels crossing the membranes over the cervical os). Uterine rupture is a rare but catastrophic cause.',
        'causes': [
            'Implantation bleeding (early, light, self-limited)',
            'Threatened, inevitable, or complete miscarriage',
            'Ectopic pregnancy (fallopian tube)',
            'Molar pregnancy (gestational trophoblastic disease)',
            'Placenta previa',
            'Placental abruption',
            'Cervical insufficiency or incompetent cervix',
            'Cervical or vaginal infection (cervicitis, vaginitis)',
            'Vasa previa',
            'Uterine rupture (rare, usually scar-related)'
        ],
        'seek_advice': 'Any vaginal bleeding during pregnancy requires immediate medical evaluation, especially if accompanied by pain, fever, or decreased fetal movement',
        'related': ['Abdominal pain', 'Back pain', 'Contractions', 'Fever', 'Decreased fetal movement']
    },
    {
        'title': 'Blood Clots (Venous Thromboembolism)',
        'definition': 'Formation of a blood clot (thrombus) within a deep vein, most commonly in the lower extremities (deep vein thrombosis), which may dislodge and travel to the lungs (pulmonary embolism).',
        'pathophysiology': 'Virchow triad describes predisposing factors: venous stasis (immobility, surgery, long travel), endothelial injury (trauma, surgery, catheterization), and hypercoagulability (inherited thrombophilia, malignancy, pregnancy, oral contraceptives). DVT typically starts in the calf veins and may propagate proximally. Embolization to pulmonary arteries causes ventilation-perfusion mismatch, increased pulmonary vascular resistance, and potentially hemodynamic collapse.',
        'causes': [
            'Prolonged immobility (surgery, hospitalization, long-haul travel)',
            'Malignancy (cancer-associated thrombosis)',
            'Oral contraceptives or hormone replacement therapy',
            'Pregnancy and postpartum period',
            'Inherited thrombophilia (Factor V Leiden, prothrombin mutation)',
            'Antiphospholipid syndrome',
            'Trauma or major surgery (especially orthopedic)',
            'Central venous catheters',
            'Obesity',
            'Advanced age'
        ],
        'seek_advice': 'Unilateral leg swelling, warmth, and redness (possible DVT), or sudden chest pain, shortness of breath, and hemoptysis (possible PE) — seek emergency care',
        'related': ['Leg swelling', 'Chest pain', 'Shortness of breath', 'Calf pain', 'Hemoptysis']
    },
    {
        'title': 'Burning Feet',
        'definition': 'A sensation of heat, burning, or warmth in the feet, often accompanied by tingling, numbness, or sharp pain, indicating underlying peripheral nerve dysfunction.',
        'pathophysiology': 'Burning feet most commonly result from peripheral neuropathy, particularly length-dependent axonal neuropathy where distal nerve endings are affected first. Metabolic (diabetes), toxic (alcohol), nutritional (B vitamin deficiencies), and inflammatory (autoimmune) causes damage to small nerve fibers (A-delta and C fibers) that transmit pain and temperature sensation, leading to aberrant nociceptive signaling.',
        'causes': [
            'Diabetic peripheral neuropathy (most common)',
            'Alcoholic neuropathy',
            'Vitamin B deficiency (B1, B6, B12)',
            'Peripheral arterial disease (critical limb ischemia)',
            'Tarsal tunnel syndrome',
            'Hypothyroidism',
            'Chemotherapy-induced peripheral neuropathy',
            'Chronic kidney disease (uremic neuropathy)',
            'Erythromelalgia (rare vascular disorder)',
            'Heavy metal toxicity (lead, mercury, arsenic)'
        ],
        'seek_advice': 'Burning feet with uncontrolled diabetes, progressive weakness, skin breakdown, or weight loss',
        'related': ['Foot numbness', 'Tingling', 'Leg pain', 'Skin changes', 'Foot ulcers']
    },
    {
        'title': 'Dark Circles Under Eyes',
        'definition': 'Dark, discolored appearance of the skin beneath the eyes, which may be black, blue, brown, or purple, resulting from vascular, pigmentary, or structural causes.',
        'pathophysiology': 'Dark circles arise from multiple mechanisms: vascular congestion (thin periorbital skin reveals underlying blood vessels, exacerbated by fatigue, allergies, or aging), melanin deposition (constitutional/genetic hyperpigmentation, more common in darker skin types), post-inflammatory hyperpigmentation (from atopic or allergic dermatitis), and shadowing from infraorbital fat herniation or tear trough hollowing with aging.',
        'causes': [
            'Fatigue and sleep deprivation (vascular stasis)',
            'Allergic rhinitis and atopic dermatitis (venous congestion)',
            'Genetic/constitutional periorbital hyperpigmentation',
            'Aging (skin thinning, fat herniation, tear trough hollowing)',
            'Dehydration',
            'Iron deficiency anemia',
            'Sun exposure (increased melanin production)',
            'Eye strain or prolonged screen time',
            'Periorbital edema (fluid retention)',
            'Medications (prostaglandin analogs for glaucoma)'
        ],
        'seek_advice': 'Dark circles with persistent fatigue, pallor, or other signs of anemia, or if accompanied by periorbital swelling or pain',
        'related': ['Eye puffiness', 'Fatigue', 'Nasal congestion', 'Headache', 'Pale skin']
    },
    {
        'title': 'Dry Orgasm',
        'definition': 'Orgasm achieved without ejaculation of semen (anejaculation) or with significantly reduced or absent seminal fluid, occurring retrograde into the bladder or due to failure of seminal emission.',
        'pathophysiology': 'Dry orgasm results from either retrograde ejaculation (semen flows backward into the bladder due to failure of the bladder neck to close during emission) or anejaculation (failure of seminal emission from the seminal vesicles, prostate, and vas deferens). The internal bladder sphincter normally contracts during orgasm to prevent retrograde flow; disruption by surgery, medication, or neuropathy causes retrograde ejaculation.',
        'causes': [
            'Transurethral resection of the prostate (TURP)',
            'Spinal cord injury or neurological disease',
            'Diabetes mellitus with autonomic neuropathy',
            'Medication side effects (alpha-blockers, antipsychotics, antidepressants)',
            'Retroperitoneal lymph node dissection (testicular cancer surgery)',
            'Multiple sclerosis',
            'Spinal stenosis or cauda equina syndrome',
            'Bladder neck surgery',
            'Severe hypospadias or congenital abnormalities',
            'Psychogenic anejaculation'
        ],
        'seek_advice': 'Persistent dry orgasm with fertility concerns, associated with back pain or neurological symptoms, or after pelvic surgery',
        'related': ['Erectile dysfunction', 'Infertility', 'Reduced libido', 'Testicular pain', 'Urinary symptoms']
    },
    {
        'title': 'Elbow Pain',
        'definition': 'Pain or discomfort localized to the elbow joint and surrounding soft tissues, commonly arising from tendinopathy, arthritis, trauma, or nerve entrapment.',
        'pathophysiology': 'Elbow pain localizes based on anatomy: lateral epicondylitis (tennis elbow) involves degenerative changes in the extensor carpi radialis brevis origin; medial epicondylitis (golfer\'s elbow) affects the common flexor origin; olecranon bursitis involves inflammation of the bursa overlying the olecranon process. Articular pain suggests osteoarthritis, inflammatory arthritis, or intra-articular loose bodies.',
        'causes': [
            'Lateral epicondylitis (tennis elbow)',
            'Medial epicondylitis (golfer\'s elbow)',
            'Olecranon bursitis',
            'Elbow osteoarthritis',
            'Rheumatoid arthritis',
            'Cubital tunnel syndrome (ulnar nerve entrapment)',
            'Distal biceps or triceps tendinopathy',
            'Elbow dislocation or fracture (radial head, olecranon)',
            'Ligamentous injury (UCL tear — Tommy John lesion)',
            'Septic arthritis or gout'
        ],
        'seek_advice': 'Elbow pain after acute injury with deformity or inability to move, fever, or severe pain with swelling and warmth',
        'related': ['Arm pain', 'Forearm pain', 'Numbness in fingers', 'Swelling', 'Decreased range of motion']
    },
    {
        'title': 'Eye Pain (Ophthalmalgia)',
        'definition': 'Pain or discomfort localized to the eye or orbital region, which may be sharp, dull, burning, or throbbing, originating from ocular or periocular structures.',
        'pathophysiology': 'Eye pain is categorized as ocular (surface: cornea, conjunctiva, sclera) or orbital (deeper: optic nerve, extraocular muscles, vascular structures). Surface pain (foreign body sensation, burning) arises from corneal epithelial disruption (abrasion, dry eye, keratitis) or conjunctival inflammation. Deep, aching pain suggests glaucoma, optic neuritis, uveitis, or orbital pathology. Referred pain from trigeminal nerve branches may mimic eye pain.',
        'causes': [
            'Corneal abrasion or foreign body',
            'Dry eye disease (keratoconjunctivitis sicca)',
            'Conjunctivitis (viral, bacterial, allergic)',
            'Keratitis (infectious, contact lens-related)',
            'Acute angle-closure glaucoma (emergency)',
            'Uveitis or iritis',
            'Optic neuritis (associated with multiple sclerosis)',
            'Sinusitis (referred pain to eye)',
            'Orbital cellulitis (emergency)',
            'Cluster headache or migraine (ocular pain)'
        ],
        'seek_advice': 'Sudden severe eye pain with vision loss, redness, and halos (possible acute glaucoma), eye pain after trauma, or eye pain with fever and proptosis',
        'related': ['Headache', 'Vision blurred', 'Red eye', 'Photophobia', 'Nausea']
    },
    {
        'title': 'Foot Pain',
        'definition': 'Pain or discomfort localized anywhere in the foot, from the hindfoot (heel, ankle) through the midfoot (arch) to the forefoot (toes, metatarsals), with causes ranging from mechanical to systemic.',
        'pathophysiology': 'Foot pain etiology varies by location: heel pain most commonly from plantar fasciitis; midfoot pain from degenerative arthritis or stress fracture; metatarsalgia (forefoot pain) from weight-bearing overload, Morton neuroma, or Freiberg infarction; great toe pain from hallux valgus (bunion), hallux rigidus, or gout. The foot\'s 26 bones, 33 joints, and complex ligamentous/tendinous architecture create numerous pain generators.',
        'causes': [
            'Plantar fasciitis',
            'Metatarsalgia',
            'Morton neuroma (interdigital neuroma)',
            'Hallux valgus (bunion)',
            'Hallux rigidus (great toe arthritis)',
            'Hammer toe or claw toe deformity',
            'Stress fracture (metatarsal, navicular)',
            'Tarsal tunnel syndrome',
            'Gout (usually first metatarsophalangeal joint)',
            'Flatfoot (pes planus) or cavus foot deformity'
        ],
        'seek_advice': 'Foot pain with inability to bear weight, open wound or ulcer, fever, redness spreading up the leg, or sudden severe pain with swelling',
        'related': ['Heel pain', 'Ankle pain', 'Toe pain', 'Swelling', 'Numbness or tingling']
    },
    {
        'title': 'Frequent Bowel Movements',
        'definition': 'Increased frequency of defecation exceeding three bowel movements per day, often with loose or urgent stools, reflecting altered gastrointestinal motility or secretion.',
        'pathophysiology': 'Increased stool frequency results from reduced colonic transit time (rapid transit prevents water absorption leading to loose stools), increased secretion (enterotoxins, bile acid malabsorption), or increased smooth muscle contractility (IBS, hyperthyroidism). Acute onset suggests infection (gastroenteritis) while chronic suggests functional IBS, IBD, malabsorption, or medication effect.',
        'causes': [
            'Acute gastroenteritis (viral, bacterial, parasitic)',
            'Irritable bowel syndrome (IBS-D)',
            'Inflammatory bowel disease (Crohn disease, ulcerative colitis)',
            'Food intolerances (lactose, gluten, FODMAPs)',
            'Hyperthyroidism',
            'Bile acid malabsorption',
            'Medication side effects (metformin, antibiotics, laxatives, SSRIs)',
            'Anxiety or stress-related',
            'Celiac disease',
            'Colon cancer or carcinoid syndrome (rare)'
        ],
        'seek_advice': 'Frequent bowel movements with blood, weight loss, fever, nocturnal symptoms, or dehydration',
        'related': ['Diarrhea', 'Abdominal pain', 'Nausea', 'Urgency', 'Bloating']
    },
    {
        'title': 'Green Stool',
        'definition': 'Green-colored stool resulting from the presence of bile pigments, rapid intestinal transit, or ingestion of green-colored foods or supplements.',
        'pathophysiology': 'Bilirubin produced from heme breakdown is conjugated in the liver, secreted into bile, and normally metabolized by gut bacteria to stercobilin (brown pigment). Green stool occurs when bile passes through the intestine too rapidly for bacterial conversion to stercobilin, or when biliverdin (green pigment) is not fully reduced. Dietary chlorophyll (green vegetables) and artificial food coloring (green dyes) are common benign causes.',
        'causes': [
            'Dietary: green leafy vegetables (spinach, kale)',
            'Food coloring (green dyes in beverages, candies, gelatin)',
            'Rapid intestinal transit (diarrhea, IBS-D)',
            'Bile acid malabsorption',
            'Antibiotic use (altered gut flora)',
            'Iron supplements',
            'Green-colored medications or supplements',
            'Infectious gastroenteritis (especially Salmonella)',
            'Crohn disease or ulcerative colitis',
            'Malabsorption syndromes'
        ],
        'seek_advice': 'Persistent green stool with diarrhea, weight loss, abdominal pain, or other concerning GI symptoms',
        'related': ['Diarrhea', 'Abdominal pain', 'Bloating', 'Weight loss', 'Nausea']
    },
    {
        'title': 'Neck Pain',
        'definition': 'Pain or discomfort localized to the cervical spine region, from the base of the skull to the upper shoulders, arising from musculoskeletal, neurological, or referred sources.',
        'pathophysiology': 'Neck pain most commonly results from mechanical dysfunction: muscle strain, ligamentous sprain, or facet joint irritation. Degenerative changes (cervical spondylosis) involve disc desiccation, osteophyte formation, and facet hypertrophy, which may lead to foraminal stenosis and nerve root compression (cervical radiculopathy). Myelopathy from spinal cord compression is a serious but less common cause.',
        'causes': [
            'Mechanical neck pain (muscle strain, poor posture)',
            'Cervical spondylosis (degenerative disc disease)',
            'Cervical radiculopathy (herniated disc, foraminal stenosis)',
            'Whiplash injury (motor vehicle accident)',
            'Tension-type headache (referred to neck)',
            'Meningitis (with fever, photophobia, Kernig sign)',
            'Cervical myelopathy (spinal cord compression)',
            'Fibromyalgia or myofascial pain syndrome',
            'Rheumatoid arthritis (atlantoaxial instability)',
            'Vertebral artery dissection (rare, with neurological symptoms)'
        ],
        'seek_advice': 'Neck pain with fever and stiff neck (possible meningitis), neck pain after trauma, or neck pain with arm weakness/numbness',
        'related': ['Headache', 'Shoulder pain', 'Arm pain or numbness', 'Stiffness', 'Limited range of motion']
    },
    {
        'title': 'Painful Urination (Dysuria)',
        'definition': 'Pain, burning, or discomfort experienced during urination, typically indicating irritation or inflammation of the lower urinary tract (urethra, bladder, or prostate).',
        'pathophysiology': 'Dysuria results from inflammation of the urethral or bladder mucosa, stimulating nociceptive nerve endings during urine passage. In women, the short urethra facilitates ascending bacterial infection (cystitis). In men, urethral irritation from infection (STI, prostatitis) or obstruction (BPH) is more common. Non-infectious causes include chemical irritation, interstitial cystitis, and atrophic vaginitis.',
        'causes': [
            'Urinary tract infection (cystitis)',
            'Urethritis (gonorrhea, chlamydia, trichomonas)',
            'Prostatitis (acute or chronic bacterial)',
            'Interstitial cystitis (painful bladder syndrome)',
            'Atrophic vaginitis (postmenopausal)',
            'Chemical irritants (soaps, spermicides, hygiene products)',
            'Urethral stricture',
            'Bladder stones',
            'Medication side effects (cyclophosphamide)',
            'Sexually transmitted infections'
        ],
        'seek_advice': 'Dysuria with fever, flank pain, blood in urine, vaginal/penile discharge, or inability to urinate',
        'related': ['Urinary frequency', 'Urinary urgency', 'Blood in urine', 'Flank pain', 'Fever']
    },
    {
        'title': 'Peeling Skin',
        'definition': 'Desquamation or shedding of the outer epidermal layer of skin, which may be localized or generalized, resulting from environmental damage, infection, inflammation, or systemic disease.',
        'pathophysiology': 'Peeling skin results from disruption of intercellular adhesion between keratinocytes or accelerated epidermal turnover. Sunburn causes direct keratinocyte DNA damage triggering apoptosis and detachment. In inflammatory conditions (eczema, psoriasis), dysregulated immune responses accelerate epidermal proliferation and shedding. Infectious causes (staphylococcal scalded skin syndrome, fungal infections) directly disrupt desmosomal adhesion.',
        'causes': [
            'Sunburn (UV-induced skin damage)',
            'Dry skin (xerosis) from low humidity or over-washing',
            'Allergic contact dermatitis (poison ivy, nickel, cosmetics)',
            'Atopic dermatitis (eczema)',
            'Psoriasis (plaque or guttate)',
            'Fungal infections (tinea pedis/athlete\'s foot)',
            'Kawasaki disease (in children, with fever and rash)',
            'Scarlet fever (desquamation after fever resolves)',
            'Staphylococcal scalded skin syndrome (emergency)',
            'Medication reactions (Stevens-Johnson syndrome — emergency)'
        ],
        'seek_advice': 'Peeling skin with fever, blistering, mucosal involvement, or widespread skin detachment (possible SJS/TEN)',
        'related': ['Rash', 'Itching', 'Dry skin', 'Redness', 'Blisters']
    },
    {
        'title': 'Petechiae',
        'definition': 'Small (1-3 mm), non-blanching, red or purple spots on the skin caused by intradermal hemorrhage from ruptured capillaries, indicating platelet or vascular abnormalities.',
        'pathophysiology': 'Petechiae result from bleeding into the dermis due to thrombocytopenia (low platelet count), platelet dysfunction, capillary fragility, or increased intravascular pressure. Non-blanching with diascopy distinguishes petechiae from erythema. Distribution provides clues: dependent areas (lower extremities) suggest vasculitis or increased pressure; widespread suggests systemic thrombocytopenia or coagulopathy.',
        'causes': [
            'Thrombocytopenia (ITP, chemotherapy, leukemia, bone marrow failure)',
            'Platelet dysfunction (aspirin, NSAIDs, uremia)',
            'Vasculitis (Henoch-Schonlein purpura, microscopic polyangiitis)',
            'Infections (meningococcemia, endocarditis, RMSF, viral)',
            'Coagulation disorders (hemophilia, von Willebrand disease)',
            'Trauma or vigorous coughing/vomiting (Valsalva)',
            'Medication reactions',
            'Fat embolism syndrome',
            'Sepsis or disseminated intravascular coagulation (DIC)',
            'Senile purpura (fragile capillaries in elderly)'
        ],
        'seek_advice': 'Petechiae with fever, bleeding from other sites, neurological symptoms, or widespread rapid onset (possible meningococcemia or DIC)',
        'related': ['Easy bruising', 'Bleeding gums', 'Nosebleeds', 'Fever', 'Fatigue']
    },
    {
        'title': 'Rectal Bleeding',
        'definition': 'Passage of blood from the rectum, which may be bright red (hematochezia, indicating distal GI source) or dark/maroon (suggesting proximal source).',
        'pathophysiology': 'Bright red blood coating stool or on toilet paper typically originates from hemorrhoids (internal or external), anal fissures, or distal rectal pathology. Darker blood mixed with stool suggests a colonic source (diverticulosis, colitis, polyps, malignancy). Massive bright red bleeding with clots may indicate diverticular hemorrhage or angiodysplasia. Hemorrhoids are the most common cause but colorectal cancer must always be excluded.',
        'causes': [
            'Internal or external hemorrhoids',
            'Anal fissure',
            'Diverticulosis (diverticular bleeding)',
            'Colorectal polyps or carcinoma',
            'Inflammatory bowel disease (ulcerative colitis, Crohn disease)',
            'Angiodysplasia (vascular malformation)',
            'Infectious colitis (E. coli, Shigella, Campylobacter)',
            'Radiation proctitis',
            'Ischemic colitis',
            'Rectal trauma or foreign body'
        ],
        'seek_advice': 'Heavy rectal bleeding with dizziness or syncope, bleeding with abdominal pain, or any rectal bleeding in patients over 50',
        'related': ['Blood in stool', 'Anal pain', 'Abdominal pain', 'Constipation', 'Weight loss']
    },
    {
        'title': 'Red Eye',
        'definition': 'Redness of the eye due to dilation of superficial blood vessels of the conjunctiva, episclera, or sclera, ranging from benign conjunctival injection to sight-threatening ocular emergencies.',
        'pathophysiology': 'Red eye results from vasodilation of conjunctival or episcleral vessels triggered by inflammation, infection, allergy, trauma, or increased intraocular pressure. Pattern of injection helps localize pathology: diffuse conjunctival injection suggests conjunctivitis; circumcorneal (ciliary flush) suggests keratitis, iritis, or acute glaucoma; sectoral injection suggests episcleritis or scleritis.',
        'causes': [
            'Conjunctivitis (viral, bacterial, allergic) — most common',
            'Subconjunctival hemorrhage (benign, spontaneous)',
            'Corneal abrasion or foreign body',
            'Keratitis (infectious, contact lens-related)',
            'Acute angle-closure glaucoma (emergency)',
            'Uveitis or iritis',
            'Episcleritis or scleritis',
            'Dry eye disease (keratoconjunctivitis sicca)',
            'Trauma (corneal laceration, globe rupture)',
            'Orbital cellulitis (with proptosis, fever, pain with eye movement)'
        ],
        'seek_advice': 'Red eye with severe pain, vision loss, photophobia, halos around lights, corneal opacity, or trauma',
        'related': ['Eye pain', 'Vision blurred', 'Photophobia', 'Eye discharge', 'Headache']
    },
    {
        'title': 'Urine Odor',
        'definition': 'Unusual or strong smell of urine, which may be sweet, foul, fishy, or ammonia-like, reflecting dietary, metabolic, infectious, or medication-related causes.',
        'pathophysiology': 'Normal urine has a mild odor from byproducts of metabolism. Strong ammonia odor results from bacterial urea breakdown (UTI or prolonged urine stasis). Sweet or fruity odor suggests ketones (diabetic ketoacidosis, starvation) or maple syrup urine disease. Fishy odor indicates bacterial vaginosis or trichomonas (contaminating urine sample) or trimethylaminuria. Asparagus causes a characteristic sulfurous odor from asparagusic acid metabolism.',
        'causes': [
            'Urinary tract infection (ammonia or foul odor)',
            'Dehydration (concentrated urine with strong ammonia)',
            'Dietary: asparagus, garlic, onions, curry, coffee',
            'Diabetic ketoacidosis (sweet or fruity odor)',
            'Medications and supplements (B vitamins, sulfonamides)',
            'Liver failure (musty odor)',
            'Maple syrup urine disease (sweet, maple syrup odor in infants)',
            'Phenylketonuria (musty or mousy odor)',
            'Trimethylaminuria (fishy odor, rare metabolic disorder)',
            'Bacterial vaginosis or trichomonas (contaminating urine sample)'
        ],
        'seek_advice': 'Urine odor with fever, flank pain, dysuria, blood in urine, or unusual odor persisting without clear dietary cause',
        'related': ['Frequent urination', 'Painful urination', 'Urinary urgency', 'Dehydration', 'Vaginal discharge']
    },
    {
        'title': 'Watery Eyes (Epiphora)',
        'definition': 'Excessive production of tears or impaired drainage of tears from the eye, causing tears to spill onto the face.',
        'pathophysiology': 'Epiphora results from either tear overproduction (reflex tearing from dry eye, irritation, or inflammation) or impaired tear drainage (nasolacrimal duct obstruction, punctal stenosis, eyelid malposition). Reflex tearing from dry eye is the most common mechanism: ocular surface dryness triggers a neural reflex for excessive tear production, which overwhelms normal drainage.',
        'causes': [
            'Dry eye syndrome (reflex tearing)',
            'Nasolacrimal duct obstruction (congenital or acquired)',
            'Punctal stenosis or occlusion',
            'Ectropion or entropion (eyelid malposition)',
            'Allergic conjunctivitis',
            'Viral conjunctivitis',
            'Corneal foreign body or abrasion',
            'Eyelash irritation (trichiasis)',
            'Sinusitis or nasal congestion (impaired drainage)',
            'Medication side effects (some glaucoma drops, chemotherapy)'
        ],
        'seek_advice': 'Persistent watery eyes with pain, discharge, vision changes, or recurrent eye infections',
        'related': ['Red eye', 'Eye pain', 'Blurred vision', 'Eye discharge', 'Nasal congestion']
    },
    {
        'title': 'White Tongue',
        'definition': 'White discoloration or coating on the dorsal surface of the tongue, which may be patchy or diffuse, resulting from accumulation of debris, fungal overgrowth, or epithelial abnormalities.',
        'pathophysiology': 'White tongue most commonly results from oral thrush (Candida albicans overgrowth), which penetrates the superficial epithelial layer producing creamy white plaques that can be scraped off. Oral hairy leukoplakia (EBV-associated) presents with adherent white corrugated patches on the lateral tongue in immunocompromised individuals. Leukoplakia (premalignant) and lichen planus produce adherent white plaques that cannot be scraped off.',
        'causes': [
            'Oral thrush (candidiasis) — most common',
            'Poor oral hygiene with bacterial/food debris coating',
            'Oral lichen planus (reticular form)',
            'Leukoplakia (premalignant white patch)',
            'Oral hairy leukoplakia (EBV, HIV-associated)',
            'Dehydration or dry mouth (xerostomia)',
            'Smoking or tobacco use (smoker\'s keratosis)',
            'Geographic tongue (benign migratory glossitis)',
            'Mouth breathing (drying of tongue surface)',
            'Autoimmune conditions (lupus, Sjogren syndrome)'
        ],
        'seek_advice': 'White patch on tongue that does not scrape off, persists more than 2 weeks, or is associated with pain, bleeding, or difficulty swallowing',
        'related': ['Bad breath', 'Dry mouth', 'Oral thrush', 'Taste changes', 'Sore throat']
    },
    {
        'title': 'Yellow Tongue',
        'definition': 'Yellowish discoloration of the dorsal tongue surface, usually resulting from accumulation of bacteria, debris, or staining on elongated filiform papillae.',
        'pathophysiology': 'Yellow tongue typically arises from overgrowth of chromogenic bacteria or fungi (often Candida) on the tongue dorsum, especially when filiform papillae are elongated (hairy tongue). Elongation occurs when normal desquamation is impaired by poor oral hygiene, dry mouth, soft diet, or medications. The yellow color may also result from staining by food, tobacco, or mouthwashes containing oxidizing agents.',
        'causes': [
            'Poor oral hygiene (bacterial overgrowth)',
            'Dry mouth (xerostomia)',
            'Dehydration',
            'Smoking or tobacco use',
            'Mouthwashes containing peroxide or witch hazel',
            'Oral thrush (Candida overgrowth, can appear yellow)',
            'Coffee, tea, or food staining',
            'Antibiotic use (altered oral flora)',
            'Fever or illness (reduced oral clearance)',
            'Jaundice (rare — sclera also yellow, bilirubin elevated)'
        ],
        'seek_advice': 'Yellow tongue persisting more than 2 weeks despite good oral hygiene, or with jaundice, pain, or difficulty eating',
        'related': ['Bad breath', 'White tongue', 'Dry mouth', 'Taste changes', 'Oral thrush']
    },
]

for s in missing:
    create_chapter(**s)

print(f'\nGenerated {len(missing)} chapters.')
