terraform {
  backend "s3" {
    bucket         = "tfstate-824308980797-eu-central-1"
    key            = "terraform/lesson7/terraform.tfstate"
    region         = "eu-central-1"
    encrypt        = true
  }
}
