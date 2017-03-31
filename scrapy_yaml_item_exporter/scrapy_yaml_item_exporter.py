import yaml
from scrapy.exporters import BaseItemExporter
from scrapy.utils.python import to_bytes


class YAMLItemExporter(BaseItemExporter):

    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file = file

    def export_item(self, item):
        data = [dict(item)]
        self.file.write(to_bytes(yaml.safe_dump(data)))
