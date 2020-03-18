
from pathlib import Path

HOME_DIR = Path.home()

BASE_DIR = HOME_DIR / 'covid_phylo_data'
BASE_DIR.mkdir(exist_ok=True)

CACHE_DIR = BASE_DIR / 'cache'

RAW_SEQUENCE_SHELVE_FNAME = 'raw_seqs.shelve'
