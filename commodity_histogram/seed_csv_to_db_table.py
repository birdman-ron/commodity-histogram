import argparse
import csv
import re
from typing import List

from repository.models import Projection
from repository.dao import insert_projections


def check_column_names(column_names: List[str]):
    column_names_to_check = ['Attribute', 'Commodity', 'CommodityType', 'Units', 'YearType', 'Year', 'Value']

    if not column_names == column_names_to_check:
        raise ValueError("Invalid CSV file. Header does not much specification.")


def seed_projection_csv_to_db_table(csv_file: str):
    with open(csv_file, encoding='utf-8-sig') as csv_file_handle:
        csv_reader = csv.reader(csv_file_handle, delimiter=',')
        header = next(csv_reader)
        check_column_names(header)

        projections = []

        bulk_insert_length = 20
        bulk_insert_count = 0

        for row in csv_reader:
            projection = Projection()
            projection.attribute = row[0]
            projection.commodity = row[1]
            projection.commodity_type = row[2]
            projection.units = row[3]
            projection.year_type = row[4]
            projection.year = int(row[5].split('/')[0])
            projection.value = float(row[6])

            projections.append(projection)
            bulk_insert_count += 1

            if bulk_insert_count == bulk_insert_length:
                insert_projections(projections)
                bulk_insert_count = 0
                projections = []

        if len(projections) > 0:
            insert_projections(projections)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This tool imports .csv files into a SQL database table.'
                                                 'It is assumed the .csv file contains a header which will provide '
                                                 'the table column name(s)')

    parser.add_argument('--csv', dest='csv_file', required=True, help="Example: python_csv_to_db_table.py --csv foo.csv")

    args = parser.parse_args()
    seed_projection_csv_to_db_table(args.csv_file)

