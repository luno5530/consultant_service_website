from django.db import models
from PIL import Image

class Profile(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)
    description = models.TextField(default="To Do")
    image = models.ImageField(default="profile.jpg", upload_to="profile_pics")

    # def save(self, *args, **kwargs):
    #   super().save(*args, **kwargs)
    #   img = Image.open(self.image.path)
    #   width, height = img.size
    #   if not width == height:
    #     size = min(width, height)    
    #     left = (width - size) // 2
    #     top = (height - size) // 2
    #     right = (width + size) // 2
    #     bottom = (height + size) // 2
    #     croped_image = img.crop((left, top, right, bottom))
    #     croped_image.thumbnail((500, 500))
    #   croped_image.save(self.image.path)


    def __str__(self) -> str:
        return f"{self.first_name}\'s profile"