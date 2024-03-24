.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  runserver  to run the site locally"
	@echo "  clean      to clean the site"

.PHONY: runserver
runserver:
	bundle install && bundle exec jekyll s --safe --strict_front_matter

.PHONY: clean
clean:
	@rm -rf _site
