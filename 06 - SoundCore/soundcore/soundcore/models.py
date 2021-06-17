import string
import random
import functools

from django.contrib.auth.models import User
from django.db import models

from upload.models import MusicList


# Create your models here.


class ShortUrl:
    def __init__(self):
        self.short_letter = self.__short_letter()

    def __short_letter(self) -> str:
        letters = string.ascii_lowercase + string.ascii_uppercase
        rand_letters = random.choices(letters, k=16)
        rand_letters = "".join(rand_letters)
        self.short_letter = rand_letters
        return self.short_letter

    def __does_short_exists(self) -> bool:
        is_true_or_false = LibraryGenerator.objects.filter(
            short_form=self.short_letter
        ).exists()
        if is_true_or_false:
            return True
        elif not is_true_or_false:
            return False

    def logic(self) -> str:
        if not self.__does_short_exists():
            return self.short_letter
        elif self.__does_short_exists():
            self.__short_letter()


class LibraryGenerator(models.Model):
    name = models.CharField(max_length=50)
    musics = models.ManyToManyField(MusicList)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    short_form = models.CharField(max_length=16)

    def count_total_number(self):
        # Anchored to 'soundcore/library/index.html'

        data = LibraryGenerator.objects.values_list("musics__length")
        total_number = 0

        for i in data:
            try:
                __res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
                total_number += round(float(__res), 2)
            except TypeError:
                pass

        return total_number

    # Modify the save option
    def save(self, *args, **kwargs) -> None:
        self.short_form = ShortUrl().logic()
        super(LibraryGenerator, self).save(*args, **kwargs)

    # Return the ID to the admin panel
    def __str__(self) -> str:
        return str(self.name)
