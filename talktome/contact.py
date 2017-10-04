
class Contact:

    def __init__(self, name, ids=None):
        self._service_contacts = {}
        self.name = name
        if ids:
            for (service, contact_id) in ids.items():
                self[service] = contact_id

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f"Service already exists in contact: {repr(key)}")
        self._service_contacts[key] = value

    def __getitem__(self, key):
        return self._service_contacts[key]

    def __delitem__(self, key):
        del self._service_contacts[key]

    def __contains__(self, key):
        return key in self._service_contacts
