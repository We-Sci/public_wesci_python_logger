# We-Sci Python Logger

## Introduction
This repo contains instructions and examples of how to use We-Sci's [Python Logger SDK](https://pypi.python.org/pypi/wesci) to curate research done using python, in your We-Sci's private cloud account.

## Current SDK Version
0.4.0

## Python Versions Supported
We're in a closed beta, currently supporting only Python 2.7.9+ and Python 3+ (including Jupyter Notebook), on Mac OS, Linux and Windows 7+.


## Using We-Sci's python logger:
### Installation and Configuration
1. Install We-Sci's pip [package](https://pypi.python.org/pypi/wesci) by running `pip install wesci`
2. Follow the instruction you received in the email and create a a local config file (`echo "<your_api_key> >> ~/.wesci.conf`)

### Initializing
```python
import wesci

logger = wesci.Logger(
    script_file=__file__,
    log_file_prefix="./prefix"
)

### Your script starts here ###
```
The `log_file_prefix` parameter is used to specify the path and possibly the prefix of the local log file.
e.g: (for script named `script.py`)
1. If `log_file_prefix=None` --> log file will be stored at `./script_wesci_log`
1. If `log_file_prefix=prefix` --> log file will be stored at `./prefix_wesci_log`
1. If `log_file_prefix=/log/prefix` --> log file will be stored at `/log/prefix_wesci_log`

### Adding Input/Output Parameters and Files
```python
### Your script inputs ###
a1 = parameter_input
a2 = another_parameter_input

logger.add_input_params({'a1': a1,
                         'a2': a2})
logger.add_input_files({'input_csv': 'input.csv'})

### Your script calculations ###
# ...
# ...
# ...

b1 = some_ground_breaking_research_result
b2 = another_ground_breaking_research_result

logger.add_output_files({'output_csv': 'output.csv'})
logger.add_output_params({'b1': b1,
                          'b2': b2})
```
**Note:** We don't support all variable types yet (e.g: Pandas Data Frame). When an unsupported type is passed as input/output param, a warning will be issued when the code is executed, and the param will be ignored.

### Adding Matplotlib figures ###
After creating a matplotlib figure, capture it by simply add this line to your code:
```
from matplotlib import pyplot 
...
# create a plot of your data
pyplot.plot(your_data)

# add this line to log the current figure
logger.add_output_figure('fig1')
...
```
The logger automatically creates a thumbnail on your local drive and uploads it to our servers when the logging is finalized (see below).
The thumbnail's filename is a unique hash of its content.

### Adding Images ###
_Coming soon..._

### Logging ###
Just before the script exits, or at any point deemed important, insert the following code to log the data fed into the logger:
```python
logger.log()
```
**Note:** Each call to `logger.log()` will record a new assay (experiment/test) - which will be displayed as a separate entity in your timeline on the We-Sci web app.

### Jupyter Notebook support
Everything's basically the same, besides initialization:
```python
logger = wesci.Logger(
    script_file='notebook_file.ipynb',  # Note that you need to specify the notebook's file
                                        # path explicitely!
    log_file_prefix="./prefix"          # the log file will be written to ./prefix_wesci_log.csv
)
```
**Important:** Only the code will be extracted from the notebook, with separation between cells, without images, data tables, etc..
Furthermore, the code is extracted from the **last saved .ipynb file** - not the one currently being evaluated, due to the architecture of Jupyter Notebook. We will be releasing a feature to dynamically capture the code in the near future.


## Examples
You can see usage examples, both for a python script and python notebook at [script_example.py](./script_example.py) and 
[notebook_example.ipynb](./notebook_example.ipynb) respectively.


## Support
We currently maintain three channels for support:
- For Python package related issues - you can open a git-issue.
- For general issues, you can email us at support@we-sci.com.
- For anything else, you can **[join](https://join.slack.com/t/public-wesci-users/shared_invite/MjI1MzQzNDM3MzI4LTE1MDI2NDExNDktNGM1MTIzZTY5MA)** the conversation on our **[Public-We-Sci-Users](https://public-wesci-users.slack.com/)** group on **Slack**.
