"""A ``Solution`` custom item type registered via this package's
``pydatalab.item_types`` entry point.

The fields carry ``datalab_*`` schema hints and are rendered automatically by
the datalab web UI — this plugin ships no JavaScript. The companion plugin
`datalab-item-plugin-example-custom-vue` defines an ``example:mixed-solutions``
type that references items of this type and renders them with a custom Vue panel.

The valid ``datalab_*`` hints are defined (and validated at registration) in
``pydatalab.models.schema_hints``:

- fields: ``datalab_include_field_in_summary``, ``datalab_hidden``,
  ``datalab_multiline``, ``datalab_section``, ``datalab_ref_types``,
  ``datalab_quantity``
- model config: ``datalab_ui_color``, ``datalab_ui_hidden_fields``,
  ``datalab_section_title``
"""

from typing import Literal

from pydantic import ConfigDict, Field
from pydatalab.models.samples import Sample
from pydatalab.models.utils import EntryReference

# solute/solvent reference a starting material or another sample.
_SUBSTANCE_REF_TYPES = ["starting_materials", "samples"]


class Solution(Sample):
    """A solution of a single solute at a stated concentration."""

    # This example derives from `Sample`, so it inherits all sample behaviour
    # (relationships, files, blocks, ...). Any concrete `Item` subclass works.
    model_config = ConfigDict(
        title="Solution",
        json_schema_extra={
            # Accent colour for this item type in the UI.
            "datalab_ui_color": "#3a7ca5",
            # Inherited fields that make no sense for this type can be hidden.
            "datalab_ui_hidden_fields": ["synthesis_information"],
            # Title of the card containing the fields without a `datalab_section`.
            "datalab_section_title": "Solution",
        },
    )

    # The complete canonical type identifier has the form `<namespace>:<type-name>`.
    type: Literal["example:solutions"] = "example:solutions"  # type: ignore[assignment]

    solute: EntryReference | None = Field(
        None, json_schema_extra={"datalab_ref_types": _SUBSTANCE_REF_TYPES}
    )

    concentration: float | None = Field(
        None,
        ge=0,
        json_schema_extra={
            "datalab_include_field_in_summary": True,
            "datalab_quantity": {
                # The model, REST API and database always use mol/L. The web UI
                # may convert to mmol/L without changing the stored value.
                "canonical_unit": "mol/L",
                "display_units": {
                    "mol/L": {"scale": 1.0},
                    "mmol/L": {"scale": 0.001},
                },
                "default_display_unit": "mol/L",
                "display_unit_field": "concentration_display_unit",
            },
        },
    )
    concentration_display_unit: Literal["mol/L", "mmol/L"] | None = None
    """Presentation preference only; ``concentration`` always uses mol/L."""

    solvent: EntryReference | None = Field(
        None, json_schema_extra={"datalab_ref_types": _SUBSTANCE_REF_TYPES}
    )
