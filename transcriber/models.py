from django.db import models

class AudioFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    transcribed_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name