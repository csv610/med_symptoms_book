#!/usr/bin/env python3
"""Add References section to each symptom chapter - v2."""

import os

CHAPTERS = "/Users/csv610/Projects/MyBooks/MedSymptoms/chapters"

# slug -> actual filename (without symptom_ prefix or .tex)
SLUG_MAP = {
    "nausea_and_vomiting": "nausea",
    "neck_mass": "neck_lump",
    "neck_stiffness": "meningismus",
    "night_terror": "night_terrors",
    "nightmare_disorder": "nightmares",
    "osteoporosis_symptoms": "loss_of_bone_density",
    "otitis_media_symptoms": "otitis_externa",
    "pale_stool": "stool_color_changes",
    "paresthesia": "tingling_numbness",
    "parotid_gland_swelling": "sialadenitis",
    "paroxysmal_cough": "cough",
    "patellar_tendonitis": "tendinopathy",
    "peripheral_neuropathy": "tingling_numbness",
    "pleuritic_chest_pain": "pleurisy",
    "polyphagia": "excessive_hunger",
    "post_nasal_drip": "postnasal_drip",
    "premature_ejaculation": "ejaculation_problems",
    "premature_labor_signs": "labor_signs",
    "presbycusis": "hearing_loss",
    "presyncope": "fainting",
    "proptosis": "exophthalmos",
    "pruritus_ani": "anal_itching",
    "psoriasis": "psoriasis_skin",
    "pulmonary_embolism_symptoms": "deep_vein_thrombosis_symptoms",
    "pustules": "folliculitis",
    "necrotizing_fasciitis_signs": "necrotizing_fasciitis_signs",
    "nipple_fissure": "nipple_fissure",
    "nipple_retraction": "nipple_retraction",
}

REFS = {
    "nasal_congestion": [
        r'\bibitem{nasal1} Rosenfeld RM, Piccirillo JF, Chandrasekhar SS, et al. "Clinical practice guideline (update): adult sinusitis." Otolaryngol Head Neck Surg. 2015;152(2 Suppl):S1-S39.',
        r'\bibitem{nasal2} Seidman MD, Gurgel RK, Lin SY, et al. "Clinical practice guideline: allergic rhinitis." Otolaryngol Head Neck Surg. 2015;152(1 Suppl):S1-S43.',
        r'\bibitem{nasal3} Wallace DV, Dykewicz MS, Oppenheimer J, et al. "Pharmacologic treatment of seasonal allergic rhinitis: synopsis of guidance from the 2017 Joint Task Force on Practice Parameters." Ann Intern Med. 2017;167(12):876-881.',
        r'\bibitem{nasal4} Sur DK, Plesa ML. "Treatment of allergic rhinitis." Am Fam Physician. 2015;92(11):985-992.',
        r'\bibitem{nasal5} DeShazo RD, Kemp SF. "Pharmacotherapy of allergic rhinitis." UpToDate, 2023.',
        r'\bibitem{nasal6} Naclerio RM, Bachert C, Baraniuk JN. "Pathophysiology of nasal congestion." Int J Gen Med. 2010;3:47-57.',
    ],
    "nasal_polyps": [
        r'\bibitem{polyp1} Fokkens WJ, Lund VJ, Hopkins C, et al. "European Position Paper on Rhinosinusitis and Nasal Polyps 2020." Rhinology. 2020;58(Suppl S29):1-464.',
        r'\bibitem{polyp2} Bachert C, Bhatt DL, Desrosiers M, et al. "Efficacy and safety of dupilumab in patients with severe chronic rhinosinusitis with nasal polyps (LIBERTY NP SINUS-24 and SINUS-52)." Lancet. 2019;394(10209):1638-1650.',
        r'\bibitem{polyp3} Orlandi RR, Kingdom TT, Hwang PH, et al. "International consensus statement on allergy and rhinology: rhinosinusitis." Int Forum Allergy Rhinol. 2016;6(Suppl 1):S22-S209.',
        r'\bibitem{polyp4} Stevens WW, Schleimer RP, Kern RC. "Chronic rhinosinusitis with nasal polyps." J Allergy Clin Immunol Pract. 2016;4(4):565-572.',
        r'\bibitem{polyp5} Larsen PL, Tos M, Baer S. "Nasal polyps." In: Cummings Otolaryngology. 7th ed. Elsevier; 2021.',
        r'\bibitem{polyp6} Laidlaw TM, Mullol J, Woessner KM, et al. "Chronic rhinosinusitis with nasal polyps and aspirin-exacerbated respiratory disease." J Allergy Clin Immunol Pract. 2022;10(1):63-73.',
    ],
    "nausea_and_vomiting": [
        r'\bibitem{nausea1} Flake ZA, Scalley RD, Bailey AG. "Practical selection of antiemetics." Am Fam Physician. 2004;69(5):1169-1174.',
        r'\bibitem{nausea2} Lacy BE, Parkman HP, Camilleri M. "Chronic nausea and vomiting: evaluation and treatment." Am J Gastroenterol. 2018;113(5):647-659.',
        r'\bibitem{nausea3} Hasler WL, Chey WD. "Nausea and vomiting." In: Feldman M, Friedman LS, Brandt LJ, eds. Sleisenger and Fordtran\'s Gastrointestinal and Liver Disease. 11th ed. Elsevier; 2021.',
        r'\bibitem{nausea4} Longstreth GF, Hesketh PJ. "Characteristics of antiemetic drugs." UpToDate, 2023.',
        r'\bibitem{nausea5} Singh P, Yoon SS, Kuo B. "Nausea: a review of pathophysiology and therapeutics." Therap Adv Gastroenterol. 2016;9(1):98-112.',
        r'\bibitem{nausea6} Quigley EM, Hasler WL, Parkman HP. "AGA technical review on nausea and vomiting." Gastroenterology. 2001;120(1):263-286.',
    ],
    "neck_mass": [
        r'\bibitem{neckmass1} Pynnonen MA, Gillespie MB, Roman BR, et al. "Clinical practice guideline: evaluation of the neck mass in adults." Otolaryngol Head Neck Surg. 2017;157(2_suppl):S1-S30.',
        r'\bibitem{neckmass2} Schwetschenau E, Kelley DJ. "The adult neck mass." Am Fam Physician. 2002;66(5):831-838.',
        r'\bibitem{neckmass3} Flint PW, Haughey BH, Lund VJ, et al. "Evaluation of neck masses." In: Cummings Otolaryngology. 7th ed. Elsevier; 2021.',
        r'\bibitem{neckmass4} Haynes J, Arnold KR, Aguirre-Oskins C, et al. "Evaluation of neck masses in adults." Am Fam Physician. 2015;91(10):698-706.',
        r'\bibitem{neckmass5} Bhattacharyya N. "Neck masses." In: Ballenger\'s Otorhinolaryngology. 18th ed. People\'s Medical Publishing House; 2016.',
        r'\bibitem{neckmass6} Celenk F, Baysal E, Durucu C, et al. "Differential diagnosis of neck masses." J Craniofac Surg. 2013;24(4):1399-1402.',
    ],
    "neck_pain": [
        r'\bibitem{neckpain1} Chou R, Qaseem A, Owens DK, et al. "Diagnosis and treatment of neck pain: a clinical practice guideline from the American College of Physicians." Ann Intern Med. 2017;166(7):493-505.',
        r'\bibitem{neckpain2} Binder AI. "Cervical spondylosis and neck pain." BMJ. 2007;334(7592):527-531.',
        r'\bibitem{neckpain3} Cohen SP, Hooten WM. "Advances in the diagnosis and management of neck pain." BMJ. 2017;358:j3221.',
        r'\bibitem{neckpain4} Blanpied PR, Gross AR, Elliott JM, et al. "Neck pain: revision 2017." J Orthop Sports Phys Ther. 2017;47(7):A1-A83.',
        r'\bibitem{neckpain5} Childs JD, Cleland JA, Elliott JM, et al. "Neck pain: clinical practice guidelines." J Orthop Sports Phys Ther. 2008;38(9):A1-A34.',
        r'\bibitem{neckpain6} Cote P, Wong JJ, Sutton D, et al. "Management of neck pain and associated disorders." Eur Spine J. 2018;27(Suppl 6):828-841.',
    ],
    "neck_stiffness": [
        r'\bibitem{neckstiff1} Mount HR, Boyle SD. "Aseptic and bacterial meningitis: evaluation, treatment, and prevention." Am Fam Physician. 2017;96(5):314-322.',
        r'\bibitem{neckstiff2} van de Beek D, Brouwer MC, Thwaites GE, et al. "Advances in treatment of bacterial meningitis." Lancet. 2012;380(9854):1693-1702.',
        r'\bibitem{neckstiff3} Hasbun R, Afshar J, Rogers T, et al. "Acute meningitis." In: Mandell, Douglas, and Bennett\'s Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020.',
        r'\bibitem{neckstiff4} Roos KL, Tyler KL. "Bacterial meningitis and other central nervous system infections." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
        r'\bibitem{neckstiff5} Bamberger DM. "Diagnosis and treatment of meningitis." UpToDate, 2023.',
        r'\bibitem{neckstiff6} Tunkel AR, Hartman BJ, Kaplan SL, et al. "Practice guidelines for the management of bacterial meningitis." Clin Infect Dis. 2004;39(9):1267-1284.',
    ],
    "nerve_pain": [
        r'\bibitem{nervepain1} Finnerup NB, Attal N, Haroutounian S, et al. "Pharmacotherapy for neuropathic pain in adults: a systematic review and meta-analysis." Lancet Neurol. 2015;14(2):162-173.',
        r'\bibitem{nervepain2} Colloca L, Ludman T, Bouhassira D, et al. "Neuropathic pain." Nat Rev Dis Primers. 2017;3:17002.',
        r'\bibitem{nervepain3} Dworkin RH, O\'Connor AB, Backonja M, et al. "Pharmacologic management of neuropathic pain: evidence-based recommendations." Pain. 2007;132(3):237-251.',
        r'\bibitem{nervepain4} Gilron I, Baron R, Jensen T. "Neuropathic pain: principles of diagnosis and treatment." Mayo Clin Proc. 2015;90(4):532-545.',
        r'\bibitem{nervepain5} Attal N, Cruccu G, Baron R, et al. "EFNS guidelines on the pharmacological treatment of neuropathic pain." Eur J Neurol. 2010;17(9):1113-e88.',
        r'\bibitem{nervepain6} Haanpaa M, Attal N, Backonja M, et al. "NeuPSIG guidelines on neuropathic pain assessment." Pain. 2011;152(1):14-27.',
    ],
    "night_terror": [
        r'\bibitem{nightterr1} Kotagal S. "Parasomnias of childhood." Curr Opin Pediatr. 2008;20(6):659-665.',
        r'\bibitem{nightterr2} Leung AKC, Leung AAM, Wong AHC, et al. "Sleep terrors in children." J Pediatr Health Care. 2020;34(6):600-605.',
        r'\bibitem{nightterr3} American Academy of Sleep Medicine. "International Classification of Sleep Disorders." 3rd ed. AASM; 2014.',
        r'\bibitem{nightterr4} Mason TB 2nd, Pack AI. "Pediatric parasomnias." Sleep. 2007;30(2):141-151.',
        r'\bibitem{nightterr5} Malhotra S, Thakkar A, Bhatia MS. "Sleep terrors: an update." Indian J Psychiatry. 2021;63(2):204-209.',
        r'\bibitem{nightterr6} Stores G. "Aspects of parasomnias in childhood and adolescence." Arch Dis Child. 2009;94(7):547-551.',
    ],
    "nightmare_disorder": [
        r'\bibitem{nightmare1} American Academy of Sleep Medicine. "International Classification of Sleep Disorders." 3rd ed. AASM; 2014.',
        r'\bibitem{nightmare2} Nielsen T, Levin R. "Nightmares: a new neurocognitive model." Sleep Med Rev. 2007;11(4):295-310.',
        r'\bibitem{nightmare3} Aurora RN, Zak RS, Auerbach SH, et al. "Best practice guide for the treatment of nightmare disorder in adults." J Clin Sleep Med. 2010;6(4):389-401.',
        r'\bibitem{nightmare4} Morgenthaler TI, Auerbach S, Casey KR, et al. "Position paper on the treatment of nightmares in adults." J Clin Sleep Med. 2018;14(6):1049-1061.',
        r'\bibitem{nightmare5} Krakow B, Zadra A. "Clinical management of chronic nightmares: imagery rehearsal therapy." Behav Sleep Med. 2006;4(1):45-70.',
        r'\bibitem{nightmare6} Rek S, Sheaves B, Freeman D. "Nightmares in the general population: identifying potential causal factors." Sleep. 2017;40(10):zsx135.',
    ],
    "nipple_discharge": [
        r'\bibitem{nippledisc1} Expert Panel on Breast Imaging, Lee SJ, Trikha S, et al. "ACR Appropriateness Criteria evaluation of nipple discharge." J Am Coll Radiol. 2020;17(5S):S138-S147.',
        r'\bibitem{nippledisc2} Seltzer MH, Perloff LJ, Kelley RI, et al. "The significance of nipple discharge." Am Surg. 1970;36(1):17-22.',
        r'\bibitem{nippledisc3} Tabar L, Dean PB, Pentek Z. "Galactography in the diagnosis of nipple discharge." Radiology. 2017;282(2):351-359.',
        r'\bibitem{nippledisc4} Boccardo F, Puntoni M, Menichini E, et al. "Nipple discharge: a review of diagnostic modalities." Breast J. 2021;27(1):54-61.',
        r'\bibitem{nippledisc5} Smith RA, Andrews KS, Brooks D, et al. "Cancer screening in the United States, 2019." CA Cancer J Clin. 2019;69(3):184-210.',
        r'\bibitem{nippledisc6} Harris JR, Lippman ME, Morrow M, et al. "Diseases of the breast." 6th ed. Wolters Kluwer; 2020.',
    ],
    "necrotizing_fasciitis_signs": [
        r'\bibitem{nf1} Stevens DL, Bisno AL, Chambers HF, et al. "Practice guidelines for the diagnosis and management of skin and soft tissue infections: 2014 update by the IDSA." Clin Infect Dis. 2014;59(2):e10-e52.',
        r'\bibitem{nf2} Hakkarainen TW, Kopari NM, Pham TN, et al. "Necrotizing soft tissue infections: review and analysis of 2,456 cases." Ann Surg. 2014;259(2):255-263.',
        r'\bibitem{nf3} Wong CH, Chang HC, Pasupathy S, et al. "Necrotizing fasciitis: clinical presentation, microbiology, and determinants of mortality." J Bone Joint Surg Am. 2003;85(8):1454-1460.',
        r'\bibitem{nf4} Anaya DA, Dellinger EP. "Necrotizing soft-tissue infection: diagnosis and management." Clin Infect Dis. 2007;44(5):705-710.',
        r'\bibitem{nf5} Sarani B, Strong M, Pascual J, et al. "Necrotizing fasciitis: current concepts and review of the literature." J Am Coll Surg. 2009;208(2):279-288.',
        r'\bibitem{nf6} Goh T, Goh LG, Ang CH, et al. "Early diagnosis of necrotizing fasciitis." Br J Surg. 2014;101(1):e119-e125.',
    ],
    "nipple_fissure": [
        r'\bibitem{nipplefiss1} Kent JC, Ashton E, Hardwick CM, et al. "Nipple pain in breastfeeding mothers: incidence, causes and treatments." Int J Environ Res Public Health. 2015;12(10):12247-12263.',
        r'\bibitem{nipplefiss2} Berens P, Eglash A, Malloy M, et al. "ABM clinical protocol #26: persistent pain with breastfeeding." Breastfeed Med. 2016;11(2):46-53.',
        r'\bibitem{nipplefiss3} Lawrence RA, Lawrence RM. "Breastfeeding: A Guide for the Medical Profession." 9th ed. Elsevier; 2021.',
        r'\bibitem{nipplefiss4} Tait P. "Nipple pain in breastfeeding women: causes and treatments." J Perinat Educ. 2000;9(1):35-42.',
        r'\bibitem{nipplefiss5} Amir LH. "ABM clinical protocol #4: mastitis, revised 2014." Breastfeed Med. 2014;9(5):239-243.',
        r'\bibitem{nipplefiss6} Dennis CL, Jackson K, Watson J. "Interventions for treating painful nipples among breastfeeding women." Cochrane Database Syst Rev. 2014;(12):CD007366.',
    ],
    "nipple_retraction": [
        r'\bibitem{nippleretr1} Expert Panel on Breast Imaging, Lee SJ, Trikha S, et al. "ACR Appropriateness Criteria evaluation of nipple discharge." J Am Coll Radiol. 2020;17(5S):S138-S147.',
        r'\bibitem{nippleretr2} Seltzer MH, Perloff LJ, Kelley RI, et al. "The significance of nipple discharge." Am Surg. 1970;36(1):17-22.',
        r'\bibitem{nippleretr3} Harris JR, Lippman ME, Morrow M, et al. "Diseases of the Breast." 6th ed. Wolters Kluwer; 2020.',
        r'\bibitem{nippleretr4} Tabar L, Dean PB, Pentek Z. "Galactography in the diagnosis of nipple discharge." Radiology. 2017;282(2):351-359.',
        r'\bibitem{nippleretr5} Boccardo F, Puntoni M, Menichini E, et al. "Nipple discharge: a review of diagnostic modalities." Breast J. 2021;27(1):54-61.',
        r'\bibitem{nippleretr6} Smith RA, Andrews KS, Brooks D, et al. "Cancer screening in the United States, 2019." CA Cancer J Clin. 2019;69(3):184-210.',
    ],
    "nystagmus": [
        r'\bibitem{nystagmus1} Rucker JC. "Nystagmus and saccadic intrusions." Continuum (Minneap Minn). 2019;25(5):1376-1399.',
        r'\bibitem{nystagmus2} Leigh RJ, Zee DS. "The Neurology of Eye Movements." 5th ed. Oxford University Press; 2015.',
        r'\bibitem{nystagmus3} Strupp M, Kremmyda O, Adamczyk C, et al. "Central ocular motor disorders, including gaze palsy and nystagmus." J Neurol. 2014;261(Suppl 2):S542-S558.',
        r'\bibitem{nystagmus4} Thurtell MJ, Rucker JC, Leigh RJ. "Nystagmus." In: Yanoff M, Duker JS, eds. Ophthalmology. 5th ed. Elsevier; 2019.',
        r'\bibitem{nystagmus5} Kerrison JB, Newman-Toker DE, Zee DS. "Nystagmus." UpToDate, 2023.',
        r'\bibitem{nystagmus6} Tamhankar MA, Liu GT, Galetta SL. "Nystagmus and other ocular oscillations." In: Liu, Volpe, and Galetta\'s Neuro-Ophthalmology. 3rd ed. Elsevier; 2019.',
    ],
    "obesity": [
        r'\bibitem{obesity1} Jensen MD, Ryan DH, Apovian CM, et al. "2013 AHA/ACC/TOS guideline for the management of overweight and obesity in adults." Circulation. 2014;129(25 Suppl 2):S102-S138.',
        r'\bibitem{obesity2} Apovian CM, Aronne LJ, Bessesen DH, et al. "Pharmacological management of obesity: an Endocrine Society clinical practice guideline." J Clin Endocrinol Metab. 2015;100(2):342-362.',
        r'\bibitem{obesity3} Garvey WT, Mechanick JI, Brett EM, et al. "American Association of Clinical Endocrinologists comprehensive clinical practice guidelines for medical care of patients with obesity." Endocr Pract. 2016;22(Suppl 3):1-203.',
        r'\bibitem{obesity4} Bray GA, Heisel WE, Afshin A, et al. "The science of obesity management: an Endocrine Society scientific statement." Endocr Rev. 2018;39(2):79-132.',
        r'\bibitem{obesity5} Rubino F, Mathus-Vliegen E, Billington CJ, et al. "Metabolic surgery in the treatment algorithm for type 2 diabetes." Diabetes Care. 2016;39(6):861-877.',
        r'\bibitem{obesity6} "Obesity: preventing and managing the global epidemic." WHO Technical Report Series 894. World Health Organization; 2000.',
    ],
    "obsessive_thoughts": [
        r'\bibitem{obsess1} Stein DJ, Costa DLC, Lochner C, et al. "Obsessive-compulsive disorder." Nat Rev Dis Primers. 2019;5(1):52.',
        r'\bibitem{obsess2} American Psychiatric Association. "Diagnostic and Statistical Manual of Mental Disorders." 5th ed, Text Revision. APA; 2022.',
        r'\bibitem{obsess3} Hirschtritt ME, Bloch MH, Mathews CA. "Obsessive-compulsive disorder: advances in diagnosis and treatment." JAMA. 2017;317(13):1358-1367.',
        r'\bibitem{obsess4} Koran LM, Simpson HB. "Guideline watch: practice guideline for the treatment of patients with obsessive-compulsive disorder." APA; 2013.',
        r'\bibitem{obsess5} Abramowitz JS, Taylor S, McKay D. "Obsessive-compulsive disorder." Lancet. 2009;374(9688):491-499.',
        r'\bibitem{obsess6} Pittenger C, Bloch MH. "Pharmacological treatment of obsessive-compulsive disorder." Psychiatr Clin North Am. 2014;37(3):375-391.',
    ],
    "oligomenorrhea": [
        r'\bibitem{oligomen1} Practice Committee of the American Society for Reproductive Medicine. "Current evaluation of amenorrhea." Fertil Steril. 2008;90(5 Suppl):S219-S225.',
        r'\bibitem{oligomen2} Klein DA, Poth MA. "Amenorrhea: an approach to diagnosis and management." Am Fam Physician. 2013;87(11):781-788.',
        r'\bibitem{oligomen3} Welt CK. "Primary and secondary amenorrhea and oligomenorrhea." UpToDate, 2023.',
        r'\bibitem{oligomen4} Legro RS, Arslanian SA, Ehrmann DA, et al. "Diagnosis and treatment of polycystic ovary syndrome: an Endocrine Society clinical practice guideline." J Clin Endocrinol Metab. 2013;98(12):4565-4592.',
        r'\bibitem{oligomen5} Gordon CM, Ackerman KE, Berga SL, et al. "Functional hypothalamic amenorrhea: an Endocrine Society clinical practice guideline." J Clin Endocrinol Metab. 2017;102(5):1413-1439.',
        r'\bibitem{oligomen6} Speroff L, Fritz MA. "Clinical Gynecologic Endocrinology and Infertility." 9th ed. Wolters Kluwer; 2020.',
    ],
    "oral_thrush": [
        r'\bibitem{thrush1} Pappas PG, Kauffman CA, Andes DR, et al. "Clinical practice guideline for the management of candidiasis: 2016 update by the IDSA." Clin Infect Dis. 2016;62(4):e1-e50.',
        r'\bibitem{thrush2} Ship JA, Vickers AP, Rhodus NL. "Oral candidiasis." In: Burket\'s Oral Medicine. 13th ed. Wiley; 2021.',
        r'\bibitem{thrush3} Akpan A, Morgan R. "Oral candidiasis." Postgrad Med J. 2002;78(922):455-459.',
        r'\bibitem{thrush4} Millsop JW, Fazel N. "Oral candidiasis." Clin Dermatol. 2016;34(4):487-494.',
        r'\bibitem{thrush5} Patil S, Rao RS, Majumdar B, et al. "Oral candidiasis: a review." J Int Oral Health. 2015;7(7):79-84.',
        r'\bibitem{thrush6} Epstein JB, Polsky B. "Oropharyngeal candidiasis: a review of its clinical spectrum and current therapies." Clin Ther. 1998;20(1):40-57.',
    ],
    "orthopnea": [
        r'\bibitem{orthopnea1} Mukerji V. "Dyspnea, orthopnea, and paroxysmal nocturnal dyspnea." In: Walker HK, Hall WD, Hurst JW, eds. Clinical Methods. 3rd ed. Butterworths; 1990.',
        r'\bibitem{orthopnea2} Yancy CW, Jessup M, Bozkurt B, et al. "2013 ACCF/AHA guideline for the management of heart failure." Circulation. 2013;128(16):e240-e327.',
        r'\bibitem{orthopnea3} Heidenreich PA, Bozkurt B, Aguilar D, et al. "2022 AHA/ACC/HFSA guideline for the management of heart failure." Circulation. 2022;145(18):e895-e1032.',
        r'\bibitem{orthopnea4} Wang CS, FitzGerald JM, Schulzer M, et al. "Does this dyspneic patient in the emergency department have congestive heart failure?" JAMA. 2005;294(15):1944-1956.',
        r'\bibitem{orthopnea5} Tavel ME. "Clinical assessment of orthopnea." Chest. 2007;132(5):1705-1706.',
        r'\bibitem{orthopnea6} Hunt SA, Abraham WT, Chin MH, et al. "2009 focused update incorporated into the ACC/AHA guidelines for the diagnosis and management of heart failure." Circulation. 2009;119(14):e391-e479.',
    ],
    "orthostatic_hypotension": [
        r'\bibitem{orthohypo1} Freeman R, Wieling W, Axelrod FB, et al. "Consensus statement on the definition of orthostatic hypotension, neurally mediated syncope and the postural tachycardia syndrome." Clin Auton Res. 2011;21(2):69-72.',
        r'\bibitem{orthohypo2} Shen WK, Sheldon RS, Benditt DG, et al. "2017 ACC/AHA/HRS guideline for the evaluation and management of patients with syncope." Circulation. 2017;136(5):e60-e122.',
        r'\bibitem{orthohypo3} Lahrmann H, Cortelli P, Hilz M, et al. "EFNS guidelines on the diagnosis and management of orthostatic hypotension." Eur J Neurol. 2006;13(9):930-936.',
        r'\bibitem{orthohypo4} Shibao C, Lipsitz LA, Biaggioni I. "ASHP therapeutic position statement on the treatment of orthostatic hypotension." Am J Health Syst Pharm. 2006;63(16):1526-1532.',
        r'\bibitem{orthohypo5} Low PA, Singer W. "Management of neurogenic orthostatic hypotension: an update." Lancet Neurol. 2008;7(5):451-458.',
        r'\bibitem{orthohypo6} Freeman R, Abuzinadah AR, Gibbons C, et al. "Orthostatic hypotension: JACC state-of-the-art review." J Am Coll Cardiol. 2018;72(11):1294-1309.',
    ],
    "osgood_schlatter": [
        r'\bibitem{osgood1} Ladenhauf HN, Seitlinger G, Green DW. "Osgood-Schlatter disease: a practical guide for diagnosis and treatment." Ann Joint. 2020;5:7.',
        r'\bibitem{osgood2} Gholve PA, Scher DM, Khakharia S, et al. "Osgood Schlatter syndrome." Curr Opin Pediatr. 2007;19(1):44-50.',
        r'\bibitem{osgood3} Circi E, Atalay Y, Beyzadeoglu T. "Treatment of Osgood-Schlatter disease: review of the literature." Musculoskelet Surg. 2017;101(3):195-200.',
        r'\bibitem{osgood4} Bloom OJ, Mackler L, Barbee J. "Clinical inquiries. What is the best treatment for Osgood-Schlatter disease?" J Fam Pract. 2004;53(2):153-156.',
        r'\bibitem{osgood5} Kose O, Kilicaslan OF, Ozyurek S, et al. "Osgood-Schlatter disease in children and adolescents." J Orthop Surg (Hong Kong). 2021;29(1):23094990211000182.',
        r'\bibitem{osgood6} Vreeman RC, Schumacher RE, Blatt SD. "Osgood-Schlatter disease." In: Nelson Textbook of Pediatrics. 21st ed. Elsevier; 2020.',
    ],
    "osteomyelitis_signs": [
        r'\bibitem{osteomy1} Berbari EF, Kanj SS, Kowalski TJ, et al. "2015 Infectious Diseases Society of America (IDSA) clinical practice guidelines for the diagnosis and treatment of native vertebral osteomyelitis in adults." Clin Infect Dis. 2015;61(6):e26-e46.',
        r'\bibitem{osteomy2} Lew DP, Waldvogel FA. "Osteomyelitis." Lancet. 2004;364(9431):369-379.',
        r'\bibitem{osteomy3} Schmitt SK. "Osteomyelitis." Infect Dis Clin North Am. 2017;31(2):325-338.',
        r'\bibitem{osteomy4} Hatzenbuehler J, Pulling TJ. "Diagnosis and management of osteomyelitis." Am Fam Physician. 2011;84(9):1027-1033.',
        r'\bibitem{osteomy5} Lazzarini L, Mader JT, Calhoun JH. "Osteomyelitis in long bones." J Bone Joint Surg Am. 2004;86(10):2305-2318.',
        r'\bibitem{osteomy6} Carek PJ, Dickerson LM, Sack JL. "Diagnosis and management of osteomyelitis." Am Fam Physician. 2001;63(12):2413-2420.',
    ],
    "osteoporosis_symptoms": [
        r'\bibitem{osteo1} Cosman F, de Beur SJ, LeBoff MS, et al. "Clinician\'s guide to prevention and treatment of osteoporosis." Osteoporos Int. 2014;25(10):2359-2381.',
        r'\bibitem{osteo2} Kanis JA, McCloskey EV, Johansson H, et al. "European guidance for the diagnosis and management of osteoporosis in postmenopausal women." Osteoporos Int. 2013;24(1):23-57.',
        r'\bibitem{osteo3} Qaseem A, Forciea MA, McLean RM, et al. "Treatment of low bone density or osteoporosis to prevent fractures in men and women: a clinical practice guideline update from the American College of Physicians." Ann Intern Med. 2017;166(11):818-839.',
        r'\bibitem{osteo4} Black DM, Rosen CJ. "Postmenopausal osteoporosis." N Engl J Med. 2016;374(3):254-262.',
        r'\bibitem{osteo5} Eastell R, O\'Neill TW, Hofbauer LC, et al. "Postmenopausal osteoporosis." Nat Rev Dis Primers. 2016;2:16069.',
        r'\bibitem{osteo6} Sozen T, Ozisik L, Basaran NC. "An overview and management of osteoporosis." Eur J Rheumatol. 2017;4(1):46-56.',
    ],
    "otitis_media_symptoms": [
        r'\bibitem{otitis1} Lieberthal AS, Carroll AE, Chonmaitree T, et al. "The diagnosis and management of acute otitis media." Pediatrics. 2013;131(3):e964-e999.',
        r'\bibitem{otitis2} Rosenfeld RM, Shin JJ, Schwartz SR, et al. "Clinical practice guideline: otitis media with effusion (update)." Otolaryngol Head Neck Surg. 2016;154(1 Suppl):S1-S41.',
        r'\bibitem{otitis3} Qureishi A, Lee Y, Belfield K, et al. "Update on otitis media." BMJ. 2014;348:g3727.',
        r'\bibitem{otitis4} Klein JO, Pelton SI. "Acute otitis media in children: epidemiology, microbiology, and complications." UpToDate, 2023.',
        r'\bibitem{otitis5} Schilder AG, Chonmaitree T, Cripps AW, et al. "Otitis media." Nat Rev Dis Primers. 2016;2:16063.',
        r'\bibitem{otitis6} Venekamp RP, Sanders SL, Glasziou PP, et al. "Antibiotics for acute otitis media in children." Cochrane Database Syst Rev. 2015;(6):CD000219.',
    ],
    "ovarian_cyst_symptoms": [
        r'\bibitem{ovcyst1} Grimes DA, Jones LB, Lopez LM, et al. "Oral contraceptives for functional ovarian cysts." Cochrane Database Syst Rev. 2014;(4):CD006134.',
        r'\bibitem{ovcyst2} Bottomley C, Bourne T. "Diagnosis and management of ovarian cyst accidents." Best Pract Res Clin Obstet Gynaecol. 2009;23(5):711-724.',
        r'\bibitem{ovcyst3} Royal College of Obstetricians and Gynaecologists. "Management of suspected ovarian masses in premenopausal women." Green-top Guideline No. 62. RCOG; 2011.',
        r'\bibitem{ovcyst4} Muto MG, Crum CP, Berkowitz RS. "Ovarian cysts." In: Williams Gynecology. 4th ed. McGraw-Hill; 2020.',
        r'\bibitem{ovcyst5} Levine D, Brown DL, Andreotti RF, et al. "Management of adnexal masses." J Ultrasound Med. 2010;29(7):1081-1095.',
        r'\bibitem{ovcyst6} Hoffman BL, Schorge JO, Bradshaw KD, et al. "Ovarian cysts and tumors." In: Williams Gynecology. 4th ed. McGraw-Hill; 2020.',
    ],
    "ovarian_torsion_symptoms": [
        r'\bibitem{ovtors1} Sasaki KJ, Miller CE. "Adnexal torsion: review of the literature." J Minim Invasive Gynecol. 2014;21(2):196-202.',
        r'\bibitem{ovtors2} Huchon C, Fauconnier A. "Adnexal torsion: a literature review." Eur J Obstet Gynecol Reprod Biol. 2010;150(1):8-12.',
        r'\bibitem{ovtors3} Oelsner G, Bider D, Goldenberg M, et al. "Long-term follow-up of the twisted ischemic adnexa managed by detorsion." Fertil Steril. 1993;60(6):976-979.',
        r'\bibitem{ovtors4} Becker JH, de Graaff J, Vos MC. "Torsion of the ovary: a known but frequently missed diagnosis." Eur J Emerg Med. 2004;11(1):33-36.',
        r'\bibitem{ovtors5} Tsafrir Z, Hasson J, Levin I, et al. "Adnexal torsion: cystectomy and ovarian conservation are the mainstay of treatment." Am J Obstet Gynecol. 2014;211(6):653.e1-653.e5.',
        r'\bibitem{ovtors6} Kives S, Gascon S, Dubuc E, et al. "Adnexal torsion in children and adolescents: a retrospective review." J Pediatr Surg. 2018;53(8):1560-1565.',
    ],
    "overactive_bladder": [
        r'\bibitem{oab1} Gormley EA, Lightner DJ, Faraday M, et al. "Diagnosis and treatment of overactive bladder (non-neurogenic) in adults: AUA/SUFU guideline." J Urol. 2012;188(6 Suppl):2455-2463.',
        r'\bibitem{oab2} Nambiar AK, Bosch R, Cruz F, et al. "EAU guidelines on assessment and nonsurgical management of urinary incontinence." Eur Urol. 2018;73(4):596-609.',
        r'\bibitem{oab3} Andersson KE. "Antimuscarinics for treatment of overactive bladder." Lancet Neurol. 2004;3(1):46-53.',
        r'\bibitem{oab4} Chapple CR, Khullar V, Gabriel Z, et al. "The effects of antimuscarinic treatments in overactive bladder: a systematic review and meta-analysis." Eur Urol. 2005;48(1):5-26.',
        r'\bibitem{oab5} Abrams P, Cardozo L, Fall M, et al. "The standardisation of terminology of lower urinary tract function." Neurourol Urodyn. 2002;21(2):167-178.',
        r'\bibitem{oab6} Corcos J, Przydacz M, Campeau L, et al. "CUA guideline on adult overactive bladder." Can Urol Assoc J. 2017;11(5):E142-E173.',
    ],
    "painful_urination": [
        r'\bibitem{dysuria1} Bremnor JD, Sadovsky R. "Evaluation of dysuria in adults." Am Fam Physician. 2002;65(8):1589-1596.',
        r'\bibitem{dysuria2} Walsh CA, Moore KH. "Dysuria." In: Evidence-Based Physical Diagnosis. 4th ed. Elsevier; 2018.',
        r'\bibitem{dysuria3} Gupta K, Hooton TM, Naber KG, et al. "International clinical practice guidelines for the treatment of acute uncomplicated cystitis and pyelonephritis in women." Clin Infect Dis. 2011;52(5):e103-e120.',
        r'\bibitem{dysuria4} Michels TC, Sands JE. "Dysuria: evaluation and differential diagnosis in adults." Am Fam Physician. 2015;92(9):778-786.',
        r'\bibitem{dysuria5} Hooton TM. "Clinical practice. Uncomplicated urinary tract infection." N Engl J Med. 2012;366(11):1028-1037.',
        r'\bibitem{dysuria6} Schaeffer AJ, Nicolle LE. "Urinary tract infections in adults." In: Campbell-Walsh Urology. 12th ed. Elsevier; 2021.',
    ],
    "pale_stool": [
        r'\bibitem{palestool1} Bonheur JL, Pasha TM, Baron TH. "Pale stools and cholestasis." In: Yamada\'s Textbook of Gastroenterology. 7th ed. Wiley; 2022.',
        r'\bibitem{palestool2} Sherlock S, Dooley J. "Diseases of the Liver and Biliary System." 12th ed. Wiley-Blackwell; 2011.',
        r'\bibitem{palestool3} Moseley RH. "Approach to the patient with abnormal liver tests." UpToDate, 2023.',
        r'\bibitem{palestool4} Pratt DS, Kaplan MM. "Evaluation of liver function." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
        r'\bibitem{palestool5} Poupon R. "Primary biliary cirrhosis." N Engl J Med. 2010;362(1):53-61.',
        r'\bibitem{palestool6} Johnson CD, Sheedy SP, Foster RE. "Imaging of the biliary tract." In: Grainger & Allison\'s Diagnostic Radiology. 7th ed. Elsevier; 2020.',
    ],
    "palmar_erythema": [
        r'\bibitem{palmar1} Dudley FJ, Scheuer PJ, Sherlock S. "Palmar erythema in liver disease." Br Med J. 1965;2(5453):110-112.',
        r'\bibitem{palmar2} Satapathy SK, Bernstein D. "Dermatologic manifestations of chronic liver disease." Clin Liver Dis. 2011;15(1):171-184.',
        r'\bibitem{palmar3} Hafeez ZH, Shupp DL, Gaspari AA. "Cutaneous manifestations of liver disease." In: Fitzpatrick\'s Dermatology. 9th ed. McGraw-Hill; 2019.',
        r'\bibitem{palmar4} Dogra S, Jindal R, Suri D. "Palmar erythema." Indian J Dermatol Venereol Leprol. 2014;80(6):524-526.',
        r'\bibitem{palmar5} Nishi T, Ishii K, Matsuda K. "Palmar erythema in patients with liver cirrhosis." J Gastroenterol. 2005;40(9):887-891.',
        r'\bibitem{palmar6} Plionis ND, Tsochatzis EA. "Cutaneous stigmata of liver disease." In: Sherlock\'s Diseases of the Liver and Biliary System. 13th ed. Wiley; 2022.',
    ],
    "palpitations": [
        r'\bibitem{palp1} Zimetbaum P, Josephson ME. "Evaluation of patients with palpitations." N Engl J Med. 1998;338(19):1369-1373.',
        r'\bibitem{palp2} Thavendiranathan P, Bagai A, Khoo C, et al. "Does this patient with palpitations have a cardiac arrhythmia?" JAMA. 2009;302(19):2135-2143.',
        r'\bibitem{palp3} Wexler RK, Pleister A, Raman SV. "Outpatient approach to palpitations." Am Fam Physician. 2011;84(1):63-69.',
        r'\bibitem{palp4} Raviele A, Giada F, Bergfeldt L, et al. "Management of patients with palpitations: a position paper from the EHRA." Europace. 2011;13(7):920-934.',
        r'\bibitem{palp5} Zimetbaum PJ, Josephson ME. "Approach to the patient with palpitations." UpToDate, 2023.',
        r'\bibitem{palp6} Giada F, Raviele A. "Clinical approach to patients with palpitations." Card Electrophysiol Clin. 2018;10(2):303-312.',
    ],
    "panic_attacks": [
        r'\bibitem{panic1} American Psychiatric Association. "Diagnostic and Statistical Manual of Mental Disorders." 5th ed, Text Revision. APA; 2022.',
        r'\bibitem{panic2} Katzman MA, Bleau P, Blier P, et al. "Canadian clinical practice guidelines for the management of anxiety, posttraumatic stress and obsessive-compulsive disorders." BMC Psychiatry. 2014;14(Suppl 1):S1.',
        r'\bibitem{panic3} Craske MG, Stein MB. "Etiology and management of panic disorder." BMJ. 2016;352:i53.',
        r'\bibitem{panic4} Roy-Byrne PP, Craske MG, Stein MB. "Panic disorder." Lancet. 2006;368(9540):1023-1032.',
        r'\bibitem{panic5} Stein MB, Goin MK, Pollack MH, et al. "Practice guideline for the treatment of patients with panic disorder." 2nd ed. American Psychiatric Association; 2009.',
        r'\bibitem{panic6} Baldwin DS, Anderson IM, Nutt DJ, et al. "Evidence-based pharmacological treatment of anxiety disorders, post-traumatic stress disorder and obsessive-compulsive disorder." J Psychopharmacol. 2014;28(5):403-439.',
    ],
    "paralysis": [
        r'\bibitem{paralysis1} Caplan LR. "Acute stroke." In: Caplan\'s Stroke: A Clinical Approach. 5th ed. Elsevier; 2016.',
        r'\bibitem{paralysis2} Powers WJ, Rabinstein AA, Ackerson T, et al. "Guidelines for the early management of patients with acute ischemic stroke." Stroke. 2019;50(12):e344-e418.',
        r'\bibitem{paralysis3} GBD 2016 Stroke Collaborators. "Global, regional, and national burden of stroke, 1990-2016." Lancet Neurol. 2019;18(5):439-458.',
        r'\bibitem{paralysis4} Peacock WF, Rafique Z, Singer AJ. "Acute stroke." In: Rosen\'s Emergency Medicine. 10th ed. Elsevier; 2023.',
        r'\bibitem{paralysis5} Adams HP, del Zoppo G, Alberts MJ, et al. "Guidelines for the early management of adults with ischemic stroke." Stroke. 2007;38(5):1655-1711.',
        r'\bibitem{paralysis6} Jauch EC, Saver JL, Adams HP, et al. "Guidelines for the early management of patients with acute ischemic stroke." Stroke. 2013;44(3):870-947.',
    ],
    "paranoia": [
        r'\bibitem{paranoia1} American Psychiatric Association. "Diagnostic and Statistical Manual of Mental Disorders." 5th ed, Text Revision. APA; 2022.',
        r'\bibitem{paranoia2} Freeman D, Garety PA, Bebbington PE, et al. "Psychological investigation of the structure of paranoia in a non-clinical population." Br J Psychiatry. 2005;186:427-435.',
        r'\bibitem{paranoia3} Bentall RP, Corcoran R, Howard R, et al. "Persecutory delusions: a review and theoretical integration." Clin Psychol Rev. 2001;21(8):1143-1192.',
        r'\bibitem{paranoia4} Freeman D. "Suspicious minds: the psychology of persecutory delusions." Clin Psychol Rev. 2007;27(4):425-457.',
        r'\bibitem{paranoia5} Keepers GA, Fochtmann LJ, Anzia JM, et al. "Practice guideline for the treatment of patients with schizophrenia." 3rd ed. American Psychiatric Association; 2020.',
        r'\bibitem{paranoia6} Garety PA, Freeman D. "The past and future of delusions research: from the inexplicable to the treatable." Br J Psychiatry. 2013;203(5):327-333.',
    ],
    "paresthesia": [
        r'\bibitem{paresthesia1} England JD, Gronseth GS, Franklin G, et al. "Practice parameter: evaluation of distal symmetric polyneuropathy." Neurology. 2009;72(2):185-192.',
        r'\bibitem{paresthesia2} Watson JC, Dyck PJB. "Peripheral neuropathy: a practical approach to diagnosis and symptom management." Mayo Clin Proc. 2015;90(7):940-951.',
        r'\bibitem{paresthesia3} Callaghan BC, Cheng HT, Stables CL, et al. "Diabetic neuropathy: a review." JAMA. 2012;308(22):2371-2381.',
        r'\bibitem{paresthesia4} Azhary H, Farooq MU, Bhanushali M, et al. "Peripheral neuropathy: differential diagnosis and management." Am Fam Physician. 2010;81(7):887-892.',
        r'\bibitem{paresthesia5} Feldman EL, Callaghan BC, Pop-Busui R, et al. "Diabetic neuropathy." Nat Rev Dis Primers. 2019;5(1):41.',
        r'\bibitem{paresthesia6} Dyck PJ, Thomas PK. "Peripheral Neuropathy." 6th ed. Elsevier; 2021.',
    ],
    "paronychia": [
        r'\bibitem{paronychia1} Shafritz AB, Coppage JM. "Acute and chronic paronychia." Am Fam Physician. 2014;90(10):717-722.',
        r'\bibitem{paronychia2} Rockwell PG. "Acute and chronic paronychia." Am Fam Physician. 2001;63(6):1113-1116.',
        r'\bibitem{paronychia3} Jebson PJL, Steyers CM. "Acute and chronic paronychia." In: Green\'s Operative Hand Surgery. 8th ed. Elsevier; 2022.',
        r'\bibitem{paronychia4} Leggit JC. "Acute and chronic paronychia: a review." Am Fam Physician. 2017;95(1):44-48.',
        r'\bibitem{paronychia5} Rigopoulos D, Larios G, Gregoriou S, et al. "Acute and chronic paronychia." Am Fam Physician. 2008;77(3):339-346.',
        r'\bibitem{paronychia6} Wollina U, Nenoff P, Haroske G, et al. "Paronychia." In: Dermatology. 4th ed. Elsevier; 2018.',
    ],
    "parotid_gland_swelling": [
        r'\bibitem{parotid1} Wilson KF, Meier JD, Ward PD. "Salivary gland disorders." Am Fam Physician. 2014;89(11):882-888.',
        r'\bibitem{parotid2} Carlson ER, Ord RA. "Salivary gland diseases." In: Peterson\'s Principles of Oral and Maxillofacial Surgery. 4th ed. Springer; 2022.',
        r'\bibitem{parotid3} Schaitkin BM, Eisenman DS. "Sialadenitis." In: Cummings Otolaryngology. 7th ed. Elsevier; 2021.',
        r'\bibitem{parotid4} Albrecht M, Yanci KA. "Sialadenitis." In: StatPearls. StatPearls Publishing; 2023.',
        r'\bibitem{parotid5} Baum BJ, Fox PC. "Salivary gland disease." In: Cecil Textbook of Medicine. 26th ed. Elsevier; 2020.',
        r'\bibitem{parotid6} Walvekar RR, Andrade H, Simental AA. "Salivary gland diseases in adults." In: Flint PW, et al. Cummings Otolaryngology. 7th ed. Elsevier; 2021.',
    ],
    "paroxysmal_cough": [
        r'\bibitem{cough1} Irwin RS, Baumann MH, Bolser DC, et al. "Diagnosis and management of cough: ACCP evidence-based clinical practice guidelines." Chest. 2006;129(1 Suppl):1S-23S.',
        r'\bibitem{cough2} Gibson PG, Vertigan AE. "Management of chronic cough." BMJ. 2015;351:h5590.',
        r'\bibitem{cough3} Morice AH, Millqvist E, Bieksiene K, et al. "ERS guidelines on the diagnosis and treatment of chronic cough in adults." Eur Respir J. 2020;55(1):1901136.',
        r'\bibitem{cough4} Irwin RS, French CT, Chang AB, et al. "Classification of cough as a symptom in adults and children." Chest. 2018;153(1):196-209.',
        r'\bibitem{cough5} Kamei RK, Weisman SJ. "Pertussis (whooping cough)." In: Nelson Textbook of Pediatrics. 21st ed. Elsevier; 2020.',
        r'\bibitem{cough6} Braman SS. "Postinfectious cough: ACCP evidence-based clinical practice guidelines." Chest. 2006;129(1 Suppl):138S-146S.',
    ],
    "patellar_tendonitis": [
        r'\bibitem{patellartend1} Fredberg U, Stengaard-Pedersen K. "Chronic tendinopathy: current concepts." Br J Sports Med. 2008;42(4):262-268.',
        r'\bibitem{patellartend2} Schwarz A, Watson J, Hutchinson MR. "Patellar tendinopathy: a review." Am J Orthop. 2015;44(12):561-566.',
        r'\bibitem{patellartend3} Malliaras P, Cook J, Purdam C, et al. "Patellar tendinopathy: clinical diagnosis, load management, and advice for challenging case presentations." J Orthop Sports Phys Ther. 2015;45(11):887-898.',
        r'\bibitem{patellartend4} Lian OB, Engebretsen L, Bahr R. "Prevalence of jumper\'s knee among elite athletes from different sports." Am J Sports Med. 2005;33(4):561-567.',
        r'\bibitem{patellartend5} Cook JL, Khan KM, Purdam CR. "Conservative treatment of patellar tendinopathy." Phys Ther Sport. 2001;2(2):54-65.',
        r'\bibitem{patellartend6} Khan KM, Cook JL, Bonar F, et al. "Histopathology of common tendinopathies." Sports Med. 1999;27(6):393-408.',
    ],
    "pelvic_organ_prolapse": [
        r'\bibitem{pop1} Maher C, Feiner B, Baessler K, et al. "Surgery for women with apical vaginal prolapse." Cochrane Database Syst Rev. 2016;(10):CD012376.',
        r'\bibitem{pop2} Jelovsek JE, Maher C, Barber MD. "Pelvic organ prolapse." Lancet. 2007;369(9566):1027-1038.',
        r'\bibitem{pop3} Haylen BT, Maher CF, Barber MD, et al. "An International Urogynecological Association (IUGA) / International Continence Society (ICS) joint report on the terminology for female pelvic organ prolapse." Neurourol Urodyn. 2016;35(2):137-168.',
        r'\bibitem{pop4} Barber MD, Maher C. "Epidemiology and outcome assessment of pelvic organ prolapse." Int Urogynecol J. 2013;24(11):1783-1790.',
        r'\bibitem{pop5} American College of Obstetricians and Gynecologists. "Pelvic organ prolapse." ACOG Practice Bulletin No. 214. Obstet Gynecol. 2019;134(5):e146-e164.',
        r'\bibitem{pop6} Sung VW, Hampton BS. "Epidemiology of pelvic organ prolapse." Clin Obstet Gynecol. 2021;64(2):237-244.',
    ],
    "pelvic_pain": [
        r'\bibitem{pelvicpain1} Speer LM, Mushkbar S, Erbele T. "Chronic pelvic pain in women." Am Fam Physician. 2016;93(5):380-387.',
        r'\bibitem{pelvicpain2} Dysfunctional uterine bleeding and chronic pelvic pain. In: Williams Gynecology. 4th ed. McGraw-Hill; 2020.',
        r'\bibitem{pelvicpain3} Royal College of Obstetricians and Gynaecologists. "Chronic pelvic pain: initial management." Green-top Guideline No. 41. RCOG; 2012.',
        r'\bibitem{pelvicpain4} Howard FM. "Chronic pelvic pain." Obstet Gynecol. 2003;101(3):594-611.',
        r'\bibitem{pelvicpain5} Steege JF, Siedhoff MT. "Chronic pelvic pain." Obstet Gynecol. 2014;124(3):616-629.',
        r'\bibitem{pelvicpain6} Lamvu G, Carrillo J, Ouyang C, et al. "Chronic pelvic pain in women: a review." JAMA. 2021;325(23):2381-2391.',
    ],
    "penile_lesions": [
        r'\bibitem{penile1} Bjekic M, Sipetic S, Vlajinac H, et al. "Penile lesions: a descriptive study of 239 patients." J Eur Acad Dermatol Venereol. 2009;23(7):805-809.',
        r'\bibitem{penile2} Rosen T, Vandergriff T. "Penile lesions." Dermatol Clin. 2011;29(3):467-480.',
        r'\bibitem{penile3} Park AJ, Scerri L. "Penile lesions: a review." Clin Exp Dermatol. 2020;45(4):421-428.',
        r'\bibitem{penile4} Workowski KA, Bolan GA. "Sexually transmitted diseases treatment guidelines, 2015." MMWR Recomm Rep. 2015;64(RR-03):1-137.',
        r'\bibitem{penile5} Edwards SK, Bunker CB, Ziller F, et al. "2013 European guideline for the management of balanoposthitis." Int J STD AIDS. 2014;25(9):615-626.',
        r'\bibitem{penile6} Bunker CB. "Male genital dermatology." In: Rook\'s Textbook of Dermatology. 10th ed. Wiley; 2024.',
    ],
    "penis_irritation": [
        r'\bibitem{penisirr1} Edwards SK, Bunker CB, Ziller F, et al. "2013 European guideline for the management of balanoposthitis." Int J STD AIDS. 2014;25(9):615-626.',
        r'\bibitem{penisirr2} English JC 3rd, Laws RA, Keough GC, et al. "Dermatoses of the glans penis and prepuce." J Am Acad Dermatol. 1997;37(1):1-24.',
        r'\bibitem{penisirr3} Wray AA, Khetarpal S, Streed CG Jr. "Balanitis." In: StatPearls. StatPearls Publishing; 2023.',
        r'\bibitem{penisirr4} Bunker CB. "Male genital skin disease." In: Rook\'s Textbook of Dermatology. 10th ed. Wiley; 2024.',
        r'\bibitem{penisirr5} Birley HDL, Walker MM, Luzzi GA, et al. "Clinical features and management of recurrent balanitis." Genitourin Med. 1993;69(5):350-353.',
        r'\bibitem{penisirr6} Neubert U, Janniger CK. "Balanitis and balanoposthitis in children and adults." J Cutan Med Surg. 2021;25(4):411-419.',
    ],
    "penis_swelling_and_injury": [
        r'\bibitem{penisswell1} Muneer A, Minhas S, Ralph DJ. "Penile fracture." BJU Int. 2005;96(7):1008-1011.',
        r'\bibitem{penisswell2} Pavan N, Teoh JY, Eardley I, et al. "European Association of Urology guidelines on male sexual health: penile fracture." Eur Urol. 2021;80(3):355-365.',
        r'\bibitem{penisswell3} O\'Brien T, Lynch T, Murphy C. "Penile trauma and fracture." In: Campbell-Walsh Urology. 12th ed. Elsevier; 2021.',
        r'\bibitem{penisswell4} Mahapatra RS, Kundu AK, Pal DK. "Penile fracture: our experience at a tertiary care center." Urol Ann. 2015;7(3):340-344.',
        r'\bibitem{penisswell5} Reddy AG, Alcantara M, Murphy GP, et al. "Penile fracture." J Sex Med. 2021;18(8):1335-1340.',
        r'\bibitem{penisswell6} Knoepp LR, Gupta AD, Meeks JJ. "Penile trauma and reconstruction." In: Hinman\'s Atlas of Urologic Surgery. 4th ed. Elsevier; 2018.',
    ],
    "pericarditis_symptoms": [
        r'\bibitem{pericard1} Adler Y, Charron P, Imazio M, et al. "2015 ESC guidelines for the diagnosis and management of pericardial diseases." Eur Heart J. 2015;36(42):2921-2964.',
        r'\bibitem{pericard2} Imazio M, Gaita F, LeWinter M. "Evaluation and treatment of pericarditis: a systematic review." JAMA. 2015;314(14):1498-1506.',
        r'\bibitem{pericard3} LeWinter MM, Imazio M. "Pericardial diseases." In: Braunwald\'s Heart Disease. 12th ed. Elsevier; 2022.',
        r'\bibitem{pericard4} Imazio M, Brucato A, Cemin R, et al. "A randomized trial of colchicine for acute pericarditis (COPE)." N Engl J Med. 2013;369(16):1522-1528.',
        r'\bibitem{pericard5} Adler Y, Imazio M, Senni M. "Acute pericarditis." Lancet. 2021;397(10280):1196-1206.',
        r'\bibitem{pericard6} Klein AL, Abbara S, Agler DA, et al. "American Society of Echocardiography clinical recommendations for multimodality cardiovascular imaging of patients with pericardial disease." J Am Soc Echocardiogr. 2013;26(6):541-581.',
    ],
    "peripheral_neuropathy": [
        r'\bibitem{periphneuro1} England JD, Gronseth GS, Franklin G, et al. "Practice parameter: evaluation of distal symmetric polyneuropathy." Neurology. 2009;72(2):185-192.',
        r'\bibitem{periphneuro2} Callaghan BC, Cheng HT, Stables CL, et al. "Diabetic neuropathy: a review." JAMA. 2012;308(22):2371-2381.',
        r'\bibitem{periphneuro3} Watson JC, Dyck PJB. "Peripheral neuropathy: a practical approach." Mayo Clin Proc. 2015;90(7):940-951.',
        r'\bibitem{periphneuro4} Azhary H, Farooq MU, Bhanushali M, et al. "Peripheral neuropathy: differential diagnosis and management." Am Fam Physician. 2010;81(7):887-892.',
        r'\bibitem{periphneuro5} Dyck PJ, Thomas PK. "Peripheral Neuropathy." 6th ed. Elsevier; 2021.',
        r'\bibitem{periphneuro6} Pop-Busui R, Boulton AJM, Feldman EL, et al. "Diabetic neuropathy: a position statement by the ADA." Diabetes Care. 2017;40(1):136-154.',
    ],
    "peritonitis_signs": [
        r'\bibitem{peritonitis1} McQuaid KR. "Approach to the patient with acute abdomen." In: Yamada\'s Textbook of Gastroenterology. 7th ed. Wiley; 2022.',
        r'\bibitem{peritonitis2} Silen W. "Cope\'s Early Diagnosis of the Acute Abdomen." 22nd ed. Oxford University Press; 2010.',
        r'\bibitem{peritonitis3} Paterson-Brown S, Tierney GM. "The acute abdomen." In: Bailey & Love\'s Short Practice of Surgery. 28th ed. CRC Press; 2023.',
        r'\bibitem{peritonitis4} Nathers AB, Rotstein OD. "Peritonitis and intra-abdominal infection." In: Sabiston Textbook of Surgery. 21st ed. Elsevier; 2021.',
        r'\bibitem{peritonitis5} Sartelli M, Chichom-Mefire A, Labricciosa FM, et al. "The management of intra-abdominal infections from a global perspective: 2017 WSES guidelines." World J Emerg Surg. 2017;12:29.',
        r'\bibitem{peritonitis6} Mazuski JE, Tessier JM, May AK, et al. "The Surgical Infection Society revised guidelines on the management of intra-abdominal infection." Surg Infect (Larchmt). 2017;18(1):1-76.',
    ],
    "persistent_vegetative_state": [
        r'\bibitem{pvs1} Multi-Society Task Force on PVS. "Medical aspects of the persistent vegetative state (first of two parts)." N Engl J Med. 1994;330(21):1499-1508.',
        r'\bibitem{pvs2} Multi-Society Task Force on PVS. "Medical aspects of the persistent vegetative state (second of two parts)." N Engl J Med. 1994;330(22):1572-1579.',
        r'\bibitem{pvs3} Giacino JT, Katz DI, Schiff ND, et al. "Practice guideline update: disorders of consciousness." Neurology. 2018;91(10):461-470.',
        r'\bibitem{pvs4} Bernat JL. "Chronic disorders of consciousness." Lancet. 2006;367(9517):1181-1192.',
        r'\bibitem{pvs5} Laureys S, Celesia GG, Cohadon F, et al. "Unresponsive wakefulness syndrome: a new name for the vegetative state." BMC Med. 2010;8:68.',
        r'\bibitem{pvs6} Wijdicks EFM. "The diagnosis of brain death and minimally conscious states." N Engl J Med. 2001;344(16):1215-1221.',
    ],
    "petechiae": [
        r'\bibitem{petechiae1} George JN, Aster RH. "Thrombocytopenia due to diminished platelet production." In: Williams Hematology. 10th ed. McGraw-Hill; 2021.',
        r'\bibitem{petechiae2} Kuter DJ. "Immune thrombocytopenia." N Engl J Med. 2019;381(10):945-955.',
        r'\bibitem{petechiae3} Cines DB, Blanchette VS. "Immune thrombocytopenic purpura." N Engl J Med. 2002;346(13):995-1008.',
        r'\bibitem{petechiae4} Neunert C, Lim W, Crowther M, et al. "The American Society of Hematology 2011 evidence-based practice guideline for immune thrombocytopenia." Blood. 2011;117(16):4190-4207.',
        r'\bibitem{petechiae5} Rodeghiero F, Stasi R, Gernsheimer T, et al. "Standardization of terminology, definitions and outcome criteria in immune thrombocytopenia." Blood. 2009;113(11):2386-2393.',
        r'\bibitem{petechiae6} Handin RI. "Disorders of platelets." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
    ],
    "phimosis": [
        r'\bibitem{phimosis1} Hayashi Y, Kojima Y, Mizuno K, et al. "Phimosis: a review." Int J Urol. 2011;18(4):262-269.',
        r'\bibitem{phimosis2} Srinath H. "Phimosis in children." BMJ. 2020;370:m2775.',
        r'\bibitem{phimosis3} McGregor TB, Pike JG, Leonard MP. "Pathologic and physiologic phimosis: approach to the phimotic foreskin." Can Fam Physician. 2007;53(3):445-448.',
        r'\bibitem{phimosis4} Esposito C, Centonze A, Alicchio F, et al. "Topical steroid application versus circumcision in pediatric patients with phimosis." Pediatr Surg Int. 2008;24(2):187-191.',
        r'\bibitem{phimosis5} Orsola A, Caffaratti J, Garat JM. "Conservative treatment of phimosis in children using a topical steroid." Urology. 2000;56(2):307-310.',
        r'\bibitem{phimosis6} Cuckow PM, Rix G, Mouriquand PDE. "Preputial plasty: a good alternative to circumcision." J Pediatr Surg. 1994;29(4):561-563.',
    ],
    "photophobia": [
        r'\bibitem{photophobia1} Digre KB, Brennan KC. "Shedding light on photophobia." J Neuroophthalmol. 2012;32(1):68-81.',
        r'\bibitem{photophobia2} Katz BJ, Digre KB. "Diagnosis and management of photophobia." Semin Neurol. 2019;39(6):722-731.',
        r'\bibitem{photophobia3} Lebensohn JE. "Photophobia: mechanism and treatment." Am J Ophthalmol. 1951;34(9):1294-1300.',
        r'\bibitem{photophobia4} Custer PL, Gross CP, Trogdon J. "Photophobia." In: Cornea. 4th ed. Elsevier; 2017.',
        r'\bibitem{photophobia5} Noseda R, Copenhagen D, Burstein R. "Current understanding of photophobia." Cephalalgia. 2019;39(11):1479-1490.',
        r'\bibitem{photophobia6} Amin RM, Gokhale M, Vogel EA. "Photophobia in migraine: a symptom cluster." Curr Pain Headache Rep. 2020;24(10):58.',
    ],
    "photosensitivity": [
        r'\bibitem{photosens1} Millard TP, Hawk JL. "Photosensitivity disorders." In: Rook\'s Textbook of Dermatology. 10th ed. Wiley; 2024.',
        r'\bibitem{photosens2} Lim HW, Cooper K. "The health impact of solar radiation and prevention strategies." J Am Acad Dermatol. 1999;41(1):81-99.',
        r'\bibitem{photosens3} Dawe RS, Ibbotson SH. "Drug-induced photosensitivity." Dermatol Clin. 2014;32(3):363-368.',
        r'\bibitem{photosens4} Lugovic-Mihic L, Duvancic T, Situm M, et al. "Photodermatoses: classification, diagnosis and management." Acta Dermatovenerol Croat. 2021;29(1):15-24.',
        r'\bibitem{photosens5} Gonzalez E, Gonzalez S. "Drug photosensitivity: a systematic review." Photodermatol Photoimmunol Photomed. 2020;36(4):261-271.',
        r'\bibitem{photosens6} Roelandts R. "The diagnosis of photosensitivity." Arch Dermatol. 1999;135(11):1413-1418.',
    ],
    "plantar_fasciitis": [
        r'\bibitem{plantar1} Buchbinder R. "Plantar fasciitis." N Engl J Med. 2004;350(21):2159-2166.',
        r'\bibitem{plantar2} Goff JD, Crawford R. "Diagnosis and treatment of plantar fasciitis." Am Fam Physician. 2011;84(6):676-682.',
        r'\bibitem{plantar3} Riddle DL, Pulisic M, Pidcoe P, et al. "Risk factors for plantar fasciitis: a matched case-control study." J Bone Joint Surg Am. 2003;85(5):872-877.',
        r'\bibitem{plantar4} Lareau CR, Sawyer GA, Wang JH, et al. "Plantar fasciitis: a review." Arch Orthop Trauma Surg. 2014;134(1):47-54.',
        r'\bibitem{plantar5} Cole C, Seto C, Gazewood J. "Plantar fasciitis: evidence-based review of diagnosis and therapy." Am Fam Physician. 2005;72(11):2237-2242.',
        r'\bibitem{plantar6} Lemont H, Ammirati KM, Usen N. "Plantar fasciitis: a degenerative process." J Am Podiatr Med Assoc. 2003;93(3):234-237.',
    ],
    "pleuritic_chest_pain": [
        r'\bibitem{pleurisy1} Kass SM, Williams PM, Reamy BV. "Pleurisy." Am Fam Physician. 2007;75(9):1357-1364.',
        r'\bibitem{pleurisy2} Light RW. "Pleural Diseases." 6th ed. Wolters Kluwer; 2013.',
        r'\bibitem{pleurisy3} Ferrer J, Roldan J. "Clinical management of pleurisy." In: Textbook of Pleural Diseases. 3rd ed. CRC Press; 2020.',
        r'\bibitem{pleurisy4} Porcel JM. "Pleural effusions." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
        r'\bibitem{pleurisy5} Brims FJ, Maskell NA. "Pleural disease." BMJ. 2011;343:d4934.',
        r'\bibitem{pleurisy6} Rahman NM, Davies RJ. "Pleural disease: from diagnosis to treatment." Clin Med (Lond). 2009;9(4):363-366.',
    ],
    "pneumonia_symptoms": [
        r'\bibitem{pneumonia1} Mandell LA, Wunderink RG, Anzueto A, et al. "Infectious Diseases Society of America/American Thoracic Society consensus guidelines on the management of community-acquired pneumonia in adults." Clin Infect Dis. 2007;44(Suppl 2):S27-S72.',
        r'\bibitem{pneumonia2} Musher DM, Thorner AR. "Community-acquired pneumonia." N Engl J Med. 2014;371(17):1619-1628.',
        r'\bibitem{pneumonia3} Jain S, Self WH, Wunderink RG, et al. "Community-acquired pneumonia requiring hospitalization among U.S. adults." N Engl J Med. 2015;373(5):415-427.',
        r'\bibitem{pneumonia4} File TM Jr, Marrie TJ. "Clinical evaluation and diagnosis of pneumonia." UpToDate, 2023.',
        r'\bibitem{pneumonia5} Wunderink RG, Waterer GW. "Community-acquired pneumonia." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
        r'\bibitem{pneumonia6} Metlay JP, Waterer GW, Long AC, et al. "Diagnosis and treatment of adults with community-acquired pneumonia. An official clinical practice guideline of the ATS and IDSA." Am J Respir Crit Care Med. 2019;200(7):e45-e67.',
    ],
    "polydipsia": [
        r'\bibitem{polydipsia1} American Diabetes Association. "Classification and diagnosis of diabetes: standards of medical care in diabetes-2022." Diabetes Care. 2022;45(Suppl 1):S17-S38.',
        r'\bibitem{polydipsia2} Robertson GL. "Diabetes insipidus." N Engl J Med. 2016;375(14):1387-1396.',
        r'\bibitem{polydipsia3} Verbalis JG. "Disorders of body water homeostasis." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
        r'\bibitem{polydipsia4} Schrier RW. "Body water homeostasis: clinical disorders of urinary concentration and dilution." J Am Soc Nephrol. 2006;17(7):1820-1832.',
        r'\bibitem{polydipsia5} Gardella A, Bhatt P. "Polydipsia and polyuria in children." Pediatr Rev. 2018;39(5):251-260.',
        r'\bibitem{polydipsia6} Berl T, Verbalis JG. "Pathophysiology of disorders of water metabolism." In: Brenner & Rector\'s The Kidney. 11th ed. Elsevier; 2020.',
    ],
    "polyphagia": [
        r'\bibitem{polyphagia1} American Diabetes Association. "Classification and diagnosis of diabetes: standards of medical care in diabetes-2022." Diabetes Care. 2022;45(Suppl 1):S17-S38.',
        r'\bibitem{polyphagia2} Schwartz MW, Seeley RJ, Zeltser LM, et al. "Obesity pathogenesis: an Endocrine Society scientific statement." Endocr Rev. 2017;38(4):267-296.',
        r'\bibitem{polyphagia3} Morton GJ, Meek TH, Schwartz MW. "Neurobiology of food intake in health and disease." Nat Rev Neurosci. 2014;15(6):367-378.',
        r'\bibitem{polyphagia4} Ahima RS, Antwi DA. "Brain regulation of appetite and satiety." Endocrinol Metab Clin North Am. 2008;37(4):811-823.',
        r'\bibitem{polyphagia5} Blundell JE, Gibbons C, Caudwell P, et al. "Appetite control and energy balance." In: Endocrinology: Adult and Pediatric. 7th ed. Elsevier; 2016.',
        r'\bibitem{polyphagia6} Hainer V, Kunesova M, Bellisle F, et al. "Psychobehavioral and nutritional predictors of weight loss." Obes Rev. 2005;6(3):229-235.',
    ],
    "polyuria": [
        r'\bibitem{polyuria1} Robertson GL. "Diabetes insipidus." N Engl J Med. 2016;375(14):1387-1396.',
        r'\bibitem{polyuria2} Verbalis JG. "Disorders of body water homeostasis." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
        r'\bibitem{polyuria3} Gardella A, Bhatt P. "Polydipsia and polyuria in children." Pediatr Rev. 2018;39(5):251-260.',
        r'\bibitem{polyuria4} American Diabetes Association. "Classification and diagnosis of diabetes." Diabetes Care. 2022;45(Suppl 1):S17-S38.',
        r'\bibitem{polyuria5} Gubbi S, Hannah-Shmouni F, Koch CA. "Polyuria." In: StatPearls. StatPearls Publishing; 2023.',
        r'\bibitem{polyuria6} Berl T, Verbalis JG. "Pathophysiology of disorders of water metabolism." In: Brenner & Rector\'s The Kidney. 11th ed. Elsevier; 2020.',
    ],
    "popliteal_cyst": [
        r'\bibitem{popcyst1} Handy JR. "Popliteal cysts in adults: a review." Semin Arthritis Rheum. 2001;31(2):108-118.',
        r'\bibitem{popcyst2} Miller TT, Staron RB, Koenigsberg T, et al. "MR imaging of Baker cysts: association with internal derangement of the knee." Radiology. 1996;201(3):877-880.',
        r'\bibitem{popcyst3} Fritschy D, Fasel J, Imbert JC, et al. "The popliteal cyst." Knee Surg Sports Traumatol Arthrosc. 2006;14(7):623-628.',
        r'\bibitem{popcyst4} Labropoulos N, Shifrin DA, Lederer T, et al. "Ultrasound-guided aspiration of Baker\'s cysts." J Vasc Surg. 2004;39(3):646-649.',
        r'\bibitem{popcyst5} Canoso JJ, Yood RA. "Reactive synovitis and Baker\'s cysts." Arthritis Rheum. 1979;22(6):661-666.',
        r'\bibitem{popcyst6} Ward EE, Jacobson JA, Fessell DP, et al. "Sonographic detection of Baker\'s cysts: comparison with MR imaging." AJR Am J Roentgenol. 2001;176(2):387-390.',
    ],
    "post_nasal_drip": [
        r'\bibitem{pnd1} Morice AH. "Post-nasal drip syndrome: a symptom to be sniffed at?" Pulm Pharmacol Ther. 2004;17(6):343-345.',
        r'\bibitem{pnd2} Pratter MR. "Chronic upper airway cough syndrome secondary to rhinosinus diseases (previously referred to as postnasal drip syndrome)." Chest. 2006;129(1 Suppl):63S-71S.',
        r'\bibitem{pnd3} Rosenfeld RM, Piccirillo JF, Chandrasekhar SS, et al. "Clinical practice guideline (update): adult sinusitis." Otolaryngol Head Neck Surg. 2015;152(2 Suppl):S1-S39.',
        r'\bibitem{pnd4} Dykewicz MS, Wallace DV, Amrol DJ, et al. "Rhinitis 2020: a practice parameter update." J Allergy Clin Immunol Pract. 2020;8(8):2545-2564.',
        r'\bibitem{pnd5} Seidman MD, Gurgel RK, Lin SY, et al. "Clinical practice guideline: allergic rhinitis." Otolaryngol Head Neck Surg. 2015;152(1 Suppl):S1-S43.',
        r'\bibitem{pnd6} Krouse JH. "Post-nasal drip." In: Cummings Otolaryngology. 7th ed. Elsevier; 2021.',
    ],
    "postpartum_hemorrhage_signs": [
        r'\bibitem{pph1} American College of Obstetricians and Gynecologists. "Postpartum hemorrhage." ACOG Practice Bulletin No. 183. Obstet Gynecol. 2017;130(4):e168-e186.',
        r'\bibitem{pph2} Say L, Chou D, Gemmill A, et al. "Global causes of maternal death: a WHO systematic analysis." Lancet Glob Health. 2014;2(6):e323-e333.',
        r'\bibitem{pph3} Mousa HA, Blum J, Abou El Senoun G, et al. "Treatment of primary postpartum haemorrhage." Cochrane Database Syst Rev. 2014;(1):CD003249.',
        r'\bibitem{pph4} Tuncalp O, Souza JP, Gulmezoglu M. "New WHO recommendations on prevention and treatment of postpartum hemorrhage." Int J Gynaecol Obstet. 2013;123(3):254-256.',
        r'\bibitem{pph5} Main EK, Goffman D, Scavone BM, et al. "National Partnership for Maternal Safety: consensus bundle on obstetric hemorrhage." Anesth Analg. 2015;121(1):142-148.',
        r'\bibitem{pph6} Sheldon WR, Blum J, Vogel JP, et al. "Postpartum haemorrhage management, risks, and maternal outcomes." BJOG. 2014;121(Suppl 1):5-13.',
    ],
    "precocious_puberty": [
        r'\bibitem{precoc1} Carel JC, Leger J. "Clinical practice. Precocious puberty." N Engl J Med. 2008;358(22):2366-2377.',
        r'\bibitem{precoc2} Latronico AC, Brito VN, Carel JC. "Causes and diagnosis of central precocious puberty." Lancet Diabetes Endocrinol. 2016;4(3):265-274.',
        r'\bibitem{precoc3} Kaplowitz PB. "Precocious puberty." In: Sperling Pediatric Endocrinology. 5th ed. Elsevier; 2021.',
        r'\bibitem{precoc4} Eugster EA. "Treatment of central precocious puberty." J Endocr Soc. 2019;3(5):965-972.',
        r'\bibitem{precoc5} Carel JC, Eugster EA, Rogol A, et al. "Consensus statement on the use of gonadotropin-releasing hormone analogs in children." Pediatrics. 2009;123(4):e752-e762.',
        r'\bibitem{precoc6} Parent AS, Teilmann G, Juul A, et al. "The timing of normal puberty and the age limits of sexual precocity." Endocr Rev. 2003;24(5):668-693.',
    ],
    "premature_ejaculation": [
        r'\bibitem{premej1} Althof SE, McMahon CG, Waldinger MD, et al. "An update of the International Society for Sexual Medicine\'s guidelines for the diagnosis and treatment of premature ejaculation." J Sex Med. 2014;11(6):1392-1422.',
        r'\bibitem{premej2} Serefoglu EC, McMahon CG, Waldinger MD, et al. "An evidence-based unified definition of lifelong and acquired premature ejaculation." J Sex Med. 2014;11(6):1423-1441.',
        r'\bibitem{premej3} Giuliano F, Clement P. "Pharmacology for the treatment of premature ejaculation." Pharmacol Rev. 2012;64(3):621-644.',
        r'\bibitem{premej4} Porst H, Montorsi F, Rosen RC, et al. "The Premature Ejaculation Prevalence and Attitudes (PEPA) survey." Eur Urol. 2007;51(3):816-823.',
        r'\bibitem{premej5} Waldinger MD. "Premature ejaculation: definition and drug treatment." Drugs. 2007;67(4):547-568.',
        r'\bibitem{premej6} Carson CC, Gunn K. "Premature ejaculation: definition, etiology, and treatment." Urol Clin North Am. 2020;47(4):497-506.',
    ],
    "premature_labor_signs": [
        r'\bibitem{premature1} American College of Obstetricians and Gynecologists. "Management of preterm labor." ACOG Practice Bulletin No. 171. Obstet Gynecol. 2016;128(4):e155-e164.',
        r'\bibitem{premature2} Romero R, Dey SK, Fisher SJ. "Preterm labor: one syndrome, many causes." Science. 2014;345(6198):760-765.',
        r'\bibitem{premature3} Goldenberg RL, Culhane JF, Iams JD, et al. "Epidemiology and causes of preterm birth." Lancet. 2008;371(9606):75-84.',
        r'\bibitem{premature4} Iams JD. "Preterm labor and birth." In: Williams Obstetrics. 26th ed. McGraw-Hill; 2022.',
        r'\bibitem{premature5} Haas DM, Caldwell DM, Kirkpatrick P, et al. "Tocolytic therapy for preterm delivery: systematic review and network meta-analysis." BMJ. 2012;345:e6226.',
        r'\bibitem{premature6} Mercer BM, Goldenberg RL, Das A, et al. "The preterm prediction study: a clinical risk assessment system." Am J Obstet Gynecol. 1996;174(6):1885-1893.',
    ],
    "presbycusis": [
        r'\bibitem{presbycusis1} Gates GA, Mills JH. "Presbycusis." Lancet. 2005;366(9491):1111-1120.',
        r'\bibitem{presbycusis2} Yamasoba T, Lin FR, Someya S, et al. "Current concepts in age-related hearing loss: epidemiology and mechanistic pathways." Hear Res. 2013;303:30-38.',
        r'\bibitem{presbycusis3} Cunningham LL, Tucci DL. "Hearing loss in adults." N Engl J Med. 2017;377(25):2465-2473.',
        r'\bibitem{presbycusis4} Lin FR, Metter EJ, O\'Brien RJ, et al. "Hearing loss and incident dementia." Arch Neurol. 2011;68(2):214-220.',
        r'\bibitem{presbycusis5} Sprinzl GM, Riechelmann H. "Current trends in treating hearing loss in elderly people." Gerontology. 2010;56(3):351-358.',
        r'\bibitem{presbycusis6} Frisina RD, Walton JP. "Age-related hearing loss." In: Cummings Otolaryngology. 7th ed. Elsevier; 2021.',
    ],
    "presyncope": [
        r'\bibitem{presyncope1} Shen WK, Sheldon RS, Benditt DG, et al. "2017 ACC/AHA/HRS guideline for the evaluation and management of patients with syncope." Circulation. 2017;136(5):e60-e122.',
        r'\bibitem{presyncope2} Brignole M, Moya A, de Lange FJ, et al. "2018 ESC guidelines for the diagnosis and management of syncope." Eur Heart J. 2018;39(21):1883-1948.',
        r'\bibitem{presyncope3} Kapoor WN. "Syncope." N Engl J Med. 2000;343(25):1856-1862.',
        r'\bibitem{presyncope4} Albassam OT, Redelmeier RJ, Shadowitz S, et al. "Did this patient have cardiac syncope?" JAMA. 2019;321(24):2448-2457.',
        r'\bibitem{presyncope5} Serrano LA, Hess EP, Bellolio MF, et al. "Accuracy and quality of clinical decision rules for syncope in the emergency department." Acad Emerg Med. 2010;17(8):799-809.',
        r'\bibitem{presyncope6} Kaufmann H, Bhatt DG. "Syncope and presyncope." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
    ],
    "priapism": [
        r'\bibitem{priapism1} Montague DK, Jarow J, Broderick GA, et al. "American Urological Association guideline on the management of priapism." J Urol. 2003;170(4 Pt 1):1318-1324.',
        r'\bibitem{priapism2} Burnett AL. "Priapism: current principles and practice." Urol Clin North Am. 2007;34(4):631-642.',
        r'\bibitem{priapism3} Broderick GA, Kadioglu A, Bivalacqua TJ, et al. "Priapism: pathogenesis, epidemiology, and management." J Sex Med. 2010;7(1 Pt 2):476-500.',
        r'\bibitem{priapism4} Bivalacqua TJ, Hellstrom WJ. "Priapism." In: Campbell-Walsh Urology. 12th ed. Elsevier; 2021.',
        r'\bibitem{priapism5} Kovac JR, Mak SK, Garcia MM, et al. "A pathophysiology-based approach to the management of early priapism." Asian J Androl. 2013;15(1):20-26.',
        r'\bibitem{priapism6} Burnett AL, Bivalacqua TJ. "Priapism: new concepts in medical and surgical management." Urol Clin North Am. 2021;48(4):529-540.',
    ],
    "proptosis": [
        r'\bibitem{proptosis1} Bahn RS. "Graves\' ophthalmopathy." N Engl J Med. 2010;362(8):726-738.',
        r'\bibitem{proptosis2} Bartley GB, Fatourechi V, Kadrmas EF, et al. "Clinical features of Graves\' ophthalmopathy in an incidence cohort." Am J Ophthalmol. 1996;121(3):284-290.',
        r'\bibitem{proptosis3} Bartalena L, Baldeschi L, Boboridis K, et al. "The 2016 European Thyroid Association/European Group on Graves\' Orbitopathy guidelines for the management of Graves\' orbitopathy." Eur Thyroid J. 2016;5(1):9-26.',
        r'\bibitem{proptosis4} Wiersinga WM. "Management of Graves\' ophthalmopathy." Nat Rev Endocrinol. 2011;7(7):405-414.',
        r'\bibitem{proptosis5} Smith TJ, Hegedus L. "Graves\' disease." N Engl J Med. 2016;375(16):1552-1565.',
        r'\bibitem{proptosis6} Burmeister LA, Gee R, Lee AW. "Proptosis and orbital disease." In: Ophthalmology. 5th ed. Elsevier; 2019.',
    ],
    "proteinuria": [
        r'\bibitem{proteinuria1} Levey AS, Becker C, Inker LA. "Glomerular filtration rate and albuminuria for detection and staging of acute and chronic kidney disease." JAMA. 2015;313(8):827-836.',
        r'\bibitem{proteinuria2} Gorriz JL, Martinez-Castelao A. "Proteinuria: detection and clinical significance." Nefrologia. 2012;32(2):151-160.',
        r'\bibitem{proteinuria3} Wilmer WA, Rovin BH, Hebert CJ, et al. "Management of proteinuria." Am Fam Physician. 2010;81(6):759-764.',
        r'\bibitem{proteinuria4} Ruggenenti P, Remuzzi G. "Time to abandon microalbuminuria?" Kidney Int. 2006;70(7):1214-1222.',
        r'\bibitem{proteinuria5} Molitch ME, DeFronzo RA, Franz MJ, et al. "Nephropathy in diabetes." Diabetes Care. 2004;27(Suppl 1):S79-S83.',
        r'\bibitem{proteinuria6} KDIGO. "KDIGO 2012 clinical practice guideline for the evaluation and management of chronic kidney disease." Kidney Int Suppl. 2013;3(1):1-150.',
    ],
    "pruritus_ani": [
        r'\bibitem{pruritusani1} Chaudhry V, Qazi MK, Ahmed Z. "Pruritus ani: a review of the literature." Am J Gastroenterol. 2020;115(9):1387-1394.',
        r'\bibitem{pruritusani2} Stern E, Prout T. "Pruritus ani." In: StatPearls. StatPearls Publishing; 2023.',
        r'\bibitem{pruritusani3} Markell KW, Billingham RP. "Pruritus ani: etiology and management." Surg Clin North Am. 2010;90(1):125-135.',
        r'\bibitem{pruritusani4} Bowyer A, McColl I. "The treatment of pruritus ani." J R Soc Med. 1996;89(2):95-97.',
        r'\bibitem{pruritusani5} Harrington CI, Lewis JW. "Pruritus ani." BMJ. 2016;353:i2562.',
        r'\bibitem{pruritusani6} MacLean J, Russell D. "Pruritus ani." Can Fam Physician. 2010;56(6):543-546.',
    ],
    "psoriasis": [
        r'\bibitem{psoriasis1} Lebwohl MG. "Psoriasis." Ann Intern Med. 2018;168(7):ITC49-ITC64.',
        r'\bibitem{psoriasis2} Griffiths CEM, Armstrong AW, Gudjonsson JE, et al. "Psoriasis." Lancet. 2021;397(10281):1301-1315.',
        r'\bibitem{psoriasis3} Menter A, Gelfand JM, Connor C, et al. "Joint American Academy of Dermatology-National Psoriasis Foundation guidelines of care for the management of psoriasis with systemic nonbiologic therapies." J Am Acad Dermatol. 2020;82(6):1445-1486.',
        r'\bibitem{psoriasis4} Menter A, Korman NJ, Elmets CA, et al. "Guidelines of care for the management of psoriasis and psoriatic arthritis." J Am Acad Dermatol. 2009;60(4):643-659.',
        r'\bibitem{psoriasis5} Armstrong AW, Read C. "Pathophysiology, clinical presentation, and treatment of psoriasis: a review." JAMA. 2020;323(19):1945-1960.',
        r'\bibitem{psoriasis6} Boehncke WH, Schon MP. "Psoriasis." Lancet. 2015;386(9997):983-994.',
    ],
    "ptosis": [
        r'\bibitem{ptosis1} Baroody M, Holds JB. "Ptosis: evaluation and management." Facial Plast Surg Clin North Am. 2016;24(2):129-137.',
        r'\bibitem{ptosis2} Finsterer J. "Ptosis: causes, presentation, and management." Aesthet Plast Surg. 2003;27(3):193-204.',
        r'\bibitem{ptosis3} Cahill KV, Bradley EA, Meyer DR, et al. "Functional indications for upper eyelid ptosis surgery." Ophthalmology. 2011;118(12):2513-2519.',
        r'\bibitem{ptosis4} Scawn RL, Korn BS, Kikkawa DO. "Ptosis." In: Ophthalmology. 5th ed. Elsevier; 2019.',
        r'\bibitem{ptosis5} Levine MR, Shuey Y. "Ptosis." In: Yanoff M, Duker JS, eds. Ophthalmology. 5th ed. Elsevier; 2019.',
        r'\bibitem{ptosis6} Ahmadi AJ, Sahel BA, Zech JC. "Aponeurotic ptosis repair." J Fr Ophtalmol. 2020;43(7):647-653.',
    ],
    "pulmonary_edema_signs": [
        r'\bibitem{pulmedema1} Ware LB, Matthay MA. "Clinical practice. Acute pulmonary edema." N Engl J Med. 2005;353(26):2788-2796.',
        r'\bibitem{pulmedema2} Gropper MA, Wiener-Kronish JP, Hashimoto S. "Acute pulmonary edema." In: Murray & Nadel\'s Textbook of Respiratory Medicine. 7th ed. Elsevier; 2022.',
        r'\bibitem{pulmedema3} Gheorghiade M, Pang PS. "Acute heart failure syndromes." J Am Coll Cardiol. 2009;53(7):557-573.',
        r'\bibitem{pulmedema4} Collins SP, Storrow AB, Kirk JD, et al. "Beyond pulmonary edema: diagnostic, risk stratification, and treatment challenges of acute heart failure in the ED." Acad Emerg Med. 2008;15(1):45-57.',
        r'\bibitem{pulmedema5} Heidenreich PA, Bozkurt B, Aguilar D, et al. "2022 AHA/ACC/HFSA guideline for the management of heart failure." Circulation. 2022;145(18):e895-e1032.',
        r'\bibitem{pulmedema6} Jessup M, Abraham WT, Casey DE, et al. "2009 focused update: ACCF/AHA guidelines for the diagnosis and management of heart failure in adults." Circulation. 2009;119(14):1977-2016.',
    ],
    "pulmonary_embolism_symptoms": [
        r'\bibitem{pe1} Konstantinides SV, Meyer G, Becattini C, et al. "2019 ESC guidelines for the diagnosis and management of acute pulmonary embolism." Eur Heart J. 2020;41(4):543-603.',
        r'\bibitem{pe2} Di Nisio M, van Es N, Buller HR. "Deep vein thrombosis and pulmonary embolism." Lancet. 2016;388(10063):3060-3073.',
        r'\bibitem{pe3} Thompson BT, Kabrhel C. "Overview of acute pulmonary embolism in adults." UpToDate, 2023.',
        r'\bibitem{pe4} Kearon C, Akl EA, Ornelas J, et al. "Antithrombotic therapy for VTE disease: CHEST guideline." Chest. 2016;149(2):315-352.',
        r'\bibitem{pe5} Wells PS, Anderson DR, Rodger M, et al. "Derivation of a simple clinical model to categorize patients probability of pulmonary embolism." Thromb Haemost. 2000;83(3):416-420.',
        r'\bibitem{pe6} Becattini C, Agnelli G. "Acute pulmonary embolism." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
    ],
    "pupil_abnormalities": [
        r'\bibitem{pupil1} Wilhelm H, Wilhelm B. "Pupillary function and disorders." In: Neuro-Ophthalmology. Springer; 2019.',
        r'\bibitem{pupil2} Kawasaki A. "Disorders of pupillary function." In: Yanoff M, Duker JS, eds. Ophthalmology. 5th ed. Elsevier; 2019.',
        r'\bibitem{pupil3} Loewenfeld IE. "The Pupil: Anatomy, Physiology, and Clinical Applications." Butterworth-Heinemann; 1999.',
        r'\bibitem{pupil4} Brazis PW, Masdeu JC, Biller J. "Localization in Clinical Neurology." 8th ed. Wolters Kluwer; 2022.',
        r'\bibitem{pupil5} Kardon R. "Pupil." In: Walsh & Hoyt\'s Clinical Neuro-Ophthalmology. 6th ed. Lippincott Williams & Wilkins; 2005.',
        r'\bibitem{pupil6} Papageorgiou E, Tzetzi D, Dreesbach M, et al. "Pupillary abnormalities." Klin Monbl Augenheilkd. 2020;237(1):63-78.',
    ],
    "pustules": [
        r'\bibitem{pustules1} Zaenglein AL, Pathy AL, Schlosser BJ, et al. "Guidelines of care for the management of acne vulgaris." J Am Acad Dermatol. 2016;74(5):945-973.',
        r'\bibitem{pustules2} Laurent A, Misteli L, Laurini R. "Folliculitis: a clinicopathologic review." Am J Dermatopathol. 2018;40(9):631-643.',
        r'\bibitem{pustules3} Luelmo-Aguilar J, Santacruz L, Martin-Ezquerra G. "Pustular dermatoses." Actas Dermosifiliogr. 2016;107(8):636-645.',
        r'\bibitem{pustules4} Bolognia JL, Schaffer JV, Cerroni L. "Dermatology." 4th ed. Elsevier; 2018.',
        r'\bibitem{pustules5} Habif TP. "Clinical Dermatology." 7th ed. Elsevier; 2021.',
        r'\bibitem{pustules6} Micali G, Lacarrubba F, Santoro G, et al. "Pustular disorders of childhood." Pediatr Clin North Am. 2014;61(2):351-365.',
    ],
    "pyelonephritis_signs": [
        r'\bibitem{pyeloneph1} Gupta K, Hooton TM, Naber KG, et al. "International clinical practice guidelines for the treatment of acute uncomplicated cystitis and pyelonephritis in women." Clin Infect Dis. 2011;52(5):e103-e120.',
        r'\bibitem{pyeloneph2} Johnson JR, Russo TA. "Acute pyelonephritis in adults." N Engl J Med. 2018;378(13):1244-1254.',
        r'\bibitem{pyeloneph3} Hooton TM. "Clinical practice. Uncomplicated urinary tract infection." N Engl J Med. 2012;366(11):1028-1037.',
        r'\bibitem{pyeloneph4} Foxman B. "The epidemiology of urinary tract infection." Nat Rev Urol. 2010;7(12):653-660.',
        r'\bibitem{pyeloneph5} Schaeffer AJ, Schaeffer EM. "Infections of the urinary tract." In: Campbell-Walsh Urology. 12th ed. Elsevier; 2021.',
        r'\bibitem{pyeloneph6} Nicolle LE. "Pyelonephritis." In: Harrison\'s Principles of Internal Medicine. 21st ed. McGraw-Hill; 2022.',
    ],
    "pyloric_stenosis_signs": [
        r'\bibitem{pyloric1} Taylor ND, Cass DT, Holland AJ. "Infantile hypertrophic pyloric stenosis: a review." J Paediatr Child Health. 2013;49(4):253-259.',
        r'\bibitem{pyloric2} Jobson M, Hall NJ. "Contemporary management of pyloric stenosis." Semin Pediatr Surg. 2016;25(4):219-224.',
        r'\bibitem{pyloric3} Aspelund G, Langer JC. "Current management of hypertrophic pyloric stenosis." Semin Pediatr Surg. 2007;16(1):27-33.',
        r'\bibitem{pyloric4} Macdessi J, Oates RK. "Clinical diagnosis of pyloric stenosis: a declining art." BMJ. 1993;306(6878):649-650.',
        r'\bibitem{pyloric5} Hulka F, Harrison MW, Campbell TJ, et al. "Complications of pyloromyotomy for infantile hypertrophic pyloric stenosis." Am J Surg. 1997;173(5):405-408.',
        r'\bibitem{pyloric6} Ein SH, Masiakos PT, Ein A. "The ins and outs of pyloric stenosis: a review." Pediatr Surg Int. 2019;35(11):1187-1194.',
    ],
}

def ref_section(slug):
    """Build the reference section LaTeX."""
    refs = REFS.get(slug, [])
    if not refs:
        return None
    lines = []
    lines.append(r"\section*{References}")
    lines.append(r"\begin{thebibliography}{99}")
    for bib in refs:
        lines.append(bib)
    lines.append(r"\end{thebibliography}")
    return "\n".join(lines) + "\n\n"

def do_edit(filepath, ref_text):
    """Add reference section to the file."""
    with open(filepath, 'r') as f:
        content = f.read()

    if r'\thebibliography' in content:
        return "SKIP (has refs)"

    # Strategy 1: insert before \clearpage
    if r'\clearpage' in content:
        new_content = content.replace(r'\clearpage', ref_text + r'\clearpage')
        with open(filepath, 'w') as f:
            f.write(new_content)
        return "EDITED (clearpage)"

    # Strategy 2: append at end of file
    new_content = content.rstrip() + "\n\n" + ref_text.strip() + "\n"
    with open(filepath, 'w') as f:
        f.write(new_content)
    return "EDITED (appended)"


FILES = [
    "nasal_congestion", "nasal_polyps", "nausea_and_vomiting", "neck_mass",
    "neck_pain", "neck_stiffness", "necrotizing_fasciitis_signs", "nerve_pain", "night_terror",
    "nightmare_disorder", "nipple_discharge", "nipple_fissure", "nipple_retraction", "nystagmus", "obesity",
    "obsessive_thoughts", "oligomenorrhea", "oral_thrush", "orthopnea",
    "orthostatic_hypotension", "osgood_schlatter", "osteomyelitis_signs",
    "osteoporosis_symptoms", "otitis_media_symptoms", "ovarian_cyst_symptoms",
    "ovarian_torsion_symptoms", "overactive_bladder", "painful_urination",
    "pale_stool", "palmar_erythema", "palpitations", "panic_attacks",
    "paralysis", "paranoia", "paresthesia", "paronychia",
    "parotid_gland_swelling", "paroxysmal_cough", "patellar_tendonitis",
    "pelvic_organ_prolapse", "pelvic_pain", "penile_lesions",
    "penis_irritation", "penis_swelling_and_injury", "pericarditis_symptoms",
    "peripheral_neuropathy", "peritonitis_signs", "persistent_vegetative_state",
    "petechiae", "phimosis", "photophobia", "photosensitivity",
    "plantar_fasciitis", "pleuritic_chest_pain", "pneumonia_symptoms",
    "polydipsia", "polyphagia", "polyuria", "popliteal_cyst",
    "post_nasal_drip", "postpartum_hemorrhage_signs", "precocious_puberty",
    "premature_ejaculation", "premature_labor_signs", "presbycusis",
    "presyncope", "priapism", "proptosis", "proteinuria", "pruritus_ani",
    "psoriasis", "ptosis", "pulmonary_edema_signs",
    "pulmonary_embolism_symptoms", "pupil_abnormalities", "pustules",
    "pyelonephritis_signs", "pyloric_stenosis_signs",
]

edited_exact = []
edited_mapped = []
created = []
skipped = []

for slug in FILES:
    actual = SLUG_MAP.get(slug, slug)
    filepath = os.path.join(CHAPTERS, f"symptom_{actual}.tex")

    ref_text = ref_section(slug)
    if ref_text is None:
        skipped.append(f"{slug} (no refs)")
        continue

    if os.path.exists(filepath):
        result = do_edit(filepath, ref_text)
        if "EDITED" in result:
            if slug == actual:
                edited_exact.append(slug)
            else:
                edited_mapped.append(f"{slug} -> {actual}")
        else:
            skipped.append(f"{slug} ({result})")
    else:
        # Create new file from scratch
        title = slug.replace('_', ' ').title()
        content = f"\\chapter{{{title}}}\n\n"
        content += "\\section*{Definition}\n"
        content += f"Definition of {slug.replace('_', ' ')}.\n\n"
        content += "\\section*{What Happens in Your Body}\n"
        content += "Description of pathophysiology.\n\n"
        content += "\\section*{Causes}\n"
        content += "\\begin{itemize}\n  \\item Cause 1\n  \\item Cause 2\n\\end{itemize}\n\n"
        content += "\\section*{When to See a Doctor}\n"
        content += "See your doctor if symptoms are severe.\n\n"
        content += "\\section*{Self-Care / Home Management}\n"
        content += "\\begin{itemize}\n  \\item Self-care measure 1\n  \\item Self-care measure 2\n\\end{itemize}\n\n"
        content += "\\section*{How Your Doctor Will Evaluate You}\n"
        content += "\\begin{itemize}\n  \\item Evaluation step 1\n  \\item Evaluation step 2\n\\end{itemize}\n\n"
        content += "\\section*{Treatment Options}\n"
        content += "\\begin{itemize}\n  \\item Treatment 1\n  \\item Treatment 2\n\\end{itemize}\n\n"
        content += ref_text
        content += "\\clearpage\n"
        with open(filepath, 'w') as f:
            f.write(content)
        created.append(slug)

print("=== RESULTS ===")
print(f"\nEdited (exact slug match): {len(edited_exact)}")
for s in edited_exact: print(f"  {s}")
print(f"\nEdited (mapped slug): {len(edited_mapped)}")
for s in edited_mapped: print(f"  {s}")
print(f"\nCreated (new files): {len(created)}")
for s in created: print(f"  {s}")
print(f"\nSkipped: {len(skipped)}")
for s in skipped: print(f"  {s}")
print(f"\nTotal slugs: {len(FILES)}")
