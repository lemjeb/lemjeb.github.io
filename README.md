# twigs site

This site uses the [Jekyll](https://jekyllrb.com/) static site generation engine. The idea is that all the assets of the site can be configured using
HTML/CSS templates (Liquid) and Markdown with front matter and then Jekyll glues them together into a static website that can easily be hosted anywhere. The Jekyll docs are really good and should be able to tell you everything you need to know about itself, Github Pages hosting, Liquid templating, etc.

Another advantage of using Jekyll sites is free hosting of up to 1 GB with GitHub pages. When this repo is pushed to `https://github.com/lemjeb/lemjeb.github.io`,
the changes are seen on the live site. 

## How to Add Panels (The Short Version)

1) Add the panel image to `resources/twigs_panels` (Make sure it's in order, maybe use a naming scheme like 'twigs_<panel_num>_blablawhateve.jpg')
2) If you just want to test it out, run `submit_dev.py` and check the site out at `http://127.0.0.1:4000/`. Otherwise, run `submit_live.py` to push your changes to the live site. 

Done!

## How To Develop on This Site

### Install Jekyll
First, you'll need to set up Jekyll on your machine. Go check out that webpage, though if you already have Ruby, these might be all the commands you need:

```
gem install bundler jekyll
cd lemjeb.github.io
jekyll serve
```

And open `http://127.0.0.1:4000/` in a web browser.

### Make edits

Once you are serving the local version of the site, Jekyll will stay in sync with most of your changes (though if you make changes to _config.yml you will need to restart the dev server). This makes the iteration loop pretty convenient for making changes to SCSS and layout, etc. The template files in `_layouts` and `_includes` configure most of the formatting for the site, the `_sass` directory contains stylesheets for all elements of the sites (buttons, links, text), and 
`resources` contains images.

Check out `about.md` for an example of adding a page to the site with Markdown. The about page is added to the navbar in `header.html`.

### The Dev Scripts and Adding Comic Panels 

To reduce fuss with adding new comic panels, I tried to make the process as automated as I could. The way it currently works is a sort of workaround to leverage the blogging features of Jekyll for organization, paging, etc. There are two Python scripts currently that add comic panels: `submit_dev.py` and `submit_live.py`. Both scripts take all the comic panels in `resources/twigs_panels` and generate blog posts associated with each panel in order. Then the site takes those images from the blog post and lays them out in order to make the front page long scroll version of the comic. The **difference** between the scripts is that `submit_dev.py` simply does the generation and hosts a local version of the site at `http://127.0.0.1:4000/`, whereas `submit_live.py` actually pushes the new version of the site up to be hosted live.

## Improvements / Plugins

Right now, this approach with the scripts for adding panels and hosting/generating with Github Pages and Jekyll seems to be pretty straightforward and simple.
If things start to get hand and you need to host the site elsewhere, you might want to write or use some Jekyll plugins to automate the process further.

Unfortunately, a security related drawback of Github Pages is that Jekyll plugins cannot be used live. So keep in mind that if you do want to use those plugins, 
you'll have to generate the site locally and then push the `_site` directory (the generated static site) to Github or wherever your new hosting location is. 

### contact jackcampbell@acm.org for q's etc