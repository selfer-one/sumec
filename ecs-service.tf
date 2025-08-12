resource "aws_ecs_cluster" "lesson7" {
  name = "lesson7"
}

resource "aws_ecs_task_definition" "lesson7" {
  family                   = "lesson7"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"
  task_role_arn            = aws_iam_role.ecs_role.arn
  execution_role_arn       = aws_iam_role.ecs_role.arn
  
  container_definitions = jsonencode([
    {
      name      = "web"
      image     = "824308980797.dkr.ecr.eu-central-1.amazonaws.com/sumec:latest"
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
          protocol      = "tcp"
        }
      ]
    }
  ])
}


resource "aws_ecs_service" "lesson7" {
  name            = "lesson7"
  cluster        = aws_ecs_cluster.lesson7.id
  task_definition = aws_ecs_task_definition.lesson7.arn
  desired_count   = 2

  launch_type = "FARGATE"

  network_configuration {
    subnets          = [data.aws_subnets.ecssubnets.ids[0], data.aws_subnets.ecssubnets.ids[1]]
    security_groups  = [aws_security_group.ecs_tasks.id]
    assign_public_ip = true
  }

    load_balancer {
        target_group_arn = aws_lb_target_group.main.arn
        container_name   = "web"
        container_port   = 80
    }
}
