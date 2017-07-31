# playground_for_wesci_python_logger

## Introduction
This repo contains instructions and examples of how to use We-Sci's [Python Logger SDK](https://pypi.python.org/pypi/wesci) to curate research done using python.

## Current SDK Version
0.1.0

## Using We-Sci's python logger:
### Installation
Install We-Sci's pip [package](https://pypi.python.org/pypi/wesci) by running `pip install wesci`.

### Initializing
```python
import wesci

logger = wesci.Logger(
    user_id='Crazy Scientist',
    script_file=__file__,
    log_file_prefix="./prefix"  # the log file will be written to ./prefix_wesci_log.csv
)
# @yaron - Shoud we consider explaining where the thumbnails / files are to be stored ? also - to me 
# it isn't so clear if the "./prefix" includes the path where the log file should be stored at.
### Your script starts here ###
```

### Adding Input/Output Parameters and Files
```python
### Your script inputs ###
a = paramter_input

logger.add_input_params({'a': a})
logger.add_input_files({'input_csv': 'input.csv'})

### Your script calculations ###
# ...
# ...
# ...

b = some_ground_breaking_research_result

logger.add_output_files({'output_csv': 'output.csv'})
logger.add_output_params({'b': b}) #@yaron - what about when there are several params / files ? what should the syntex be?
```

### Adding Matplotlib figures ###
```python
plot(ground_breaking_data)
# log the current figure under the name output_fig and 
# save a thumbnail ./prefix_wesci_log_figures/
logger.add_output_figure('output_fig')
```

### Adding Images ###
_Coming soon..._

### Logging ###
Just before the script exits, or at any point deemed important, insert the following code to log the data fed into the logger:
```python
logger.log()
```

### Jupyter Notebook support
Everything's basically the same, besides initialization:
```python
logger = wesci.Logger(
    user_id='Crazy Scientist',
    script_file='notebook_file.ipynb'  # Note that you need to specify the notebook's file path explicitely!
    log_file_prefix="./prefix"  # the log file will be written to ./prefix_wesci_log.csv
)
```
**Important:** Only the code will be extracted from the notebook, with separation between cells, without images, data tables, etc..
Furthermore, the code is extracted from the **last saved .ipynb file** - not the one currently being evaluated, due to the architecture of Jupyter Notebook. We will be releasing a feature to dynamically capture the code in the near future.


## Examples
You can see usage examples, both for a python script and python notebook at [script_example.py](./script_example.py) and 
[notebook_example.ipynb](./notebook_example.ipynb) respectively.

Please feel free to open issues here or ping us at contact@we-sci.com!
