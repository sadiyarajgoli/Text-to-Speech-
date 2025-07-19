import whisper
from django.shortcuts import render, redirect
from .forms import AudioUploadForm
from .models import AudioFile

# Load model once (can take a few seconds)
model = whisper.load_model("base")  # or "small" / "medium" / "large"

def upload_audio(request):
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            audio_obj = form.save()

            # Transcribe using Whisper
            result = model.transcribe(audio_obj.file.path)
            audio_obj.transcribed_text = result["text"]
            audio_obj.save()

            return render(request, 'transcriber/result.html', {
                'audio': audio_obj,
                'transcript': result["text"]
            })
    else:
        form = AudioUploadForm()
    
    return render(request, 'transcriber/upload.html', {'form': form})
