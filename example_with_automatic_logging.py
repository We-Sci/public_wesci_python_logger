from matplotlib import pyplot as plt
import pandas
import wesci

logger = wesci.Logger(
    script_file=__file__,
    log_file_prefix="./script"
)

a = 3
df = pandas.DataFrame.from_records([{'mean': 0, 'std': 0.5}, {'mean': 2, 'std': 0.6}])

# add all input files
logger.add_input_files({'input_csv': 'input.csv'})
logger.add_input_files({'input_txt': 'input.txt'})
logger.add_input_files({'input_json': 'input.json'})

# do some work
b = a**2

# add a figure
plt.plot([1, 2, 3], [4, 5, 6])
logger.add_output_figure('fig1')

# add output files
logger.add_output_files({'output_csv': 'output.csv'})

# log automatically all params
logger.log(globals())
