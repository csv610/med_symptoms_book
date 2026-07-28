#!/usr/bin/env python3
"""Generate missing menopause symptom chapters from The Menopause Charity."""
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
    lines.append('\\begin{itemize}')
    for r in related:
        lines.append('  \\item ' + r)
    lines.append('\\end{itemize}')
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
        'title': 'Acne',
        'definition': 'A common skin condition characterised by the formation of comedones (blackheads and whiteheads), papules, pustules, nodules, and cysts, typically on the face, chest, and back, resulting from pilosebaceous unit inflammation.',
        'pathophysiology': 'Acne vulgaris develops from four key processes: increased sebum production driven by androgens (testosterone converted to dihydrotestosterone), follicular hyperkeratinisation leading to comedone formation, Cutibacterium acnes colonisation of the follicle, and subsequent inflammation. In perimenopause, declining oestrogen unmasks androgen effects, increasing sebaceous gland activity. Menopausal hormonal shifts can trigger late-onset acne in previously clear skin.',
        'causes': [
            'Hormonal fluctuations (perimenopause, menopause, puberty, polycystic ovary syndrome)',
            'Androgen excess (increased sebum production)',
            'Genetic predisposition to follicular hyperkeratinisation',
            'Cutibacterium acnes overgrowth',
            'Comedogenic cosmetics or skincare products',
            'Medications (corticosteroids, lithium, androgens,某些 contraceptives)',
            'Stress (cortisol-mediated androgen stimulation)',
            'High glycaemic load diet (controversial, potential insulin/IGF-1 mediated)',
            'Mechanical occlusion (headbands, helmets, face masks)',
            'Excessive facial cleansing or scrubbing (irritation)'
        ],
        'seek_advice': 'Acne that is severe, painful, cystic, causing scarring, or unresponsive to over-the-counter treatments for 2-3 months',
        'related': ['Oily skin', 'Hair loss', 'Hirsutism', 'Irregular periods', 'Skin changes']
    },
    {
        'title': 'Anhedonia (Loss of Interest)',
        'definition': 'The reduced ability to experience pleasure or interest in activities that were previously enjoyable, a core symptom of depression that may also occur independently during hormonal transitions.',
        'pathophysiology': 'Anhedonia involves dysfunction of the brain reward circuitry, particularly the mesolimbic dopamine pathway projecting from the ventral tegmental area to the nucleus accumbens and prefrontal cortex. Oestrogen modulates dopamine receptor density and sensitivity; declining oestrogen during perimenopause reduces dopaminergic tone, blunting reward perception. Serotonergic and noradrenergic systems are also affected, contributing to diminished anticipation and experience of pleasure.',
        'causes': [
            'Major depressive disorder (most common association)',
            'Perimenopausal and menopausal hormonal changes',
            'Chronic stress (elevated cortisol suppressing dopamine)',
            'Schizophrenia or schizoaffective disorder',
            'Substance use disorders (dopamine receptor downregulation)',
            'Parkinson disease (dopamine depletion)',
            'Post-traumatic stress disorder',
            'Medication side effects (SSRIs, antipsychotics)',
            'Hypothyroidism',
            'Vitamin D deficiency'
        ],
        'seek_advice': 'Persistent loss of interest lasting more than 2 weeks, especially with depressed mood, sleep or appetite changes, or suicidal thoughts',
        'related': ['Depression', 'Fatigue', 'Low mood', 'Mood swings', 'Difficulty concentrating']
    },
    {
        'title': 'Breast Tenderness (Mastalgia)',
        'definition': 'Pain, discomfort, or tenderness in one or both breasts, ranging from mild soreness to severe pain that interferes with daily activities, often cyclical in relation to hormonal fluctuations.',
        'pathophysiology': 'Cyclical mastalgia correlates with the luteal phase of the menstrual cycle when progesterone and oestrogen peak, causing breast tissue oedema, ductal proliferation, and stromal expansion. Hormone-sensitive breast tissue contains oestrogen and progesterone receptors; hormonal fluctuations during perimenopause alter the normal cyclical pattern. Non-cyclical mastalgia arises from extramammary structures (chest wall, costochondral junctions) or focal breast pathology (cysts, fibroadenomas, duct ectasia).',
        'causes': [
            'Cyclical hormonal fluctuations (perimenopause, menstrual cycle)',
            'Hormone replacement therapy (HRT) or oral contraceptives',
            'Breast cysts (fibrocystic breast changes)',
            'Fibroadenomas',
            'Mastitis (infectious or non-infectious inflammation)',
            'Duct ectasia',
            'Costochondritis (chest wall pain referred to breast)',
            'Trauma or prior breast surgery',
            'Large or heavy breasts (mechanical strain)',
            'Breast cancer (rare, usually painless but possible)'
        ],
        'seek_advice': 'Breast pain with a new palpable lump, skin changes (dimpling, redness, peau d\'orange), nipple discharge, or persistent focal pain lasting more than one menstrual cycle',
        'related': ['Breast lump', 'Nipple discharge', 'Breast swelling', 'Premenstrual syndrome', 'Painful sex']
    },
    {
        'title': 'Brittle Nails (Nail Changes)',
        'definition': 'Nails that are weak, thin, split, peel, or break easily, reflecting impaired keratinisation or nutritional deficiencies affecting the nail matrix and plate.',
        'pathophysiology': 'Nail plate formation occurs in the nail matrix through keratinocyte differentiation and keratinisation. Oestrogen receptors in the nail matrix regulate keratin production; declining oestrogen during menopause reduces nail thickness and integrity. Reduced oil production (sebum) also affects the nail cuticle and hydration. Nutritional deficiencies, repeated wet-dry cycles (housework, swimming), and trauma from manicure techniques further compromise nail structure.',
        'causes': [
            'Hormonal changes of perimenopause and menopause',
            'Iron deficiency anaemia',
            'Zinc deficiency',
            'Biotin deficiency',
            'Hypothyroidism or hyperthyroidism',
            'Repeated exposure to water and detergents',
            'Fungal nail infection (onychomycosis)',
            'Psoriasis (nail pitting, onycholysis)',
            'Trauma or aggressive manicure techniques',
            'Raynaud phenomenon or peripheral vascular disease'
        ],
        'seek_advice': 'Brittle nails with nail discolouration, thickening, separation from nail bed, or associated with fatigue, pallor, or weight changes',
        'related': ['Hair loss', 'Dry skin', 'Fatigue', 'Anaemia', 'Hypothyroidism']
    },
    {
        'title': 'Burning Mouth Syndrome',
        'definition': 'A chronic or recurrent burning sensation in the oral cavity without clinically identifiable mucosal abnormalities, commonly affecting the tongue, lips, palate, or entire mouth.',
        'pathophysiology': 'Burning mouth syndrome (BMS) involves dysfunction of the trigeminal nerve (CN V) and gustatory pathways, likely due to central and peripheral neuropathic mechanisms. Declining oestrogen alters oral mucosal sensitivity, salivary composition, and neurosensory processing. Reduced salivary flow (xerostomia) contributes to mucosal dryness and irritation. Cranial small fibre neuropathy, possibly autoimmune or hormonal in origin, is implicated in many cases. Subtypes include: Type 1 (worsens during the day), Type 2 (constant), Type 3 (intermittent with symptom-free periods).',
        'causes': [
            'Perimenopausal and menopausal hormonal changes (most common)',
            'Xerostomia (dry mouth from medications, autoimmune, or radiation)',
            'Nutritional deficiencies (iron, zinc, B vitamins, folate)',
            'Oral candidiasis (thrush)',
            'Gastro-oesophageal reflux disease (acid reaching the mouth)',
            'Medication side effects (ACE inhibitors, antiretrovirals, chemotherapy)',
            'Anxiety and depression (psychogenic BMS)',
            'Allergic contact stomatitis (dental materials, flavourings)',
            'Diabetes mellitus (peripheral neuropathy)',
            'Geographic tongue or oral lichen planus'
        ],
        'seek_advice': 'Burning mouth lasting more than 2 weeks with weight loss, difficulty eating, mucosal lesions, or associated systemic symptoms',
        'related': ['Dry mouth', 'Altered taste', 'Oral thrush', 'Mouth ulcers', 'Bad breath']
    },
    {
        'title': 'Clitoral Pain (Clitorodynia)',
        'definition': 'Pain, discomfort, hypersensitivity, or altered sensation localised to the clitoris, which may be burning, stabbing, or aching, and can occur spontaneously or with stimulation.',
        'pathophysiology': 'Clitoral tissue is densely innervated with sensory nerve endings and contains abundant oestrogen and androgen receptors. Declining oestrogen and testosterone during menopause cause clitoral tissue atrophy, reduced blood flow, and altered nerve sensitivity. The clitoral nerve is a terminal branch of the pudendal nerve (S2-S4); entrapment or irritation may cause referred or localised pain. Vulvodynia and clitorodynia share overlapping neuropathic and musculoskeletal mechanisms.',
        'causes': [
            'Genitourinary syndrome of menopause (clitoral atrophy)',
            'Vulvodynia (generalised or localised vulvar pain)',
            'Pudendal nerve entrapment or neuralgia',
            'Trauma (childbirth, surgery, sexual)',
            'Lichen sclerosus or lichen planus',
            'Recurrent candidiasis or fungal infection',
            'Contact dermatitis (soaps, lubricants, laundry products)',
            'Peyronie disease (affecting clitoral suspensory ligament, rare)',
            'Endometriosis of the clitoris (rare)',
            'Psychosexual factors (anxiety, history of abuse)'
        ],
        'seek_advice': 'Clitoral pain with visible lesions, discharge, fever, or associated with bladder/bowel symptoms, or pain that interferes with daily function',
        'related': ['Vulvovaginal irritation', 'Vaginal dryness', 'Painful sex', 'Pelvic pain', 'Labia changes']
    },
    {
        'title': 'Cold Intolerance (Feeling Cold)',
        'definition': 'An exaggerated sensitivity to cold temperatures or a persistent sensation of feeling cold even in normal environmental conditions, often with visible vasoconstriction of the extremities.',
        'pathophysiology': 'Cold intolerance results from altered thermoregulation, reduced metabolic heat production, or impaired vasomotor control. Oestrogen influences hypothalamic thermoregulatory set-point; declining oestrogen destabilises the thermoregulatory centre, causing both hot flushes and cold spells. Reduced basal metabolic rate (age-related and thyroid-related) decreases heat production. Vasomotor symptoms alternate between vasodilation (hot flushes) and vasoconstriction (cold flushes) as the hypothalamus attempts to regulate temperature.',
        'causes': [
            'Perimenopausal vasomotor instability (cold flushes)',
            'Hypothyroidism (reduced metabolic rate)',
            'Iron deficiency anaemia (impaired oxygen delivery)',
            'Peripheral arterial disease',
            'Raynaud phenomenon or disease',
            'Low body weight or inadequate caloric intake',
            'Anorexia nervosa (loss of insulating fat)',
            'Vitamin B12 deficiency (impaired myelination)',
            'Diabetes mellitus (peripheral neuropathy)',
            'Medications (beta-blockers, ergot derivatives)'
        ],
        'seek_advice': 'Persistent cold intolerance with fatigue, weight gain, constipation, dry skin, or colour changes in fingers/toes (blue/white)',
        'related': ['Fatigue', 'Cold hands and feet', 'Weight gain', 'Dry skin', 'Hot flushes']
    },
    {
        'title': 'Crying Spells',
        'definition': 'Episodes of uncontrollable or excessive tearfulness that occur unexpectedly or with minimal provocation, often unrelated to the severity of the triggering event.',
        'pathophysiology': 'Crying spells during perimenopause result from hormonal fluctuations affecting neurotransmitter systems that regulate emotional control. Oestrogen modulates serotonin synthesis, receptor sensitivity, and reuptake; declining and fluctuating oestrogen reduces serotonergic tone, impairing emotional regulation. The limbic system, particularly the amygdala and anterior cingulate cortex, becomes more reactive to emotional stimuli. Reduced GABAergic inhibition further disinhibits emotional expression.',
        'causes': [
            'Perimenopausal and menopausal hormonal fluctuations',
            'Premenstrual syndrome or premenstrual dysphoric disorder',
            'Major depressive disorder',
            'Anxiety disorders (generalised, panic)',
            'Adjustment disorder with depressed mood',
            'Post-traumatic stress disorder',
            'Pseudobulbar affect (neurological condition)',
            'Chronic stress and burnout',
            'Bereavement or grief',
            'Medication side effects (hormonal contraceptives, corticosteroids)'
        ],
        'seek_advice': 'Crying spells with suicidal thoughts, hopelessness, sleep or appetite changes, or lasting more than 2 weeks with functional impairment',
        'related': ['Depression', 'Anxiety', 'Mood swings', 'Irritability', 'Fatigue']
    },
    {
        'title': 'Electric Shock Sensation (Formication)',
        'definition': 'A sudden, brief sensation resembling an electric shock, tingling, or crawling feeling on or under the skin, typically lasting seconds, and often occurring without an external stimulus.',
        'pathophysiology': 'Electric shock sensations, medically termed paresthesias, arise from ectopic impulse generation in peripheral sensory nerves or central sensory pathways. Oestrogen supports myelin integrity and nerve conduction; declining oestrogen during perimenopause may increase nerve irritability. Reduced progesterone (which has a membrane-stabilising effect) further lowers the nerve excitation threshold. Hormonal fluctuations alter ion channel function (sodium, potassium, calcium) in sensory neurons, leading to spontaneous depolarisation.',
        'causes': [
            'Perimenopausal and menopausal hormonal fluctuations',
            'Cervical or lumbar nerve root compression (radiculopathy)',
            'Peripheral neuropathy (diabetic, alcoholic, nutritional)',
            'Multiple sclerosis (central demyelination)',
            'Migraine aura (sensory variant)',
            'Anxiety and hyperventilation syndrome',
            'Medication side effects (antidepressants, anticonvulsants)',
            'Vitamin B12 deficiency',
            'Hypocalcaemia or hypomagnesaemia',
            'Transient ischaemic attack (sensory cortex involvement)'
        ],
        'seek_advice': 'Frequent or persistent electric shock sensations with weakness, numbness, vision changes, or other neurological symptoms',
        'related': ['Tingling numbness', 'Nerve pain', 'Dizziness', 'Anxiety', 'Headache']
    },
    {
        'title': 'Irritability',
        'definition': 'An excessive or disproportionate response to stimuli characterised by anger, frustration, impatience, and a lowered threshold for annoyance, often with verbal or behavioural outbursts.',
        'pathophysiology': 'Irritability in perimenopause is driven by oestrogen fluctuation affecting neurotransmitter systems involved in impulse control and emotional regulation. Oestrogen modulates serotonin synthesis and receptor sensitivity in the prefrontal cortex, which governs executive control over emotions. Declining oestrogen reduces serotonergic tone, decreasing the brain\'s ability to inhibit anger and frustration. Progesterone fluctuations affect GABAergic inhibition, further lowering the irritability threshold. Sleep disruption (common in menopause) amplifies irritability through prefrontal cortex dysfunction.',
        'causes': [
            'Perimenopausal and menopausal hormonal changes',
            'Sleep deprivation or insomnia',
            'Premenstrual syndrome or PMDD',
            'Major depressive disorder or bipolar disorder',
            'Generalised anxiety disorder',
            'Chronic stress and burnout',
            'Hyperthyroidism (thyrotoxicosis)',
            'Chronic pain conditions',
            'Substance use or withdrawal (alcohol, caffeine, nicotine)',
            'Medication side effects (corticosteroids, stimulants)'
        ],
        'seek_advice': 'Irritability with mood swings, depression, anxiety, sleep disturbance, or relationship difficulties, especially if affecting daily function',
        'related': ['Mood swings', 'Depression', 'Anxiety', 'Insomnia', 'Fatigue']
    },
    {
        'title': 'Labia Changes (Atrophy)',
        'definition': 'Structural changes to the labia majora and minora including shrinkage, loss of elasticity, colour changes, and reduced tissue volume, resulting from hormonal insufficiency.',
        'pathophysiology': 'Labial tissues contain oestrogen and androgen receptors that maintain collagen density, vascularity, and elastic fibres. Declining oestrogen during menopause causes dermal thinning, reduced collagen synthesis, loss of subcutaneous fat, and decreased blood flow. The labia minora may become pale, thin, and gradually resorbed; the labia majora lose subcutaneous fat volume. These changes contribute to vulvovaginal atrophy (part of genitourinary syndrome of menopause) and can affect urinary and sexual function.',
        'causes': [
            'Genitourinary syndrome of menopause (oestrogen deficiency)',
            'Natural ageing (collagen loss independent of hormones)',
            'Lichen sclerosus (autoimmune, causes scarring and fusion)',
            'Lichen planus (inflammatory dermatosis)',
            'Crohn disease (vulvar involvement)',
            'Radiation therapy to the pelvic region',
            'Surgical menopause (bilateral oophorectomy)',
            'Chemotherapy-induced ovarian failure',
            'Autoimmune oophoritis',
            'Smoking (accelerated oestrogen metabolism)'
        ],
        'seek_advice': 'Labial changes with itching, burning, pain, skin thickening or whitening, fissures, or difficulty with intercourse',
        'related': ['Vaginal dryness', 'Vaginal atrophy', 'Painful sex', 'Clitoral pain', 'Urinary symptoms']
    },
    {
        'title': 'Lack of Motivation (Avolition)',
        'definition': 'A reduction or absence of the drive to initiate and persist in goal-directed activities, often experienced as apathy, indifference, or difficulty starting tasks despite a desire to complete them.',
        'pathophysiology': 'Motivation depends on intact dopaminergic signalling in the mesolimbic and mesocortical pathways connecting the ventral tegmental area to the nucleus accumbens (reward anticipation) and prefrontal cortex (executive planning). Oestrogen upregulates dopamine synthesis and receptor density; declining oestrogen reduces dopaminergic tone, impairing the brain\'s reward anticipation and motivational drive. Serotonin-dopamine interactions also influence motivation; low serotonin (from hormonal fluctuation) can inhibit dopamine function.',
        'causes': [
            'Perimenopausal and menopausal hormonal changes',
            'Major depressive disorder',
            'Chronic fatigue syndrome (myalgic encephalomyelitis)',
            'Hypothyroidism',
            'Vitamin D deficiency',
            'Sleep disorders (obstructive sleep apnoea, insomnia)',
            'Attention deficit hyperactivity disorder (executive dysfunction)',
            'Schizophrenia (negative symptoms)',
            'Frontal lobe disorders (dementia, traumatic brain injury)',
            'Medication side effects (SSRIs, antipsychotics, beta-blockers)'
        ],
        'seek_advice': 'Persistent lack of motivation with depressed mood, sleep changes, weight changes, or inability to perform daily activities',
        'related': ['Fatigue', 'Anhedonia', 'Depression', 'Difficulty concentrating', 'Insomnia']
    },
    {
        'title': 'Loss of Bone Density (Osteopenia/Osteoporosis)',
        'definition': 'Progressive reduction in bone mineral density, leading to weakened skeletal structure and increased fracture risk, most commonly resulting from oestrogen deficiency after menopause.',
        'pathophysiology': 'Oestrogen inhibits osteoclast activity through receptor activator of nuclear factor-kB ligand (RANKL) regulation. Oestrogen binds to oestrogen receptors on osteoclasts, promoting apoptosis and reducing bone resorption. The rapid decline in oestrogen during menopause removes this inhibitory signal, uncoupling bone remodelling: osteoclast activity increases while osteoblast activity does not keep pace, leading to net bone loss. Trabecular bone (vertebrae, distal radius) is affected more rapidly than cortical bone. Peak bone loss occurs in the first 3-5 years after menopause.',
        'causes': [
            'Menopausal oestrogen deficiency (primary cause)',
            'Advanced age',
            'Low peak bone mass (genetic, nutritional, exercise-related)',
            'Calcium and vitamin D deficiency',
            'Glucocorticoid use (corticosteroid-induced osteoporosis)',
            'Smoking',
            'Excessive alcohol consumption',
            'Low body weight (BMI < 19)',
            'Family history of osteoporosis or hip fracture',
            'Secondary causes (hyperthyroidism, hyperparathyroidism, malabsorption, rheumatoid arthritis)'
        ],
        'seek_advice': 'Bone density screening (DXA scan) is recommended for all women aged 65 and older, or younger with risk factors; seek advice after any low-trauma fracture',
        'related': ['Back pain', 'Loss of height', 'Joint pain', 'Fractures', 'Muscle weakness']
    },
    {
        'title': 'Low Self-Esteem (Loss of Confidence)',
        'definition': 'A negative perception of self-worth and abilities, often accompanied by self-doubt, social withdrawal, and difficulty asserting oneself in personal or professional settings.',
        'pathophysiology': 'Self-esteem is influenced by prefrontal cortical regulation of amygdala and limbic system responses to social evaluation. Oestrogen modulates serotonin and dopamine neurotransmission; declining oestrogen reduces serotonergic tone, increasing sensitivity to negative social feedback and self-criticism. Physical symptoms of menopause (hot flushes, weight gain, skin/hair changes) may alter body image and self-perception. Sleep disruption and fatigue impair cognitive function, further undermining confidence in work and social roles.',
        'causes': [
            'Perimenopausal and menopausal changes (physical and emotional)',
            'Major depressive disorder',
            'Generalised anxiety disorder',
            'Social anxiety disorder',
            'Body image disturbance (weight gain, skin/hair changes)',
            'Chronic illness or pain',
            'Workplace stress or discrimination',
            'Relationship difficulties or divorce',
            'History of trauma or abuse',
            'Perfectionism and high self-standards'
        ],
        'seek_advice': 'Low self-esteem with depressed mood, social withdrawal, work impairment, or thoughts of self-harm',
        'related': ['Depression', 'Anxiety', 'Mood swings', 'Fatigue', 'Body image concerns']
    },
    {
        'title': 'Low Libido (Female Hypoactive Sexual Desire Disorder)',
        'definition': 'Persistent or recurrent absence or deficiency of sexual fantasies, thoughts, and desire for sexual activity, causing marked distress or interpersonal difficulty.',
        'pathophysiology': 'Female sexual desire involves a complex interplay of neurological, hormonal, and psychosocial factors. Testosterone (produced by ovaries and adrenals) is the primary hormone driving sexual desire in women; its levels decline with age and fall significantly after menopause. Oestrogen maintains vaginal health and lubrication; its decline causes dyspareunia, which secondarily reduces desire. Dopamine (reward/anticipation) and serotonin (inhibition) balance sexual motivation. Menopausal hormonal shifts tilt this balance toward inhibition, while sleep deprivation, fatigue, and mood changes further suppress desire.',
        'causes': [
            'Menopausal testosterone and oestrogen decline',
            'Psychosocial factors (relationship conflict, stress, body image)',
            'Depression and anxiety',
            'Medication side effects (SSRIs, SNRIs, antipsychotics, hormonal contraceptives)',
            'Vaginal dryness and dyspareunia (fear of pain)',
            'Fatigue and sleep disturbance',
            'Hypothyroidism',
            'Hyperprolactinaemia',
            'Bilateral oophorectomy (surgical menopause)',
            'Chronic illness (diabetes, cardiovascular disease, cancer)'
        ],
        'seek_advice': 'Low libido causing personal distress, affecting relationships, or associated with depression, pain during sex, or other menopausal symptoms',
        'related': ['Vaginal dryness', 'Painful sex', 'Fatigue', 'Depression', 'Anxiety']
    },
    {
        'title': 'Migraine',
        'definition': 'A primary headache disorder characterised by recurrent attacks of moderate to severe unilateral pulsating headache lasting 4-72 hours, often accompanied by nausea, photophobia, phonophobia, and sometimes aura.',
        'pathophysiology': 'Migraine involves cortical spreading depression (CSD) activating the trigeminovascular system, releasing calcitonin gene-related peptide (CGRP) and substance P, causing neurogenic inflammation and vasodilation of meningeal blood vessels. Oestrogen modulates trigeminal nerve sensitivity and CGRP release; the natural perimenopausal oestrogen decline and fluctuation can destabilise migraine patterns. The classic oestrogen withdrawal trigger occurs during the late luteal phase when oestrogen falls sharply. Perimenopause typically worsens migraine frequency in women with menstrual-related migraine, while post-menopause may improve it in some.',
        'causes': [
            'Oestrogen fluctuation or withdrawal (perimenopause, menstrual cycle)',
            'Genetic predisposition (family history of migraine)',
            'Stress and anxiety',
            'Sleep disturbance (insufficient or excessive sleep)',
            'Dietary triggers (aged cheese, chocolate, alcohol, caffeine)',
            'Weather changes (barometric pressure, humidity)',
            'Hormonal medications (combined oral contraceptives, HRT)',
            'Dehydration or skipped meals',
            'Sensory triggers (bright lights, strong odours, loud noises)',
            'Medication overuse (analgesic rebound headache)'
        ],
        'seek_advice': 'Migraine with aura lasting more than 60 minutes, new-onset headache after age 50, worst headache of life, or headache with fever, stiff neck, or neurological deficits',
        'related': ['Headache', 'Nausea', 'Vision blurred', 'Photophobia', 'Dizziness']
    },
    {
        'title': 'Panic Attacks',
        'definition': 'Sudden episodes of intense fear or discomfort that peak within minutes, accompanied by physical symptoms such as palpitations, sweating, trembling, shortness of breath, chest pain, nausea, dizziness, and a sense of impending doom.',
        'pathophysiology': 'Panic attacks involve acute activation of the amygdala and its projections to the hypothalamus, periaqueductal grey, and locus coeruleus, triggering the sympathetic nervous system (fight-or-flight response). Oestrogen modulates the serotonergic and GABAergic systems that inhibit amygdala reactivity; declining oestrogen reduces inhibitory tone, lowering the panic threshold. Reduced progesterone (with its anxiolytic GABA-agonist metabolites) further disinhibits the panic circuit. Respiratory and interoceptive hypersensitivity (catastrophic misinterpretation of bodily sensations) amplifies the panic response.',
        'causes': [
            'Panic disorder (recurrent unexpected panic attacks with fear of recurrence)',
            'Perimenopausal and menopausal hormonal fluctuations',
            'Generalised anxiety disorder',
            'Major depressive disorder',
            'Post-traumatic stress disorder',
            'Hyperthyroidism (thyrotoxicosis)',
            'Hypoglycaemia',
            'Mitral valve prolapse',
            'Substance use or withdrawal (caffeine, alcohol, cocaine, cannabis)',
            'Medication side effects (stimulants, thyroid hormone)'
        ],
        'seek_advice': 'Recurrent panic attacks, panic attacks with suicidal thoughts, new onset after age 40 without clear trigger, or chest pain with shortness of breath (rule out cardiac)',
        'related': ['Anxiety', 'Heart palpitations', 'Shortness of breath', 'Dizziness', 'Chest pain']
    },
    {
        'title': 'Pelvic Organ Prolapse',
        'definition': 'Descent of one or more pelvic organs (uterus, bladder, rectum, bowel, or vaginal vault) into or beyond the vaginal canal due to weakened pelvic floor support structures.',
        'pathophysiology': 'Pelvic organ prolapse results from compromise of the pelvic floor musculature (levator ani complex) and connective tissue (endopelvic fascia, uterosacral ligaments). Oestrogen maintains collagen and elastin in pelvic support tissues; declining oestrogen after menopause reduces tissue strength and elasticity. Vaginal childbirth (particularly multiple or traumatic deliveries) stretches and damages the levator ani and pudendal nerve. Increased intra-abdominal pressure (obesity, chronic cough, constipation, heavy lifting) accelerates prolapse progression. Prolapse is graded I-IV based on descent relative to the hymen.',
        'causes': [
            'Menopause (oestrogen deficiency weakening connective tissue)',
            'Vaginal childbirth (especially multiple, instrumental, or macrosomic deliveries)',
            'Advanced age',
            'Obesity (increased intra-abdominal pressure)',
            'Chronic constipation or straining',
            'Chronic cough (smoking, COPD, asthma)',
            'Heavy lifting (occupational or recreational)',
            'Connective tissue disorders (Ehlers-Danlos, Marfan)',
            'Prior pelvic surgery (hysterectomy)',
            'Genetic predisposition (family history of prolapse)'
        ],
        'seek_advice': 'Sensation of a bulge or pressure in the vagina, pelvic heaviness, urinary or faecal incontinence, or difficulty emptying bladder/bowel',
        'related': ['Pelvic pain', 'Urinary incontinence', 'Urinary frequency', 'Back pain', 'Painful sex']
    },
    {
        'title': 'Restless Legs Syndrome (Willis-Ekbom Disease)',
        'definition': 'An urge to move the legs, usually accompanied by uncomfortable sensations, that begins or worsens during rest or inactivity, is partially relieved by movement, and occurs predominantly in the evening or at night.',
        'pathophysiology': 'Restless legs syndrome (RLS) involves dysfunction of the central dopaminergic system, particularly the A11 hypothalamospinal pathway that modulates sensorimotor integration in the spinal cord. Oestrogen modulates dopamine function; oestrogen fluctuation during perimenopause may unmask or worsen RLS. Iron is a cofactor for tyrosine hydroxylase (the rate-limiting enzyme in dopamine synthesis); iron deficiency impairs dopamine production. Circadian dopamine fluctuations explain the evening/nocturnal worsening of symptoms. Genetic variants in BTBD9, MEIS1, and PTPRD are associated with primary RLS.',
        'causes': [
            'Primary (idiopathic) restless legs syndrome (genetic)',
            'Iron deficiency (low ferritin < 75 mcg/L)',
            'Perimenopause and menopause (hormonal trigger)',
            'Pregnancy (especially third trimester, hormonal and iron-related)',
            'Chronic kidney disease (uraemia)',
            'Peripheral neuropathy (diabetic, alcoholic)',
            'Medication side effects (antidepressants SSRI/SNRI, antipsychotics, antihistamines)',
            'Caffeine, alcohol, or nicotine use (evening)',
            'Hypothyroidism',
            'Parkinson disease (dopamine deficiency)'
        ],
        'seek_advice': 'RLS severely disrupting sleep, causing daytime fatigue, or accompanied by leg swelling, pain, or redness (rule out vascular causes)',
        'related': ['Insomnia', 'Fatigue', 'Leg pain', 'Tingling numbness', 'Muscle cramps']
    },
    {
        'title': 'Weight Gain (Menopausal Weight Change)',
        'definition': 'Unintentional increase in body weight, typically with a shift toward abdominal (visceral) fat distribution, occurring during the perimenopausal and postmenopausal transition.',
        'pathophysiology': 'Menopausal weight gain results from several mechanisms: declining oestrogen reduces basal metabolic rate by approximately 50-100 kcal per decade; oestrogen deficiency increases visceral adipose tissue deposition by altering lipoprotein lipase activity; insulin sensitivity decreases, promoting fat storage; loss of lean muscle mass (sarcopenia) further reduces resting energy expenditure. Sleep disruption elevates cortisol and ghrelin while reducing leptin, increasing appetite and cravings. Fat distribution shifts from gynaecoid (hip/thigh) to android (abdominal) pattern, increasing cardiometabolic risk.',
        'causes': [
            'Oestrogen decline (reduced metabolic rate, increased visceral fat)',
            'Age-related sarcopenia (loss of muscle mass)',
            'Insulin resistance and glucose intolerance',
            'Sleep disruption (altered ghrelin, leptin, and cortisol)',
            'Thyroid dysfunction (hypothyroidism)',
            'Medication side effects (SSRIs, antipsychotics, beta-blockers, corticosteroids)',
            'Reduced physical activity (joint pain, fatigue)',
            'Emotional eating (mood swings, depression, stress)',
            'Cushing syndrome (cortisol excess, rare)',
            'Genetic predisposition to obesity'
        ],
        'seek_advice': 'Rapid or excessive weight gain (more than 5 kg in 6 months), weight gain with fatigue, cold intolerance, or new onset of metabolic syndrome features',
        'related': ['Fatigue', 'Joint pain', 'Bloating', 'Shortness of breath', 'Mood swings']
    },
]

for s in missing:
    create_chapter(**s)

print(f'\nGenerated {len(missing)} chapters.')
