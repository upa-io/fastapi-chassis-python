from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Utils:

    @staticmethod
    def generate_current_datetime() -> str:
        """Genera la fecha y hora actual en formato ISO."""
        return datetime.now().isoformat()
    
    @staticmethod
    def days_between_dates(date1: datetime, date2: datetime) -> int:
        """Calcula la diferencia en días entre dos fechas."""
        return abs((date2 - date1).days)

    @staticmethod
    def string_to_datetime(date_string: str, date_format: str = "%Y-%m-%d") -> datetime:
        """Convierte una cadena de texto a un objeto datetime según el formato dado."""
        return datetime.strptime(date_string, date_format)

    @staticmethod
    def get_first_day_of_month(date: datetime = datetime.now()) -> datetime:
        """Obtiene el primer día del mes para una fecha dada."""
        return date.replace(day=1)

    @staticmethod
    def get_last_day_of_month(date: datetime = datetime.now()) -> datetime:
        """Obtiene el último día del mes para una fecha dada."""
        return date.replace(day=1) + relativedelta(months=1) - timedelta(days=1)
