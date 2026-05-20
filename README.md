cbecs-microdata-eui-pacific

Median EUI by commercial building type for the Pacific census division using 2018 CBECS microdata

What it does

Reads the EIA's 2018 CBECS public use microdata file — 6,437 individual building records — filters to the Pacific census division (Washington, Oregon, California, Alaska, Hawaii), calculates Energy Use Intensity for each building, groups results by building type, and produces a ranked report comparing median EUI per type against the regional median benchmark.

Input

2018 CBECS public use microdata file (cbecs2018_final_public.csv), available from the EIA website: https://www.eia.gov/consumption/commercial/data/2018/

Output

A ranked report showing median EUI (kBtu/sq ft) for all 20 commercial building types in the Pacific division, with types exceeding the regional median flagged with ***.
Concepts demonstrated
csv module, header-based column lookup with headers.index(), grouping and aggregation with dictionary of lists, statistics.median(), tuple value storage, sorted() with lambda, enumerate() for rank numbering, f-string column formatting

Data source

U.S. Energy Information Administration — 2018 Commercial Buildings Energy Consumption Survey
https://www.eia.gov/consumption/commercial/data/2018/index.php?view=microdata
