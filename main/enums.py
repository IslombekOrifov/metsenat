from enum import Enum


class SponsorStatus(Enum):
    n = 'Yangi'
    m = 'Moderatsiyada'
    a = 'Tasdiqlangan'
    r = 'Bekor qilingan'

    @classmethod
    def choices(cls):
        return ((_.name, _.value) for _ in cls)


class PayType(Enum):
    n = 'Naqt'
    s = "Pul o'tkazish"
    c = 'Chek'

    @classmethod
    def choices(cls):
        return ((_.name, _.value) for _ in cls)
    

class StudentType(Enum):
    b = 'Bakalavr'
    m = "Magistr"

    @classmethod
    def choices(cls):
        return ((_.name, _.value) for _ in cls)