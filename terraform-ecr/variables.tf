variable "aws_region" {
    description = "AWS region"
    type = string
    default = "eu-central-1"
}

variable "repository_name" {
    description = "Name of the ECR repository"
    type = string
    default = "sumec"
}

variable "environment" {
    description = "Environment name"
    type = string
    default = "dev"
}
