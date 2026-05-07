# BOM Comparator

Tool for comparing Altium and JLCPCB BOM files to identify components missing from assembly.

---

## Features

- Generate synthetic Altium BOMs
- Generate synthetic JLCPCB BOMs
- Randomized component generation
- Randomized Altium header position
- Split top/bottom designators
- Detect missing components between BOMs

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
│
├── bom_sheet_generator.py
├── bom_comparator.py
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
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
python bom_comparator.py
```

---

## Technologies

- Python
- Pandas
- NumPy
- OpenPyXL

---

## Current Goals

- Simulate realistic Altium BOM exports
- Simulate JLCPCB assembly BOMs
- Compare both files automatically
- Export missing component reports

---

## Future Improvements

- GUI interface
- Better Excel formatting
- Component quantity validation
- Unit tests
- CSV support
- Real-world BOM support

---

## Author

Lucas Bernes