# pro účely úkolu použijeme existujici default VPC. V reálné aplikaci použijeme VPC vlastní.
data "aws_vpc" "default_vpc" {
  default = true
}

data "aws_subnets" "albsubnets" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default_vpc.id]
  }
}

# pro účely úkolu použijeme stejné subnets. V praxi použijeme různé subnets pro ALB a ECS tasks.
data "aws_subnets" "ecssubnets" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default_vpc.id]
  }
}
