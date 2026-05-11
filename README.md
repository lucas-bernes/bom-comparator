# Altium vs JLCPCB BOM Comparator

Python tool for comparing Altium Designer BOM exports against JLCPCB assembly BOM files in order to detect components missing from PCB assembly.

This project simulates a real-world electronics manufacturing workflow by parsing, normalizing, and validating Bill of Materials (BOM) files generated from different PCB design and assembly environments.

---

## Why This Project?

When designing PCBs in Altium Designer and ordering SMT assembly through JLCPCB, BOM inconsistencies may occur due to:

- Missing components
- Incorrect assembly exports
- Split top/bottom designators
- Different spreadsheet formats
- Grouped designator representations

This tool automates BOM validation and helps identify assembly discrepancies before PCB manufacturing.

---

## Features

- Generate synthetic Altium BOMs
- Generate synthetic JLCPCB BOMs
- Randomized component generation
- Randomized Altium header position
- Automatic BOM parsing and normalization
- Split grouped designators into individual components
- Compare Altium and JLCPCB BOMs
- Detect missing assembly components
- Export comparison reports to Excel
- Command-line interface (CLI) support

---

## Project Structure

```text
BOM Comparator/
│
├── data/
│   ├── altium_bom.xlsx
│   └── jlcpcb_bom.xlsx
│
├── outputs/
│   └── missing_components.xlsx
│
├── bom_sheet_generator.py
├── bom_comparator.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Enter the project folder:

```bash
cd "BOM Comparator"
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Generate synthetic BOM files:

```bash
python bom_sheet_generator.py
```

Run BOM comparison:

```bash
python bom_comparator.py --altium data/altium_bom.xlsx --jlcpcb data/jlcpcb_bom.xlsx --output outputs/missing_components.xlsx
```

---

## Example Workflow

1. Generate synthetic Altium and JLCPCB BOM files
2. Parse and normalize both spreadsheets
3. Split grouped designators into individual components
4. Compare assembly BOM against design BOM
5. Export missing components to an Excel report

---

## Technologies

- Python
- Pandas
- NumPy
- OpenPyXL
- argparse

---

## Current Goals

- Simulate realistic Altium BOM exports
- Simulate JLCPCB assembly BOMs
- Automatically compare both BOM files
- Export missing component reports
- Improve robustness of BOM parsing

---

## Future Improvements

- Graphical user interface (GUI)
- Better Excel formatting
- Component quantity validation
- Unit tests
- CSV support
- Real-world BOM support
- Extra component detection
- Footprint/value mismatch detection

---

## Author

Lucas Bernes