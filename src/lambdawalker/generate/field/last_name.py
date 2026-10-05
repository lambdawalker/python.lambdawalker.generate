from importlib import resources

from lambdawalker.random.selection.select_random_word_from_nested_directory import select_random_word_from_nested_directory


def _get_text_asset_path(subpath: str):
    try:
        p = resources.files("lambdawalker.generate").joinpath(f"assets/text/{subpath}")
        if p.is_dir() or p.is_file():
            return p
    except Exception:
        pass
    return resources.files("lambdawalker").joinpath(f"assets/text/{subpath}")


def generate_last_name():
    db_path = _get_text_asset_path("last_name")

    name, source = select_random_word_from_nested_directory(
        db_path
    )

    return {
        "data": name,
        "source": source
    }


def vis():
    print(generate_last_name())


if __name__ == "__main__":
    vis()
