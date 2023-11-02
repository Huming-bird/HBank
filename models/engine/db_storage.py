#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.basemodel import BaseModel, Base
from models.customers import Customer
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Customer": Customer}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBANK_USER = getenv('HBANK_USER')
        HBANK_PASSWD = getenv('HBANK_PWD')
        HBANK_HOST = getenv('HBANK_HOST')
        HBANK_MYSQL_DB = getenv('HBANK_MYSQL_DB')
        HBANK_ENV = getenv('HBANK_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBANK_USER,
                                             HBANK_PASSWD,
                                             HBANK_HOST,
                                             HBANK_MYSQL_DB))
        if HBANK_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """ this method retrieves only one object """
        if cls in classes and isinstance(id, str):
            cls = classes[cls]
            res = self.__session.query(cls).filter(cls.id == id).first()
            return res
        return None

    def count(self, cls=None):
        """this method counts the number of objects in the storage """
        res = 0
        if cls in classes:
            cls = classes[cls]
            res = self.__session.query(cls).count()
        elif cls is None:
            for cls in classes.values():
                res += self.__session.query(cls).count()
        return res
