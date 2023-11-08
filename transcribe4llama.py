from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = ' '.join([entry['text'] for entry in transcript])
    
    return transcript_text

def save_transcript(transcript, filename):
    with open(filename, 'w') as file:
        file.write(transcript)

def main():
    video_id = 'BkllClvT3JM' #'3b0TDBvqYsU'
    raw_transcript = get_transcript(video_id)
    save_transcript(raw_transcript, 'raw_transcript.txt')

if __name__ == "__main__":
    main()

