
import abc


class AbstractService(abc.ABC):
    NAME = None

    @classmethod
    def get_service_contact(cls, contact):
        if cls.NAME in contact:
            return contact[cls.NAME]

    @abc.abstractmethod
    def send_message(self, contact):
        pass

    @abc.abstractmethod
    def get_message_history(self, contact):
        pass

    @abc.abstractmethod
    def get_unread_messages(self, contact):
        pass

    @abc.abstractmethod
    def get_last_message_delivered(self, contact):
        pass
