"""
MOJ Data Engineering Technical Test
-----------------------------------

In this test you will need to ingest and process data from two different sources.
This data needs to be combined out output into a CSV file for stakeholders.

You may approach the tasks and structure your code as you see fit.

The environment already has the following packages installed and available for use:
- pandas
- requests
- pytest
- unittest

You can complete the full test with the above packages, plus standard library packages.
However, please feel free to use any additional open source packages you feel are appropriate.

You should consider that this code will be maintained and used by other engineers,
stored on GitHub and deployed into a production environment in the cloud.

"""

# Task 1: Setup
# -------------
# A) Create a new branch from main called 'tech-test-{yourname}'


# Task 2: Load and filter the CSV data
# ------------------------------------
# A CSV file containing severity ratings for offences committed in Leicestershire
# has been provided in 'data/crime_severity.csv':
#
# A) Load this data into an appriopriate data structure for processing
#
# Our stakeholders only require data for offences that have:
#       - a category of 'public-order'
#       - a severity of 2 or higher
#
# B) Produce a single dataset containing only the required records


# Task 3: Load and filter API data
# --------------------------------
# Additional data for these offences is available from: https://data.police.uk/docs/.
# The dataset required is:
#       - 'Crimes with no location'
#       - for all crimes
#       - in the month of '2024-03'
#       - for the 'Leicestershire' police force
#
# If you are unable to access the API, the full output has been provided in
# 'data/police_api_data.json' - You may use this file instead.
#
# A) Ingest the required dataset from the correct API endpoint.
#
# Our stakeholders only require data for offences that:
#       - have a category of 'public-order'
#       - have an outcome_status of either 'Unable to prosecute suspect' or 'Court result unavailable'
#
# B) Produce a single dataset containing only the required records


# Task 4: Join and enrich the data
# --------------------------------
# A single output dataset needs to be created with these fields:
#       - id
#       - category
#       - severity
#       - outcome_status_category
#       - month
#
# A) Join the two datasets together correctly into a dataset containing these fields
#
# B) Add an additional field to the dataset which categorises a severity of 2 as 'low',
#    severity of 3 as 'medium' and severity of 4 as 'high'
#
# C) Output the data set as a CSV to 'output/combined_crime_data.csv'


# Task 5: Testing
# ---------------
# A colleague has produced a function to identify cases which were added to the
# system late, and which are stil open. Some sample input data is provided.

# A) Write appropriate unit tests for the function

from datetime import date


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
print(find_open_late_offences(late_offence_data, date(2024, 5, 1)))


# Task 6: Close
# -------------
# A) Commit your code to the branch 'tech-test-{yourname}'
# B) Push the branch to GitHub
