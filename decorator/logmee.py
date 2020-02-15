"""
    * A good example using decorator showing that we could skip to use
    * importing 'logging' in this in order to use it our main func
    * and import it only in decorator func
"""


def logme(func):
    import logging  # because we don't want to require users to import it
    logging.basicConfig(level=logging.DEBUG)

    def inner():
        logging.debug(f'Called {func.__name__}')
        return func()
    return inner


@logme
def say_hello():
    print('Hi there!')


say_hello()  # logs the call and then prints 'Hi'
