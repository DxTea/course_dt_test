from json import dumps

from django.http import HttpResponse, JsonResponse

from app.internal.transport.bot_answers import for_response as users_answers

from app.internal.services.user_service import find_user


def me_endpoint(request, telegram_id: int):
    user = find_user(telegram_id)
    if user is None:
        return JsonResponse({'error': 'User not found'}, status=404)
    answer = users_answers.me(user)
    return JsonResponse(answer, status=200,
                        json_dumps_params={'ensure_ascii': False})
