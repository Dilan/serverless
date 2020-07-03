### Create Layers:

	$ virtualenv venv --python=python3
	$ source venv/bin/activate
	$ cd s3-listener-lambda/
	$ mkdir python-resize-image
	$ pip3 install pillow -t ./pillow
	$ zip -r pillow.zip pillow

	$ aws lambda publish-layer-version \
		--region=eu-west-1 \
		--profile=serverless \
	    --layer-name pillow \
	    --description "Python Imaging Library (PIL)" \
		--license-info "MIT" \
		--zip-file fileb:///Users/anton.plotnikov/Node/accenture/serverless/s3-listener-lambda/pillow.zip \
	    --compatible-runtimes python3.7 python3.8
