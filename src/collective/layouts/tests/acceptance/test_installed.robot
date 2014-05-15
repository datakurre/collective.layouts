# bin/robot-server collectivelayouts.testing.LAYOUTS_ROBOT_TESTING
# bin/robot src/collective/layouts/tests/acceptance/test_installed.robot

*** Settings ***

Resource  layouts.robot

Test Setup  Open test browser
Test Teardown  Close all browsers

*** Test Cases ***

Plone is installed
    Go to  ${PLONE_URL}
    Page should contain  Powered by Plone
