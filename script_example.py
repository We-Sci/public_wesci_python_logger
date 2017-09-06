from matplotlib import pyplot as plt
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

plt.plot([1, 2, 3], [4, 5, 6])
logger.add_output_figure('fig1')

# do some math
b = a**2

logger.add_output_files({'output_csv': 'output.csv'})
logger.add_output_params({'b': b})

# log
logger.log()
