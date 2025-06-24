import os
from jinja2 import Environment, FileSystemLoader
from shop_hopper.savers.saver import Saver


class HTMLSaver(Saver):
    def __init__(self):
        templates_dir = self.__class__._get_templates_dir()
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        self.template = self.env.get_template('report_template.html')

    def save(self, data, query, logger, output_dir='.'):
        path_to_save = self._build_file_path(query, output_dir, 'html')

        html_content = self.template.render(query=query, data=data)

        try:
            with open(path_to_save, 'w', encoding='utf-8') as f:
                f.write(html_content)

            logger.debug(f'Data saved to {path_to_save}')
            return path_to_save
        except OSError as e:
            logger.error(f'File save error: {e}')

    @staticmethod
    def _get_templates_dir():
        base_dir = os.path.dirname(os.path.dirname(__file__))
        templates_dir = os.path.join(base_dir, 'templates')
        return templates_dir
