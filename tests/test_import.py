import importlib


def test_package_import() -> None:
    assert importlib.import_module("departure_board").__name__ == "departure_board"
