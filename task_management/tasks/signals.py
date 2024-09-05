from django.db.models.signals import post_save , post_migrate
from django.contrib.auth.models import Group , Permission
from django.dispatch import receiver
from tasks.models import Task
from .tasks import send_task_notification
from users.models import User

@receiver(post_save, sender=Task)
def task_completed(sender, instance, **kwargs):
    if instance.completed:
        send_task_notification.delay(instance.id)


@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    project_manager_group, created = Group.objects.get_or_create(name='Project Manager')
    if created:
        project_manager_permissions = [
            Permission.objects.get(codename='add_project'),
            Permission.objects.get(codename='change_project'),
            Permission.objects.get(codename='add_task'),
            Permission.objects.get(codename='change_task'),
            Permission.objects.get(codename='delete_project'),
            Permission.objects.get(codename='delete_task'),
        ]
        project_manager_group.permissions.set(project_manager_permissions)
        
    developer_group , created = Group.objects.get_or_create(name='Developer')
    if created:
        developer_permissions = [
            Permission.objects.get(codename='update_task')
        ]
        developer_group.permissions.set(developer_permissions)