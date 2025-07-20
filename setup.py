from setuptools import setup, find_packages


# Compile C++ dependencies (this is optional so the below code block can be commented out)
...


# Run the Python setup 
# TODO: Finish
setup(
  name             = 'least_squares_hedge',
  version          = '0.0.1',
  install_requires = [
    ...
  ],
  packages         = find_packages(
    include = ["least_squares_hedge"],
    exclude = ["docs", "examples", "*/tests/*"]
  )
)
