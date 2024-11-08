import json
import os
from datetime import datetime
from shop_hopper.savers.saver import Saver


class JSONSaver(Saver):
    def save(self, data, query, logger, output_dir='.'):
        timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M")
        filename = f"{'_'.join(query.lower().split())}_{timestamp}.json"
        full_filename = os.path.join(output_dir, filename)

        with open(full_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        logger.info(f'Data saved to {full_filename}')
