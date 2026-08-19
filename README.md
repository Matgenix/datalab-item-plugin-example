# <div align="center"><i>datalab-item-plugin-example</i></div>

<div align="center">
<a href="https://github.com/Matgenix/datalab-item-plugin-example/releases"><img src="https://badgen.net/github/release/Matgenix/datalab-item-plugin-example?icon=github&color=blue"></a>
<a href="https://github.com/Matgenix/datalab-item-plugin-example"><img src="https://badgen.net/github/license/Matgenix/datalab-item-plugin-example?icon=license&color=purple"></a>
<a href="https://Matgenix.github.io/datalab-item-plugin-example"><img src="https://github.com/Matgenix/datalab-item-plugin-example/actions/workflows/docs.yml/badge.svg"></a>
</div>

datalab-item-plugin-example is a [*datalab*](https://datalab-org.io) plugin generated using the [datalab-item-plugin-template](https://github.com/Matgenix/datalab-item-plugin-template) template.

> [!NOTE]
> This is an **example plugin**, kept as a reference for custom item type authors — it is
> not meant to be deployed as-is. It shows the simplest kind of item plugin: a data model
> whose fields are rendered automatically by *datalab* from their schema annotations, with
> no JavaScript. Its companion example,
> [datalab-item-plugin-example-custom-vue](https://github.com/Matgenix/datalab-item-plugin-example-custom-vue),
> shows the other kind: an item type rendered by its own custom Vue panel, whose
> `mixed_solutions` items reference the `solutions` items defined here.

It registers the custom item type `solutions` — a solution of a single solute at a stated
concentration (implemented by
[`datalab_item_plugin_example.models.Solution`](src/datalab_item_plugin_example/models.py)) — with *datalab*
via the `pydatalab.item_types` entry point, making it available through the standard item
endpoints and the web UI.

The item's fields carry `datalab_*` schema annotations and are rendered automatically by the
*datalab* web UI — no JavaScript is needed in this plugin. If you later want full control over
the rendering, add a `webapp/SolutionPanel.vue` component to the package (you can
regenerate from the template with `include_custom_panel` enabled to get a starting point).

Releases are created via semantic version tags on [GitHub](https://github.com/Matgenix/datalab-item-plugin-example/releases).
