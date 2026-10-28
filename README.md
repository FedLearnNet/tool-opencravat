# tool-opencravat

Annotates genomic variant files with OpenCRAVAT and exports run status, logs, and a summary report.

## Runtime inputs

OpenCRAVAT requires installed mapper, annotator, converter, and reporter modules. Configure those resources before an annotation run.

## Inputs and outputs

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `variant_file` | PATH | Path to the input variant file (for example VCF, TSV, or TXT) passed to OpenCRAVAT. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `status_json` | JSON | OpenCRAVAT run status JSON file. |
| `log_file` | TEXT | OpenCRAVAT log output file. |
| `err_file` | TEXT | OpenCRAVAT error output file. |
| `report_files` | JSON | List of generated OpenCRAVAT output files. |
| `report` | HTML | HTML summary report of the OpenCRAVAT run. |

## Configuration

| Name | Default | Description |
| --- | --- | --- |
| `assembly` | `hg38` | Reference genome assembly used by OpenCRAVAT. |
| `annotators` | `clinvar` | Comma-separated OpenCRAVAT annotators to run. |
| `reporters` | `text` | Comma-separated OpenCRAVAT reporters to generate. |
| `preview_rows` | `100` | Number of rows to include in preview outputs if previews are added later. |

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
# Set APP_ID and platform URLs before connecting.
python main.py
```

The Docker base image provides the FL-Net API. `requirements.txt` lists additional
runtime dependencies; `requirements-dev.txt` includes the API for local development.
Runtime datasets and trained models must be supplied separately; see `data/README.md`.

Build with `docker build -t tool-opencravat .`.
