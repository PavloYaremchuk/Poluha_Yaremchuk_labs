from django.core.exceptions import ObjectDoesNotExist

class BaseRepository:
    model = None

    @classmethod
    def get(cls, pk):
        return cls.model.objects.get(pk=pk)

    @classmethod
    def all(cls):
        return cls.model.objects.all()

    @classmethod
    def create(cls, **kwargs):
        instance = cls.model(**kwargs)
        instance.save()
        return instance

    @classmethod
    def update(cls, pk, **kwargs):
        instance = cls.get(pk)
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @classmethod
    def delete(cls, pk):
        instance = cls.get(pk)
        instance.delete()