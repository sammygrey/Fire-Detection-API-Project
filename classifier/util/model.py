import hashlib
import os
from typing import Dict
from tensorflow import keras


class ModelUtility:
    def __init__(self, config: Dict[str, str]):
        """
        Instaniates a new object using data needed to load in the model.

        Args:
        config(dict): contains the following fields of interest:
            base_model_url(str): the base url where the files are located
            model_file_paths(list): collection of all the files needed to
                                         eventually load the model
            model_sha256(str): the supposed hash of one of the files
                               we need to download. Checked against the
                               one we may already have in the codebase.
        """
        self.url = config["base_model_url"]
        self.file_paths = config["model_file_paths"]
        self.file_sha256 = None
        if config["model_sha256"] is not None:
            self.file_sha256 = config["model_sha256"]

    @classmethod
    def reconstruct_model(cls, config):
        """Make a new instance, and load in the model straightaway."""
        model_utility = cls(config)
        # detect save format
        save_format = "composite"
        if config["model_file_paths"] and len(config["model_file_paths"]) == 1:
            save_format = "h5"
        # load the model
        return model_utility.load_model(save_format)

    def get_hash(self, filename):
        """
        Computes the SHA256 hash of a given file.

        This can then be used to ensure the model file(s) downloaded
        in this codebase are not corrupted.

        Args:
            filename(str): the name of the file

        Returns:
            bytes-like object
        """
        sha256_hash = hashlib.sha256()
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        return sha256_hash.hexdigest()

    def download_model(self):
        """
        Downloads the model files.

        This will first check if the files are already present,
        and not corrupted, before downloading from the address
        specified in config.yaml.

        Returns:
            None
        """
        # TODO: Check if each file present in self.file_paths is already on disk,
        #       and that its sha256 hash is the same as the one found in app/config.yaml.
        # TODO: If the file IS PRESENT, then just log that it already exists, via a print() call.
        # TODO: If the file is NOT PRESENT, then download it.
        #       Hint: read the docs on the tf.keras.utils.get_file function,
        #             and make sure you add whatever directory you're saving the 
        #             model files to the .gitignore file!!

    def load_model(self, format="composite"):
        """
        Model reconstruction.

        This will first load the model in memory using the given files
        and save format

        Args:
            format(str): currently this only supports 'composite'
                        (which is for when the model is saved using a H5 + JSON)
                        or 'h5' as the save format of the model.

        Returns:
            keras.Model object
        """

        def _model_from_composite_format():
            """Specific to using H5 + JSON as the save format"""
            params_file, layers_file = self.file_paths
            # TODO: load the model in memory, using the layers specified in the JSON file
            # TODO: load in the weights and biases of the model, using the parameters file
            # TODO: return the new model object

        def _model_from_h5():
            """Specific to using a single Hadoop(H5) file"""
            params_file = self.file_paths[0]
            # TODO: use the tf.keras.models module to instaniate a new Keras model object 
            #       from the H5 file
            # TODO: return the new model object

        # First download the model, if needed
        self.download_model()
        # load the model in memory
        if format == "composite":
            return _model_from_composite_format()
        else:  # assuming a single H5
            return _model_from_h5()
