import os, sys
from natsort import natsorted

def generate():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # delete contents of <current dir>/_posts
    current_posts = os.listdir(os.path.join(current_dir, "_posts"))
    for post in current_posts:
        os.remove(os.path.join(current_dir, "_posts", post))

    # loop through resources/twigs_panels; make sure it's in order
    overall_panel_num = 0
    for root, subdirs, files in os.walk(os.path.join(current_dir, "resources/chapters")):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg"):
                overall_panel_num += 1

    chapters = filter(os.path.isdir, [os.path.join(current_dir, "resources/chapters",f) for f in os.listdir(os.path.join(current_dir, "resources/chapters"))])
    chapters.sort()
    chapter_num = len(chapters)
    print(chapters)
    
    for chapter in chapters:
        chapter_num -= 1

        twigs_files = os.listdir(os.path.join(current_dir, "resources", chapter))
        twigs_files = natsorted(twigs_files)
        panel_num = len(twigs_files)
        print "arr"
        print twigs_files
        chapter = os.path.split(chapter)[1]
        for panel_name in twigs_files:
            print "name"
            print panel_name
            if panel_name.endswith(".png") or panel_name.endswith(".jpg"):
                panel_num -= 1 # reverse order...
                # create a markdown file in _posts
                panel_file = os.open(os.path.join(current_dir, "_posts", "{0}-01-01-{1}-{2}-{3}.md".format(str(overall_panel_num).zfill(4), chapter_num, panel_num, panel_name)), os.O_RDWR|os.O_CREAT)
                # write post
                os.write(panel_file, "---\nlayout: post\nimgurl: {0}/{1}\npanelnum: {2}\n---\n\n[![Panel]({{{{ site.baseurl }}}} {{% link resources/chapters/{0}/{1} %}})]({{{{page.previous.url}}}}#panel)".format(chapter, panel_name, overall_panel_num))
                os.close(panel_file)
                overall_panel_num -= 1