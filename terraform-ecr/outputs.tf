output "ecr_repository_url" {
    description = "URL of the ECR repository"
    value = aws_ecr_repository.sumec.repository_url
}

output "ecr_repository_arn" {
    description = "ARN of the ECR repository"
    value = aws_ecr_repository.sumec.arn
}
