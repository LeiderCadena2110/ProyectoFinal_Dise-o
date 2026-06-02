from datetime import datetime


class Notification:
    def __init__(self, notification_id, content, recipient, sent_date=None):
        self.__id = notification_id
        self.__content = content
        self.__recipient = recipient
        self.__sent_date = sent_date if sent_date else datetime.now()
        self.__read = False

    def get_id(self):
        return self.__id

    def get_content(self):
        return self.__content

    def get_recipient(self):
        return self.__recipient

    def get_sent_date(self):
        return self.__sent_date

    def is_read(self):
        return self.__read

    def mark_as_read(self):
        self.__read = True

    def __str__(self):
        return f"Notification for {self.__recipient.get_name()}: {self.__content}"
