Technical Work Program Scheduler

Standalone Python mini-application that automates scheduling of integrated oil & gas field development activities — drilling, facilities deployment, and related tasks — using the client’s templates and conventions.


Quick start:
1. Create venv: python3 -m venv .venv && source .venv/bin/activate
2. Install deps (if any): pip install -r requirements.txt
3. Run: python src/scheduler.py --csv examples/sample.csv --out examples/out_summary.csv

EOF

Expected output

An integrated field development activities Gantt chart (image file saved in the repo or output folder).
