from django.db import models

class HelpDeskQuery(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Query from {self.name} ({'Resolved' if self.is_resolved else 'Pending'})"
