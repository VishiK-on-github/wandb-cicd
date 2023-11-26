import wandb

print(f"The version of wandb is: {wandb.__version__}")

assert wandb.__version__ == '10.2.3', f"Expected version 10.2.3, got {wandb.__version__}"
