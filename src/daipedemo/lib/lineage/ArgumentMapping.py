from daipecore.lineage.argument.ArgumentMappingInterface import ArgumentMappingInterface
from daipedemo.lib.lineage.ReadCsv import ReadCsv


class ArgumentMapping(ArgumentMappingInterface):
    def get_mapping(self):
        return {
            "read_csv": ReadCsv,
        }
