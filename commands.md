# Setup Commands

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
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
echo ".venv/" > .gitignore
echo "__pycache__/" >> .gitignore
git status
git add .
git commit -m "Set up midterm project structure and virtual environment"
git remote add origin https://github.com/niaxenikis/ism3232-midterm.git
brew install gh
gh auth login
git push -u origin main
```
