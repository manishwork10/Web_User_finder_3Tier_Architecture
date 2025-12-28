

import subprocess, sys, os
from pathlib import Path

root = Path(__file__).resolve().parent
os.environ["FLASK_APP"] = "app.views:app"

try:
    api  = subprocess.Popen([sys.executable, "-m", "uvicorn", "api.main:app",
                             "--host", "0.0.0.0", "--port", "8000"])
    web  = subprocess.Popen([sys.executable, "-m", "flask", "run",
                             "--host", "0.0.0.0", "--port", "5001"])
    api.wait()
except KeyboardInterrupt:
    api.terminate()
    web.terminate()