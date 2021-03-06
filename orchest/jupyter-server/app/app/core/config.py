import os


# ---- CONFIGURATIONS ----
PRODUCTION = True


# Static configurations, please do not change these.
if PRODUCTION:
    NOTEBOOK_DIR = '/pipeline-dir'
else:
    abs_path = os.path.dirname(os.path.abspath(__file__))
    NOTEBOOK_DIR = os.path.join(abs_path, '..', 'tmp')
