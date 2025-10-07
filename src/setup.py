from setuptools import setup


# Run the setup
setup(
  name             = "least_squares_hedge",
  version          = "0.0.1",
  description      = "Library with class implementations of least squares hedge solvers",
  url              = "https://github.com/krantamaki/least_squares_hedge",
  author           = "Kasper Rantamäki",
  license          = "All rights are reserved",
  packages         = ["least_squares_hedge"],
  install_requires = ["numpy",  # TODO: add version specifiers
                      "scipy"]
)