import os, sys


"""
---
layout: post
---

![Panel]({{ site.baseurl }}{% link resources/twigs_panels/imgname %})
"""

current_dir = os.path.dirname(os.path.abspath(__file__))
# delete contents of <current dir>/_posts
current_posts = os.listdir(os.path.join(current_dir, "_posts"))
for post in current_posts:
    os.remove(os.path.join(current_dir, "_posts", post))

twigs_files = os.listdir(os.path.join(current_dir, "resources/twigs_panels"))

# loop through resources/twigs_panels; make sure it's in order
twigs_files.sort()
panel_num = len(twigs_files)
for panel_name in twigs_files:
    if panel_name.endswith(".png") or panel_name.endswith(".jpg"):
        panel_num -= 1 # reverse order...
        # create a markdown file in _posts
        panel_file = os.open(os.path.join(current_dir, "_posts", "2000-10-10-{0}-{1}.md".format(panel_num, panel_name)), os.O_RDWR|os.O_CREAT)
        # write post
        os.write(panel_file, "---\nlayout: post\nimgurl: {0}\n---\n\n[![Panel]({{{{ site.baseurl }}}} {{% link resources/twigs_panels/{0} %}})]({{{{page.previous.url}}}}#panel)".format(panel_name))
        os.close(panel_file)
# run command jekyll serve in the current dir