
# ROME (Rapid Optimizing Methods for Estimation)

![](https://github.com/arennax/rome_icse/blob/master/img/rome.jpg)

## Submission 

Submitted to [International Conference on Software Engineering](https://conf.researchr.org/home/icse-2020).

## Authors

+ Tianpei Xia
  + Computer Science, NC State University, USA 
  + txia4@ncsu.edu
+ Jianfeng Chen
  + Computer Science, NC State University, USA 
  + jchen37@ncsu.edu
+ Rui Shu
  + Computer Science, NC State University, USA 
  + rshu@ncsu.edu
+ Tim Menzies
  + Computer Science, NC State University, USA 
  + timm@ieee.org

## Data

+ [SEACRAFT on Zenodo](https://zenodo.org/communities/seacraft/search?page=1&size=20&q=effort)
+ [COCOMO Style](https://github.com/arennax/rome_icse/tree/master/data/cocomo_style)
+ [Github data](https://github.com/arennax/rome_icse/tree/master/data/github_Qi)

## Source Code

+ [FLASH](https://github.com/arennax/rome_icse/blob/master/experiments/flash0.py)
+ [Optimizers](https://github.com/arennax/rome_icse/blob/master/experiments/optimizers.py)
+ [Estimators](https://github.com/arennax/rome_icse/blob/master/experiments/learners.py)
+ [ROME and DE](https://github.com/arennax/rome_icse/blob/master/experiments/tuned_learners.py)

## Experiment Replication

To reproduce the experiment results, execute `main.py` in directory `experiments`, you need to select specific performance metrics inside `main.py`: `methods = 0` stands for Magnitude of the Relative Error, `methods = 1` stands for SA (Standardized Accuracy). You will get a `.txt` file which stores the numeric experiment results in directory `output`.

To get the scott-knott test results of experiments, execute `sk_stats.py` by typing `cat name.txt| python2 sk_stats.py --text 30 --latex True` (For windows, use `type` instead of `cat`), this will output a latex-friendly scott-knott charts for this specific `.txt` file. The actually output will look like this:

<img width="600" alt="table_V" src="https://github.com/arennax/rome_icse/blob/master/img/sk_temp.png">

Note that `sk_stats.py` in this program currently only supports python 2.7.

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

(BTW, it would be great to hear from you if you are using this material. But that is optional.)

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to http://unlicense.org
  
