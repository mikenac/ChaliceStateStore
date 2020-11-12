#!/bin/bash

pushd .
cd infra
terraform apply --auto-approve
popd
pushd .
eval ./deploy.sh

