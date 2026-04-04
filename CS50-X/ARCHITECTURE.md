***SWITCH TO CODE VIEW***


llm_autofuzzer/            --- > Language: Python
├── app.py                 # Flask: The central brain. Handles routes and @login_required.
├── helpers.py             # Python: The Bridge. Calls OpenAI API and triggers the C-Engine.
├── schema.sql             # SQL: The data blueprint.
├── fuzzer.db              # SQLite: The actual DB file. This is auto-generated via schema.sql.
├── requirements.txt       # Python: List of pip packages (Flask, openai, python-dotenv)
├── .env                   # Text: Private storage for OPENAI_API_KEY but REDACTED for project documentation.
├── .gitignore             # Git: MUST include .env, fuzzer.db, and /venv/.
├── README.md              # Markdown: The project overview for the CS50 graders.
├── ARCHITECTURE.md        # Markdown: Detailed technical breakdown of the Python/C/SQL stack.
│
├── core/                  --- > Language: C
│   ├── engine.c           # C: Logic for ROT13, Base64, and Leetspeak obfuscation.
│   ├── dictionary.h       # C: German/English keyword mapping for translation attacks.
│   └── Makefile           # Script: Simplifies compilation.
│
├── static/                --- > Languages: CSS, Javascript
│   ├── css/styles.css     # CSS: Dark mode... Hell yeah!
│   ├── js/dashboard.js    # JS: For Data Analytics. Powers the Pie Charts on index.html using Chart.js.
│   └── js/scanner.js      # JS: Handles AJAX so scans run without a page refresh.
│
└── templates/             --- > Language: HTML, CSS
    ├── layout.html        # HTML: The base (Navbar, Footer, Flash messages).
    ├── index.html         # HTML: The Data Analytics and Dashboard. High-level stats of past "attacks."
    ├── scan.html          # HTML: The "Launch" page. Form to pick target and mutation.
    └── results.html       # HTML: The Report. Shows the exact prompt that bypassed the AI.
