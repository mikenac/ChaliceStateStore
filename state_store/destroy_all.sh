#!/bin/bash

pushd .
cd deploy
terraform destroy --auto-approve
popd
pushd .
cd infra
terraform destroy --auto-approve
popd
