from django.core.validators import RegexValidator


validate_phone = RegexValidator(
    regex=r'^[+]998\d{9}$',
    message="""
        Telefon raqam: 13 ta belgidan iborat bolishi kerak. P.s: +998912345678
    """
)


