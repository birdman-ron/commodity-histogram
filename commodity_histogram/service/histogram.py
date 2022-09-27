from repository.models import Projection
from repository.dao import read_from_column

def field_count_aggregate(column_name: str):
    values = read_from_column(column_name)

    result_aggregate = {}

    for row in values:
        if row[0] not in result_aggregate:
            result_aggregate[row[0]] = 1
        else:
            result_aggregate[row[0]] += 1

    return {k: v for k, v in sorted(result_aggregate.items(), key=lambda item: item[1])}


def available_column_names_for_route():
    return [v for v in Projection.__dict__.keys() if not v.startswith('_')]
