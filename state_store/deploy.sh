#!/bin/bash

chalice package --pkg-format terraform deploy/
pushd .
cd deploy
terraform apply -auto-approve
popd
