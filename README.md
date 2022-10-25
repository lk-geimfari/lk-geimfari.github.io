<p align="center">
  <a target="_blank" href="https://isaak.dev">
  <img src="https://user-images.githubusercontent.com/15812620/124396497-a1e19f00-dd12-11eb-9b91-1fc22e316f5c.png" width="900"/>
  </a>
</p>



## Development

Make sure you have `ruby 2.5.1` installed, use `rbenv` in case you don't.

1. `rbenv install`
2. `gem install bundler`

Then run:

```
bundle install && bundle exec jekyll s --safe --strict_front_matter
```


## About posts

You need to All posts must contain this in their headers:
```
---
layout: post
title: Title of the post
date: Current date in YYYY-MM-DD format
description: Short description of the post
preview_img: file_name.png (name of the image from the directory `/assets/images/posts/`)
---
```
