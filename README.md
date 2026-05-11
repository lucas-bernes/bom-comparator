from pathlib import Path

readme_text = '''# BOM Comparator

Tool for comparing Altium and JLCPCB BOM files to identify components missing from PCB assembly.

---

## Features

- Generate synthetic Altium BOMs
- Generate synthetic JLCPCB BOMs
- Randomized component generation
- Randomized Altium header position
- Automatic BOM parsing and normalization
- Split grouped designators into individual components
- Compare Altium and JLCPCB BOMs
- Detect missing components from assembly BOMs
- Export comparison results to Excel
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
'''

Path("README.md").write_text(readme_text, encoding="utf-8")

print("README.md updated successfully.")