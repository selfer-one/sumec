variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "eu-central-1"
}

variable "aws_account_id" {
  type = string
  default = 824308980797
}

variable "project_name" {
  default = "ecs-nginx-demo-sumec"
}
