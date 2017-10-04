
import subprocess

from talktome import settings
from talktome.services import abstractservice


APPLESCRIPT_PATH = settings.SERVICES / "imessage" / "sendText.applescript"


def send_message(to_number, message):
    proc = subprocess.Popen(["osascript", "-l", "JavaScript", APPLESCRIPT_PATH, to_number, message])
    return proc


class iMessageService(abstractservice.AbstractService):
    NAME = "iMessage"

    def __init__(self):
        self.history = []
        self.outbound = []

    def send_message(self, contact, message):
        to_number = iMessageService.get_service_contact(contact)
        proc = send_message(to_number, message)
        self.outbound.append(proc)
        return proc

    def get_message_history(self, contact):
        raise NotImplementedError()

    def get_unread_messages(self, contact):
        raise NotImplementedError()

    def get_last_message_delivered(self, contact):
        raise NotImplementedError()
