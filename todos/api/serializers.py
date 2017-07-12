from rest_framework.serializers import ModelSerializer

from ..models import Todo


class TodoCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            # 'id',
            # 'user',
            'title',
            'text',
            'to_be_completed',
        ]


class TodoDetailSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'user',
            'title',
            'text',
        ]


"""

from todos.models import Todo
from todos.api.serializers import TodoDetailSerializer

data = {
    "title": "Yeah buddy",
    "content": "New content",
    "publish": "2016-2-12",
    "slug": "year-buddy",
}

obj = Todo.objects.get(id=3)
new_item = TodoDetailSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

"""