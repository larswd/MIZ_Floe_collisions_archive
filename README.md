# MIZ Floe collisions archive
Data archive for the data discussed in _Direct in-situ observations of wave-induced floe collisions in the deeper Marginal Ice Zone_, link to paper: https://www.sciencedirect.com/science/article/pii/S0165232X25002253
with a preprint at: https://arxiv.org/abs/2404.02750

If you plan to use this data, please remember to cite using either:
```Dreyer, L. W., Rabault, J., Jensen, A., Dæhlen, I., Kristoffersen, Y., Breivik, Ø., & Hope, G. (2025). Direct in-situ observations of wave-induced floe collisions in the deeper Marginal Ice Zone. Cold Regions Science and Technology, 104642.```

or with bibtex:

```
@article{dreyer2025direct,
  title={Direct in-situ observations of wave-induced floe collisions in the deeper Marginal Ice Zone},
  author={Dreyer, Lars Willas and Rabault, Jean and Jensen, Atle and D{\ae}hlen, Ingrid and Kristoffersen, Yngve and Breivik, {\O}yvind and Hope, Gaute},
  journal={Cold Regions Science and Technology},
  pages={104642},
  year={2025},
  publisher={Elsevier}
}
```

The IMU data used in the article is contained in its entirety in the data folder. The recovered data was originally encoded, and decoded from binary using the decoder written by Jean Rabault at the following github repository: https://github.com/jerabaul29/LoggerWavesInIce/tree/master/Logger_GPS_SD_VN_Binary_output_Parser. More info about the logger and the data can be found in the parent directory at https://github.com/jerabaul29/LoggerWavesInIce/tree/master. 

To run the jupyter notebook, which generates all the figures used in the paper (with the exception of the situation maps, that file will be up shortly), you need some dependencies. These are ```Scipy```, ```Numpy```, ```pandas```, ```matplotilb```. To install these using conda, you can first install anaconda by following the instruction for your operating system here: https://www.anaconda.com/docs/getting-started/anaconda/install#linux-installer Then, simply write
```bash
conda create -n inSituCollisions scipy numpy pandas matplotlib
```
To create a python kernel for the notebook file (```make_plots.ipynb```). This kernel should now be available to be selected when running the notebook, which can be run (for example) inside the text editor [Visual Studio Code](https://code.visualstudio.com/) with the Jupyter extension.
  


### License
Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
