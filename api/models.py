from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published",
                                    auto_now_add=True,
                                    db_index=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              related_name="posts",
                              blank=True,
                              null=True)

    class Meta:
        ordering = ["-pub_date"]


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField("date published", auto_now_add=True)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments",
                             blank=True,
                             null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="comments")


class Follow(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="follower"
                             )
    following = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name="following",
                                  )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "following"],
                                    name="unique_object")
        ]
