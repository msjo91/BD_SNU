# userAcc.py


class UserAcc:
    id_ = 0
    name = ""
    role = 0
    conn = None

    def __init__(self, id_=0, name="", role=0, conn=None):
        self.id_ = id_
        self.name = name
        self.role = role
        self.conn = conn

    def set_attrs(self, id_, name, role, conn):
        """Set user attributes."""
        self.id_ = id_
        self.name = name
        self.role = role
        self.conn = conn


# user account object declaration
user_acc = UserAcc()
