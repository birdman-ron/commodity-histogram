from repository.models import Projection

def field_count_aggregate(column_name: str):
    pass

def available_column_names_for_route():
    return [v for v in Projection.__dict__.keys() if not v.startswith('_')]
