# Installation

## Development installation

Clone the plugin and install its development environment with [`uv`](https://astral.sh/uv):

```shell
git clone git@github.com:Matgenix/datalab-item-plugin-example
cd datalab-item-plugin-example
uv sync --all-extras --dev
```

## Installation in *datalab*

Add the plugin to `plugins.toml` at the root of the *datalab* checkout:

```toml
dependencies = [
    "datalab-item-plugin-example",
]

[tool.uv.sources]
datalab-item-plugin-example = { git = "https://github.com/Matgenix/datalab-item-plugin-example.git" }
```

For local development, use an editable path instead of the Git source:

```toml
[tool.uv.sources]
datalab-item-plugin-example = { path = "../datalab-item-plugin-example", editable = true }
```

Install *datalab* and its declared plugins from the `pydatalab/` directory:

```shell
uv run invoke dev.install
```
