import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from shop_hopper.savers.saver import Saver


class HTMLSaver(Saver):
    def __init__(self):
        template_dir = os.path.dirname(__file__)
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template('report_template.html')

    def save(self, data, query, logger, output_dir='.'):
        timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M")
        filename = f"{'_'.join(query.lower().split())}_{timestamp}.html"
        full_filename = os.path.join(output_dir, filename)

        html_content = self.template.render(query=query, data=data)

        with open(full_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        logger.info(f'Data saved to {full_filename}')
