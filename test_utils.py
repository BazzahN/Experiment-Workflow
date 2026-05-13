import numpy as np


#Utils
def add_gaussian_noise(f_vals,tau,seed):
    """
    Adds Gaussian noise to f_vals as genrated from seed argument.
        y = f(x) + \\epsilon
        
        \\epsilon \\sim N(0,\\tau)
        Domain: x \\in [0,1]

    Inputs
    ------
    f_vals:NumpyArray
        The test/train locations for the GP
    tau: Float
        Gaussian Variance

    seed: 12345
        Set Seed of            
    Returns
    -------
    y: Float
        Evaluation of the test function
    """
    rng = np.random.default_rng(seed=seed)

    noise_std = rng.standard_normal(*f_vals.shape) * np.sqrt(tau)

    return f_vals + noise_std

#Test Functions
def test_function_1(x):
    """
   Experiment test function.
        
        f(x) = \\sin(5x) + \\cos(7x)

    Inputs
    ------
    x:NumpyArray
        The test/train locations for the GP
   
    Returns
    -------
    Float
        Evaluation of the test function
    """
    return np.sin(5*x) + np.cos(7*x)

def test_function_2(x):
    """
   Experiment test function.
        
        f(x) = 5(x-1/2)^2

    Inputs
    ------
    x:NumpyArray
        The test/train locations for the GP
   
    Returns
    -------
    Float
        Evaluation of the test function
    """
    return 5*(x-0.5)**2

#Function Dials
#To allow for function selection during experiments
FUNCTION_NAMES = ["f(x) = \\sin(5x) + \\cos(7x)",
                  "f(x) = 5(x-\\frac{{1}}{{2}})^2"]

FUNCTION_DIAL = [test_function_1,
                 test_function_2]
