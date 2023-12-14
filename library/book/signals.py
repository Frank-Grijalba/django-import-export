from django.dispatch import receiver
from import_export.signals import post_import, post_export


@receiver(post_import, dispatch_uid="balabala...")
def _post_import(model, **kwargs):
    # model is the actual model instance which after import
    pass


@receiver(post_export, dispatch_uid="balabala...")
def _post_export(model, **kwargs):
    # model is the actual model instance which after export
    pass
