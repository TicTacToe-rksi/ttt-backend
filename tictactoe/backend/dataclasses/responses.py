class Body:
    USER_ALREADY_EXISTS = {
        'error': 'Пользователь уже существует'
    }

    BAD_REQUEST = {
        'error': 'Неправильный запрос'
    }

    INVALID_FORM_BODY = {
        'error': 'Некорректное тело запроса'
    }

    AUTHORIZED_FALSE = {
        'authorized': False,
    }

    FORBIDDEN = {
        'text': 'Отказано в доступе'
    }

    AUTHORIZED_TRUE = {
        'authorized': True,
    }

    CREATED = {
        'created': True
    }

    NOT_ENOUGH_MONEY = {
        'text': 'Недостаточно средств'
    }

    DELETED = {
        'text': 'Успешно удалено'
    }

    NOT_FOUND = {
        'text': 'Не найдено'
    }


class Status:
    CONFLICT = 409
    BAD_REQUEST = 400
    OK = 200
    CREATED = 201
    DELETED = 204
    UNAUTHORIZED = 401
    INVALID = 422
    FORBIDDEN = 403
    NOT_FOUND = 404
