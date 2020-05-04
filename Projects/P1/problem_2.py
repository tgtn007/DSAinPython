import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is None or suffix is None:
        return ['Please enter suffix and path']
    list_of_paths = list()
    find_files_recursively(suffix, path, list_of_paths)
    # print(list_of_paths)
    return list_of_paths


def find_files_recursively(suffix, path, list_of_paths):
    # print(path)

    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            find_files_recursively(suffix, os.path.join(path, i), list_of_paths)
        if i.endswith(suffix):
            list_of_paths.append(os.path.join(path, i))
            # print(listOfPaths)
    return list_of_paths


def test(suffix, path):
    results = find_files(suffix, path)
    print("Files with the suffix : {} on path {}".format(suffix, path))
    if len(results) == 0:
        print("No files found.")
    elif results[0] == 'Please enter suffix, path':
        print("Suffix and Path is required.")
    else:
        for file in results:
            print(file)


test(".lll", "./testdir") # Expected output: No files found.
test(".c", "./testdir") # Expected output: [list of paths]
test(None, "./testdir") # Expected output: Please enter suffix and path

