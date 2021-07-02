# Demo-Repo


# Generate a badge
# run your tests... get the $total of covared lines and calculate the COLOR of youe badge
# for example if (( $total < 50 )) ;then COLOR=RED ;done
curl "https://img.shields.io/badge/coavrege-$total%25-$COLOR" > badge.svg
gsutil  -h "Cache-Control: no-cache" cp badge.svg gs://$SOME_BACKET/$PROJECT_NAME/codcov.svg
gsutil acl ch -u AllUsers:R gs://$SOME_BACKET/$PROJECT_NAME/codcov.svg
#REPLACE $SOME_BUCKET and $PROJECT_NAME
