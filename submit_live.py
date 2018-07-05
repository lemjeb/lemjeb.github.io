import generate_posts
import os, subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))

generate_posts.generate()

# run commands to push to live repo
_exit_code = subprocess.Popen(["git", "add", "."], cwd=current_dir).wait()
_exit_code = subprocess.Popen(["git", "commit", "-m", "Adding new comic panels via script"], cwd=current_dir).wait()
_exit_code = subprocess.Popen(["git", "push", "origin", "master"], cwd=current_dir).wait()