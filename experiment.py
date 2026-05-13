import numpy as np
import argparse
import yaml
from pathlib import Path
from test_utils import FUNCTION_DIAL,add_gaussian_noise

def main():

    #Import arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    #Import experimental config files
    with open(args.config) as f:
        config = yaml.safe_load(f)

    #Intialise Experiment
    ##Experimental Parameters
    '''
    - k
    - tau
    - seed
    - func_id
    '''   
    
    k = config['k'] #Number of data points
    tau = config['tau']
    seed = config['seed']
    func_id = config['function_id']

    grid_size = 200 # Grid for truth comparison

    ##Remove '.yml' from string
    exp_name = args.config.split("/")[-1].removesuffix(".yml")

    ## Get test function
    test_function = FUNCTION_DIAL[func_id]

    #Generate Directory
    outdir = Path(exp_name + "/Data")
    outdir.mkdir(parents=True,exist_ok=True)

    
    #Generate Output
    x = np.linspace(0,1,k)
    f = test_function(x=x)
    y = add_gaussian_noise(f_vals=f,
                           tau=tau,
                           seed=seed)


    ##Save results as arrays
    np.save(outdir / "x.npy",x)
    np.save(outdir / "y.npy",y)
    
    #Generate Truth
    x = np.linspace(0,1,grid_size)
    f = test_function(x=x)
    np.save(outdir / "x_grid.npy",x)
    np.save(outdir / "f.npy",f)

    print(f'Results in {outdir}')

    

if __name__ == "__main__":
    main()

