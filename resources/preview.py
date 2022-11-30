class Preview:

    def __init__(self, preview_dict:dict):
        self._parent_name = preview_dict.get("-parent_name-", None)
        self._child_name = preview_dict.get("-child_name-", None)
        self._title = preview_dict.get("-parent_name-", None) + " - " + preview_dict.get("-child_name-", None)
        self._email = preview_dict.get("-email-", None)
        self._phone = preview_dict.get("-phone-", None)
        self._preclass = preview_dict.get("-preclass-", None)
        self._pre1a = preview_dict.get("-pre1a-", None)
        self._pre1b = preview_dict.get("-pre1b-", None)
        self._pre2a = preview_dict.get("-pre2a-", None)
        self._pre2b = preview_dict.get("-pre2b-", None)
        self._pre3a = preview_dict.get("-pre3a-", None)
        self._pre3b = preview_dict.get("-pre3b-", None)
        self._notes = preview_dict.get("-notes-", None)
        self._followup = preview_dict.get("-followup-", None)


    ################################################################


    # Getters and Setters
    @property
    def parent_name(self):
        return self._parent_name
    @parent_name.setter
    def parent_name(self, value):
        self._parent_name = value

    @property
    def child_name(self):
        return self._child_name
    @child_name.setter
    def child_name(self, value):
        self._child_name = value

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def preclass(self):
        return self._preclass
    @preclass.setter
    def preclass(self, value):
        self._preclass = value

    @property
    def pre1a(self):
        return self._pre1a
    @pre1a.setter
    def pre1a(self, value):
        self._pre1a = value

    @property
    def pre1b(self):
        return self._pre1b
    @pre1b.setter
    def pre1b(self, value):
        self._pre1b = value

    @property
    def pre2a(self):
        return self._pre2a
    @pre2a.setter
    def pre2a(self, value):
        self._pre2a = value

    @property
    def pre2b(self):
        return self._pre2b
    @pre2b.setter
    def pre2b(self, value):
        self._pre2b = value

    @property
    def pre3a(self):
        return self._pre3a
    @pre3a.setter
    def pre3a(self, value):
        self._pre3a = value

    @property
    def pre3b(self):
        return self._pre3b
    @pre3b.setter
    def pre3b(self, value):
        self._pre3b = value

    @property
    def notes(self):
        return self._notes
    @notes.setter
    def notes(self, value):
        self._notes = value

    @property
    def followup(self):
        return self._followup
    @followup.setter
    def followup(self, value):
        self._followup = value


    ################################################################


    def set_values(self, parent_name: str = '', child_name: str = '', email: str = '', phone: str = '', preclass: str = '', pre1a: str = '', pre1b: str = '', pre2a: str = '', pre2b: str = '', pre3a: str = '', pre3b: str = '', notes: str = '', followup: str = ''):
        self.parent_name = parent_name
        self.child_name = child_name
        self.title = parent_name + " - " + child_name
        self.phone = phone
        self.email = email
        self.preclass = preclass
        self.pre1a = pre1a
        self.pre1b = pre1b
        self.pre2a = pre2a
        self.pre2b = pre2b
        self.pre3a = pre3a
        self.pre3b = pre3b
        self.notes = notes
        self.followup = followup


    # Takes values and returns a dict for use in writing to json file.
    def unpack(self):
        return {
            "-parent_name-": self.parent_name,
            "-child_name-": self.child_name,
            "-email-": self.email,
            "-phone-": self.phone,
            "-preclass-": self.preclass,
            "-pre1a-": self.pre1a,
            "-pre1b-": self.pre1b,
            "-pre2a-": self.pre2a,
            "-pre2b-": self.pre2b,
            "-pre3a-": self.pre3a,
            "-pre3b-": self.pre3b,
            "-notes-": self.notes,
            "-followup-": self.followup
        }