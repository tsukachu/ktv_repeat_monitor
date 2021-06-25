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
