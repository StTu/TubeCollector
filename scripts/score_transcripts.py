import argparse
import json
import os
from os import path
import string
from nltk import ngrams, FreqDist
from nltk.corpus import wordnet
import re

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser()
parser.add_argument('--youtube_ids_file', default='data/ids.txt')
parser.add_argument('--youtube_ids_scoring', default='data/ids_score.txt')
parser.add_argument('--transcript_folder', default='data/transcripts/')

parser.add_argument('--keywords', default=[],nargs='+', type=str)
parser.add_argument('--keywords_file', default='data/keywords.txt')
parser.add_argument('--keyword_expansion', type=str2bool, default=True)

def build_dictionary(args):
  keyword_dict = []
  if args.keywords_file and args.keywords:
    if len(args.keywords) and len(args.keywords_file):
      print('Warning using Keyword list as you took time to enter')
  if args.keywords:
    keyword_dict = args.keywords
  if args.keywords_file:
    with open(args.keywords_file, "r") as f:
      for line in f:
        word = line.strip().translate(str.maketrans('', '', string.punctuation)).lower()
        keyword_dict.append(word)

  if args.keyword_expansion:
    expanded_keywords = []
    for w in keyword_dict:
      expanded_keywords.append(w)
      for syn in wordnet.synsets(w):
        for l in syn.lemmas():
          expanded_keywords.append(l.name())
    return list(set(expanded_keywords))
  
  return list(set(keyword_dict))


def spot_words(keyword_dict, line):
  line = line.translate(str.maketrans('', '', string.punctuation)).lower()
  matches = 0

  for keyword in keyword_dict:
    matches += len(re.findall(keyword, line))
  return matches


def main(args):
  keyword_dict = build_dictionary(args)
  print(keyword_dict)
  os.makedirs(args.transcript_folder, exist_ok=True)
  # Open the main ids file
  with open(args.youtube_ids_file, "r") as f:
    with open(args.youtube_ids_scoring, "w") as score_file:
      for line in f:
        id = line.strip()
         # remove the url part
        id = id.replace("https://www.youtube.com/watch?v=","")
        print('Processing', id)

        with open(path.join(args.transcript_folder,id+'.json')) as transcript_file:
          transcript = json.load(transcript_file)
          mentions = 0
          for l in transcript:
            mentions += spot_words(keyword_dict,l["text"])
            
          score_file.write(id+','+ str(mentions) + '\n')
          print('  Score:', str(mentions))


if __name__ == '__main__':
  args = parser.parse_args()
  main(args)
