def logger_with_path(log_path):
    def logger(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(log_path, 'a') as log_file:
                log_file.write(f'{datetime.datetime.now()} - {func.__name__} called with args: {args}, kwargs: {kwargs}. Returned: {result}\n')
            return result
        return wrapper
    return logger
