# Fire Detection API Project Challenges

In this project, you'll be tasked with designing and developing a neural network that can run in production as a basic image classifier.

To get full credit on this project, you'll have to accomplish at least three major objectives:
- Create at least two image classifier models as discrete versions of your project.
    - First version should comprise a multilayered perceptron-based network.
    - Second version should comprise a convolutional neural network.
- Deploy at least one classifier online and test it with sample image uploads.
- Finish all required objectives and at least 50% of all bonus objectives.

---

For the sake of clarity, all objectives (both required and bonus) will be identified per subdirectory and file.

## 📍 REQUIRED CHALLENGES 📍

1. Save a copy of the `Fire-Detection-Image-Data` to a project subfolder called `dataset`. 

2. Work through the `project/development.ipynb` notebook, solving all required objectives to ensure successful utility of your neural network architectures. 

3. At the end of the `project/development.ipynb` notebook, be sure to **save your models** using the provided model saving functions. 

4. Upload your changes to a new Git repository and **create a new release**. (Don't worry: your model states and dataset should automatically be ignored as long as you followed the correct repository workflow.)

4. After creating a new project release, go to `app/config.yaml` and modify the `model_file_paths`, `base_model_url`, and `model_sha256` parameters. 

- The `model_file_paths` arguments should be the corresponding filename(s) of your saved model states from the final saving function of the development notebook.

- The `base_model_url` argument should be your precise GitHub URL for the current project release download version. 

- The `model_sha256` argument should be a SHA-256 hash that you can get by going to your project releases and clicking on the seven-digit pre-hash key below the release version tag. 

5. 