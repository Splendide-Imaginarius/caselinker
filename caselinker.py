#!/usr/bin/env python3

import argparse
import pathlib

import json_strings


def link_file(path: pathlib.Path, str_link: str, str_target: str) -> None:
    source_path = path.parent / (str(path.name).replace(str_target, str_link))
    if source_path.exists():
        print(f'Already Linked {source_path} to {path}')
        return
    source_path.symlink_to(path.name)
    print(f'Linked {source_path} to {path}')


def patch_file(path: pathlib.Path, strings: set[str]) -> None:
    if path.is_symlink():
        return

    for s in strings:
        if path.name.lower() == s.lower() and path.name != s:
            link_file(path, s, path.name)
        if path.stem.lower() == s.lower() and path.stem != s:
            link_file(path, s, path.stem)


def patch_folder(path: pathlib.Path, strings: set[str]) -> None:
    for p in path.rglob('*'):
        patch_file(p, strings)


def main() -> None:
    parser = argparse.ArgumentParser(prog='caselinker')

    parser.add_argument('--source-code', required=True,
                        help='path to source code')
    parser.add_argument('--assets', required=True,
                        help='path to assets')
    args = parser.parse_args()

    source_code = pathlib.Path(args.source_code)
    assets = pathlib.Path(args.assets)

    strings = json_strings.strings_folder(source_code)
    patch_folder(assets, strings)


if __name__ == '__main__':
    main()
