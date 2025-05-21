import os
import re

class TransformPath:
    """ This class takes a top level directory, and looks for gcc error 
    messages and makefile 'cd' messages and transforms any of those 
    relative paths to be paths starting from the given top directory. """

    def __init__(self, top_dir: str):
        self.top_dir = top_dir
        self.current_make_dir = ''

    def __update_current_make_dir(self, line: str) -> None:
        """ Given a line, look for the text indicating that make is entering a 
        new directory, and so all gcc error paths will be relative to that 
        directory. """
        directory_pattern = r"make\[\d+\]: Entering directory '([^']+)'"
        # Keep track of which directory make is in
        match = re.search(directory_pattern, line)
        if match:
            self.current_make_dir = match.group(1)

    def transform_line(self, line: str) -> str:
        """ Given a line of makefile output, transform any paths in error messages to be relative
        to top_dir passed to this class's constructor. """
        # Replace file paths with paths relative to the top directory in make's output
        #print("Checking line: ", line)
        self.__update_current_make_dir(line)
        rel_match = re.match(r'^(\.{1,2}/[^\s:]+):', line)
        if rel_match:
            path_fragment = rel_match.group(1)
            abs_path = os.path.join(self.current_make_dir, path_fragment)
            rel_path = os.path.relpath(abs_path, self.top_dir)
            line = line.replace(path_fragment, rel_path, 1)
        return line

