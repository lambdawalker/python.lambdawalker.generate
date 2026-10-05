import random
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


def generate_road_name():
    name_db = _get_text_asset_path("address/road/name_db")
    type_db = _get_text_asset_path("address/road/type_db")

    name, name_source = select_random_word_from_nested_directory(name_db)
    road_type, road_type_source = select_random_word_from_nested_directory(type_db)

    return {
        "data": f"{road_type} {name}",
        "source": [road_type_source, name_source]
    }


def generate_block_name():
    name_db = _get_text_asset_path("address/block/name_db")
    type_db = _get_text_asset_path("address/block/type_db")

    name, name_source = select_random_word_from_nested_directory(name_db)
    road_type, road_type_source = select_random_word_from_nested_directory(type_db)

    return {
        "data": f"{road_type} {name}",
        "source": [road_type_source, name_source]
    }


def generate_city_name():
    db_path = _get_text_asset_path("address/city")

    name, name_source = select_random_word_from_nested_directory(db_path)

    return {
        "data": name,
        "source": name_source
    }


def generate_state_name():
    db_path = _get_text_asset_path("address/state")

    name, name_source = select_random_word_from_nested_directory(db_path)

    return {
        "data": name,
        "source": name_source
    }


def generate_country_name():
    db_path = _get_text_asset_path("address/country")

    name, name_source = select_random_word_from_nested_directory(db_path)

    return {
        "data": name,
        "source": name_source
    }


def generate_address_number():
    return {
        "data": str(random.randint(1, 9999)),
        "source": "random/1-9999"
    }


def vis():
    print(generate_road_name())
    print(generate_block_name())
    print(generate_city_name())
    print(generate_state_name())
    print(generate_country_name())
    print(generate_address_number())


if __name__ == "__main__":
    vis()
