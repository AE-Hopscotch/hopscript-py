from pathlib import Path
import json
import re


def main():
    path = Path('./hopscotch-cache/project-datatypes.json')
    blocks: dict | None = None
    with path.open('r') as file:
        datatypes = json.loads(file.read())
        blocks: dict = {pair[1]: int(float(pair[0])) for pair in datatypes['blocks'].items()}
        # name_dict: dict = {pair[1]: pair[0] for pair in blocks.items()}

    if blocks is None: return
    return  # no accidental write right now

    with Path('./builder/blocks.py').open('w') as file:
        file.write('from builder.base import generate_block\n\n')

        for name, block_id in blocks.items():
            if name.startswith('HS_'): continue

            readable_name = re.sub(r'(?<!^)([A-Z])', ' \g<1>', name)
            fn_name = re.sub(r'(?<!^)([A-Z])', '_\g<1>', name).lower()

            fn = f"def {fn_name}(value: any):\n    return generate_block({block_id}" + \
                 f", '{readable_name}', [value])\n\n\n"
            file.writelines([fn])


if __name__ == '__main__':
    main()
