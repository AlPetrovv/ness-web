from django.db import models


class PsychomatrixBaseContent(models.Model):
    code = models.CharField(
        max_length=55,
        unique=True,
        null=False,
        blank=False
    )
    title = models.CharField(
        max_length=55,
        null=True,
        blank=True
    )
    text = models.CharField(
        max_length=10240,
        null=True,
        blank=True
    )
    advice = models.CharField(
        max_length=4096,
        null=True,
        blank=True
    )
    recommendation = models.CharField(
        max_length=4096,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'psychomatrix_basic_contents'


class PsychomatrixAdditionalContent(models.Model):
    code = models.CharField(
        max_length=55,
        unique=True,
        null=False,
        blank=False
    )
    title = models.CharField(
        max_length=55,
        null=True,
        blank=True
    )
    annotation = models.CharField(
        max_length=4096,
        null=True,
        blank=True
    )
    level = models.IntegerField(
        null=True,
        blank=True
    )
    text = models.CharField(
        max_length=10240,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.level if self.level else '-'} {self.title}"

    class Meta:
        db_table = 'psychomatrix_additional_contents'
