<p align="center">
  <a target="_blank" href="https://isaak.dev">
  <img src="https://raw.githubusercontent.com/lk-geimfari/lk-geimfari.github.io/master/assets/images/other/preview.png" width="900"/>
  </a>
</p>



## Development

Make sure you have `ruby 2.5.1` installed, use `rbenv` in case you don't.

1. `rbenv install`
2. `gem install bundler`

Then run:

```
bundle install && bundle run jekyll s --safe --strict_front_matter
```


## About posts

All posts must contain this in their headers:
```
---
layout: post
title: Title of the post
date: Current date in YYYY-MM-DD format
description: Short description of the post
web_preview_image: file_name.png (name of the image from the directory `/assets/images/posts/`)
---
```
