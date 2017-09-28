from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import wesci

logger = wesci.Logger(
    script_file=__file__,
    log_file_prefix="./script"
)

# inputs
a = 3

logger.add_input_params({'a': a})
logger.add_input_files({'input_csv': 'input.csv'})
logger.add_input_files({'input_txt': 'input.txt'})
logger.add_input_files({'input_json': 'input.json'})

xs = np.arange(0,10,0.1)
plt.plot(xs, np.sin(xs))
logger.add_output_figure('fig1')

b = a**2

df = pd.DataFrame(np.random.randn(50, 4), columns=list('ABCD'))

logger.add_output_files({'output_csv': 'output.csv'})
logger.add_output_params({'b': b})
logger.add_output_params({'random_data': df})

# log
logger.log()
