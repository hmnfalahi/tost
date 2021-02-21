import os

from tost import tost as app

home_directory = os.environ['HOME']
configuration_file_name = f'{home_directory}/.config/tost.yml'

app.configure()
app.initialize_orm()

