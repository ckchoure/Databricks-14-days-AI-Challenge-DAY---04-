# Day 4 – Delta Lake Introduction

## Objective
To understand Delta Lake fundamentals by converting existing sales data into Delta format and validating data reliability features.

## Dataset Used
- sale_data
- customer

## Tasks Performed
- Renamed columns to follow standard naming conventions
- Converted CSV-based sales data to Delta format
- Created managed Delta tables using PySpark
- Verified schema enforcement by attempting invalid inserts
- Tested duplicate data insertion behavior

## Key Learnings
- Delta Lake adds ACID transactions on top of Parquet
- Schema enforcement prevents accidental schema mismatch
- Delta Lake ensures safe writes but does not automatically remove duplicates

## Tools Used
- Databricks Community Edition
- Delta Lake
- Apache Spark (PySpark)

## Notes
This work is part of the Databricks 14 Days AI Challenge organized by Indian Data Club and Codebasics.
