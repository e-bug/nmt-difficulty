# Measuring Neural Translation Difficulty by Cross-Mutual Information
This is the implementation of the approaches described in the paper:
> Emanuele Bugliarello, Sabrina J. Mielke, Antonios Anastasopoulos, Ryan Cotterell and Naoaki Okazaki. It’s Easier to Translate *out of* English than *into* it: Measuring Neural Translation Difficulty by Cross-Mutual Information. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, July 2020.

## Requirements
You can clone this repository with submodules included issuing: `git clone --recurse-submodules git@github.com:e-bug/nmt-difficulty`

The requirements can be installed by setting up a conda environment: <br>
`conda env create -f environment.yml` followed by `source activate nmt`

## Data Preparation
The pre-processing steps to generate our data sets are as follows:
1. `cd scripts/data`
2. `./download_data.sh`
3. `./preprocess_data.sh`
4. `./binarize.sh` (for Fairseq)

You may want to update the default data directories used in the provided files.

## Training and Evaluation
Scripts for training and evaluating each model are provided in [`scripts/experiments`](scripts/experiments).
You can easily run these scripts for each experiment by entering its directory (e.g. [`experiments/en2de`](experiments/en2de)) and running the corresponding script (e.g. `./test.sh`).

Note that we trained our models on a SGE cluster but we also provide the associated Bash file (e.g. [`train_mt.sh`](scripts/experiments/train_mt.sh)).

## Description of this repository
- `experiments/`<br>
  Contains the following scripts to train and evaluate each model: 
  - `train.sh`: train the LM/MT model
  - `valid.sh`: validate the model
  - `test.sh`: test the model
  - `xmi_valid.sh` (MT only): evaluate XMI on the validation set
  - `xmi_test.sh` (MT only): evaluate XMI on the test set 

- `fairseq-0.6.2/`<br>
  Our code is based on [Fairseq](https://github.com/pytorch/fairseq) (version 0.6.2).
  Here, we introduce the following two files to evaluate our approximation of the cross-entropy of a model:
  - [`eval_lm.py`](fairseq-0.6.2/eval_lm.py)
  - [`eval_mt.py`](fairseq-0.6.2/eval_mt.py)

- `results/`: collects CSV files aggregating the values of each evaluated metric
  
- `scripts/`: main scripts, divided into the following subdirectories (you may want to update data and checkpoints directories in these files):
  - `data/`: contains scripts for data generation
  - `experiments/`: contains scripts for training and evaluating models
  - `results/`: contains scripts to generate the CSV files in `results/` as well as correlation coefficients and our bar plot.

- `tools/`: third-party software (i.e. Moses and BPE)

## License
This work is licensed under the MIT license. See [`LICENSE`](LICENSE) for details. 
Third-party software and data sets are subject to their respective licenses. <br>
If you find our code/models or ideas useful in your research, please consider citing the paper:
```
@inproceedings{bugliarello-etal-2020-measuring,
  title={It’s Easier to Translate out of {E}nglish than into it: {M}easuring Neural Translation Difficulty by Cross-Mutual Information},
  author={Bugliarello, Emanuele and Mielke, Sabrina J. and Anastasopoulos, Antonios and Cotterell, Ryan and Okazaki, Naoaki},
  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  month={jul},
  year={2020},
  publisher={Association for Computational Linguistics},
}
```
