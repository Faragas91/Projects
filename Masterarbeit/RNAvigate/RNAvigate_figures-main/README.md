# RNAvigate figures

This repository contains the processed data and Jupyter notebooks used in the creation of figures for the RNAvigate manuscript.

There are three options to view these notebooks:

1. [Static notebooks][]: loads instantly, no installation required
2. [Interactive notebooks via Binder][]: loads quickly (see disclaimer), no installation required
3. [Interactive notebooks via local installation][]

[Static Notebooks]: #static-notebooks
[Interactive notebooks via Binder]: #interactive-notebooks-via-binder
[Interactive notebooks via local installation]: #interactive-notebooks-via-local-installation

## Static notebooks

View the notebooks as static HTML web pages in your browser.

[figure 1](https://htmlpreview.github.io/?https://github.com/Weeks-UNC/RNAvigate_figures/blob/main/static_notebooks/F1_simple_plots.html),
[figure 2](https://htmlpreview.github.io/?https://github.com/Weeks-UNC/RNAvigate_figures/blob/main/static_notebooks/F2_smCCP_tmRNA.html),
[figure 3](https://htmlpreview.github.io/?https://github.com/Weeks-UNC/RNAvigate_figures/blob/main/static_notebooks/F3_lowSS_DENV.html),
[figure 4](https://htmlpreview.github.io/?https://github.com/Weeks-UNC/RNAvigate_figures/blob/main/static_notebooks/F4_tr-folding_RNaseP.html),
[figure 5](https://htmlpreview.github.io/?https://github.com/Weeks-UNC/RNAvigate_figures/blob/main/static_notebooks/F5_DANCE_add-riboswitch.html),
[figure 6](https://htmlpreview.github.io/?https://github.com/Weeks-UNC/RNAvigate_figures/blob/main/static_notebooks/F6_compare_SARS2.html)

## Interactive notebooks via Binder

Use Binder, a free web service from Project Jupyter, to run the notebooks in a cloud computing environment.

- [Link to RNAvigate_figures at mybinder.org](https://mybinder.org/v2/gh/Weeks-UNC/RNAvigate_figures/HEAD)

#### Instructions:

1. Click on the link above.

Usually, Binder will start up quickly, within a minute.
Binder has limited computational resources and may impose longer wait times.
In my experience, if it takes more than 10 minutes, it is best to try again later.
Once the cloud environment is ready, Jupyter Lab will open in your browser.

2. Navigate to and open an interactive notebook using the left-hand panel (locations below).

```
interactive_notebooks/
├── figure_1/
|   └── F1_simple_plots.ipynb
├── figure_2/
|   └── F2_smCCP_tmRNA.ipynb
├── figure_3/
|   └── F3_lowSS_DENV.ipynb
├── figure_4/
|   └── F4_tr-folding_RNaseP.ipynb
├── figure_5/
|   └── F5_DANCE_add-riboswitch.ipynb
└── figure_6/
    └── F6_compare_SARS2.ipynb
```

3. Hit the double-play button in the top ribbon (restart and run all cells).

The code will run, and figures from the manuscript will be recreated.
Most figures are generated within seconds;
some, especially kernel density estimates, may take a minute.

If a warning appear, but does not prevent the notebook from executing, it can be safely ignored.
If anything prevents the notebooks from executing, please submit a GitHub issue.

## Interactive notebooks via local installation

Download this repository (RNAvigate_figures). In order to run the Jupyter
notebooks, you will need a working RNAvigate installation:

  - [RNAvigate source code](https://github.com/Weeks-UNC/RNAvigate)
  - [RNAvigate documentation](https://rnavigate.readthedocs.io)

In future versions of RNAvigate, syntax changes may prevent these notebooks from
running properly. If that is the case, here is the hard link to the version of
RNAvigate used in these notebooks.

  - [RNAvigate v1.0.0 source code](https://github.com/Weeks-UNC/RNAvigate/tree/f9fa87c25d7232d8dc81b2efee8cd2e9686a7818)
