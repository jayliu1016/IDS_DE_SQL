"""
ETL-Query script
"""

import argparse

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

parser = argparse.ArgumentParser()
parser.add_argument("--step", choices=["extract", "load", "query"])
args = parser.parse_args()

if args.step == "extract":
    print("Extracting data...")
    extract()

elif args.step == "load":
    print("Transforming and loading data...")
    load()

elif args.step == "query":
    print("Querying data...")
    query()
