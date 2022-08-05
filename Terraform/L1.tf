provider "aws" {
  access_key = "AKIARNPM5FK7UEKYOYGJ"
  secret_key = "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"
  region   = "eu-central-1"
}

resource "awc_instance" "my_conteiner" {
  ami = "ami-0c9354388bb36c088"
  instance_type = "t2.micro"
}
