# TubeCollector
Tool to download  subtitles of YouTube Videos and find highest matching based on the transcription



## Setup
```bash
virtualenv -p python3 .env       # Create virtual environment
source .env/bin/activate         # Activate virtual environment
pip install -r requirements.txt  # Install dependencies
```

To setup wordnet
```python
python
import nltk
nltk.download('wordnet')
```
(This was from memory, there is a warning otherwise)

## Running
Simple approach firstly download then analyse

### Download
Edit the data/ids.txt with all the YouTube video ids

```bash
python scripts/download_transcripts.py
```
Output:
```
Processing 2UGblKA6BaQ
Processing RPeW0QeNMvY
Processing qplGd4Kbj8I
Processing 6nkVrv1jd6U
```

### Analyse
Counts words and stores in file specified

keyword_expansion = WordNet synonyms

```bash
python scripts/score_transcripts.py --keyword_expansion false --keywords legs sholder
```

Output:
```
Warning using Keyword list as you took time to enter
['sholder', 'hips', 'legs', 'weight', 'measure', 'size', 'fit']
Processing 2UGblKA6BaQ
  Score: 85
Processing RPeW0QeNMvY
  Score: 30
Processing qplGd4Kbj8I
  Score: 64
Processing 6nkVrv1jd6U
  Score: 15
```


