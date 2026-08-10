# Aaapurti Renewable Energy India Pvt. Ltd. — Customs / SIIB matters (Madras High Court)

Working repository for the two writ petitions under Article 226 concerning imported blister copper
(CTH 7402) held by two different Customs formations, plus the research compendium and the demand /
provisional-release letter.

**One FTWZ unit (Warehouse No. 12, Part-G, Survey Nos. 161–162, NDR FTWZ, Nandiambakkam Port Road,
Chennai), two separate imports, two separate SIIB formations, two separate proceedings.**

| Proceeding | Formation | Consignment | Impugned action |
| --- | --- | --- | --- |
| Writ 1 | SIIB, Air Cargo Complex, Chennai | B/E No. 2875354 dated 01.08.2026, 414.556 kg, declared ₹8,32,51,039.90 | Detention at ACC and drawal of samples on 07.08.2026 |
| Writ 2 | SIIB, Chennai-III (Preventive) Commissionerate | second consignment already warehoused in the FTWZ (B/E No./date to be inserted) | Detention and sampling inside the FTWZ on 10.08.2026, s.108 statement of Shri A. Krishnesh Raja, summons DIN 20260873MY0000276822 |

## Layout

- `sources/writ_acc.txt` — source of Writ 1 (Air Cargo / ACC SIIB)
- `sources/writ_prev.txt` — source of Writ 2 (SIIB, Chennai-III Preventive)
- `sources/compendium.md` — compendium of statutes, SEZ Rules, notifications, the Z-type B/E instrument chain, CBIC circulars, the MEPZ SOP clause table and case law, each entry tagged `[Verified]` / `[Reported]` / `[To verify]`
- `sources/letter.md` — demand / provisional-release letter to SIIB, Chennai-III (Preventive)
- `sources/research_note.md` — earlier research note (frozen)
- `drafts/*.docx` — generated filing drafts
- `build/build_writ.py`, `build/build_compendium.py`, `build/build_note.py` — DOCX generators
- `attachments/` — MEPZ SOP, the summons, the CBIC DIN verification
- `caselaw/` — primary order copies

## Regenerating the drafts

```
python3 build/build_writ.py sources/writ_acc.txt  drafts/Aaapurti_Writ_1_AirCargo_SIIB.docx
python3 build/build_writ.py sources/writ_prev.txt drafts/Aaapurti_Writ_2_SIIB_Chennai_III_Preventive.docx
python3 build/build_compendium.py
```

`build_writ.py` reads a line-tagged source (`B|` heading, `N|` numbered affidavit paragraph, `GN|`
numbered ground, `P|` prayer/plain paragraph, `TROW|` table row) and emits a paginated DOCX.

## Open facts to be settled before filing

Second Bill of Entry number and date; date of the demand letter; whether a s.110A application has
been filed; whether Shri Krishnesh Raja signed or received a copy of his statement; whether any
sample acknowledgement or mahazar was signed; whether the goods remain in the FTWZ under seal;
dated office copy of the MEPZ SOP; the Chennai Customs Sampling Procedure / Standing Instructions
referred to in SOP clause 4(c); any IRMS instruction under clause 11; current status of the CBIC
circulars relied on; and the current Chennai ACC Public Notice on movement of SEZ/FTWZ cargo.

Confidential — attorney work product.
