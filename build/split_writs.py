"""Split the composite writ source into two petitions:
   writ_acc.txt  -> SIIB, Air Cargo Complex (B/E 2875354 detention + 07.08.2026 sampling)
   writ_prev.txt -> SIIB, Chennai-III (Preventive) (10.08.2026 FTWZ detention, sampling, s.108 summons)
"""

M = [None] + open('/home/ubuntu/writ_draft.txt').read().split('\n')


def L(*idx):
    out = []
    for i in idx:
        out.append(M[i])
    return out


def rng(a, b):
    return [M[i] for i in range(a, b + 1)]


HDR = rng(1, 5)
PET = rng(6, 15)
MEMO = rng(48, 51)
DATED = rng(62, 66)
VERIF = rng(121, 129)

ACC_RESP = """C|Versus
BLANK
P|1. The Additional Commissioner of Customs,
P|    Special Intelligence and Investigation Branch (SIIB),
P|    Air Cargo Complex, Meenambakkam, Chennai - 600 027,
P|    through the Union of India,
P|    represented by the Secretary to Government,
P|    Ministry of Finance, Department of Revenue,
P|    North Block, New Delhi - 110 001.                             ... Respondent No. 1
P|    (the authority whose officers have detained the consignment covered by Bill of Entry No. 2875354 dated 01.08.2026 at the Air Cargo Complex and drawn samples therefrom on 07.08.2026)
BLANK
P|2. The Commissioner of Customs,
P|    Air Cargo Complex, Meenambakkam,
P|    Chennai - 600 027.                                             ... Respondent No. 2
BLANK
P|3. The Development Commissioner,
P|    MEPZ Special Economic Zone, National Highway 45,
P|    Tambaram, Chennai - 600 045.                                   ... Respondent No. 3
P|    (the authority administering the SEZ and the issuer of the Standard Operating Procedure "Clearance of Blister Copper under CTH 7402" bearing F.No. MEPZ-MSM043(C)/226/2025-SEZ Chennai (e-file No. I/131691/2026))
BLANK
P|4. The Specified Officer / Authorised Officer,
P|    MEPZ Special Economic Zone,
P|    Tambaram, Chennai - 600 045.                                   ... Respondent No. 4
BLANK
BLANK""".split('\n')

PREV_RESP = """C|Versus
BLANK
P|1. The Additional Commissioner of Customs,
P|    Special Intelligence and Investigation Branch (SIIB),
P|    Office of the Principal Commissioner of Customs, Chennai-III
P|    (Preventive Commissionerate), Custom House, No. 60, Rajaji Salai,
P|    Chennai - 600 001,
P|    through the Union of India,
P|    represented by the Secretary to Government,
P|    Ministry of Finance, Department of Revenue,
P|    North Block, New Delhi - 110 001.                             ... Respondent No. 1
P|    (the authority whose officers have, on 10.08.2026, detained the Blister Copper lying in the Petitioner's Free Trade Warehousing Zone unit, drawn samples therefrom and issued the summons in F.No. GEN/INV/DR/170//2026-SIIB bearing DIN-20260873MY0000276822)
BLANK
P|2. The Principal Commissioner of Customs, Chennai-III
P|    (Preventive Commissionerate), Custom House, No. 60, Rajaji Salai,
P|    Chennai - 600 001.                                             ... Respondent No. 2
BLANK
P|3. The Development Commissioner,
P|    MEPZ Special Economic Zone, National Highway 45,
P|    Tambaram, Chennai - 600 045.                                   ... Respondent No. 3
P|    (the authority administering the SEZ and the issuer of the Standard Operating Procedure "Clearance of Blister Copper under CTH 7402" bearing F.No. MEPZ-MSM043(C)/226/2025-SEZ Chennai (e-file No. I/131691/2026))
BLANK
P|4. The Specified Officer / Authorised Officer,
P|    MEPZ Special Economic Zone,
P|    Tambaram, Chennai - 600 045.                                   ... Respondent No. 4
BLANK
BLANK""".split('\n')

PRAYER_HEAD = ['B|PRAYER', M[53]]

ACC_PRAYER = [
    M[54].replace('Respondent Nos. 1, 2 and 5', 'Respondent Nos. 1 and 2'),
    M[55],
    M[56],
    M[57],
    "P|(e) in the alternative and without prejudice to prayers (a) to (d), directing the Respondents to release the said consignment to the Petitioner's Free Trade Warehousing Zone unit provisionally under Section 110A of the Customs Act, 1962, on such terms as to bond, undertaking or security as this Hon'ble Court may deem fit, pending completion of testing in accordance with the said Standard Operating Procedure; and",
    "P|(f) pass such further or other order or orders as this Hon'ble Court may deem fit and proper in the facts and circumstances of the case and thus render justice.",
]

PREV_PRAYER = [
    "P|(a) declaring the detention of the Blister Copper imported from the United Arab Emirates and lying warehoused in the Petitioner's Free Trade Warehousing Zone unit at Warehouse No. 12, Part-G, Survey Nos. 161 and 162, at the Free Trade Warehousing Zone of M/s NDR Infrastructure Private Limited, Nandiambakkam Port Road, Chennai, effected by the officers of Respondent No. 1 on 10.08.2026, and the drawal of samples therefrom on that date, without any written order, without any order of seizure or grounds of belief recorded and communicated under Section 110 of the Customs Act, 1962, without any mahazar, panchanama, sampling memo or receipt under Section 144 of the said Act, and without compliance with Section 22 of the Special Economic Zones Act, 2005 read with S.O. 2666(E) and S.O. 2667(E) both dated 05.08.2016, as illegal, arbitrary, without jurisdiction and violative of Articles 14, 19(1)(g) and 300A of the Constitution of India;",
    "P|(b) directing Respondent No. 1 to forthwith release the said goods to the Petitioner's Free Trade Warehousing Zone unit and to permit the same to be dealt with in accordance with the Standard Operating Procedure \"Clearance of Blister Copper under CTH 7402\" bearing F.No. MEPZ-MSM043(C)/226/2025-SEZ Chennai (e-file No. I/131691/2026);",
    M[59].replace('(f) directing', '(c) directing'),
    "P|(d) declaring that the summons dated 10.08.2026 in F.No. GEN/INV/DR/170//2026-SIIB bearing DIN-20260873MY0000276822, requiring the attendance of Shri A. Krishnesh Raja at 5.00 p.m. on the very date of its issue, and the statement recorded thereunder, are contrary to Section 108 of the Customs Act, 1962 and to the principles of natural justice, and directing Respondent No. 1 to furnish a copy of the said statement to the Petitioner and to the said deponent, together with the record of issuance and service of the said summons and of the generation of the said Document Identification Number;",
    "P|(e) directing Respondent No. 1 to forbear from taking any coercive step in respect of the goods lying in the Petitioner's Free Trade Warehousing Zone unit otherwise than by an order in writing passed under Section 110 of the Customs Act, 1962 upon grounds of belief recorded in writing and served upon the Petitioner, and in compliance with Section 22 of the Special Economic Zones Act, 2005;",
    "P|(f) in the alternative and without prejudice to prayers (a) to (e), directing the Respondents to release the said goods provisionally under Section 110A of the Customs Act, 1962 on such terms as to bond, undertaking or security as this Hon'ble Court may deem fit, in the terms in which this Hon'ble Court granted relief in W.P. No. 29074 of 2025 (order dated 23.09.2025); and",
    "P|(g) pass such further or other order or orders as this Hon'ble Court may deem fit and proper in the facts and circumstances of the case and thus render justice.",
]


def aff_head(short_title):
    return [
        'PB|--- PAGE BREAK ---',
        'H1|IN THE HIGH COURT OF JUDICATURE AT MADRAS',
        'C|(SPECIAL ORIGINAL JURISDICTION)',
        'B|W.P. No. ________ of 2026',
        'BLANK',
        M[72], M[73], M[74],
        'P|' + short_title + '                                  ... Respondents',
        'BLANK',
        'B|AFFIDAVIT FILED IN SUPPORT OF THE WRIT PETITION',
        'BLANK',
        M[79],
        'BLANK',
    ]


def wmp_page(short_title, wmps):
    out = [
        'PB|--- PAGE BREAK ---',
        'H1|IN THE HIGH COURT OF JUDICATURE AT MADRAS',
        'C|(SPECIAL ORIGINAL JURISDICTION)',
        'B|W.M.P. No. ________ of 2026',
        'B|in',
        'B|W.P. No. ________ of 2026',
        'BLANK',
        M[137], M[138], M[139],
        'P|' + short_title + '                                  ... Respondents',
        'BLANK',
        'B|APPLICATION FOR INTERIM DIRECTION',
        M[143],
        'BLANK',
    ]
    for w in wmps:
        out += [w, 'BLANK']
    out += ["P|                                                                      Counsel for the Petitioner"]
    return out


def index_page(short_title, rows):
    out = [
        'PB|--- PAGE BREAK ---',
        'H1|IN THE HIGH COURT OF JUDICATURE AT MADRAS',
        'C|(SPECIAL ORIGINAL JURISDICTION)',
        'B|W.P. No. ________ of 2026',
        'BLANK',
        M[158], M[159],
        'P|' + short_title + '       ... Respondents',
        'BLANK',
        'B|INDEX',
        'BLANK',
        M[164],
    ] + rows + ['TEND', 'BLANK',
                'P|Note: Page numbers are to be filled in by Counsel after pagination. The documents forming the typed set are to be arranged in chronological order and consecutively page-numbered.',
                'BLANK',
                "P|                                                                      Counsel for the Petitioner"]
    return out



# ---------------- ACC writ ----------------
acc = []
acc += HDR + PET + ACC_RESP + MEMO + ['BLANK'] + PRAYER_HEAD + ACC_PRAYER + ['BLANK'] + DATED
acc += aff_head('The Additional Commissioner of Customs, SIIB, Air Cargo Complex, Chennai and others')
acc += rng(81, 90)
acc += [M[91], M[92]]
acc += ["N|It is submitted, by way of disclosure, that officers of the Special Intelligence and Investigation Branch of the Chennai-III (Preventive) Commissionerate have, by a separate and later action taken on 10.08.2026, detained the stock of Blister Copper lying warehoused in the Petitioner's Free Trade Warehousing Zone unit and drawn samples therefrom, in respect of which the Petitioner has filed a separate Writ Petition before this Hon'ble Court. The present Writ Petition is confined to the consignment covered by Bill of Entry No. 2875354 dated 01.08.2026, which continues to lie at the Air Cargo Complex, Chennai, and to the drawal of samples therefrom on 07.08.2026."]
acc += ["N|Respondent No. 1 is a necessary and proper party to this Writ Petition, being the authority whose officers have detained the subject consignment without any written order and have drawn samples therefrom on 07.08.2026 without any panchanama, mahazar or sampling memo, and the relief of release is sought directly against it. Respondent No. 2 is a necessary and proper party, being the Commissionerate in whose jurisdiction the consignment continues to lie in the custody of the custodian at the Air Cargo Complex. Respondent No. 3 is likewise a necessary and proper party, being the authority administering the MEPZ Special Economic Zone under the Special Economic Zones Act, 2005, the authority under whose control the Petitioner's FTWZ unit and the Authorised Officer / Specified Officer function, and the very authority which has issued the Standard Operating Procedure bearing F.No. MEPZ-MSM043(C)/226/2025-SEZ Chennai governing the clearance of Blister Copper under CTH 7402. No effective relief can be granted to the Petitioner in the absence of Respondent Nos. 1, 2 and 3."]
acc += [M[98], 'BLANK', 'B|GROUNDS', M[101], 'BLANK']
acc += [M[103], M[104]]
acc += [M[112], M[113], M[114], M[115], M[111], M[116], M[117], M[109], M[110], M[118], M[119], M[120]]
acc += ['BLANK'] + VERIF
acc += wmp_page('The Additional Commissioner of Customs, SIIB, Air Cargo Complex, Chennai and others',
                [
    "P|W.M.P. No. ____ of 2026: for an interim direction to the Respondents to forthwith permit the movement of the goods covered by Bill of Entry No. 2875354 dated 01.08.2026 from the Air Cargo Complex, Chennai to the Petitioner's Free Trade Warehousing Zone unit for warehousing, examination and sampling in accordance with the Standard Operating Procedure, on the Petitioner furnishing a bond and such undertaking as this Hon'ble Court may direct, pending disposal of the Writ Petition.",
    "P|W.M.P. No. ____ of 2026: for an interim direction to Respondent No. 1 to furnish to the Petitioner the panchanama / mahazar, sampling memo and test memo in respect of the samples drawn on 07.08.2026 and the test reports as and when received, or to state in writing that no such document exists, pending disposal of the Writ Petition.",
    "P|W.M.P. No. ____ of 2026: for a direction to the custodian and to Respondent No. 2 to issue a detention certificate / waive demurrage, ground rent and custodian charges in respect of the period of the detention, pending disposal of the Writ Petition.",
])
ACC_ROWS = [
    'TROW|;;Memorandum of Writ Petition under Article 226 of the Constitution of India, with prayer;;',
    'TROW|;;Affidavit filed in support of the Writ Petition, duly sworn;;',
    'TROW|;;W.M.P. Nos. ____ of 2026 - Applications for interim directions, with affidavits;;',
    'TROW|;;Certificate of the Advocate that the documents filed are true copies of the originals;;',
] + rng(170, 189) + [M[197]]
acc += index_page('The Additional Commissioner of Customs, SIIB, Air Cargo Complex, Chennai and others', ACC_ROWS)
acc += ['PB|--- PAGE BREAK ---'] + rng(204, 217)
acc += ['H1|DOCUMENTS TO BE OBTAINED BEFORE FILING', 'BLANK', M[220], M[221], M[222], M[225], M[226], M[227], M[228], M[229], M[230], M[231], 'TEND']

# ---------------- Preventive writ ----------------
prev = []
prev += HDR + PET + PREV_RESP + MEMO + ['BLANK'] + PRAYER_HEAD + PREV_PRAYER + ['BLANK'] + DATED
prev += aff_head('The Additional Commissioner of Customs, SIIB, Chennai-III (Preventive Commissionerate) and others')
prev += rng(81, 90)
prev += ["N|The consignment covered by Z-type Bill of Entry No. 2875354 dated 01.08.2026 referred to above is presently held at the Air Cargo Complex, Chennai by the Special Intelligence and Investigation Branch of that Commissionerate, and samples were drawn therefrom on 07.08.2026. That action is the subject matter of a separate Writ Petition filed by the Petitioner before this Hon'ble Court and is referred to herein only by way of narration and disclosure. The present Writ Petition is confined to the action taken by the officers of Respondent No. 1 on 10.08.2026 within the Petitioner's Free Trade Warehousing Zone unit."]
prev += [M[93], M[94], M[95], M[96]]
prev += ["N|Respondent No. 1 is a necessary and proper party to this Writ Petition, being the authority whose officers detained the goods lying in the Petitioner's Free Trade Warehousing Zone unit on 10.08.2026, drew samples therefrom and recorded the statement of the Petitioner's employee, and the relief of release is sought directly against it. Respondent No. 2 is a necessary and proper party, being the Commissionerate under which the said Special Intelligence and Investigation Branch functions and from whose office the summons dated 10.08.2026 was issued. Respondent No. 3 is a necessary and proper party, being the authority administering the MEPZ Special Economic Zone under the Special Economic Zones Act, 2005, the authority whose prior intimation or approval Section 22 of the said Act requires, and the very authority which has issued the Standard Operating Procedure bearing F.No. MEPZ-MSM043(C)/226/2025-SEZ Chennai governing the clearance of Blister Copper under CTH 7402. Respondent No. 4 is a necessary and proper party, being the officer in whose custody the goods and the retained sample are required by the said Standard Operating Procedure to remain, and in whose office the statement of the Petitioner's employee was recorded."]
prev += ["N|The Petitioner is left with no efficacious alternative remedy. There is no order in writing capable of being appealed against, which is itself the vice complained of, and the Petitioner is therefore constrained to approach this Hon'ble Court under Article 226 of the Constitution of India."]
prev += ['BLANK', 'B|GROUNDS', M[101], 'BLANK']
prev += [M[103], M[104], M[105], M[106], M[107], M[108], M[113], M[114], M[115], M[111], M[116], M[117], M[109], M[110], M[118], M[119], M[120]]
prev += ['BLANK'] + VERIF
prev += wmp_page('The Additional Commissioner of Customs, SIIB, Chennai-III (Preventive Commissionerate) and others', [
    "P|W.M.P. No. ____ of 2026: for an interim direction to Respondent No. 1 to release the Blister Copper detained on 10.08.2026 at the Petitioner's Free Trade Warehousing Zone unit into the custody of the said unit under bond and under the supervision of Respondent No. 4, or, in the alternative, to permit the said goods to remain in the said unit under seal and to be dealt with in accordance with the Standard Operating Procedure, pending disposal of the Writ Petition.",
    "P|W.M.P. No. ____ of 2026: for an interim direction to Respondent No. 1 to furnish forthwith to the Petitioner the order of detention or seizure, the grounds of belief recorded in writing, the mahazar / panchanama, the inventory, the sampling memo and the authorisation for the drawal of samples on 10.08.2026, the copy of the statement recorded from Shri A. Krishnesh Raja and the record of issuance and service of the summons dated 10.08.2026, or to state in writing that no such document exists, pending disposal of the Writ Petition.",
    "P|W.M.P. No. ____ of 2026: for an interim direction to the Respondents to release the said goods provisionally under Section 110A of the Customs Act, 1962 on the furnishing of a bond for the declared value and such further security as this Hon'ble Court may consider adequate, in the terms in which this Hon'ble Court granted relief in W.P. No. 29074 of 2025 (order dated 23.09.2025), pending disposal of the Writ Petition.",
])
PREV_ROWS = [
    'TROW|;;Memorandum of Writ Petition under Article 226 of the Constitution of India, with prayer;;',
    'TROW|;;Affidavit filed in support of the Writ Petition, duly sworn;;',
    'TROW|;;W.M.P. Nos. ____ of 2026 - Applications for interim directions, with affidavits;;',
    'TROW|;;Certificate of the Advocate that the documents filed are true copies of the originals;;',
] + rng(170, 186) + rng(190, 197)
prev += index_page('The Additional Commissioner of Customs, SIIB, Chennai-III (Preventive Commissionerate) and others', PREV_ROWS)
prev += ['PB|--- PAGE BREAK ---'] + rng(204, 217)
prev += ['H1|DOCUMENTS TO BE OBTAINED BEFORE FILING', 'BLANK', M[220], M[223], M[224],
    'TROW|Copy of the statement recorded on 10.08.2026 from Shri A. Krishnesh Raja, and the record of issuance and service of the summons dated 10.08.2026 and of the generation of DIN-20260873MY0000276822;;To be demanded in writing forthwith; the timing disclosed by the Document Identification Number utility is to be put to the Respondents',
    M[225], M[226], M[227], M[230], M[231], 'TEND']

open('/home/ubuntu/writ_acc.txt', 'w').write('\n'.join(x for x in acc if x is not None) + '\n')
open('/home/ubuntu/writ_prev.txt', 'w').write('\n'.join(x for x in prev if x is not None) + '\n')
print('acc lines', len(acc), 'prev lines', len(prev))
