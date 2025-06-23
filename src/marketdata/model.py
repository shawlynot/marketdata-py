import pyarrow as pa

# will need to construct the pyarrow array just before we write to parquet
schema = pa.schema([
    ("open", ),
    ("high", ),
    ("low", ),
    ("close", ),
    ("trades", )
])

def save_ticks(ticks: list[dict]):
    for tick in ticks:
        