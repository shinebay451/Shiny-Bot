import wandb
import time


wandb.init(project="MicroRTS", name="CRush_V1")


def log_to_wandb():
    logged_lines = set()
    while True:
        try:
            with open("wandb_log.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line not in logged_lines: 
                        logged_lines.add(line)
                        data = {}
                        parts = line.strip().split(", ")
                        for part in parts:
                            key, value = part.split(": ")
                            data[key] = float(value) if "." in value else int(value)
                        wandb.log(data)
            time.sleep(2)  
        except FileNotFoundError:
            print("Waiting for logs...")
            time.sleep(2)


log_to_wandb()
