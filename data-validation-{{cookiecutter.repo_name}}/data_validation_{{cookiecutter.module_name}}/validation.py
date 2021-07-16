"""
{{cookiecutter.name|title}} - data validation.
"""
from osiris.validation.data_validation import DataValidation
from osiris.core.azure_client_authorization import ClientAuthorization
from osiris.core.configuration import ConfigurationWithCredentials
import pandas as pd
import requests

configuration_credentials = ConfigurationWithCredentials(__file__)
credentials_config = configuration_credentials.get_credentials_config()


class Validate{{cookiecutter.class_name}}(DataValidation):
    def read_from_source(self, **kwargs):
        """
        Read data from {{cookiecutter.name|title}} source.
        """
        df = pd.DataFrame()

        return df

    def read_from_destination(self, **kwargs):
        """
        Read data from {{cookiecutter.name|title}} Egress endpoint.
        """
        tenant_id = credentials_config['Authorization']['tenant_id']
        client_id = credentials_config['Authorization']['client_id']
        client_secret = credentials_config['Authorization']['client_secret']

        credentials = ClientAuthorization(tenant_id, client_id, client_secret)

        url = '<URL>'
        token = credentials.get_access_token()
        res = requests.get(url, headers={'Authorization': token})
        df = pd.DataFrame(res.json())

        return df


validate_{{cookiecutter.module_name}} = Validate{{cookiecutter.class_name}}()
df_source = validate_{{cookiecutter.module_name}}.read_from_source()
df_destination = validate_{{cookiecutter.module_name}}.read_from_destination()

validate_column_names = validate_{{cookiecutter.module_name}}.validate_column_names(df_source, df_destination)
validate_number_of_columns = validate_{{cookiecutter.module_name}}.validate_number_of_columns(df_source, df_destination)
validate_number_of_rows = validate_{{cookiecutter.module_name}}.validate_number_of_rows(df_source, df_destination)

print(validate_column_names)
print(validate_number_of_columns)
print(validate_number_of_rows)
