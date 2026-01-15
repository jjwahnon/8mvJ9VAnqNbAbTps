from datetime import date
import datetime
import unittest



def find_open_late_offences(
        late_crime_data: list[dict[str, str]],
        cutoff_date: date,
    ) -> list[dict[str, str]]:
    """Find offences that are still open and were received after a cutoff date.

    Args:
        late_crime_data (list[dict[str, str]]): A list of dictionaries representing late crime data.
        cutoff_date (date): A date representing the cutoff date.

    Returns:
        A list of dictionaries representing open late offences.

    Raises:
        ValueError: If the cutoff date is in the future.
    """

    if cutoff_date > date.today():
        raise ValueError("Cutoff date cannot be in the future.")

    open_late_offences: list[dict[str, str]] = []
    for offence in late_crime_data:
        if (
            offence["outcome"] == "Under investigation"
            and date.fromisoformat(offence["date"]) > cutoff_date
        ):
            open_late_offences.append(offence)
    return open_late_offences


class TestCase(unittest.TestCase):
    def is_late(self):
        find_open_late_offences(late_offence_data, date(2024, 5, 1))
        self.assertRaises(ValueError)



if __name__=="__main__":
    fun_date= date(2024, 5, 1)
    late_offence_data = [
        {
            "category": "public-order",
            "date": "2024-05-01",
            "outcome": "Closed",
        },
        {
            "category": "public-order",
            "date": "2024-05-02",
            "outcome": "Under investigation",
        },
        ]
    data = find_open_late_offences(late_offence_data, fun_date)
    test=TestCase()
    test.is_late()
 
    pass