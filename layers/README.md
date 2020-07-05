### AWS layers:

	$ cd layers
	$ virtualenv venv --python=python3
	$ source venv/bin/activate
	$ mkdir python
	$ pip3 install pillow -t ./python
	$ zip -r pillow.zip python

	$ aws lambda publish-layer-version \
		--region=eu-west-1 \
		--profile=serverless \
	    --layer-name pillow \
	    --description "Python Imaging Library (PIL)" \
		--license-info "MIT" \
		--zip-file fileb:///Users/anton.plotnikov/Node/accenture/serverless/layers/pillow.zip \
	    --compatible-runtimes python3.7 python3.8
