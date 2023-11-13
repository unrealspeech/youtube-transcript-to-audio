from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):
    """Extracts the video ID from a YouTube URL."""
    regex = r"(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    matches = re.search(regex, url)
    return matches.group(1) if matches else None


def get_youtube_transcript(url):
    """Gets the transcript of a YouTube video given its URL."""
    video_id = extract_video_id(url)
    if video_id is None:
        return "Invalid YouTube URL"

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Joining the text of the transcript segments
        transcript_text = "\n".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return f"An error occurred: {e}"


# Example usage
url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
print(get_youtube_transcript(url))
