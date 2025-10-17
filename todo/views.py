from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Start with only the logged-in user's todos
        queryset = Todo.objects.filter(user=self.request.user)

        # Optional filtering by status from query params
        status = self.request.query_params.get('status')
        if status is not None:
            if status.lower() in ['true', '1']:
                queryset = queryset.filter(status=True)
            elif status.lower() in ['false', '0']:
                queryset = queryset.filter(status=False)

        return queryset

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the owner
        serializer.save(user=self.request.user)
