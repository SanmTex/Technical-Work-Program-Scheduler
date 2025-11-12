Technical Work Program Scheduler

Standalone Python mini-application that automates scheduling of integrated oil & gas field development activities — drilling, facilities deployment, and related tasks — using the client’s templates and conventions.
Quick start

    Clone the repo

Code

git clone https://github.com/SanmTex/Technical-Work-Program-Scheduler.git
cd Technical-Work-Program-Scheduler

Create and activate a virtual environment

Code

python3 -m venv .venv
source .venv/bin/activate

Install dependencies (if requirements.txt exists)

Code

pip install -r requirements.txt

Run the scheduler (adjust script/module path as needed)

Code

    python src/scheduler.py --csv examples/sample.csv --out examples/out_summary.csv

Expected output

    An integrated field development activities Gantt chart (image file saved in the repo or output folder).
