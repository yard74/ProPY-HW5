from datetime import datetime


def logger(log_path):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            f_date = datetime.now().replace(microsecond=0)
            log = [old_function.__name__, f_date, args, kwargs, result]
            with open(log_path, 'a', newline='', encoding='utf-8') as file:
                file.write(
                    f'Функция {log[0]} вызвана {log[1]} с аргументами {log[2]}, {log[3]} и результатом "{log[4]}".\n'
                )
            return result
        return new_function
    return _logger
