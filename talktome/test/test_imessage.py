
import configparser
import subprocess
import unittest

from talktome import contact
from talktome import settings
from talktome.services.imessage import service


TEST_UNKNOWN_NUMBER = {}
TEST_KNOWN_NUMBER = {}


class TestIMessage(unittest.TestCase):

    def test_send_message_ok(self):
        cont = contact.Contact("Name", ids=TEST_KNOWN_NUMBER)
        serv = service.iMessageService()
        try:
            with serv.send_message(cont, "TestIMessage.test_send_message_ok") as proc:
                self.assertEqual(0, proc.wait(timeout=30))
        except subprocess.TimeoutExpired as exc:
            self.fail("test_send_message_ok() timed out!")

    def test_send_message_fail(self):
        cont = contact.Contact("Name", ids=TEST_UNKNOWN_NUMBER)
        serv = service.iMessageService()
        try:
            with serv.send_message(cont, "TestIMessage.test_send_message_fail") as proc:
                self.assertEqual(1, proc.wait(timeout=30))
        except subprocess.TimeoutExpired as exc:
            self.fail("test_send_message_fail() timed out!")


def load_config():
    config = configparser.ConfigParser()
    config.read(str(settings.TEST_CONFIG_PATH))
    TEST_UNKNOWN_NUMBER["iMessage"] = config["test_imessage"]["UnknownNumber"]
    TEST_KNOWN_NUMBER["iMessage"] = config["test_imessage"]["KnownNumber"]


if __name__ == '__main__':
    load_config()
    unittest.main()
