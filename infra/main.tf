resource "aws_security_group" "imc_sg" {
  name        = "imc-security-group"
  description = "Liberar SSH e porta 5000"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "App Flask"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "imc_server" {
  ami           = "ami-0e66f5495b4efdd0f" # Amazon Linux 2 (sa-east-1)
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.imc_sg.id]

  tags = {
    Name = "IMC-DevOps-Server"
  }
}
