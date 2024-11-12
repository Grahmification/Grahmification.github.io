# Grahmification.github.io

[![Gem Version](https://img.shields.io/gem/v/jekyll-theme-chirpy?color=brightgreen)](https://rubygems.org/gems/jekyll-theme-chirpy)
[![Build Status](https://github.com/cotes2020/jekyll-theme-chirpy/workflows/build/badge.svg?branch=master&event=push)](https://github.com/cotes2020/jekyll-theme-chirpy/actions?query=branch%3Amaster+event%3Apush)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8220b926db514f13afc3f02b7f884f4b)](https://app.codacy.com/manual/cotes2020/jekyll-theme-chirpy?utm_source=github.com&utm_medium=referral&utm_content=cotes2020/jekyll-theme-chirpy&utm_campaign=Badge_Grade_Dashboard)
[![GitHub license](https://img.shields.io/github/license/cotes2020/jekyll-theme-chirpy.svg)](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/LICENSE)

A personal website based on the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme which uses [Jekyll](https://github.com/jekyll/jekyll).

## Prerequisites

1. Follow the [Jekyll Docs](https://jekyllrb.com/docs/installation/) to complete the installation of `Ruby`, `RubyGems`, `Jekyll` and `Bundler`.
   * As of most recent this code has been verified with Ruby 3.3. Installing for other Ruby versions may require manually adjusting the versions of gems or installing gems not listed in the Gemfile.
2. Install GIT.

## Installation

See the [Chirpy Documentation](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v3.2.2/README.md) for installation instructions.
- See [here](docs/Install_Troubleshooting.md) if your installation fails.

## Usage

### Configuration

Update the variables of `_config.yml` as needed. Some of them are typical options:

- `url`
- `avatar`
- `timezone`
- `lang`

### Running Local Server

You may want to preview the site contents before publishing. Run it by opening git bash in the root folder and executing:

```console
$ bundle install
```
then:

```console
$ bundle exec jekyll s
```

You should see something like:

```
Configuration file: /octocat/personal-website/_config.yml
            Source: /octocat/personal-website
       Destination: /octocat/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
   GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
                    done in 14.729 seconds.
 Auto-regeneration: enabled for '/octocat/personal-website'
    Server address: http://127.0.0.1:4000
  Server running... press ctrl-c to stop.
```

Or run the site on Docker with the following command:

```terminal
$ docker run -it --rm \
    --volume="$PWD:/srv/jekyll" \
    -p 4000:4000 jekyll/jekyll \
    jekyll serve
```

Open a browser and visit to _<http://localhost:4000>_.

### Adding Javascript

Special steps need to be taken to add new javascript asset files to the website. These steps ensure the javascript will properly get minified and the website will know where to locate it. 
1. Add javascript files to folders in `/assets/js`
2. `/_includes/js-selector.html` determines which javascript file is loaded for each given page. Determine which file is needed for the page you want to add new scripts to.
3. `/gulpfile.js/tasks/js.js` specifies the process for building all javascript files at /assets/js into properly minified files at `/assets/js/dist`. Modify this file to include the new scripts as required by js-selector.html.
4. Install node.js, gulp.js, and any other dependencies listed in `/gulpfile.js/tasks/js.js`
5. Open a terminal at the root project folder and run a `gulp` command. This will execute the gulp build process and overwrite the javascript files at `/assets/js/dist`.
6. Commit all updated files to git and push to update the live website.

### Deployment

See the [Chirpy Documentation](https://github.com/cotes2020/jekyll-theme-chirpy/blob/74aac988bef2b2ed847e761e3c1e10247ce17234/README.md) for deployment instructions.

## Documentation

For more details and the better reading experience, please check out the [tutorials on demo site](https://chirpy.cotes.info/categories/tutorial/). In the meanwhile, a copy of the tutorial is also available on the [Wiki](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

## License

This work is published under [MIT](https://github.com/Grahmification/Grahmification.github.io/blob/master/LICENSE) License.

