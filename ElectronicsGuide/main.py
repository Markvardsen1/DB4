import sys
import os

# Get the absolute path of the Linearization/linearization directory
module_path = os.path.abspath(os.path.join('Linearization', 'linearization'))

# Add the directory to sys.path
if module_path not in sys.path:
    sys.path.append(module_path)

# Now you can import the module
import linearize

if __name__ == '__main__':
    linearize.main()







