# ISM3232 Midterm: Copper Kettle Coffee Roasters

- **Antonia Xenikis** 
- **ZETA:** 
- **10/25/2026** 

## What This Program Does

This program calculates the cost of wholesale coffee shipments for Copper Kettle Coffee Roasters, which sells coffee by the bag to shops and hotels. It applies bulk discounts, an extra discount for partners, and a shipping fee on small orders. It also checks whether each shipment needs prepayment or a pallet, then displays a report with one line per shipment and a summary at the end.

## Business Rules

-The bean cost is the price of one bag multiplied by the number of bags.
-Orders under 20 bags get no discount, orders of 20-79 bags get 9% off, and orders of 80 bags or more get 14% off.
-Partner cafes get 4 more percentage points off (13% or 18%), but only when they order at least 20 bags.
-If the cost after discount is under $250, a $35 shipping fee is added.
-Any shipment that totals $15,000 or more has to be paid for in advance.
-A shipment needs a freight pallet if it has more than 60 bags and its total is over $700.
## How to Run

```bash
git clone https://github.com/niaxenikis/ism3232-midterm.git
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## How to Test
```bash
ruff check
pytest -v
```

## Files in This Repository
-'business_rules.py' - the eight functions that apply the business rules
-"main.py' - the shipment list and the code that displays the report
-'commands.md' - the terminal record of how the project was built and checked
-'README.md' - this file, exmplaining what the project does and how to use it 
-'requirements.txt' - tells Git to leave the .venv and the __pycache__ folder out of the repository
-'tests/__init__.py' - an empty file that marks the test folder as a python package
-'tests/test_business_rules.py' - the pytest tests for every business rule function
## AI Use Statement
I did not use AI in the completion of this assignment.