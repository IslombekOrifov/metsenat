from enum import Enum


class StudentType(Enum):
    b = 'Bakalavr'
    m = "Magistr"

    @classmethod
    def choices(cls):
        return ((_.name, _.value) for _ in cls)