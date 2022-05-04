errors = {
  'out': 'Вы вышли из системы',
  'noaccess': 'У вас нет доступа в этот раздел',
  'unknown': 'Неизвестная ошибка',
  'timeout': 'Система долго не отвечает',
  'robot': 'Ваши действия похожи на робота'
}


def get_errors(*args):
    global errors
    return [errors[i] for i in args]


print(get_errors('out', 'noaccess'))
