from src.config.db_config import db

class BaseMixin:
    @classmethod
    def add_and_commit(cls, new_instance):
        """
        Add a new instance to the session and commit the transaction.
        """
        db.session.add(new_instance)
        db.session.commit()

    @classmethod
    def add_only(cls, new_instance):
        """
        Only Add a new instance to the session for the transaction.
        """
        db.session.add(new_instance)
    @classmethod
    def commit_only(cls):
        """
        Only commit the session for the transaction.
        """
        db.session.commit()
