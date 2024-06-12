module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = aws_instance.web.key_name
  cidr = "10.0.0.0/16"

  azs             = ["sa-east-1a", "sa-east-1b", "sa-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

# Recurso EC2
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = var.resource_name
  }
}

# Commands:
# terraform init, init and install modules like 'vpc'
# terraform plan
# terraform apply 
#   add "-var-file=enviroment/terraform-dev*"
# terraform destroy
