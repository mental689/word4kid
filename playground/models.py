from django.db import models

# Create your models here.


class Video(models.Model):
    url = models.CharField(max_length=255, null=False, blank=False, unique=True)
    duration = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Label(models.Model):
    text = models.CharField(max_length=255, null=False, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Segment(models.Model):
    start = models.FloatField(default=0.0)
    stop = models.FloatField(default=0.0)
    label = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='segments')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='segments', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Sentence(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        segments = []
        for s in self.segments:
            segments.append(s.segment.label.text)
        return '-'.join(segments)


class SegmentInSentence(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE, related_name='segments')
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='sentences')
    order = models.IntegerField(default=0, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

