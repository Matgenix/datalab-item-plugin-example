from importlib.metadata import entry_points

from datalab_item_plugin_example import __version__
from datalab_item_plugin_example.models import Solution


def test_version():
    assert __version__


def test_entry_point_is_registered():
    """The entry point is how datalab discovers this plugin at startup."""
    eps = [ep for ep in entry_points(group="pydatalab.item_types") if ep.name == "solutions"]
    assert len(eps) == 1
    assert eps[0].load() is Solution


def test_model_registers_with_datalab():
    """Mirror what `pydatalab.apps.load_item_plugins` does at server startup;
    this also validates all `datalab_*` schema hints on the model."""
    from pydatalab.models import ITEM_MODELS, register_item_model

    register_item_model(Solution)
    assert ITEM_MODELS["solutions"] is Solution


def test_model_round_trip():
    item = Solution(item_id="test-item-1")
    assert item.type == "solutions"
    assert Solution(**item.model_dump()).item_id == "test-item-1"
