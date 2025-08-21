resource "aws_ecr_repository" "sumec" {
  name                 = "sumec"

  tags = {
    Owner = "selfer",
    Purpose = "Image storage"
  }
}
