from daipecore.lineage.argument.DecoratorInputFunctionInterface import DecoratorInputFunctionInterface


class ReadCsv(DecoratorInputFunctionInterface):
    def __init__(self, csv_path: str):
        self.__csv_path = csv_path

    @property
    def csv_path(self):
        return self.__csv_path

    @property
    def identifier(self):
        return self.__csv_path
