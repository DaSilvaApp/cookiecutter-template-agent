# Recommended version (best practice)
# from pathlib import Path
# import os, tomllib

# ROOT = Path(__file__).resolve().parent.parent
# ENV = os.getenv("ENV", "dev")

# config_path = ROOT / "config" / f"config.{ENV}.toml"

# if not config_path.exists():
#     raise FileNotFoundError(f"Config file not found: {config_path}")

# with open(config_path, "rb") as f:
#     CONFIG = tomllib.load(f)



# Example: Use it anywhere
# from name_project.config import CONFIG

# print(CONFIG["llm"]["model"])