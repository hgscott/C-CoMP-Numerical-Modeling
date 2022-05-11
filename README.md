# C-CoMP-Numerical-Modeling

## How to use the included conda environment
A conda environment can be used to manage the packages needed for this project.

To create the conda environment from the included `environment.yml` file, use:

```conda env create -f environment.yml```

To verify that the new environment was installed correctly, type

```conda env list```

And check that there is an environment called ccomp-cobrapy in the list

To activate the environment, use

```conda activate ccomp-cobrapy```

If there is a package that needs to be added to the conda enviornment, install that package while the environment is activated and create a new `environment.yml` file with

```conda env export > environment.yml```

You can then push your branch and open a merge request so that all other users have your updated package information.


