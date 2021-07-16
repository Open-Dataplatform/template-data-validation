"""
Example data - data validation.
"""
from osiris.validation.data_validation import DataValidation
import pandas as pd


class ValidateExampleData(DataValidation):
    """
    Implements DataValidation methods.
    """
    def read_from_source(self, **kwargs):
        """
        Read data from Example data source.
        """
        df = pd.read_excel('example_data_source.xlsx', engine='openpyxl')

        return df

    def read_from_destination(self, **kwargs):
        """
        Read data from Example data destination.
        """
        df = pd.read_excel('example_data_destination.xlsx', engine='openpyxl')

        return df


validate_example_data = ValidateExampleData()

df_source = validate_example_data.read_from_source()
df_destination = validate_example_data.read_from_destination()

validate_column_names = validate_example_data.validate_column_names(df_source, df_destination)
validate_number_of_columns = validate_example_data.validate_number_of_columns(df_source, df_destination)
validate_number_of_rows = validate_example_data.validate_number_of_rows(df_source, df_destination)

print(validate_column_names)
print(validate_number_of_columns)
print(validate_number_of_rows)
