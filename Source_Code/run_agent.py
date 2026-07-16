import os
import sys
from argparse import ArgumentParser
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from datetime import datetime

from common_scaffold.DataAgent import DataAgent

DATASET_LIST = [
    "bookreview",
    "crmarenapro",
    "DEPS_DEV_V1",
    "GITHUB_REPOS",
    "googlelocal",
    "PANCANCER_ATLAS",
    "PATENTS",
    "stockindex",
    "stockmarket",
    "yelp",
    "agnews",
    "music_brainz_20k",
]

if __name__ == "__main__":
    parser = ArgumentParser(description="Run a basic agent with specified parameters.")

    parser.add_argument("--dataset", type=str, required=True, choices=DATASET_LIST)
    parser.add_argument("--query_id", type=int, required=True)
    parser.add_argument("--llm", type=str, default="gpt-4o-mini", help="deployment")
    parser.add_argument("--iterations", type=int, default=100, help="Maximum number of iterations for the agent.")
    parser.add_argument("--use_hints", action="store_true", help="Whether to use DB description with hints.")
    parser.add_argument("--root_name", type=str, required=False, help="Root directory name.")
    parser.add_argument("--agent", type=str, default="DataAgent", choices=["DataAgent", "GouthamAgent"], help="Agent class to use")

    args = parser.parse_args()

    db_dir = Path(os.path.join(os.path.dirname(__file__), f"query_{args.dataset}"))
    query_dir = db_dir / f"query{args.query_id}"
    if not query_dir.exists():
        raise ValueError(f"Query directory {query_dir} does not exist.")

    db_description_path = db_dir / "db_description.txt"
    if not db_description_path.exists():
        raise ValueError(f"DB description file {db_description_path} does not exist.")
    db_description = db_description_path.read_text().strip()

    if args.use_hints:
        hint_path = db_dir / "db_description_withhint.txt"
        if not hint_path.exists():
            raise ValueError(f"DB description with hints file {hint_path} does not exist.")
        hints = hint_path.read_text()
        db_description += "\n\n" + hints.strip()



    db_config_path = db_dir / "db_config.yaml"
    if not db_config_path.exists():
        raise ValueError(f"DB config file {db_config_path} does not exist.")

    # Dynamically select which agent class to instantiate based on CLI arguments.
    # GouthamAgent is the custom implementation optimized for GITHUB_REPOS,
    # whereas DataAgent is the base scaffolding class.
    if args.agent == "GouthamAgent":
        from common_scaffold.GouthamAgent import GouthamAgent
        agent_class = GouthamAgent
    else:
        agent_class = DataAgent

    data_agent = agent_class(
        query_dir=query_dir,
        db_description=db_description,
        db_config_path=db_config_path,
        deployment_name=args.llm,
        exec_python_timeout=600,
        max_iterations=args.iterations,
        root_name=args.root_name if args.root_name else datetime.now().strftime("%Y%m%d_%H%M%S")
    )
    try:
        result = data_agent.run()
    except Exception as e:
        print(f"Error during agent run: {e}")
        for tool in data_agent.tools.values():
            tool.clean_up()
    print(result)

