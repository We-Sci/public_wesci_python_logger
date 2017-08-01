import wesci

logger = wesci.Logger(
    user_id='Crazy Scientist',
    script_file=__file__,
    log_file_prefix="./script"
)

# inputs
a = 3

logger.add_input_params({'a': a})
logger.add_input_files({'input_csv': 'input.csv'})

# do some math
b = a**2

logger.add_output_files({'output_csv': 'output.csv'})
logger.add_output_params({'b': b})

# log
logger.log()
