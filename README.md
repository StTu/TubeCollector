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