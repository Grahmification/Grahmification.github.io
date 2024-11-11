# frozen_string_literal: true

source "https://rubygems.org"

gemspec

group :test do
  gem "html-proofer", "~> 5.0"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Make external links open in new tab
gem "jekyll-target-blank", "~> 2.0"

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.2.0", :install_if => Gem.win_platform?

# Needed to pull repo data from github
gem "jekyll-github-metadata"

# Removed from the standard library in Ruby 3.0
gem "webrick", "~> 1.8"

# Removed from the standard library in Ruby 3.4
gem "csv", "~> 3.3"
gem "base64", "~> 0.2.0"

# Optional
gem 'faraday-retry', '~> 2.2'
