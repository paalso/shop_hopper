import json
from shop_hopper.savers.saver import Saver


class JSONSaver(Saver):
    def save(self, data, query, logger, output_dir='.'):
        path_to_save = self._build_file_path(query, output_dir, 'json')

        try:
            with open(path_to_save, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            logger.info(f'Data saved to {path_to_save}')
            return path_to_save
        except OSError as e:
            logger.error(f'File save error: {e}')
