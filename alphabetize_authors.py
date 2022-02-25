import argparse
import re

def main():
    parser = argparse.ArgumentParser(description='Alphabetize an author list.')
    parser.add_argument('input_filename')
    parser.add_argument('-o', '--output_filename', type=str, default='output.tex')
    args = parser.parse_args()

    last_name_regex = re.compile(r'\\author.*[~\s]([^~\s\n]+)(?=})[^}\n]*')

    # Read author blocks
    author_blocks = []
    author_block = None
    with open(args.input_filename, 'r') as f:
        for line in f.readlines():
            if line.startswith('\\author'):
                if author_block is not None:
                    author_blocks.append(author_block)
                author_block = line
            else:
                author_block += line

    for author_block in author_blocks:
        test_search = last_name_regex.search(author_block)
        if test_search is None:
            print(author_block)
    author_blocks = sorted(author_blocks, key=lambda x: last_name_regex.search(x).groups(1))
    with open(args.output_filename, 'w') as f:
        for author_block in author_blocks:
            f.write(author_block)


if __name__ == '__main__':
    main()
