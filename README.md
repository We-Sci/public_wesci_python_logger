# We-Sci Python Logger

## Introduction
This repo contains instructions and examples of how to use We-Sci's [Python Logger package](https://pypi.python.org/pypi/wesci) to auto-curate research done using python, in your We-Sci's private cloud account.

## Current Package Version
0.6.0

## Python Versions Supported
We're in a beta, currently supporting only Python 2.7.9+ and Python 3+ (including Jupyter Notebook), on Mac OS, Linux and Windows 7+. The product is undergoing intensive improvement and enhancement process on a daily basis.


## Using We-Sci's python logger:
### Installation and Configuration
1. If you haven't allready done so - signup to the [web-app](https://app.we-sci.com/#/signup).
2. Install We-Sci's pip [package](https://pypi.python.org/pypi/wesci) by running `pip install wesci`
3. Follow the instructions you've received in the email and create a local config file (`echo "<your_api_key> >> ~/.wesci.conf`)

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

### Logging Params
**Note:** We don't support all variable types yet. When an unsupported type is passed as input/output param, a warning will be issued when the code is executed, and the param will be ignored.
For all supported params types - you'll be able to click on their row in the params table at [app.we-sci.com](https://app.we-sci.com) and see their preview in the bottom preview box.

The logger supports multiple methods for logging your script's params, trading-off between the amount of code needed to start logging and accuracy of logging:

#### Automatically Logging All Global Params
```python
### Your script's parameters and calculations ###
# ...
# ...
# ...
logger.log(globals())
```
The logger can accept the `globals()` dictionary (or any other dictionary) and log the parameters provided as **output params**.
When using `globals()`, you automatically get all the variables defined in your script's global scope.
The logger makes a best effort attempt to remove all the global variables that are irrelevant, e.g:
* modules
* functions
* variables whose name starts with `_`
* unsupported complex types

**Pros**
* Up and logging in 1 min
* No need to update logging code as the script code updates

**Cons**
* All params are logged as **output params**
* Useless params (like `for` loop indices `i`, `j`, etc...) are also captured

**Recommended use case:** When first experimenting with a new script, where all input and output params and the script's structure is not yet finalized. Or in cases where there's an existing complicated script and you want to invest minimum effort to start logging.

#### Defining Input and Output Blocks
```python
### Your script inputs ###
logger.input_params_start(globals())
a1 = parameter_input
a2 = another_parameter_input
logger.input_params_end(globals())

### Your script calculations ###
# ...
# ...
# ...

logger.output_params_start(globals())
b1 = some_ground_breaking_research_result
b2 = another_ground_breaking_research_result
logger.output_params_end(globals())
```
The logger has an API to define the start and end of the areas in your script where input and output params are defined. The start/end functions must be provided with the `globals()` dict, as they perform a diff between the start and end state of the global variables, keeping only the ones actually created within the block. Irrelevant variables are again removed, using the same heuristics as state above (in automatic logging).

**Pros**
* Bulk addition of many params, saves the need to add logging lines as params are added to the script
* Clear separation between input and output params in app.we-sci.com
* Useless params (like `for` loop indices) aren't captured

**Cons**
* Requires your script to have clear block designated for input and output param definitions
* All your params must be defined in the global scope

**Recommended use case:** When your script structure is finalized, and you have clear defined areas for input and output params. This method is the best trade-off between investment to start logging and accuracy of logging.

#### Manually Adding Params To Be Logged
```python
### Your script inputs ###
a1 = parameter_input
a2 = another_parameter_input

logger.add_input_params({'a1': a1,
                         'a2': a2})

### Your script calculations ###
# ...
# ...
# ...

b1 = some_ground_breaking_research_result
b2 = another_ground_breaking_research_result

logger.add_output_params({'b1': b1,
                          'b2': b2})
```
In this method - a dict with param name and value pairs is explicitly provided to the logger.

**Pros**
* Only params deemed relevant by you are captured
* Params can be captured anywhere in the script (or other modules), as the logger object is passed and the proper functions are called

**Cons**
* You need to update the logging code as you update the script

**Recommended use case:** When you need to log params that aren't in your global scope (in functions, modules, etc...).

#### Combining Param Logging Methods
It is possible to combine all the above mentioned methods  together to log params in your scripts.
The manual and in/out blocks logging takes precedence over the automatic logging, since automatic logging doesn't log a param already known to the logger.
When combining manuall logging and in/out blocks, whichever is last has precedence, as param values are overriden.

The precedence is explained by this example:
```python
import wesci

logger = wesci.Logger(
    script_file=__file__,
    log_file_prefix="./script"
)

# initialy set 'a' to be 3
logger.input_params_start(globals())
a = 3
logger.input_params_end(globals())

# this will override 'a' to be logged as 4
logger.add_input_params({'a': 4})

# initially set 'b' to 0
logger.add_output_params({'b': 0})

# override 'b' to be 3**2 = 9
logger.output_params_start(globals())
b = a**2
logger.output_params_end(globals())

c = 10

# 'c' will be logged as an output param with value of 10, but 'a' won't be overriden to 3
logger.log(globals())

```
The result will be:
* Input params: 
	* a = 4
* Output params:
	* b = 9
	* c = 10

**Note:** Files and figures currently aren't supported with the automatic and block APIs, and must be added explicitly (see below).
	
### Adding Input/Output Files
```python
### Your script inputs ###
logger.add_input_files({'input_csv': 'input.csv'})

### Your script calculations ###
# ...
# ...
# ...

logger.add_output_files({'output_csv': 'output.csv'})
```
Much like params, not all file type are supported.
For all supported file types - you'll be able to click on their row in the file table at [app.we-sci.com](https://app.we-sci.com) and see their preview in the bottom preview box.

**Note**: Unlike params, files must currently be logged explicitly, using `add_input/output_file`.

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
You can see usage examples, both for python scripts and python notebook in the repo.


## Support
We currently maintain three channels for support:
- For Python package related issues - you can open a git-issue.
- For general issues, you can email us at support@we-sci.com.
- For anything else, you can **[join](https://join.slack.com/t/public-wesci-users/shared_invite/MjI1MzQzNDM3MzI4LTE1MDI2NDExNDktNGM1MTIzZTY5MA)** the conversation on our **[Public-We-Sci-Users](https://public-wesci-users.slack.com/)** group on **Slack**.
