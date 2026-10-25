# Terminal Record: Copper Kettle Coffee Roasters 

## 1. Building the project

```bash
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
git init
git branch -M main
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip freeze > requirements.txt
touch business_rules.py main.py commands.md README.md .gitignore
mdkir tests
touch tests/__init__.py tests/test_business_rules.py
echo ".venv/" > .gitignore
echo "__pycache__/" >> .gitignore
git status
git add .
git commit -m "Set up midterm project structure and virtual enviroment"
git remote add origin https://github.com/niaxenikis/ism3232-midterm.git
brew install gh
gh auth login
git push -u origin main
```

## 2. The virtual environment
```bash
which python3
```

```text
/Users/antoniaxenikis/ism3232-midterm/.venv/bin/python3
```

## 3. The project structure
```bash
tree -L 2
```

```text
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```

## 4. Every function and test
```bash
rg 'def '
```

```text
main.py
22:def main() -> None:

business_rules.py
14:def calculate_bean_cost(bag_price: float, bags: int) -> float:
18:def get_bulk_discount(bags: int, partner: bool = False) -> float:
30:def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
39:def requires_prepayment(total: float) -> bool:
43:def needs_pallet(bags: int, total: float) -> bool:
47:def total_shipped(shipments: list) -> float:
57:def largest_shipment(shipments: list) -> str:
70:def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:

tests/test_business_rules.py
15:def test_bean_cost_multiples_price_by_bags() -> None:
19:def test_no_discount_at_19_bags() -> None:
23:def test_standard_discount_at_20_bags() -> None:
27:def test_standard_discount_at_79_bags() -> None:
31:def test_large_discount_at_80_bags() -> None:
35:def test_partner_gets_no_bonus_under_20_bags() -> None:
39:def test_partner_bonus_at_20_bags() -> None:
43:def test_partner_bonus_at_80_bags() -> None:
47:def test_partner_changes_shipment_total() -> None:
52:def test_no_shipping_fee_at_250() -> None:
56:def test_shipping_fee_added_below_250() -> None:
60:def test_prepayment_required_at_1500() -> None:
64:def test_no_prepayment_at_1499_99() -> None:
68:def test_pallet_no_pallet_at_60_bags() -> None:
72:def test_pallet_needed_at_61_bags() -> None:
76:def test_no_pallet_at_700_total() -> None:
80:def test_pallet_needed_above_700_total() -> None:
84:def test_total_shipped_adds_shipment_totals() -> None:
92:def test_total_shipped_empty_list() -> None:
96:def test_largest_shipment_returns_biggest_buyer() -> None:
104:def test_largest_shipment_tie_returns_first() -> None:
112:def test_largest_shipment_empty_list() -> None:
116:def test_format_line_with_no_and_no() -> None:
121:def test_format_line_with_yes_and_yes() -> None:
```

## 5. Which files print
```bash
rg -l 'print'
```

```text
main.py
commands.md
```

## 6. The commit history
'''bash
git log --oneline
```

```text 
3b9082c (HEAD -> main, origin/main) Add pytest tests and fix bean cost function name
57f96ed Add pytest tests and fix bean cost function name
6e63c9d Add main.py shipment report
d8e4359 Add business rule functions
364bba5 Record setup commands
ef63707 Set up midterm project structure and virtual enviroment
```