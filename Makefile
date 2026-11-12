.PHONY: ssh

ssh:
	ssh -i "$(CURDIR)/LightsailDefaultKey-us-west-2.pem" admin@32.185.210.182
