variable "region" {
  description = "Região AWS (us-east-1 ou us-west-2)"
  default     = "us-east-1"
}

variable "key_name" {
  description = "Nome da chave SSH para EC2 (deve existir na AWS)"
  type        = string
}
