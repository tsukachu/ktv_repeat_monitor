terraform {
  required_providers {
    heroku = {
      source  = "heroku/heroku"
      version = "4.5.1"
    }
  }

  required_version = "= 1.0.1"

  backend "pg" {
  }
}

provider "heroku" {
  # Configuration options
}

resource "heroku_app" "main" {
  name   = "ktv-repeat-monitor"
  region = "us"
  config_vars = {
    SIMPLE_SETTINGS = "app.settings.production"
  }
}

resource "heroku_addon" "database" {
  app  = heroku_app.main.name
  plan = "heroku-postgresql:hobby-dev"
}
