terraform {
  required_version = ">= 1.0.0"
}

resource "local_file" "devops_info" {
  filename = "infrastructure-info.txt"
  content  = "This file simulates infrastructure setup using Terraform for the DevOps final project."
}

output "message" {
  value = "Terraform simulation completed successfully."
}