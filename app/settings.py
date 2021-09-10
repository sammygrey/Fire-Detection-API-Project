import os
from pathlib import Path

# TODO: give some general info about the API
API_TITLE = "TODO"
API_DESCRIPTION = "TODO"
API_VERSION = "TODO"

# STRETCH CHALLENGE: Share metadata about what users can request from the endpoints.
# These are intended shown on the UI, related only to a specific endpoint.
# Note: the value in the "name" field should match what goes in the
#       "tags" parameter of the corresponding app route in main.py!!
API_ENDPOINT_METADATA = (
    {
        "name": "TODO",
        "description": "TODO",
    },
)

# Tells the app how to find the config.yaml (for running ML inference)
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = os.path.join(BASE_DIR, "app", "config.yaml")

# Wraps all the API metadata as one dictionary
API_SETTINGS = {
    "title": API_TITLE,
    "description": API_DESCRIPTION,
    "version": API_VERSION,
    "openapi_tags": API_ENDPOINT_METADATA,
    "predictor_config_path": CONFIG_PATH,
}
