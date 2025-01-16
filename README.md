# divvy-dynamic-communities

## Project OverviewDescription
Masters course project that transformed divvy data into network graphs, created global communities, 
evaluated community change across each year and per-year communities, and visualizes the results. 

## Environment
Required packages can be found in the requirements.txt file. Environment installation from top of directory:
```bash
conda create --name divvy --file requirements.txt
```

## Folder Structure
TODO: move code from local project to public repo. Delete TODO when done.

```bash
├── data/                      # Data storage
│   ├── raw/                   # Links to raw data provided below
│   ├── processed/             # Processed network graphs
│   └── results/               # Outputs: clustering results, metrics, and visualizations
├── src/                       # Source code
│   ├── data_processing/       # Scripts for data transformation
│   ├── clustering/            # Scripts for clustering
│   ├── evaluation/            # Metrics for evaluating changes
│   └── visualization/         # Visualization scripts
├── notebooks/                 # Jupyter notebooks for experimentation
├── scripts/                   # High-level scripts for running pipelines
├── requirements.txt           # Python dependencies
└── README.md                  # you are HERE
```

## Data Sources

Raw data was found using the following links:
* cleaned divvy data (2013-2019): https://data.cityofchicago.org/Transportation/Divvy-Trips/fg6s-gzvg/about_data
* Raw divvy data (2020 - Present): https://divvy-tripdata.s3.amazonaws.com/index.html
  * Please note, data directly from divvy comes in monthly batches, which can be time consuming to pull / transform.
  * I recommend utilizing an external hard drive to host raw data before transformation.

## Acknowledgements
I would like to thank the city of Chicago, specifically CDOT, for allowing Divvy Bike Share data to be publicly 
available. 