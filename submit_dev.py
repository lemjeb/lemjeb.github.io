import generate_posts
import os, subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))

generate_posts.generate()

# run command jekyll serve in the current dir
_exit_code = subprocess.Popen(["jekyll", "serve"], cwd=current_dir).wait()