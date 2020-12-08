from youtube_transcript_api import YouTubeTranscriptApi
import argparse
import json
import os
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('--youtube_ids_file', default='data/ids.txt')
parser.add_argument('--transcript_folder', default='data/transcripts/')



def main(args):
  os.makedirs(args.transcript_folder, exist_ok=True)
  # Open the main ids file
  with open(args.youtube_ids_file, "r") as f:
    for line in f:
      id = line.strip()
      # remove the url part
      id = id.replace("https://www.youtube.com/watch?v=","")
      print('Processing', id)
      # retrieve the available transcripts
      transcript_list = YouTubeTranscriptApi.list_transcripts(id)

      # you can also directly filter for the language you are looking for, using the transcript list
      transcript = transcript_list.find_transcript(['en'])  
      transcript = transcript.fetch()

      with open(path.join(args.transcript_folder,id+'.json'),"w") as o:
        json.dump(transcript, o)


if __name__ == '__main__':
  args = parser.parse_args()
  main(args)
