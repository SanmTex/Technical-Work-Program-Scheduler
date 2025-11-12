Technical Work Program Scheduler

Standalone Python mini-application that automates scheduling of integrated oil and gas field development activities — drilling, facilities deployment, and related tasks — using the client’s templates and conventions.

Quick start
git clone https://github.com/SanmTex/Technical-Work-Program-Scheduler.git
cd Technical-Work-Program-Scheduler

python3 -m venv .venv
source .venv/bin/activate

install dependencies if you have requirements.txt
pip install -r requirements.txt

run (adjust script/module path as needed)
python src/scheduler.py --csv examples/sample.csv --out examples/out_summary.csv

Expected output
Integrated field devleopment activities Gantt chart
