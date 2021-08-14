from rest_framework import serializers

from questionnaire.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'uuid',
            'title',
            'text',
            'questionnaire'
        )
        read_only_fileds = ('created_at', 'updated_at')
