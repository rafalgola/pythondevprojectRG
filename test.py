import unittest
from datetime import datetime, timedelta
import os


def was_db_modified_within_last_minute(file_path):
    last_modified_time = os.path.getmtime(file_path)
    last_modified_date = datetime.fromtimestamp(last_modified_time)
    current_time = datetime.now()
    return (current_time - last_modified_date) <= timedelta(minutes=1)


class TestFileModification(unittest.TestCase):
    def test_file_modification_within_last_minute(self):
        db_file_path = r'.\projektzaliczeniowy\db.sqlite3'
        self.assertTrue(was_db_modified_within_last_minute(db_file_path), "DB was not modified lately ...")
