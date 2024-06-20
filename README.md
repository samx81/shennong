# Shennong

[![Build Status](https://api.travis-ci.org/bootphon/shennong.svg?branch=master)](
https://travis-ci.org/bootphon/shennong)
[![codecov](https://codecov.io/gh/bootphon/shennong/branch/master/graph/badge.svg)](
https://codecov.io/gh/bootphon/shennong)
[![Anaconda-Server Badge](https://anaconda.org/coml/shennong/badges/version.svg)](
https://anaconda.org/coml/shennong)

### A Python toolbox for speech features extraction

Shennong provides a wide range of speech features extraction algorithms as well
as post-processing pipelines. It relies on [Kaldi](https://kaldi-asr.org) for
most of the algorithms while providing simple to use **Python API** and
**command line interface**.

* See the complete documentation at https://docs.cognitive-ml.fr/shennong.

* See the detailed installation procedure
  [here](https://docs.cognitive-ml.fr/shennong/installation.html). On
  Linux, simply have a:
  ```bash
  # https://anaconda.org/samx81/ezai-pykaldi
  # build by using https://github.com/samx81/pykaldi-conda-package
  conda install samx81::ezai-pykaldi  -c intel -c conda-forge

  # To avoid `'GLIBCXX_3.4.XX' not found`
  conda install -c conda-forge libstdcxx-ng=12
  # or download from https://anaconda.org/conda-forge/libstdcxx-ng/files cuz conda solving sometimes sucks

  pip install -r requirements.txt
  pip install wheel/shennong-1.0-py3-none-any.whl
  ```

* Implementented models include filterbanks, MFCC, PLP, bottleneck, pitch,
  delta, CMVN, VAD, VTLN. See the complete list of available features
  [here](https://docs.cognitive-ml.fr/shennong/intro_features.html).

* To reference Shennong in your own work, please cite the following [Behavior Research Methods paper](https://doi.org/10.3758/s13428-022-02029-6) which is also available on [arXiv](https://arxiv.org/pdf/2112.05555.pdf):

```bibtex
@article{bernard2023shennong,
  title = {Shennong: {{A Python}} Toolbox for Audio Speech Features Extraction},
  author = {Bernard, Mathieu and Poli, Maxime and Karadayi, Julien and Dupoux, Emmanuel},
  year = {2023},
  journal = {Behavior Research Methods},
  url = {https://doi.org/10.3758/s13428-022-02029-6},
  doi = {10.3758/s13428-022-02029-6},
}
```
