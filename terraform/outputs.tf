data "aws_caller_identity" "current" {}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}

output "caller_user" {
  value = data.aws_caller_identity.current.user_id
}

data "aws_region" "current" {}

output "asw_rgn" {
  value = data.aws_region.current.id
}

#data "aws_instance" "bubuntu" {}

output "priv_ip" {
  value       = aws_instance.bubuntu.private_ip
  depends_on = [ aws_instance.bubuntu ]
}

output "subn_id" {
   value       = aws_instance.bubuntu.subnet_id
 }
