import json
import pathlib
from typing import TypeAlias

JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None


def strings_json(j: JSON) -> set[str]:
    strings = set()

    if isinstance(j, list):
        for e in j:
            strings.update(strings_json(e))
    elif isinstance(j, dict):
        for e in j.keys():
            strings.update(strings_json(e))
        for e in j.values():
            strings.update(strings_json(e))
    elif isinstance(j, str):
        for s in j.split('/'):
            strings.update(s.split('\\'))
    elif isinstance(j, (int, float, bool)):
        pass
    elif j is None:
        pass
    else:
        raise Exception('unknown type ' + str(type(j)))

    return strings


def strings_json_file(path: pathlib.Path) -> set[str]:
    with open(path) as f:
        j = json.load(f)

    return strings_json(j)


def strings_folder(path: pathlib.Path) -> set[str]:
    strings = set()

    for p in path.rglob('*.json'):
        strings.update(strings_json_file(p))

    return strings
