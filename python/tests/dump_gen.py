from typing import Any
import os.path
import pathlib

from h2o_nitro.protocol import marshal_pretty, dump
from dump_list import dump_list

dumps_dir = pathlib.Path(__file__).parent.resolve().joinpath('dumps')


def write(file_name: str, obj: Any):
    with open(os.path.join(dumps_dir, file_name), 'w') as f:
        f.write(marshal_pretty(dump(obj)))


def main():
    for name, obj in dump_list:
        write(f'{name}.json', obj)


if __name__ == '__main__':
    main()
