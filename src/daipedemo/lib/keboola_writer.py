import pandas as pd
from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from daipecore.decorator.OutputDecorator import OutputDecorator
from injecta.container.ContainerInterface import ContainerInterface


@DecoratedDecorator
class keboola_writer(OutputDecorator):  # noqa: N801
    def __init__(self, path: str, **kwargs):
        self.__path = path
        self.__kwargs = kwargs

    def process_result(self, result: pd.DataFrame, container: ContainerInterface):
        result.to_csv(self.__path, **self.__kwargs)
