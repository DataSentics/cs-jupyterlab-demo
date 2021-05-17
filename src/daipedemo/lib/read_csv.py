import pandas as pd
from injecta.container.ContainerInterface import ContainerInterface
from daipecore.function.input_decorator_function import input_decorator_function


@input_decorator_function
def read_csv(path: str, **kwargs):
    def wrapper(container: ContainerInterface):
        return pd.read_csv(path, **kwargs)

    return wrapper
