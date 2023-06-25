# End-To-End-BostonHousePricing

This repository contains the code and resources for the End-To-End-BostonHousePricing project.

## Project Description

The End-To-End-BostonHousePricing project is a machine learning project that aims to predict house prices in the Boston area using a linear regression model. It provides a web app interface where users can input the required parameters, and the model will generate a predicted price based on those inputs.

The project is implemented in Python using [Flask](https://flask.palletsprojects.com/) framework for the web app and [scikit-learn](https://scikit-learn.org/stable/) library for the machine learning model. It also utilizes Docker for containerization and [GitHub Actions](https://github.com/features/actions) for continuous integration.

## Project Structure

The repository has the following structure:

- [.github/workflows](.github/workflows): Contains GitHub Actions workflow configuration files.
- [templates](templates): Contains HTML templates for the web app.
- [.gitignore](.gitignore): Specifies the files and directories that should be ignored by Git.
- [Dockerfile](Dockerfile): Defines the Docker image configuration for the project.
- [LICENSE](LICENSE): Specifies the license terms for the project.
- [Linear_Regression_ML_Implementation.ipynb](Linear_Regression_ML_Implementation.ipynb): Jupyter Notebook containing the implementation of the linear regression machine learning model.
- [Procfile](Procfile): Specifies the command to run the web app in a Heroku environment.
- [README.md](README.md): This file, providing an overview of the project.
- [app.py](app.py): Python script that defines the Flask web app.
- [linear_regression_ml_implementation.py](linear_regression_ml_implementation.py): Python script containing the implementation of the linear regression model.
- [regmodel.pkl](regmodel.pkl): Pickled file storing the trained linear regression model.
- [requirements.txt](requirements.txt): Lists the required Python packages and their versions.
- [scaling.pkl](scaling.pkl): Pickled file storing the data scaling parameters.

## Software and Tools Requirements

To run and contribute to this project, you need the following software and tools:

- [GitHub Account](https://github.com/): Sign up for a GitHub account if you don't have one.
- [Heroku Account](https://www.heroku.com/): Create a Heroku account for deploying the web app.
- [VSCode IDE](https://code.visualstudio.com/): Install Visual Studio Code or any preferred IDE for code editing.
- [Git CLI](https://git-scm.com/): Install Git command-line interface for version control.

## Setup Instructions

To set up the project environment, follow these steps:

1. Create a new environment using conda:

   ```shell
   conda create -p venv python==3.7 -y
   ```

2. Activate the environment:

   ```shell
   conda activate venv
   ```

3. Install the required packages:

   ```shell
   pip install -r requirements.txt
   ```

4. Start the Flask web app:

   ```shell
   python app.py
   ```

5. Access the web app by opening the provided URL in a web browser.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore the code, contribute, and use it as a reference for your own projects.

---

_This project is part of the End-To-End-BostonHousePricing series by Mahmoud Nasser. Visit the [main repository](https://github.com/nasserml/End-To-End-BostonHousePricing) for more projects and resources._
