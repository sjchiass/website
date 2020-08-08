# A website

## What it is

This is a simple website made in the standard `pelican` way. I write content in `./content`, have `pelican` build it, and serve up the output at <https://www.sjchiass.com>.

Everything I've done so far comes from the tutorial: <https://docs.getpelican.com/en/stable/>.

## How to use

On the computer you want to write things, clone/pull this repo.

Write your content in `./content`. `pelican` works on markdown, and these are at the top-level. The images I keep in sub-folders organized by topic, to make things easier to manage.

As you write, run `pelican -lr` in the project's root folder. This will give you a live preview of the website.

When you're satisfied, `git push` to GitHub.

Then just have the server build the website itself and serve it.

## Versions

I'm using `pelican` 4.2.0. Some Python package providers still only have 3.x.x versions, so you need to dig a little to find the right version.

## Extras

### Resizing images

While there are nice plugins for image galleries and the like, so far I'm sticking to the basics.

When I have a folder full of images, I resize them all with this command

```
mkdir resized; mogrify -auto-orient -resize 500 -path ./resized *.jpg
```

The `-auto-orient` option is there for those photos that have embedded rotation instructions. The images will be saved with the correct rotation.

### Converting from Zim

Zim is a personal wiki tool: <https://zim-wiki.org/>

If you want to export your Zim to markdown, go to File > Export and then follow the prompts.

I've tried figuring out how to use `pandoc` directly to convert Zim, but it seems that Zim has its own format. It's easier to use their tool or to write your blog entries in notepad.
