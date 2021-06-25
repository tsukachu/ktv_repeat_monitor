terraform {
  required_providers {
    heroku = {
      source  = "heroku/heroku"
      version = "4.5.1"
    }
  }
}

provider "heroku" {
  # Configuration options
}
