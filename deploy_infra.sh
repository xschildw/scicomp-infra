#!/usr/bin/env bash
set -e

# deploy cloudformation templates
# Need to upload TEMPLATES to S3 before validating due to template-body MAX 51K length
# https://docs.aws.amazon.com/cli/latest/reference/cloudformation/validate-template.html#options
S3_BUCKET="bootstrap-awss3cloudformationbucket-114n2ojlbvj21"
S3_BUCKET_PATH="scicomp-infra/$TRAVIS_BRANCH"
S3_BUCKET_URL="s3://$S3_BUCKET/$S3_BUCKET_PATH"
TEMP_DIR="temp"

# get list of templates
pushd cf_templates
TEMPLATES=*

for f in $TEMPLATES
do
  echo -e "\nUploading cf_templates to $S3_BUCKET_URL/$TEMP_DIR/$f"
  aws s3 cp $f $S3_BUCKET_URL/$TEMP_DIR/$f
done

TEMPLATE_URL="https://s3.amazonaws.com/$S3_BUCKET/$S3_BUCKET_PATH/$TEMP_DIR"
for f in $TEMPLATES
do
  echo -e "\nValidating CF template $TEMPLATE_URL/$f"
  aws cloudformation validate-template --template-url $TEMPLATE_URL/$f
done

for f in $TEMPLATES
do
  echo -e "\nPromote CF template to https://s3.amazonaws.com/$S3_BUCKET/$S3_BUCKET_PATH/$f"
  aws s3 mv $S3_BUCKET_URL/$TEMP_DIR/$f $S3_BUCKET_URL/$f
done

popd

# deploy lambda code
LAMBDA_ARTIFACTS_BUCKET="essentials-awss3lambdaartifactsbucket-1ef8sqdil160e"
LAMBDA_PACKAGE="jumpcloud.zip"
pushd lambda/jumpcloud
zip -r ../$LAMBDA_PACKAGE *
popd
echo -e "\nUploading lambda package to s3://$LAMBDA_ARTIFACTS_BUCKET/$S3_BUCKET_PATH/$LAMBDA_PACKAGE"
aws s3 cp lambda/$LAMBDA_PACKAGE s3://$LAMBDA_ARTIFACTS_BUCKET/$S3_BUCKET_PATH/$LAMBDA_PACKAGE
