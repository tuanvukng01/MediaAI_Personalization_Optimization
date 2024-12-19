#!/usr/bin/env bash
python src/data_simulation.py
python src/data_preprocessing.py
python src/database_utils.py
dbt run --project-dir dbt