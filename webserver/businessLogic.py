import tempfile, os
from pprint import pprint

import whisper
from pytube import YouTube

from docx import Document
from comtypes.client import CreateObject

def save_transcription_to_word(transcript, filename="transcript.docx"):
    doc = Document()
    doc.add_paragraph(transcript)
    doc.save(filename)
    return filename

def convert_word_to_pdf(word_filename, pdf_filename="transcript.pdf"):
    # This function is platform-dependent
    word = CreateObject('Word.Application')
    doc = word.Documents.Open(word_filename)
    doc.SaveAs(pdf_filename, FileFormat=17)  # 17 represents wdFormatPDF
    doc.Close()
    word.Quit()
    return pdf_filename

def transcribeYoutubeVideo(youtube_url: str,  model_name: str):
    video = downloadYoutubeVideo(youtube_url)
    transcription = transcribe(video, model_name)
    return transcription

def transcribeLocalVideo(local_video: any, model_name="medium"):
    video = downloadLocalVideo(local_video)
    transcription = transcribe(video, model_name)
    return transcription


def transcribe(video: dict, model_name="medium"):
    print("Transcribing...", video['name'])
    print("Using model:", model_name)
    model = whisper.load_model(model_name)
    result = model.transcribe(video['path'], )
    print(result)
    return result["text"]


def downloadYoutubeVideo(youtube_url: str) -> dict:
    print("Processing : " + youtube_url)
    yt = YouTube(youtube_url)
    directory = tempfile.gettempdir()
    file_path = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(directory)
    print("VIDEO NAME " + yt._title)
    print("Download complete:" + file_path)
    return {"name": yt._title, "thumbnail": yt.thumbnail_url, "path": file_path}

def downloadLocalVideo(local_video: any) -> dict:
    directory = tempfile.gettempdir()
    file_path = os.path.join(directory, local_video.name)
    with open(file_path, "wb") as f:
        f.write(local_video.getbuffer())
    video_name = local_video.name
    thumbnail_url = ""  # Local videos typically don't have a thumbnail URL

    print("Download complete: " + file_path)
    return {"name": video_name, "thumbnail": thumbnail_url, "path": file_path}

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")
